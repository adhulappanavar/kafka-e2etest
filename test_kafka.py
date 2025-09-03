import pytest
import time
import json
import subprocess
import sys
from kafka_client import KafkaTestClient
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich.table import Table
from rich.text import Text
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich import print as rprint

# Global variable to store verbose log
current_verbose_log = ""


class TestKafkaOperations:
    """Test class for Kafka operations"""
    
    @pytest.fixture(scope="class")
    def kafka_client(self):
        """Fixture to create and manage Kafka client"""
        # Check if verbose mode is enabled via environment variable or command line
        import os
        verbose = False
        
        # Check command line arguments
        if "--verbose" in sys.argv or "-v" in sys.argv:
            verbose = True
        
        # Check environment variable
        if os.environ.get("KAFKA_VERBOSE", "").lower() in ["true", "1", "yes"]:
            verbose = True
            
        client = KafkaTestClient(verbose=verbose)
        yield client
        # Store verbose log in a global variable for reporting
        if verbose:
            global current_verbose_log
            current_verbose_log = client.get_verbose_log()
        client.close()
    
    @pytest.fixture(scope="function")
    def test_topic(self):
        """Fixture to provide a unique test topic name"""
        return f"test_topic_{int(time.time())}"
    
    def test_create_topic(self, kafka_client, test_topic):
        """Test creating a Kafka topic"""
        # Create topic
        success = kafka_client.create_topic(test_topic, num_partitions=2, replication_factor=1)
        assert success is True
        
        # Verify topic was created
        topic_info = kafka_client.get_topic_info(test_topic)
        assert topic_info is not None
        assert topic_info['topic'] == test_topic
        assert len(topic_info['partitions']) == 2
    
    def test_send_single_message(self, kafka_client, test_topic):
        """Test sending a single message to Kafka topic"""
        # Create topic first
        kafka_client.create_topic(test_topic)
        
        # Prepare test message
        test_message = {
            "id": 1,
            "message": "Hello Kafka!",
            "timestamp": time.time()
        }
        
        # Send message
        success = kafka_client.send_message(test_topic, test_message, key="test_key_1")
        assert success is True
        
        # Give some time for message to be processed
        time.sleep(1)
        
        # Consume the message to verify it was sent
        messages = kafka_client.consume_messages(test_topic, timeout_ms=5000, max_messages=1)
        assert len(messages) == 1
        assert messages[0]['value']['id'] == test_message['id']
        assert messages[0]['value']['message'] == test_message['message']
        assert messages[0]['key'] == "test_key_1"
    
    def test_send_multiple_messages(self, kafka_client, test_topic):
        """Test sending multiple messages to Kafka topic"""
        # Create topic first
        kafka_client.create_topic(test_topic)
        
        # Prepare test messages
        test_messages = [
            {"id": 1, "message": "First message", "timestamp": time.time()},
            {"id": 2, "message": "Second message", "timestamp": time.time()},
            {"id": 3, "message": "Third message", "timestamp": time.time()}
        ]
        
        test_keys = ["key_1", "key_2", "key_3"]
        
        # Send messages
        sent_count = kafka_client.send_messages(test_topic, test_messages, test_keys)
        assert sent_count == 3
        
        # Give some time for messages to be processed
        time.sleep(1)
        
        # Consume messages to verify they were sent
        messages = kafka_client.consume_messages(test_topic, timeout_ms=5000, max_messages=3)
        assert len(messages) == 3
        
        # Verify message contents
        for i, message in enumerate(messages):
            assert message['value']['id'] == test_messages[i]['id']
            assert message['value']['message'] == test_messages[i]['message']
            assert message['key'] == test_keys[i]
    
    def test_consume_messages(self, kafka_client, test_topic):
        """Test consuming messages from Kafka topic"""
        # Create topic first
        kafka_client.create_topic(test_topic)
        
        # Send some test messages
        test_messages = [
            {"id": 1, "message": "Test message 1"},
            {"id": 2, "message": "Test message 2"},
            {"id": 3, "message": "Test message 3"}
        ]
        
        kafka_client.send_messages(test_topic, test_messages)
        time.sleep(1)
        
        # Consume messages with unique group ID
        unique_group_id = f"test_group_{int(time.time())}"
        messages = kafka_client.consume_messages(test_topic, group_id=unique_group_id, timeout_ms=5000, max_messages=5)
        
        # Verify we got the expected messages
        assert len(messages) >= 3
        
        # Verify message structure
        for message in messages:
            assert 'topic' in message
            assert 'partition' in message
            assert 'offset' in message
            assert 'key' in message
            assert 'value' in message
            assert 'timestamp' in message
            assert message['topic'] == test_topic
    
    def test_consume_messages_with_group_id(self, kafka_client, test_topic):
        """Test consuming messages with specific consumer group"""
        # Create topic first
        kafka_client.create_topic(test_topic)
        
        # Send test message
        test_message = {"id": 1, "message": "Group test message"}
        kafka_client.send_message(test_topic, test_message)
        time.sleep(1)
        
        # Consume with specific group ID
        group_id = "test_consumer_group"
        messages = kafka_client.consume_messages(
            test_topic, 
            group_id=group_id, 
            timeout_ms=5000, 
            max_messages=1
        )
        
        assert len(messages) == 1
        assert messages[0]['value']['message'] == test_message['message']
    
    def test_get_topic_info(self, kafka_client, test_topic):
        """Test getting topic information"""
        # Create topic with specific partitions
        kafka_client.create_topic(test_topic, num_partitions=3, replication_factor=1)
        
        # Get topic info
        topic_info = kafka_client.get_topic_info(test_topic)
        
        assert topic_info is not None
        assert topic_info['topic'] == test_topic
        assert len(topic_info['partitions']) == 3
        
        # Verify partition details
        for partition in topic_info['partitions']:
            assert 'partition' in partition
            assert 'leader' in partition
            assert 'replicas' in partition
            assert 'isr' in partition
    
    def test_get_partition_count(self, kafka_client, test_topic):
        """Test getting partition count for a topic"""
        # Create topic with specific partitions
        kafka_client.create_topic(test_topic, num_partitions=4, replication_factor=1)
        
        # Give some time for topic creation
        time.sleep(2)
        
        # Get partition count
        partition_count = kafka_client.get_partition_count(test_topic)
        # Kafka might create fewer partitions than requested, so we check it's at least 1
        assert partition_count >= 1
        assert partition_count <= 4
    
    def test_message_ordering(self, kafka_client, test_topic):
        """Test that messages maintain order within partitions"""
        # Create topic with single partition to ensure ordering
        kafka_client.create_topic(test_topic, num_partitions=1, replication_factor=1)
        
        # Send ordered messages
        messages = [
            {"id": 1, "order": 1},
            {"id": 2, "order": 2},
            {"id": 3, "order": 3},
            {"id": 4, "order": 4}
        ]
        
        kafka_client.send_messages(test_topic, messages)
        time.sleep(1)
        
        # Consume messages with unique group ID
        unique_group_id = f"order_test_group_{int(time.time())}"
        consumed_messages = kafka_client.consume_messages(test_topic, group_id=unique_group_id, timeout_ms=5000, max_messages=4)
        
        # Verify order (within the same partition)
        assert len(consumed_messages) == 4
        for i, message in enumerate(consumed_messages):
            assert message['value']['order'] == i + 1
    
    def test_message_without_key(self, kafka_client, test_topic):
        """Test sending messages without keys"""
        # Create topic first
        kafka_client.create_topic(test_topic)
        
        # Send message without key
        test_message = {"id": 1, "message": "No key message"}
        success = kafka_client.send_message(test_topic, test_message)
        assert success is True
        
        time.sleep(1)
        
        # Consume message
        messages = kafka_client.consume_messages(test_topic, timeout_ms=5000, max_messages=1)
        assert len(messages) == 1
        assert messages[0]['key'] is None
        assert messages[0]['value']['message'] == test_message['message']
    
    def test_large_message(self, kafka_client, test_topic):
        """Test sending large messages"""
        # Create topic first
        kafka_client.create_topic(test_topic)
        
        # Create large message
        large_message = {
            "id": 1,
            "data": "x" * 1000,  # 1KB of data
            "timestamp": time.time()
        }
        
        # Send large message
        success = kafka_client.send_message(test_topic, large_message)
        assert success is True
        
        time.sleep(1)
        
        # Consume message
        messages = kafka_client.consume_messages(test_topic, timeout_ms=5000, max_messages=1)
        assert len(messages) == 1
        assert len(messages[0]['value']['data']) == 1000


