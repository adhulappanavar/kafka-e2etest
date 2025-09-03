# Kafka E2E Test Report

## Test Summary

- **Test Session**: 2025-09-03 11:35:16 to 2025-09-03 11:37:42
- **Total Duration**: 145.72 seconds
- **Total Tests**: 13
- **Passed**: 13 ✅
- **Failed**: 0 ❌
- **Success Rate**: 100.0%

## Test Results

| Test Name | Status | Duration (s) | Details |
|-----------|--------|--------------|---------|
| TestKafkaOperations::test_create_topic | ✅ PASSED | 3.76 | test_index: 1; category: Topic Management; verbose_mode: True |
| TestKafkaOperations::test_send_single_message | ✅ PASSED | 10.33 | test_index: 2; category: Send Operations; verbose_mode: True |
| TestKafkaOperations::test_send_multiple_messages | ✅ PASSED | 10.61 | test_index: 3; category: Send Operations; verbose_mode: True |
| TestKafkaOperations::test_consume_messages | ✅ PASSED | 10.37 | test_index: 4; category: Consume Operations; verbose_mode: True |
| TestKafkaOperations::test_consume_messages_with_group_id | ✅ PASSED | 10.43 | test_index: 5; category: Consume Operations; verbose_mode: True |
| TestKafkaOperations::test_get_topic_info | ✅ PASSED | 8.83 | test_index: 6; category: Topic Management; verbose_mode: True |
| TestKafkaOperations::test_get_partition_count | ✅ PASSED | 11.75 | test_index: 7; category: Other; verbose_mode: True |
| TestKafkaOperations::test_message_ordering | ✅ PASSED | 10.67 | test_index: 8; category: Other; verbose_mode: True |
| TestKafkaOperations::test_message_without_key | ✅ PASSED | 10.91 | test_index: 9; category: Other; verbose_mode: True |
| TestKafkaOperations::test_large_message | ✅ PASSED | 10.64 | test_index: 10; category: Other; verbose_mode: True |
| TestKafkaQueueLength::test_queue_length_after_sending | ✅ PASSED | 14.57 | test_index: 11; category: Send Operations; verbose_mode: True |
| TestKafkaQueueLength::test_partition_distribution | ✅ PASSED | 12.94 | test_index: 12; category: Queue Length Operations; verbose_mode: True |
| TestKafkaQueueLength::test_queue_length_verbose | ✅ PASSED | 12.82 | test_index: 13; category: Queue Length Operations; verbose_mode: True |

## Detailed Test Information

### TestKafkaOperations::test_create_topic

- **Status**: PASSED
- **Duration**: 3.76 seconds
- **Timestamp**: 2025-09-03T11:35:27.276293

#### Test Details

**test_index**: 1

**category**: Topic Management

**verbose_mode**: True

#### Verbose Output

```
============================== test session starts ==============================
platform darwin -- Python 3.12.2, pytest-8.4.1, pluggy-1.5.0 -- /Users/anidhula/.pyenv/versions/3.12.2/bin/python
cachedir: .pytest_cache
rootdir: /Users/anidhula/learn/kafka-e2etest
configfile: pytest.ini
plugins: asyncio-1.1.0, cov-4.1.0, anyio-4.10.0, dash-2.14.2
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collecting ... collected 1 item

test_kafka.py::TestKafkaOperations::test_create_topic PASSED              [100%]

=============================== 1 passed in 2.28s ===============================

```

### TestKafkaOperations::test_send_single_message

- **Status**: PASSED
- **Duration**: 10.33 seconds
- **Timestamp**: 2025-09-03T11:35:37.602530

#### Test Details

**test_index**: 2

**category**: Send Operations

**verbose_mode**: True

#### Verbose Output

```
============================== test session starts ==============================
platform darwin -- Python 3.12.2, pytest-8.4.1, pluggy-1.5.0 -- /Users/anidhula/.pyenv/versions/3.12.2/bin/python
cachedir: .pytest_cache
rootdir: /Users/anidhula/learn/kafka-e2etest
configfile: pytest.ini
plugins: asyncio-1.1.0, cov-4.1.0, anyio-4.10.0, dash-2.14.2
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collecting ... collected 1 item

test_kafka.py::TestKafkaOperations::test_send_single_message PASSED       [100%]

============================== 1 passed in 10.11s ===============================


=== VERBOSE KAFKA OUTPUT ===
📤 Message Sent
Topic: test_topic_1756879532
Partition: 0
Offset: 0
Key: test_key_1
Message ID: 1
Message: Hello Kafka!
Timestamp: 1756879533.462236

📥 Message Consumed #1
Topic: test_topic_1756879532
Partition: 0
Offset: 0
Key: test_key_1
Message ID: 1
Message: Hello Kafka!
Timestamp: 1756879533582

```

