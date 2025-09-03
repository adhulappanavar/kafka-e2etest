# Kafka E2E Testing Suite

A comprehensive pytest-based testing framework for Apache Kafka with interactive menu, verbose output, and detailed reporting capabilities.

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Docker and Docker Compose
- Git

### Installation
```bash
# Clone the repository
git clone <your-repo-url>
cd kafka-e2etest

# Install dependencies
pip install -r requirements.txt

# Start Kafka infrastructure
docker-compose up -d
```

### Basic Usage
```bash
# Interactive menu (recommended)
python test_kafka.py --menu

# Or use the launcher script
python run_tests.py
```

## 📁 File Structure & Purpose

### Core Files

| File | Purpose | When to Use |
|------|---------|-------------|
| `test_kafka.py` | **Main test suite with interactive menu** | **Primary entry point** - Use this for all testing |
| `kafka_client.py` | Kafka client wrapper with verbose logging | Used internally by tests |
| `conftest.py` | Pytest configuration and fixtures | Used internally by pytest |

### Report Generation

| File | Purpose | When to Use |
|------|---------|-------------|
| `test_report_generator.py` | Basic report generator | **Deprecated** - Use verbose_test_capture.py instead |
| `verbose_test_capture.py` | **Advanced report generator with verbose output** | **Use this for comprehensive reports** |

### Utilities

| File | Purpose | When to Use |
|------|---------|-------------|
| `run_tests.py` | Simple launcher script | Alternative to `python test_kafka.py --menu` |
| `example.py` | Basic usage example | Learning/development reference |
| `docker-compose.yml` | Kafka infrastructure setup | Used automatically by tests |
| `requirements.txt` | Python dependencies | Install with `pip install -r requirements.txt` |
| `pytest.ini` | Pytest configuration | Used automatically by pytest |

## 🎯 Usage Scenarios

### 1. Interactive Testing (Recommended)
```bash
# Start the interactive menu
python test_kafka.py --menu

# With verbose output
python test_kafka.py --menu --verbose
```

**What you get:**
- 16 different test options
- Real-time verbose output with Rich tables
- Individual test execution
- Category-based testing

### 2. Comprehensive Report Generation
```bash
# Generate detailed markdown report with verbose output
python verbose_test_capture.py --verbose
```

**What you get:**
- Individual test execution with output capture
- Detailed markdown report (`kafka_test_report_YYYYMMDD_HHMMSS.md`)
- Verbose output included in report
- Test statistics and recommendations

### 3. Direct Test Execution
```bash
# Run specific test
pytest test_kafka.py::TestKafkaOperations::test_send_single_message -v

# Run all tests
pytest test_kafka.py -v

# Run with verbose output
KAFKA_VERBOSE=true pytest test_kafka.py -v
```

### 4. Simple Launcher
```bash
# Quick start (same as interactive menu)
python run_tests.py
```

## 📊 Test Categories

### Send Operations
- `test_send_single_message` - Send one message to a topic
- `test_send_multiple_messages` - Send multiple messages
- `test_message_without_key` - Send messages without keys
- `test_large_message` - Send large messages

### Consume Operations
- `test_consume_messages` - Consume messages from topic
- `test_consume_messages_with_group_id` - Consume with specific group ID
- `test_message_ordering` - Verify message ordering

### Queue Length Operations
- `test_queue_length_after_sending` - Check queue length after sending
- `test_partition_distribution` - Test partition distribution
- `test_queue_length_verbose` - Queue length with verbose output

### Topic Management
- `test_create_topic` - Create new topics
- `test_get_topic_info` - Get topic information
- `test_get_partition_count` - Get partition count

## 🔧 Configuration

### Environment Variables
```bash
# Enable verbose mode
export KAFKA_VERBOSE=true

# Kafka bootstrap servers (default: localhost:9092)
export KAFKA_BOOTSTRAP_SERVERS=localhost:9092
```

### Verbose Mode
When enabled, verbose mode provides:
- 📤 **Message Sent Details**: Topic, partition, offset, key, message content, timestamp
- 📥 **Message Consumed Details**: Same details for consumed messages
- 📊 **Queue Length Information**: Total messages, read messages, current queue length

## 📈 Report Features

The generated markdown reports include:

### Test Summary
- Total duration and test count
- Pass/fail statistics
- Success rate percentage

### Detailed Test Information
- Individual test results with timing
- Verbose output for each test
- Test categorization

### Verbose Output Examples
```
📤 Message Sent
Topic: test_topic_1234567890
Partition: 0
Offset: 0
Key: test_key_1
Message ID: 1
Message: Hello Kafka!
Timestamp: 1756879093.057634

📥 Message Consumed #1
Topic: test_topic_1234567890
Partition: 0
Offset: 0
Key: test_key_1
Message ID: 1
Message: Hello Kafka!
Timestamp: 1756879093174

📊 Queue Length Information
Topic: test_topic_1234567890
Total Messages: 3
Read Messages: 0
Queue Length: 3
```

## 🐳 Docker Infrastructure

The test suite automatically manages Kafka infrastructure:

```bash
# Start Kafka (done automatically by tests)
docker-compose up -d

# Stop Kafka (done automatically by tests)
docker-compose down

# View logs
docker-compose logs -f
```

## 🚨 Troubleshooting

### Common Issues

1. **"NoBrokersAvailable" Error**
   ```bash
   # Ensure Kafka is running
   docker-compose up -d
   # Wait 5-10 seconds for Kafka to start
   ```

2. **Port Already in Use**
   ```bash
   # Stop existing containers
   docker-compose down
   # Start fresh
   docker-compose up -d
   ```

3. **Permission Denied**
   ```bash
   # Make scripts executable
   chmod +x run_tests.py
   ```

4. **Import Errors**
   ```bash
   # Reinstall dependencies
   pip install -r requirements.txt --force-reinstall
   ```

### Debug Mode
```bash
# Run with maximum verbosity
python test_kafka.py --menu --verbose -v

# Check Kafka status
docker-compose ps
docker-compose logs kafka
```

## 📝 Development

### Adding New Tests
1. Add test methods to `TestKafkaOperations` or `TestKafkaQueueLength` classes
2. Update test names in `verbose_test_capture.py` if using report generation
3. Test with: `pytest test_kafka.py::YourTestClass::your_test_method -v`

### Customizing Verbose Output
Modify `kafka_client.py` methods:
- `_log_message_sent()` - Customize sent message logging
- `_log_message_consumed()` - Customize consumed message logging
- `get_queue_length()` - Customize queue length logging

## 🎯 Quick Reference

| Command | Purpose |
|---------|---------|
| `python test_kafka.py --menu` | **Start interactive menu** |
| `python verbose_test_capture.py --verbose` | **Generate comprehensive report** |
| `python run_tests.py` | Quick launcher |
| `pytest test_kafka.py -v` | Run all tests directly |
| `docker-compose up -d` | Start Kafka manually |
| `docker-compose down` | Stop Kafka manually |

## 📋 Dependencies

- `pytest` - Testing framework
- `kafka-python` - Kafka client
- `confluent-kafka` - Advanced Kafka operations
- `rich` - Beautiful terminal output
- `pytest-html` - HTML report generation
- `PyYAML` - YAML configuration support

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

**Need help?** Check the troubleshooting section or open an issue on GitHub.