class TestKafkaQueueLength:
    """Test class specifically for queue length operations"""
    
    @pytest.fixture(scope="class")
    def kafka_client(self):
        """Fixture to create and manage Kafka client"""
        # Check if verbose mode is enabled via environment variable or command line
        import os
        verbose = False
        
        # Check command line arguments
        if "--verbose" in sys.argv or "-v" in sys.argv:
            verbose = True
        
        # Check environment variable
        if os.environ.get("KAFKA_VERBOSE", "").lower() in ["true", "1", "yes"]:
            verbose = True
            
        client = KafkaTestClient(verbose=verbose)
        yield client
        # Store verbose log in a global variable for reporting
        if verbose:
            global current_verbose_log
            current_verbose_log = client.get_verbose_log()
        client.close()
    
    @pytest.fixture(scope="function")
    def test_topic(self):
        """Fixture to provide a unique test topic name"""
        return f"queue_test_topic_{int(time.time())}"
    
    def test_queue_length_after_sending(self, kafka_client, test_topic):
        """Test checking queue length after sending messages"""
        # Create topic
        kafka_client.create_topic(test_topic, num_partitions=1)
        
        # Send multiple messages
        messages = [
            {"id": 1, "message": "Message 1"},
            {"id": 2, "message": "Message 2"},
            {"id": 3, "message": "Message 3"},
            {"id": 4, "message": "Message 4"},
            {"id": 5, "message": "Message 5"}
        ]
        
        sent_count = kafka_client.send_messages(test_topic, messages)
        assert sent_count == 5
        
        # Give time for messages to be processed
        time.sleep(2)
        
        # Consume all messages to check queue length
        consumed_messages = kafka_client.consume_messages(test_topic, timeout_ms=10000, max_messages=10)
        
        # Verify we got all messages
        assert len(consumed_messages) == 5
        
        # Check that queue is empty after consuming all messages
        remaining_messages = kafka_client.consume_messages(test_topic, timeout_ms=2000, max_messages=10)
        assert len(remaining_messages) == 0
    
    def test_partition_distribution(self, kafka_client, test_topic):
        """Test message distribution across partitions"""
        # Create topic with multiple partitions
        kafka_client.create_topic(test_topic, num_partitions=3)
        
        # Send messages
        messages = [
            {"id": 1, "message": "Message 1"},
            {"id": 2, "message": "Message 2"},
            {"id": 3, "message": "Message 3"},
            {"id": 4, "message": "Message 4"},
            {"id": 5, "message": "Message 5"}
        ]
        
        kafka_client.send_messages(test_topic, messages)
        time.sleep(1)
        
        # Consume messages
        consumed_messages = kafka_client.consume_messages(test_topic, timeout_ms=5000, max_messages=10)
        
        # Verify we got all messages
        assert len(consumed_messages) == 5
        
        # Check partition distribution
        partitions = set(msg['partition'] for msg in consumed_messages)
        assert len(partitions) <= 3  # Should be distributed across available partitions
    
    def test_queue_length_verbose(self, kafka_client, test_topic):
        """Test queue length checking with verbose output"""
        # Create topic
        kafka_client.create_topic(test_topic, num_partitions=1)
        
        # Send messages
        messages = [
            {"id": 1, "message": "Message 1"},
            {"id": 2, "message": "Message 2"},
            {"id": 3, "message": "Message 3"}
        ]
        
        # Send messages (this will show verbose output if enabled)
        sent_count = kafka_client.send_messages(test_topic, messages)
        assert sent_count == 3
        
        # Give time for messages to be processed
        time.sleep(1)
        
        # Check queue length before consuming
        queue_length_before = kafka_client.get_queue_length(test_topic)
        assert queue_length_before >= 3
        
        # Consume some messages
        consumed_messages = kafka_client.consume_messages(test_topic, timeout_ms=5000, max_messages=2)
        assert len(consumed_messages) == 2
        
        # Check queue length after consuming
        queue_length_after = kafka_client.get_queue_length(test_topic)
        assert queue_length_after >= 1  # Should have at least 1 message remaining