### TestKafkaOperations::test_send_multiple_messages

- **Status**: PASSED
- **Duration**: 10.61 seconds
- **Timestamp**: 2025-09-03T11:35:48.213001

#### Test Details

**test_index**: 3

**category**: Send Operations

**verbose_mode**: True

#### Verbose Output

```
============================== test session starts ==============================
platform darwin -- Python 3.12.2, pytest-8.4.1, pluggy-1.5.0 -- /Users/anidhula/.pyenv/versions/3.12.2/bin/python
cachedir: .pytest_cache
rootdir: /Users/anidhula/learn/kafka-e2etest
configfile: pytest.ini
plugins: asyncio-1.1.0, cov-4.1.0, anyio-4.10.0, dash-2.14.2
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collecting ... collected 1 item

test_kafka.py::TestKafkaOperations::test_send_multiple_messages PASSED    [100%]

============================== 1 passed in 10.37s ===============================


=== VERBOSE KAFKA OUTPUT ===
📤 Message Sent #1
Topic: test_topic_1756879542
Partition: 0
Offset: 0
Key: key_1
Message ID: 1
Message: First message
Timestamp: 1756879544.017008

📤 Message Sent #2
Topic: test_topic_1756879542
Partition: 0
Offset: 1
Key: key_2
Message ID: 2
Message: Second message
Timestamp: 1756879544.017014

📤 Message Sent #3
Topic: test_topic_1756879542
Partition: 0
Offset: 2
Key: key_3
Message ID: 3
Message: Third message
Timestamp: 1756879544.0170188

📥 Message Consumed #1
Topic: test_topic_1756879542
Partition: 0
Offset: 0
Key: key_1
Message ID: 1
Message: First message
Timestamp: 1756879544136

📥 Message Consumed #2
Topic: test_topic_1756879542
Partition: 0
Offset: 1
Key: key_2
Message ID: 2
Message: Second message
Timestamp: 1756879544170

📥 Message Consumed #3
Topic: test_topic_1756879542
Partition: 0
Offset: 2
Key: key_3
Message ID: 3
Message: Third message
Timestamp: 1756879544174

```

### TestKafkaOperations::test_consume_messages

- **Status**: PASSED
- **Duration**: 10.37 seconds
- **Timestamp**: 2025-09-03T11:35:58.580083

#### Test Details

**test_index**: 4

**category**: Consume Operations

**verbose_mode**: True

#### Verbose Output

```
============================== test session starts ==============================
platform darwin -- Python 3.12.2, pytest-8.4.1, pluggy-1.5.0 -- /Users/anidhula/.pyenv/versions/3.12.2/bin/python
cachedir: .pytest_cache
rootdir: /Users/anidhula/learn/kafka-e2etest
configfile: pytest.ini
plugins: asyncio-1.1.0, cov-4.1.0, anyio-4.10.0, dash-2.14.2
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collecting ... collected 1 item

test_kafka.py::TestKafkaOperations::test_consume_messages PASSED          [100%]

============================== 1 passed in 10.14s ===============================


=== VERBOSE KAFKA OUTPUT ===
📤 Message Sent #1
Topic: test_topic_1756879553
Partition: 0
Offset: 0
Key: None
Message ID: 1
Message: Test message 1
Timestamp: N/A

📤 Message Sent #2
Topic: test_topic_1756879553
Partition: 0
Offset: 1
Key: None
Message ID: 2
Message: Test message 2
Timestamp: N/A

📤 Message Sent #3
Topic: test_topic_1756879553
Partition: 0
Offset: 2
Key: None
Message ID: 3
Message: Test message 3
Timestamp: N/A

📥 Message Consumed #1
Topic: test_topic_1756879553
Partition: 0
Offset: 0
Key: None
Message ID: 1
Message: Test message 1
Timestamp: 1756879554547

📥 Message Consumed #2
Topic: test_topic_1756879553
Partition: 0
Offset: 1
Key: None
Message ID: 2
Message: Test message 2
Timestamp: 1756879554579

📥 Message Consumed #3
Topic: test_topic_1756879553
Partition: 0
Offset: 2
Key: None
Message ID: 3
Message: Test message 3
Timestamp: 1756879554583

```

