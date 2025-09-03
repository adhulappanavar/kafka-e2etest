# File Reference Guide

## 🎯 Primary Files (Use These)

| File | Purpose | Command |
|------|---------|---------|
| **`test_kafka.py`** | **Main test suite with interactive menu** | `python test_kafka.py --menu` |
| **`verbose_test_capture.py`** | **Generate detailed reports** | `python verbose_test_capture.py --verbose` |
| **`run_tests.py`** | Simple launcher | `python run_tests.py` |
| **`what_to_run.py`** | Interactive guide | `python what_to_run.py` |

## 📚 Documentation Files

| File | Purpose |
|------|---------|
| **`README.md`** | **Complete documentation** |
| **`USAGE.md`** | **Quick usage guide** |
| **`FILES.md`** | **This file - file reference** |

## ⚙️ Internal Files (Used Automatically)

| File | Purpose |
|------|---------|
| `kafka_client.py` | Kafka client wrapper with verbose logging |
| `conftest.py` | Pytest configuration and fixtures |
| `test_report_generator.py` | Basic report generator (deprecated) |

## 🐳 Infrastructure Files

| File | Purpose |
|------|---------|
| `docker-compose.yml` | Kafka and Zookeeper setup |
| `requirements.txt` | Python dependencies |
| `pytest.ini` | Pytest configuration |

## 📖 Example Files

| File | Purpose |
|------|---------|
| `example.py` | Basic usage example |

## 🗑️ Removed Files

These files were removed to reduce confusion:
- `run_verbose_test.py` (replaced by `verbose_test_capture.py`)
- `example_verbose.py` (functionality moved to main files)

## 🚀 Quick Start Commands

```bash
# Interactive testing (recommended)
python test_kafka.py --menu

# Generate report
python verbose_test_capture.py --verbose

# Quick launcher
python run_tests.py

# Get help
python what_to_run.py
```

## 📊 What Each Primary File Does

### `test_kafka.py`
- **Main entry point** for all testing
- Interactive menu with 16 test options
- Real-time verbose output with Rich tables
- Individual and category-based test execution
- **Use this for: Daily testing, development, debugging**

### `verbose_test_capture.py`
- Runs all tests individually
- Captures verbose output for each test
- Generates comprehensive markdown reports
- Includes test statistics and recommendations
- **Use this for: Documentation, CI/CD, reporting**

### `run_tests.py`
- Simple launcher script
- Same functionality as `test_kafka.py --menu`
- **Use this for: Quick access, automation**

### `what_to_run.py`
- Interactive guide explaining all files
- Helps users understand what to run when
- **Use this for: Learning, troubleshooting**

## 🎯 Decision Tree

**"I want to test Kafka"** → Use `test_kafka.py --menu`

**"I want a report"** → Use `verbose_test_capture.py --verbose`

**"I'm confused about files"** → Use `what_to_run.py`

**"I want to learn"** → Read `README.md` and `USAGE.md`

**"I want quick access"** → Use `run_tests.py`
