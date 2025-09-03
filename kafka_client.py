import json
import time
from typing import List, Dict, Any, Optional
from kafka import KafkaProducer, KafkaConsumer
from kafka.admin import KafkaAdminClient, NewTopic
from kafka.errors import TopicAlreadyExistsError
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text


class KafkaTestClient:
    def __init__(self, bootstrap_servers: str = 'localhost:9092', verbose: bool = False):
        self.bootstrap_servers = bootstrap_servers
        self.verbose = verbose
        self.console = Console() if verbose else None
        self.producer = None
        self.consumer = None
        self.admin_client = None
        self.verbose_log = []  # Store verbose output for reporting
    
    def create_producer(self) -> KafkaProducer:
        """Create and return a Kafka producer"""
        if not self.producer:
            self.producer = KafkaProducer(
                bootstrap_servers=self.bootstrap_servers,
                value_serializer=lambda v: json.dumps(v).encode('utf-8'),
                key_serializer=lambda k: k.encode('utf-8') if k else None
            )
        return self.producer
    
    def create_consumer(self, topic: str, group_id: str = 'test_group') -> KafkaConsumer:
        """Create and return a Kafka consumer"""
        # Close existing consumer if it exists
        if self.consumer:
            self.consumer.close()
            self.consumer = None
            
        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=self.bootstrap_servers,
            group_id=group_id,
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            value_deserializer=lambda x: json.loads(x.decode('utf-8')),
            key_deserializer=lambda x: x.decode('utf-8') if x else None
        )
        return self.consumer
    
    def create_admin_client(self) -> KafkaAdminClient:
        """Create and return a Kafka admin client"""
        if not self.admin_client:
            self.admin_client = KafkaAdminClient(
                bootstrap_servers=self.bootstrap_servers
            )
        return self.admin_client
    
    def create_topic(self, topic_name: str, num_partitions: int = 1, replication_factor: int = 1) -> bool:
        """Create a Kafka topic"""
        try:
            admin_client = self.create_admin_client()
            topic = NewTopic(
                name=topic_name,
                num_partitions=num_partitions,
                replication_factor=replication_factor
            )
            admin_client.create_topics([topic])
            return True
        except TopicAlreadyExistsError:
            return True  # Topic already exists
        except Exception as e:
            print(f"Error creating topic: {e}")
            return False
    
    def send_message(self, topic: str, message: Dict[str, Any], key: Optional[str] = None) -> bool:
        """Send a message to a Kafka topic"""
        try:
            producer = self.create_producer()
            future = producer.send(topic, value=message, key=key)
            record_metadata = future.get(timeout=10)
            
            if self.verbose:
                self._log_message_sent(topic, message, key, record_metadata)
            
            return True
        except Exception as e:
            if self.verbose:
                self.console.print(f"[red]Error sending message: {e}[/red]")
            else:
                print(f"Error sending message: {e}")
            return False
    
    def send_messages(self, topic: str, messages: List[Dict[str, Any]], keys: Optional[List[str]] = None) -> int:
        """Send multiple messages to a Kafka topic"""
        sent_count = 0
        producer = self.create_producer()
        
        if self.verbose:
            self.console.print(f"\n[bold blue]📤 Sending {len(messages)} messages to topic '{topic}'[/bold blue]")
        
        for i, message in enumerate(messages):
            try:
                key = keys[i] if keys and i < len(keys) else None
                future = producer.send(topic, value=message, key=key)
                record_metadata = future.get(timeout=10)
                sent_count += 1
                
                if self.verbose:
                    self._log_message_sent(topic, message, key, record_metadata, message_index=i+1)
                    
            except Exception as e:
                if self.verbose:
                    self.console.print(f"[red]Error sending message {i}: {e}[/red]")
                else:
                    print(f"Error sending message {i}: {e}")
        
        if self.verbose:
            self.console.print(f"[green]✓ Successfully sent {sent_count}/{len(messages)} messages[/green]\n")
        
        return sent_count
    
    def consume_messages(self, topic: str, group_id: str = 'test_group', timeout_ms: int = 5000, max_messages: int = 10) -> List[Dict[str, Any]]:
        """Consume messages from a Kafka topic"""
        messages = []
        consumer = self.create_consumer(topic, group_id)
        
        if self.verbose:
            self.console.print(f"\n[bold green]📥 Consuming messages from topic '{topic}' (max: {max_messages})[/bold green]")
        
        try:
            # Poll for messages
            message_batch = consumer.poll(timeout_ms=timeout_ms)
            
            for tp, records in message_batch.items():
                for record in records:
                    message_data = {
                        'topic': record.topic,
                        'partition': record.partition,
                        'offset': record.offset,
                        'key': record.key,
                        'value': record.value,
                        'timestamp': record.timestamp
                    }
                    messages.append(message_data)
                    
                    if self.verbose:
                        self._log_message_consumed(message_data, len(messages))
                    
                    if len(messages) >= max_messages:
                        break
                if len(messages) >= max_messages:
                    break
                    
        except Exception as e:
            if self.verbose:
                self.console.print(f"[red]Error consuming messages: {e}[/red]")
            else:
                print(f"Error consuming messages: {e}")
        
        if self.verbose:
            self.console.print(f"[green]✓ Consumed {len(messages)} messages from topic '{topic}'[/green]\n")
        
        return messages
    
    def get_topic_info(self, topic: str) -> Optional[Dict[str, Any]]:
        """Get information about a Kafka topic"""
        try:
            admin_client = self.create_admin_client()
            metadata = admin_client.list_topics()
            
            if topic in metadata:
                topic_metadata = admin_client.describe_topics([topic])
                return topic_metadata[0]
            return None
        except Exception as e:
            print(f"Error getting topic info: {e}")
            return None
    
    def get_partition_count(self, topic: str) -> int:
        """Get the number of partitions for a topic"""
        topic_info = self.get_topic_info(topic)
        if topic_info and 'partitions' in topic_info:
            return len(topic_info['partitions'])
        return 0
    
    def _log_message_sent(self, topic: str, message: Dict[str, Any], key: Optional[str], record_metadata, message_index: int = None):
        """Log detailed information about a sent message"""
        index_text = f" #{message_index}" if message_index else ""
        
        # Create message details table
        table = Table(title=f"📤 Message Sent{index_text}", show_header=True, header_style="bold blue")
        table.add_column("Property", style="cyan", no_wrap=True)
        table.add_column("Value", style="white")
        
        table.add_row("Topic", topic)
        table.add_row("Partition", str(record_metadata.partition))
        table.add_row("Offset", str(record_metadata.offset))
        table.add_row("Key", str(key) if key else "None")
        table.add_row("Message ID", str(message.get('id', 'N/A')))
        table.add_row("Message", str(message.get('message', 'N/A')))
        table.add_row("Timestamp", str(message.get('timestamp', 'N/A')))
        
        self.console.print(table)
        
        # Store verbose output for reporting with Rich table formatting
        if self.verbose:
            # Capture the Rich table as markdown
            table_markdown = self._table_to_markdown(table)
            self.verbose_log.append(table_markdown)
            self.verbose_log.append("")
    
    def _log_message_consumed(self, message_data: Dict[str, Any], message_index: int):
        """Log detailed information about a consumed message"""
        # Create message details table
        table = Table(title=f"📥 Message Consumed #{message_index}", show_header=True, header_style="bold green")
        table.add_column("Property", style="cyan", no_wrap=True)
        table.add_column("Value", style="white")
        
        table.add_row("Topic", message_data['topic'])
        table.add_row("Partition", str(message_data['partition']))
        table.add_row("Offset", str(message_data['offset']))
        table.add_row("Key", str(message_data['key']) if message_data['key'] else "None")
        table.add_row("Message ID", str(message_data['value'].get('id', 'N/A')))
        table.add_row("Message", str(message_data['value'].get('message', 'N/A')))
        table.add_row("Timestamp", str(message_data['timestamp']))
        
        self.console.print(table)
        
        # Store verbose output for reporting with Rich table formatting
        if self.verbose:
            # Capture the Rich table as markdown
            table_markdown = self._table_to_markdown(table)
            self.verbose_log.append(table_markdown)
            self.verbose_log.append("")
    
    def get_queue_length(self, topic: str, group_id: str = 'test_group') -> int:
        """Get the current queue length (number of unread messages) for a topic"""
        if self.verbose:
            self.console.print(f"\n[bold yellow]📊 Checking queue length for topic '{topic}'[/bold yellow]")
        
        # Create a temporary consumer to check queue length
        temp_consumer = KafkaConsumer(
            topic,
            bootstrap_servers=self.bootstrap_servers,
            group_id=f"{group_id}_queue_check",
            auto_offset_reset='earliest',
            enable_auto_commit=False,
            value_deserializer=lambda x: json.loads(x.decode('utf-8')),
            key_deserializer=lambda x: x.decode('utf-8') if x else None
        )
        
        try:
            # Get end offset (total messages)
            partitions = temp_consumer.partitions_for_topic(topic)
            if not partitions:
                if self.verbose:
                    self.console.print("[red]No partitions found for topic[/red]")
                return 0
            
            total_messages = 0
            for partition in partitions:
                from kafka import TopicPartition
                tp = TopicPartition(topic, partition)
                end_offset = temp_consumer.end_offsets([tp])[tp]
                total_messages += end_offset
            
            # For a new consumer group, current position is 0
            current_messages = 0
            
            queue_length = total_messages - current_messages
            
            if self.verbose:
                table = Table(title="📊 Queue Length Information", show_header=True, header_style="bold yellow")
                table.add_column("Metric", style="cyan", no_wrap=True)
                table.add_column("Value", style="white")
                
                table.add_row("Topic", topic)
                table.add_row("Total Messages", str(total_messages))
                table.add_row("Read Messages", str(current_messages))
                table.add_row("Queue Length", str(queue_length))
                
                self.console.print(table)
                self.console.print(f"[green]✓ Queue length: {queue_length} messages[/green]\n")
                
                # Store verbose output for reporting with Rich table formatting
                table_markdown = self._table_to_markdown(table)
                self.verbose_log.append(table_markdown)
                self.verbose_log.append("")
            
            return queue_length
            
        finally:
            temp_consumer.close()
    
    def _table_to_markdown(self, table) -> str:
        """Convert a Rich table to markdown format"""
        # Get table title
        title = getattr(table, 'title', None)
        title_text = f"**{title}**\n\n" if title else ""
        
        # Get table data
        rows = []
        for row in table.rows:
            # Extract text from Rich Text objects
            row_data = []
            for cell in row.cells:
                if hasattr(cell, 'plain'):
                    row_data.append(cell.plain)
                else:
                    row_data.append(str(cell))
            rows.append(row_data)
        
        if not rows:
            return title_text + "No data available"
        
        # Create markdown table
        markdown = title_text
        markdown += "| " + " | ".join(rows[0]) + " |\n"
        markdown += "| " + " | ".join(["---"] * len(rows[0])) + " |\n"
        
        for row in rows[1:]:
            markdown += "| " + " | ".join(row) + " |\n"
        
        return markdown
    
    def get_verbose_log(self) -> str:
        """Get the verbose log as a string"""
        return "\n".join(self.verbose_log)
    
    def close(self):
        """Close all Kafka connections"""
        if self.producer:
            self.producer.close()
        if self.consumer:
            self.consumer.close()
        if self.admin_client:
            self.admin_client.close()