### TestKafkaOperations::test_consume_messages_with_group_id

- **Status**: PASSED
- **Duration**: 10.43 seconds
- **Timestamp**: 2025-09-03T11:36:09.013767

#### Test Details

**test_index**: 5

**category**: Consume Operations

**verbose_mode**: True

#### Verbose Output

```
============================== test session starts ==============================
platform darwin -- Python 3.12.2, pytest-8.4.1, pluggy-1.5.0 -- /Users/anidhula/.pyenv/versions/3.12.2/bin/python
cachedir: .pytest_cache
rootdir: /Users/anidhula/learn/kafka-e2etest
configfile: pytest.ini
plugins: asyncio-1.1.0, cov-4.1.0, anyio-4.10.0, dash-2.14.2
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collecting ... collected 1 item

test_kafka.py::TestKafkaOperations::test_consume_messages_with_group_id PASSED [100%]

============================== 1 passed in 10.18s ===============================


=== VERBOSE KAFKA OUTPUT ===
📤 Message Sent
Topic: test_topic_1756879563
Partition: 0
Offset: 0
Key: None
Message ID: 1
Message: Group test message
Timestamp: N/A

📥 Message Consumed #1
Topic: test_topic_1756879563
Partition: 0
Offset: 0
Key: None
Message ID: 1
Message: Group test message
Timestamp: 1756879564674

```

### TestKafkaOperations::test_get_topic_info

- **Status**: PASSED
- **Duration**: 8.83 seconds
- **Timestamp**: 2025-09-03T11:36:17.841339

#### Test Details

**test_index**: 6

**category**: Topic Management

**verbose_mode**: True

#### Verbose Output

```
============================== test session starts ==============================
platform darwin -- Python 3.12.2, pytest-8.4.1, pluggy-1.5.0 -- /Users/anidhula/.pyenv/versions/3.12.2/bin/python
cachedir: .pytest_cache
rootdir: /Users/anidhula/learn/kafka-e2etest
configfile: pytest.ini
plugins: asyncio-1.1.0, cov-4.1.0, anyio-4.10.0, dash-2.14.2
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collecting ... collected 1 item

test_kafka.py::TestKafkaOperations::test_get_topic_info PASSED            [100%]

=============================== 1 passed in 8.54s ===============================

```

### TestKafkaOperations::test_get_partition_count

- **Status**: PASSED
- **Duration**: 11.75 seconds
- **Timestamp**: 2025-09-03T11:36:29.590192

#### Test Details

**test_index**: 7

**category**: Other

**verbose_mode**: True

#### Verbose Output

```
============================== test session starts ==============================
platform darwin -- Python 3.12.2, pytest-8.4.1, pluggy-1.5.0 -- /Users/anidhula/.pyenv/versions/3.12.2/bin/python
cachedir: .pytest_cache
rootdir: /Users/anidhula/learn/kafka-e2etest
configfile: pytest.ini
plugins: asyncio-1.1.0, cov-4.1.0, anyio-4.10.0, dash-2.14.2
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collecting ... collected 1 item

test_kafka.py::TestKafkaOperations::test_get_partition_count PASSED       [100%]

============================== 1 passed in 11.51s ===============================

```

### TestKafkaOperations::test_message_ordering

- **Status**: PASSED
- **Duration**: 10.67 seconds
- **Timestamp**: 2025-09-03T11:36:40.256449

#### Test Details

**test_index**: 8

**category**: Other

**verbose_mode**: True

#### Verbose Output

