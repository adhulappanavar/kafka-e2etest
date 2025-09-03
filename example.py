#!/usr/bin/env python3
"""
Simple example demonstrating Kafka operations:
a) Send messages to a topic
b) Read messages from topic  
c) Check queue length
"""

import time
from kafka_client import KafkaTestClient


def main():
    # Initialize Kafka client
    client = KafkaTestClient()
    
    # Create a test topic
    topic_name = f"example_topic_{int(time.time())}"
    print(f"Creating topic: {topic_name}")
    client.create_topic(topic_name, num_partitions=2)
    
    # A) Send messages to topic
    print("\n=== Sending Messages ===")
    messages = [
        {"id": 1, "message": "Hello Kafka!", "timestamp": time.time()},
        {"id": 2, "message": "This is a test message", "timestamp": time.time()},
        {"id": 3, "message": "Testing queue length", "timestamp": time.time()}
    ]
    
    sent_count = client.send_messages(topic_name, messages)
    print(f"Sent {sent_count} messages")
    
    # Give time for messages to be processed
    time.sleep(1)
    
    # B) Read messages from topic
    print("\n=== Reading Messages ===")
    consumed_messages = client.consume_messages(topic_name, timeout_ms=5000, max_messages=5)
    print(f"Consumed {len(consumed_messages)} messages:")
    
    for i, msg in enumerate(consumed_messages):
        print(f"  Message {i+1}: {msg['value']}")
    
    # C) Check queue length
    print("\n=== Checking Queue Length ===")
    # Consume any remaining messages to check if queue is empty
    remaining_messages = client.consume_messages(topic_name, timeout_ms=2000, max_messages=10)
    print(f"Remaining messages in queue: {len(remaining_messages)}")
    
    # Get topic info
    topic_info = client.get_topic_info(topic_name)
    if topic_info:
        partition_count = len(topic_info['partitions'])
        print(f"Topic has {partition_count} partitions")
    
    # Cleanup
    client.close()
    print("\n=== Example completed ===")


if __name__ == "__main__":
    main()
