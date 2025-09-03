#!/usr/bin/env python3
"""
What to Run - Interactive Guide
Helps users understand which files to use for different purposes
"""

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich.table import Table
from rich.text import Text

console = Console()

def show_file_purpose():
    """Show what each file does"""
    table = Table(title="📁 File Purpose Guide", show_header=True, header_style="bold blue")
    table.add_column("File", style="cyan", no_wrap=True)
    table.add_column("Purpose", style="white")
    table.add_column("When to Use", style="green")
    
    table.add_row("test_kafka.py", "Main test suite with interactive menu", "🎯 Use this most of the time")
    table.add_row("verbose_test_capture.py", "Generate detailed reports", "📊 When you need documentation")
    table.add_row("run_tests.py", "Simple launcher script", "🚀 Quick alternative to test_kafka.py")
    table.add_row("example.py", "Basic usage example", "📚 Learning reference only")
    table.add_row("kafka_client.py", "Internal Kafka wrapper", "⚙️ Used automatically")
    table.add_row("conftest.py", "Pytest configuration", "⚙️ Used automatically")
    
    console.print(table)

def show_common_commands():
    """Show most common commands"""
    table = Table(title="🚀 Most Common Commands", show_header=True, header_style="bold green")
    table.add_column("Command", style="cyan", no_wrap=True)
    table.add_column("What It Does", style="white")
    
    table.add_row("python test_kafka.py --menu", "Opens interactive menu with 16 test options")
    table.add_row("python verbose_test_capture.py --verbose", "Generates comprehensive markdown report")
    table.add_row("python run_tests.py", "Quick launcher (same as menu)")
    table.add_row("pytest test_kafka.py -v", "Run all tests directly")
    
    console.print(table)

def show_use_cases():
    """Show different use cases"""
    console.print("\n[bold blue]🎯 Use Cases:[/bold blue]")
    
    console.print("\n[bold green]1. Interactive Testing (Recommended)[/bold green]")
    console.print("   Command: [cyan]python test_kafka.py --menu[/cyan]")
    console.print("   What you get: 16 test options, real-time verbose output, individual test execution")
    
    console.print("\n[bold green]2. Generate Documentation Report[/bold green]")
    console.print("   Command: [cyan]python verbose_test_capture.py --verbose[/cyan]")
    console.print("   What you get: Detailed markdown report with verbose output for each test")
    
    console.print("\n[bold green]3. Quick Start[/bold green]")
    console.print("   Command: [cyan]python run_tests.py[/cyan]")
    console.print("   What you get: Same as #1, just a different launcher")
    
    console.print("\n[bold green]4. Direct Testing[/bold green]")
    console.print("   Command: [cyan]pytest test_kafka.py -v[/cyan]")
    console.print("   What you get: Run all tests directly without menu")

def main():
    """Main interactive guide"""
    welcome_text = Text("Kafka E2E Testing Suite - What to Run Guide", style="bold blue")
    welcome_panel = Panel(welcome_text, title="Guide", border_style="blue", padding=(1, 2))
    console.print(welcome_panel)
    
    while True:
        console.print("\n[bold yellow]What would you like to know?[/bold yellow]")
        console.print("1. 📁 What each file does")
        console.print("2. 🚀 Most common commands")
        console.print("3. 🎯 Use cases and examples")
        console.print("4. 🚨 Quick troubleshooting")
        console.print("5. 🏃‍♂️ Just run the main menu")
        console.print("6. 📊 Generate a report")
        console.print("7. ❌ Exit")
        
        choice = Prompt.ask("Choose an option", choices=["1", "2", "3", "4", "5", "6", "7"], default="1")
        
        if choice == "1":
            show_file_purpose()
        elif choice == "2":
            show_common_commands()
        elif choice == "3":
            show_use_cases()
        elif choice == "4":
            console.print("\n[bold red]🚨 Quick Troubleshooting:[/bold red]")
            console.print("\n[bold]Problem:[/bold] 'NoBrokersAvailable' error")
            console.print("[green]Solution:[/green] docker-compose up -d (wait 5 seconds)")
            
            console.print("\n[bold]Problem:[/bold] 'Port already in use'")
            console.print("[green]Solution:[/green] docker-compose down && docker-compose up -d")
            
            console.print("\n[bold]Problem:[/bold] Import errors")
            console.print("[green]Solution:[/green] pip install -r requirements.txt")
            
            console.print("\n[bold]Problem:[/bold] Permission denied")
            console.print("[green]Solution:[/green] chmod +x run_tests.py")
            
        elif choice == "5":
            if Confirm.ask("Run the main interactive menu?"):
                console.print("\n[green]Starting main menu...[/green]")
                import subprocess
                subprocess.run(["python", "test_kafka.py", "--menu"])
            break
        elif choice == "6":
            if Confirm.ask("Generate a comprehensive report?"):
                console.print("\n[green]Generating report...[/green]")
                import subprocess
                subprocess.run(["python", "verbose_test_capture.py", "--verbose"])
            break
        elif choice == "7":
            console.print("\n[green]Goodbye! 👋[/green]")
            break
        
        if choice in ["1", "2", "3", "4"]:
            if not Confirm.ask("\nContinue with guide?"):
                break

if __name__ == "__main__":
    main()
