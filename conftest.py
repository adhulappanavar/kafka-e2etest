import pytest
import time
import subprocess
import os
from kafka_client import KafkaTestClient


def wait_for_kafka_ready():
    """Wait for Kafka to be ready"""
    max_attempts = 30
    attempt = 0
    
    while attempt < max_attempts:
        try:
            client = KafkaTestClient()
            # Try to list topics to check if Kafka is ready
            admin_client = client.create_admin_client()
            admin_client.list_topics()
            client.close()
            return True
        except Exception:
            attempt += 1
            time.sleep(2)
    
    return False


@pytest.fixture(scope="session", autouse=True)
def setup_kafka():
    """Setup Kafka using docker-compose before running tests"""
    print("Starting Kafka with docker-compose...")
    
    # Start Kafka
    subprocess.run(["docker-compose", "up", "-d"], check=True)
    
    # Wait for Kafka to be ready
    if not wait_for_kafka_ready():
        raise Exception("Kafka failed to start within expected time")
    
    print("Kafka is ready!")
    
    yield
    
    # Cleanup
    print("Stopping Kafka...")
    subprocess.run(["docker-compose", "down"], check=True)


@pytest.fixture(scope="function")
def kafka_client():
    """Provide a fresh Kafka client for each test"""
    client = KafkaTestClient()
    yield client
    client.close()


@pytest.fixture(scope="function")
def unique_topic():
    """Provide a unique topic name for each test"""
    return f"test_topic_{int(time.time() * 1000)}"