```
============================== test session starts ==============================
platform darwin -- Python 3.12.2, pytest-8.4.1, pluggy-1.5.0 -- /Users/anidhula/.pyenv/versions/3.12.2/bin/python
cachedir: .pytest_cache
rootdir: /Users/anidhula/learn/kafka-e2etest
configfile: pytest.ini
plugins: asyncio-1.1.0, cov-4.1.0, anyio-4.10.0, dash-2.14.2
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collecting ... collected 1 item

test_kafka.py::TestKafkaOperations::test_message_ordering PASSED          [100%]

============================== 1 passed in 10.41s ===============================


=== VERBOSE KAFKA OUTPUT ===
📤 Message Sent #1
Topic: test_topic_1756879594
Partition: 0
Offset: 0
Key: None
Message ID: 1
Message: N/A
Timestamp: N/A

📤 Message Sent #2
Topic: test_topic_1756879594
Partition: 0
Offset: 1
Key: None
Message ID: 2
Message: N/A
Timestamp: N/A

📤 Message Sent #3
Topic: test_topic_1756879594
Partition: 0
Offset: 2
Key: None
Message ID: 3
Message: N/A
Timestamp: N/A

📤 Message Sent #4
Topic: test_topic_1756879594
Partition: 0
Offset: 3
Key: None
Message ID: 4
Message: N/A
Timestamp: N/A

📥 Message Consumed #1
Topic: test_topic_1756879594
Partition: 0
Offset: 0
Key: None
Message ID: 1
Message: N/A
Timestamp: 1756879596243

📥 Message Consumed #2
Topic: test_topic_1756879594
Partition: 0
Offset: 1
Key: None
Message ID: 2
Message: N/A
Timestamp: 1756879596275

📥 Message Consumed #3
Topic: test_topic_1756879594
Partition: 0
Offset: 2
Key: None
Message ID: 3
Message: N/A
Timestamp: 1756879596279

📥 Message Consumed #4
Topic: test_topic_1756879594
Partition: 0
Offset: 3
Key: None
Message ID: 4
Message: N/A
Timestamp: 1756879596283

```

### TestKafkaOperations::test_message_without_key

- **Status**: PASSED
- **Duration**: 10.91 seconds
- **Timestamp**: 2025-09-03T11:36:51.169777

#### Test Details

**test_index**: 9

**category**: Other

**verbose_mode**: True

#### Verbose Output

```
============================== test session starts ==============================
platform darwin -- Python 3.12.2, pytest-8.4.1, pluggy-1.5.0 -- /Users/anidhula/.pyenv/versions/3.12.2/bin/python
cachedir: .pytest_cache
rootdir: /Users/anidhula/learn/kafka-e2etest
configfile: pytest.ini
plugins: asyncio-1.1.0, cov-4.1.0, anyio-4.10.0, dash-2.14.2
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collecting ... collected 1 item

test_kafka.py::TestKafkaOperations::test_message_without_key PASSED       [100%]

============================== 1 passed in 10.67s ===============================


=== VERBOSE KAFKA OUTPUT ===
📤 Message Sent
Topic: test_topic_1756879605
Partition: 0
Offset: 0
Key: None
Message ID: 1
Message: No key message
Timestamp: N/A

📥 Message Consumed #1
Topic: test_topic_1756879605
Partition: 0
Offset: 0
Key: None
Message ID: 1
Message: No key message
Timestamp: 1756879606999

```

### TestKafkaOperations::test_large_message

- **Status**: PASSED
- **Duration**: 10.64 seconds
- **Timestamp**: 2025-09-03T11:37:01.815038

#### Test Details

**test_index**: 10

**category**: Other

**verbose_mode**: True

#### Verbose Output

```
============================== test session starts ==============================
platform darwin -- Python 3.12.2, pytest-8.4.1, pluggy-1.5.0 -- /Users/anidhula/.pyenv/versions/3.12.2/bin/python
cachedir: .pytest_cache
rootdir: /Users/anidhula/learn/kafka-e2etest
configfile: pytest.ini
plugins: asyncio-1.1.0, cov-4.1.0, anyio-4.10.0, dash-2.14.2
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collecting ... collected 1 item

test_kafka.py::TestKafkaOperations::test_large_message PASSED             [100%]

============================== 1 passed in 10.38s ===============================


=== VERBOSE KAFKA OUTPUT ===
📤 Message Sent
Topic: test_topic_1756879616
Partition: 0
Offset: 0
Key: None
Message ID: 1
Message: N/A
Timestamp: 1756879617.641097

📥 Message Consumed #1
Topic: test_topic_1756879616
Partition: 0
Offset: 0
Key: None
Message ID: 1
Message: N/A
Timestamp: 1756879617761

```

### TestKafkaQueueLength::test_queue_length_after_sending

- **Status**: PASSED
- **Duration**: 14.57 seconds
- **Timestamp**: 2025-09-03T11:37:16.382325