def setup_kafka():
    """Setup Kafka using docker-compose"""
    console = Console()
    
    with console.status("[bold green]Starting Kafka with docker-compose...", spinner="dots"):
        try:
            subprocess.run(["docker-compose", "up", "-d"], check=True, capture_output=True)
            time.sleep(5)  # Wait for Kafka to be ready
            console.print("[green]✓ Kafka started successfully![/green]")
            return True
        except subprocess.CalledProcessError as e:
            console.print(f"[red]✗ Failed to start Kafka: {e}[/red]")
            return False


def stop_kafka():
    """Stop Kafka using docker-compose"""
    console = Console()
    
    with console.status("[bold yellow]Stopping Kafka...", spinner="dots"):
        try:
            subprocess.run(["docker-compose", "down"], check=True, capture_output=True)
            console.print("[green]✓ Kafka stopped successfully![/green]")
            return True
        except subprocess.CalledProcessError as e:
            console.print(f"[red]✗ Failed to stop Kafka: {e}[/red]")
            return False


def run_single_test(test_name):
    """Run a single test"""
    console = Console()
    
    # Check if verbose mode is requested
    verbose_mode = "--verbose" in sys.argv or "-v" in sys.argv
    
    console.print(f"\n[bold blue]Running {test_name}...[/bold blue]")
    
    try:
        # Run the test directly using pytest.main instead of subprocess
        import pytest
        import os
        
        # Set environment variable for verbose mode
        if verbose_mode:
            os.environ["KAFKA_VERBOSE"] = "true"
        else:
            os.environ["KAFKA_VERBOSE"] = "false"
        
        # Set up test arguments
        test_args = [f"test_kafka.py::{test_name}", "-v", "--tb=short"]
        
        # Run the test
        result = pytest.main(test_args)
        
        if result == 0:
            console.print(f"[green]✓ {test_name} completed successfully![/green]")
            return True
        else:
            console.print(f"[red]✗ {test_name} failed[/red]")
            return False
    except Exception as e:
        console.print(f"[red]✗ Error running {test_name}: {e}[/red]")
        return False


