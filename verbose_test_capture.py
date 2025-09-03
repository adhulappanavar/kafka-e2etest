#!/usr/bin/env python3
"""
Verbose Test Capture
Captures verbose output from Kafka tests and includes it in reports
"""

import io
import sys
import time
from contextlib import redirect_stdout, redirect_stderr
from test_report_generator import TestReportGenerator


class VerboseOutputCapture:
    def __init__(self):
        self.output_buffer = io.StringIO()
        self.original_stdout = sys.stdout
        self.original_stderr = sys.stderr
        self.captured_rich_output = []
        
    def start_capture(self):
        """Start capturing output"""
        self.output_buffer = io.StringIO()
        sys.stdout = self.output_buffer
        sys.stderr = self.output_buffer
        self.captured_rich_output = []
        
    def capture_rich_output(self, output):
        """Capture rich output specifically"""
        self.captured_rich_output.append(output)
        
    def stop_capture(self):
        """Stop capturing output and return captured content"""
        captured_output = self.output_buffer.getvalue()
        sys.stdout = self.original_stdout
        sys.stderr = self.original_stderr
        
        # Combine stdout/stderr with rich output
        combined_output = captured_output + "\n".join(self.captured_rich_output)
        return combined_output


def run_single_test_with_capture(test_name: str, verbose: bool = False) -> tuple:
    """Run a single test and capture its verbose output"""
    import pytest
    import os
    
    # Set environment variable for verbose mode
    if verbose:
        os.environ["KAFKA_VERBOSE"] = "true"
    else:
        os.environ["KAFKA_VERBOSE"] = "false"
    
    # Capture output
    capture = VerboseOutputCapture()
    capture.start_capture()
    
    try:
        # Run the test
        start_time = time.time()
        result = pytest.main([f"test_kafka.py::{test_name}", "-v", "--tb=short"])
        end_time = time.time()
        
        # Get captured output
        captured_output = capture.stop_capture()
        
        # Get verbose log from the test module
        import test_kafka
        verbose_log = getattr(test_kafka, 'current_verbose_log', '')
        
        # Combine outputs
        combined_output = captured_output
        if verbose_log:
            combined_output += "\n\n=== VERBOSE KAFKA OUTPUT ===\n"
            combined_output += verbose_log
        
        # Determine status
        status = "PASSED" if result == 0 else "FAILED"
        duration = end_time - start_time
        
        return status, duration, combined_output
        
    except Exception as e:
        captured_output = capture.stop_capture()
        return "ERROR", 0, f"Error: {e}\n{captured_output}"


def run_all_tests_with_verbose_capture(verbose: bool = False) -> str:
    """Run all tests with verbose output capture and generate comprehensive report"""
    from rich.console import Console
    from rich.panel import Panel
    from rich.text import Text
    import subprocess
    
    console = Console()
    
    # Welcome panel
    welcome_text = Text("Kafka Comprehensive Test Suite with Verbose Output Capture", style="bold blue")
    welcome_panel = Panel(welcome_text, title="Test Suite", border_style="blue", padding=(1, 2))
    console.print(welcome_panel)
    
    # Initialize report generator
    report_generator = TestReportGenerator(verbose=verbose)
    report_generator.start_test_session()
    
    # Start Kafka
    console.print("\n[bold green]Starting Kafka infrastructure...[/bold green]")
    try:
        subprocess.run(["docker-compose", "up", "-d"], check=True, capture_output=True)
        time.sleep(5)  # Wait for Kafka to be ready
        console.print("[green]✓ Kafka started successfully![/green]")
    except subprocess.CalledProcessError:
        console.print("[red]✗ Failed to start Kafka. Please check Docker.[/red]")
        return None
    
    # Define all test names
    test_names = [
        "TestKafkaOperations::test_create_topic",
        "TestKafkaOperations::test_send_single_message", 
        "TestKafkaOperations::test_send_multiple_messages",
        "TestKafkaOperations::test_consume_messages",
        "TestKafkaOperations::test_consume_messages_with_group_id",
        "TestKafkaOperations::test_get_topic_info",
        "TestKafkaOperations::test_get_partition_count",
        "TestKafkaOperations::test_message_ordering",
        "TestKafkaOperations::test_message_without_key",
        "TestKafkaOperations::test_large_message",
        "TestKafkaQueueLength::test_queue_length_after_sending",
        "TestKafkaQueueLength::test_partition_distribution",
        "TestKafkaQueueLength::test_queue_length_verbose"
    ]
    
    # Run each test individually and capture output
    console.print(f"\n[bold blue]Running {len(test_names)} tests with verbose output capture...[/bold blue]")
    
    for i, test_name in enumerate(test_names, 1):
        console.print(f"\n[dim]Running test {i}/{len(test_names)}: {test_name}[/dim]")
        
        status, duration, verbose_output = run_single_test_with_capture(test_name, verbose)
        
        # Add test result to report
        report_generator.add_test_result(
            test_name,
            status,
            duration,
            {
                "test_index": i,
                "category": report_generator._get_test_category(test_name),
                "verbose_mode": verbose
            },
            verbose_output
        )
        
        # Show progress
        status_icon = "✅" if status == "PASSED" else "❌"
        console.print(f"[{status_icon}] {test_name} - {status} ({duration:.2f}s)")
    
    report_generator.end_test_session()
    
    # Generate report
    console.print("\n[bold yellow]Generating comprehensive test report with verbose output...[/bold yellow]")
    report_file = report_generator.generate_markdown_report()
    
    # Stop Kafka
    console.print("\n[bold yellow]Stopping Kafka infrastructure...[/bold yellow]")
    try:
        subprocess.run(["docker-compose", "down"], check=True, capture_output=True)
        console.print("[green]✓ Kafka stopped successfully![/green]")
    except subprocess.CalledProcessError:
        console.print("[red]✗ Failed to stop Kafka.[/red]")
    
    console.print(f"\n[bold green]✓ Test report generated: {report_file}[/bold green]")
    console.print(f"[dim]Report contains detailed test results, verbose output, and recommendations.[/dim]")
    
    return report_file


if __name__ == "__main__":
    import sys
    verbose = "--verbose" in sys.argv or "-v" in sys.argv
    run_all_tests_with_verbose_capture(verbose)
