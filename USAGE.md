# Quick Usage Guide

## 🚀 Most Common Commands

### 1. Interactive Testing (Use This!)
```bash
python test_kafka.py --menu
```
**What it does:** Opens a menu with 16 test options, shows verbose output in real-time

### 2. Generate Report (For Documentation)
```bash
python verbose_test_capture.py --verbose
```
**What it does:** Runs all tests individually, captures verbose output, generates markdown report

### 3. Quick Start
```bash
python run_tests.py
```
**What it does:** Same as #1, just a different launcher

## 📁 File Purpose Summary

| File | What It Does | When to Use |
|------|--------------|-------------|
| `test_kafka.py` | **Main testing with menu** | **Use this most of the time** |
| `verbose_test_capture.py` | **Generate reports** | **When you need documentation** |
| `run_tests.py` | Simple launcher | Alternative to test_kafka.py |
| `example.py` | Basic example | Learning reference only |
| `kafka_client.py` | Internal Kafka wrapper | Used automatically |
| `conftest.py` | Pytest setup | Used automatically |

## 🎯 What Each Test Does

### Send Tests
- **Send Single Message** - Send one message, see verbose output
- **Send Multiple Messages** - Send 3 messages, see all details
- **Message Without Key** - Test messages without keys
- **Large Message** - Test with big messages

### Consume Tests  
- **Consume Messages** - Read messages from topic
- **Consume with Group ID** - Test consumer groups
- **Message Ordering** - Verify message sequence

### Queue Length Tests
- **Queue Length After Sending** - Check queue after sending
- **Partition Distribution** - Test across partitions
- **Queue Length Verbose** - Queue info with details

### Topic Management
- **Create Topic** - Make new topics
- **Get Topic Info** - Topic details
- **Get Partition Count** - How many partitions

## 🔧 Verbose Mode

**Enable with:** `--verbose` flag or `KAFKA_VERBOSE=true`

**Shows:**
- 📤 What messages were sent (topic, partition, offset, content)
- 📥 What messages were read (same details)
- 📊 Queue length information (total, read, remaining)

## 📊 Reports

**Generate with:** `python verbose_test_capture.py --verbose`

**Contains:**
- Test results and timing
- Verbose output for each test
- Statistics and recommendations
- Saved as `kafka_test_report_YYYYMMDD_HHMMSS.md`

## 🐳 Docker Commands

```bash
# Start Kafka (tests do this automatically)
docker-compose up -d

# Stop Kafka (tests do this automatically)  
docker-compose down

# Check if running
docker-compose ps
```

## 🚨 Quick Fixes

**"NoBrokersAvailable":**
```bash
docker-compose up -d
# Wait 5 seconds, then try again
```

**"Port in use":**
```bash
docker-compose down
docker-compose up -d
```

**Import errors:**
```bash
pip install -r requirements.txt
```

## 🎯 TL;DR

1. **For testing:** `python test_kafka.py --menu`
2. **For reports:** `python verbose_test_capture.py --verbose`
3. **For learning:** Look at `example.py`
4. **For problems:** Check Docker is running with `docker-compose ps`
