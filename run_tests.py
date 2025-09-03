#!/usr/bin/env python3
"""
Kafka E2E Test Launcher
Simple launcher for the Kafka testing framework with rich menu interface
"""

import sys
import subprocess
from pathlib import Path

def main():
    """Launch the Kafka test menu"""
    # Check if test_kafka.py exists
    test_file = Path("test_kafka.py")
    if not test_file.exists():
        print("Error: test_kafka.py not found in current directory")
        sys.exit(1)
    
    # Run the test menu
    try:
        subprocess.run([sys.executable, "test_kafka.py", "--menu"], check=True)
    except subprocess.CalledProcessError:
        print("Error running test menu")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)

if __name__ == "__main__":
    main()