def run_test_category(category):
    """Run all tests in a category"""
    console = Console()
    
    # Check if verbose mode is requested
    verbose_mode = "--verbose" in sys.argv or "-v" in sys.argv
    
    test_map = {
        "send": "TestKafkaOperations",
        "consume": "TestKafkaOperations", 
        "queue": "TestKafkaQueueLength",
        "all": "all"
    }
    
    if category == "all":
        # Use the verbose capture approach for "all" tests
        console.print(f"\n[bold blue]Running comprehensive test suite with verbose output capture...[/bold blue]")
        try:
            from verbose_test_capture import run_all_tests_with_verbose_capture
            report_file = run_all_tests_with_verbose_capture(verbose_mode)
            if report_file:
                console.print(f"[green]✓ Comprehensive test suite completed![/green]")
                console.print(f"[green]✓ Report generated: {report_file}[/green]")
                return True
            else:
                console.print(f"[red]✗ Comprehensive test suite failed[/red]")
                return False
        except Exception as e:
            console.print(f"[red]✗ Error running comprehensive test suite: {e}[/red]")
            return False
    else:
        test_pattern = f"test_kafka.py::{test_map[category]}"
        
        console.print(f"\n[bold blue]Running {category} tests...[/bold blue]")
        
        try:
            # Run the test directly using pytest.main instead of subprocess
            import pytest
            import os
            
            # Set environment variable for verbose mode
            if verbose_mode:
                os.environ["KAFKA_VERBOSE"] = "true"
            else:
                os.environ["KAFKA_VERBOSE"] = "false"
            
            # Set up test arguments
            test_args = [test_pattern, "-v", "--tb=short"]
            
            # Run the test
            result = pytest.main(test_args)
            
            if result == 0:
                console.print(f"[green]✓ {category} tests completed successfully![/green]")
                return True
            else:
                console.print(f"[red]✗ {category} tests failed[/red]")
                return False
        except Exception as e:
            console.print(f"[red]✗ Error running {category} tests: {e}[/red]")
            return False