#### Test Details

**test_index**: 11

**category**: Send Operations

**verbose_mode**: True

#### Verbose Output

```
============================== test session starts ==============================
platform darwin -- Python 3.12.2, pytest-8.4.1, pluggy-1.5.0 -- /Users/anidhula/.pyenv/versions/3.12.2/bin/python
cachedir: .pytest_cache
rootdir: /Users/anidhula/learn/kafka-e2etest
configfile: pytest.ini
plugins: asyncio-1.1.0, cov-4.1.0, anyio-4.10.0, dash-2.14.2
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collecting ... collected 1 item

test_kafka.py::TestKafkaQueueLength::test_queue_length_after_sending PASSED [100%]

============================== 1 passed in 14.31s ===============================


=== VERBOSE KAFKA OUTPUT ===
📤 Message Sent #1
Topic: queue_test_topic_1756879629
Partition: 0
Offset: 0
Key: None
Message ID: 1
Message: Message 1
Timestamp: N/A

📤 Message Sent #2
Topic: queue_test_topic_1756879629
Partition: 0
Offset: 1
Key: None
Message ID: 2
Message: Message 2
Timestamp: N/A

📤 Message Sent #3
Topic: queue_test_topic_1756879629
Partition: 0
Offset: 2
Key: None
Message ID: 3
Message: Message 3
Timestamp: N/A

📤 Message Sent #4
Topic: queue_test_topic_1756879629
Partition: 0
Offset: 3
Key: None
Message ID: 4
Message: Message 4
Timestamp: N/A

📤 Message Sent #5
Topic: queue_test_topic_1756879629
Partition: 0
Offset: 4
Key: None
Message ID: 5
Message: Message 5
Timestamp: N/A

📥 Message Consumed #1
Topic: queue_test_topic_1756879629
Partition: 0
Offset: 0
Key: None
Message ID: 1
Message: Message 1
Timestamp: 1756879629238

📥 Message Consumed #2
Topic: queue_test_topic_1756879629
Partition: 0
Offset: 1
Key: None
Message ID: 2
Message: Message 2
Timestamp: 1756879629273

📥 Message Consumed #3
Topic: queue_test_topic_1756879629
Partition: 0
Offset: 2
Key: None
Message ID: 3
Message: Message 3
Timestamp: 1756879629277

📥 Message Consumed #4
Topic: queue_test_topic_1756879629
Partition: 0
Offset: 3
Key: None
Message ID: 4
Message: Message 4
Timestamp: 1756879629281

📥 Message Consumed #5
Topic: queue_test_topic_1756879629
Partition: 0
Offset: 4
Key: None
Message ID: 5
Message: Message 5
Timestamp: 1756879629284

```

### TestKafkaQueueLength::test_partition_distribution

- **Status**: PASSED
- **Duration**: 12.94 seconds
- **Timestamp**: 2025-09-03T11:37:29.318941

#### Test Details

**test_index**: 12

**category**: Queue Length Operations

**verbose_mode**: True

#### Verbose Output

```
============================== test session starts ==============================
platform darwin -- Python 3.12.2, pytest-8.4.1, pluggy-1.5.0 -- /Users/anidhula/.pyenv/versions/3.12.2/bin/python
cachedir: .pytest_cache
rootdir: /Users/anidhula/learn/kafka-e2etest
configfile: pytest.ini
plugins: asyncio-1.1.0, cov-4.1.0, anyio-4.10.0, dash-2.14.2
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collecting ... collected 1 item

test_kafka.py::TestKafkaQueueLength::test_partition_distribution PASSED   [100%]

============================== 1 passed in 12.65s ===============================


=== VERBOSE KAFKA OUTPUT ===
📤 Message Sent #1
Topic: queue_test_topic_1756879644
Partition: 0
Offset: 0
Key: None
Message ID: 1
Message: Message 1
Timestamp: N/A

📤 Message Sent #2
Topic: queue_test_topic_1756879644
Partition: 2
Offset: 0
Key: None
Message ID: 2
Message: Message 2
Timestamp: N/A

📤 Message Sent #3
Topic: queue_test_topic_1756879644
Partition: 0
Offset: 1
Key: None
Message ID: 3
Message: Message 3
Timestamp: N/A

📤 Message Sent #4
Topic: queue_test_topic_1756879644
Partition: 0
Offset: 2
Key: None
Message ID: 4
Message: Message 4
Timestamp: N/A

📤 Message Sent #5
Topic: queue_test_topic_1756879644
Partition: 1
Offset: 0
Key: None
Message ID: 5
Message: Message 5
Timestamp: N/A

📥 Message Consumed #1
Topic: queue_test_topic_1756879644
Partition: 0
Offset: 0
Key: None
Message ID: 1
Message: Message 1
Timestamp: 1756879644828

📥 Message Consumed #2
Topic: queue_test_topic_1756879644
Partition: 0
Offset: 1
Key: None
Message ID: 3
Message: Message 3
Timestamp: 1756879644868

📥 Message Consumed #3
Topic: queue_test_topic_1756879644
Partition: 0
Offset: 2
Key: None
Message ID: 4
Message: Message 4
Timestamp: 1756879644872

📥 Message Consumed #4
Topic: queue_test_topic_1756879644
Partition: 1
Offset: 0
Key: None
Message ID: 5
Message: Message 5
Timestamp: 1756879644875

📥 Message Consumed #5
Topic: queue_test_topic_1756879644
Partition: 2
Offset: 0
Key: None
Message ID: 2
Message: Message 2
Timestamp: 1756879644864

```