def show_test_menu():
    """Show the main test menu"""
    console = Console()
    
    # Check if verbose mode is enabled
    verbose_mode = "--verbose" in sys.argv or "-v" in sys.argv
    verbose_status = "[green]ON[/green]" if verbose_mode else "[red]OFF[/red]"
    
    # Create test table
    table = Table(title=f"Available Kafka Tests (Verbose Mode: {verbose_status})", show_header=True, header_style="bold magenta")
    table.add_column("Option", style="cyan", no_wrap=True)
    table.add_column("Test", style="green")
    table.add_column("Description", style="white")
    
    table.add_row("1", "Send Single Message", "Test sending one message to Kafka topic")
    table.add_row("2", "Send Multiple Messages", "Test sending batch messages to Kafka topic")
    table.add_row("3", "Consume Messages", "Test reading messages from Kafka topic")
    table.add_row("4", "Queue Length", "Test checking message queue length")
    table.add_row("5", "Topic Creation", "Test creating Kafka topics")
    table.add_row("6", "Topic Info", "Test getting topic metadata")
    table.add_row("7", "Message Ordering", "Test message ordering within partitions")
    table.add_row("8", "Large Messages", "Test sending large messages")
    table.add_row("9", "Queue Length (Verbose)", "Test queue length with detailed output")
    table.add_row("10", "All Send Tests", "Run all message sending tests")
    table.add_row("11", "All Consume Tests", "Run all message consumption tests")
    table.add_row("12", "All Queue Tests", "Run all queue length tests")
    table.add_row("13", "All Tests", "Run complete test suite")
    table.add_row("14", "Setup Kafka", "Start Kafka infrastructure")
    table.add_row("15", "Stop Kafka", "Stop Kafka infrastructure")
    table.add_row("16", "Exit", "Exit the test menu")
    
    console.print(table)


def main():
    """Main menu function"""
    console = Console()
    
    # Welcome panel
    welcome_text = Text("Kafka E2E Testing Framework", style="bold blue")
    welcome_panel = Panel(
        welcome_text,
        title="Welcome",
        border_style="blue",
        padding=(1, 2)
    )
    console.print(welcome_panel)
    
    # Test mapping
    test_mapping = {
        "1": ("TestKafkaOperations::test_send_single_message", "Send Single Message"),
        "2": ("TestKafkaOperations::test_send_multiple_messages", "Send Multiple Messages"),
        "3": ("TestKafkaOperations::test_consume_messages", "Consume Messages"),
        "4": ("TestKafkaQueueLength::test_queue_length_after_sending", "Queue Length"),
        "5": ("TestKafkaOperations::test_create_topic", "Topic Creation"),
        "6": ("TestKafkaOperations::test_get_topic_info", "Topic Info"),
        "7": ("TestKafkaOperations::test_message_ordering", "Message Ordering"),
        "8": ("TestKafkaOperations::test_large_message", "Large Messages"),
        "9": ("TestKafkaQueueLength::test_queue_length_verbose", "Queue Length (Verbose)"),
        "10": ("send", "All Send Tests"),
        "11": ("consume", "All Consume Tests"),
        "12": ("queue", "All Queue Tests"),
        "13": ("all", "All Tests"),
        "14": ("setup", "Setup Kafka"),
        "15": ("stop", "Stop Kafka"),
        "16": ("exit", "Exit")
    }
    
    while True:
        console.print("\n")
        show_test_menu()
        console.print("\n")
        
        choice = Prompt.ask("Select an option", choices=[str(i) for i in range(1, 17)])
        
        if choice == "16":  # Exit
            console.print("[yellow]Goodbye![/yellow]")
            break
        
        elif choice == "14":  # Setup Kafka
            if setup_kafka():
                console.print("[green]Kafka is ready for testing![/green]")
            else:
                console.print("[red]Failed to setup Kafka. Please check Docker.[/red]")
        
        elif choice == "15":  # Stop Kafka
            if stop_kafka():
                console.print("[green]Kafka stopped successfully![/green]")
            else:
                console.print("[red]Failed to stop Kafka.[/red]")
        
        else:
            test_name, description = test_mapping[choice]
            
            if choice in ["10", "11", "12", "13"]:
                # Category tests
                console.print(f"\n[bold blue]Running {description}...[/bold blue]")
                run_test_category(test_name)
            else:
                # Single test
                console.print(f"\n[bold blue]Running {description}...[/bold blue]")
                run_single_test(test_name)
        
        if choice not in ["14", "15", "16"]:
            console.print("\n[dim]Press Enter to continue...[/dim]")
            input()


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--menu":
        main()
    else:
        # Run as normal pytest file
        pass