### TestKafkaQueueLength::test_queue_length_verbose

- **Status**: PASSED
- **Duration**: 12.82 seconds
- **Timestamp**: 2025-09-03T11:37:42.136830

#### Test Details

**test_index**: 13

**category**: Queue Length Operations

**verbose_mode**: True

#### Verbose Output

```
============================== test session starts ==============================
platform darwin -- Python 3.12.2, pytest-8.4.1, pluggy-1.5.0 -- /Users/anidhula/.pyenv/versions/3.12.2/bin/python
cachedir: .pytest_cache
rootdir: /Users/anidhula/learn/kafka-e2etest
configfile: pytest.ini
plugins: asyncio-1.1.0, cov-4.1.0, anyio-4.10.0, dash-2.14.2
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collecting ... collected 1 item

test_kafka.py::TestKafkaQueueLength::test_queue_length_verbose PASSED     [100%]

============================== 1 passed in 12.59s ===============================


=== VERBOSE KAFKA OUTPUT ===
📤 Message Sent #1
Topic: queue_test_topic_1756879656
Partition: 0
Offset: 0
Key: None
Message ID: 1
Message: Message 1
Timestamp: N/A

📤 Message Sent #2
Topic: queue_test_topic_1756879656
Partition: 0
Offset: 1
Key: None
Message ID: 2
Message: Message 2
Timestamp: N/A

📤 Message Sent #3
Topic: queue_test_topic_1756879656
Partition: 0
Offset: 2
Key: None
Message ID: 3
Message: Message 3
Timestamp: N/A

📊 Queue Length Information
Topic: queue_test_topic_1756879656
Total Messages: 3
Read Messages: 0
Queue Length: 3

📥 Message Consumed #1
Topic: queue_test_topic_1756879656
Partition: 0
Offset: 0
Key: None
Message ID: 1
Message: Message 1
Timestamp: 1756879657061

📥 Message Consumed #2
Topic: queue_test_topic_1756879656
Partition: 0
Offset: 1
Key: None
Message ID: 2
Message: Message 2
Timestamp: 1756879657088

📊 Queue Length Information
Topic: queue_test_topic_1756879656
Total Messages: 3
Read Messages: 0
Queue Length: 3

```


## Test Categories Summary

### Send Operations
- **Tests**: 3
- **Passed**: 3
- **Success Rate**: 100.0%

### Consume Operations
- **Tests**: 2
- **Passed**: 2
- **Success Rate**: 100.0%

### Queue Length Operations
- **Tests**: 2
- **Passed**: 2
- **Success Rate**: 100.0%

### Topic Management
- **Tests**: 2
- **Passed**: 2
- **Success Rate**: 100.0%

### Other
- **Tests**: 4
- **Passed**: 4
- **Success Rate**: 100.0%


## Environment Information

- **Python Version**: 3.12.2 (main, Apr  6 2025, 19:39:36) [Clang 15.0.0 (clang-1500.3.9.4)]
- **Test Framework**: pytest
- **Verbose Mode**: Enabled
- **Report Generated**: 2025-09-03 11:37:42


## Recommendations

🎉 **All tests passed successfully!**

