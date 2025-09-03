# Kafka E2E Test Report

## Test Summary

- **Test Session**: 2025-09-03 11:27:57 to 2025-09-03 11:30:17
- **Total Duration**: 140.10 seconds
- **Total Tests**: 13
- **Passed**: 13 ✅
- **Failed**: 0 ❌
- **Success Rate**: 100.0%

## Test Results

| Test Name | Status | Duration (s) | Details |
|-----------|--------|--------------|---------|
| TestKafkaOperations::test_create_topic | ✅ PASSED | 3.54 | test_index: 1; category: Topic Management; verbose_mode: True |
| TestKafkaOperations::test_send_single_message | ✅ PASSED | 10.51 | test_index: 2; category: Send Operations; verbose_mode: True |
| TestKafkaOperations::test_send_multiple_messages | ✅ PASSED | 11.83 | test_index: 3; category: Send Operations; verbose_mode: True |
| TestKafkaOperations::test_consume_messages | ✅ PASSED | 10.44 | test_index: 4; category: Consume Operations; verbose_mode: True |
| TestKafkaOperations::test_consume_messages_with_group_id | ✅ PASSED | 10.53 | test_index: 5; category: Consume Operations; verbose_mode: True |
| TestKafkaOperations::test_get_topic_info | ✅ PASSED | 8.28 | test_index: 6; category: Topic Management; verbose_mode: True |
| TestKafkaOperations::test_get_partition_count | ✅ PASSED | 10.09 | test_index: 7; category: Other; verbose_mode: True |
| TestKafkaOperations::test_message_ordering | ✅ PASSED | 10.60 | test_index: 8; category: Other; verbose_mode: True |
| TestKafkaOperations::test_message_without_key | ✅ PASSED | 11.77 | test_index: 9; category: Other; verbose_mode: True |
| TestKafkaOperations::test_large_message | ✅ PASSED | 10.39 | test_index: 10; category: Other; verbose_mode: True |
| TestKafkaQueueLength::test_queue_length_after_sending | ✅ PASSED | 13.99 | test_index: 11; category: Send Operations; verbose_mode: True |
| TestKafkaQueueLength::test_partition_distribution | ✅ PASSED | 10.49 | test_index: 12; category: Queue Length Operations; verbose_mode: True |
| TestKafkaQueueLength::test_queue_length_verbose | ✅ PASSED | 11.66 | test_index: 13; category: Queue Length Operations; verbose_mode: True |

## Detailed Test Information

### TestKafkaOperations::test_create_topic

- **Status**: PASSED
- **Duration**: 3.54 seconds
- **Timestamp**: 2025-09-03T11:28:06.982500

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

=============================== 1 passed in 2.16s ===============================

```

### TestKafkaOperations::test_send_single_message

- **Status**: PASSED
- **Duration**: 10.51 seconds
- **Timestamp**: 2025-09-03T11:28:17.490155

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

=============================== 1 passed in 9.96s ===============================


=== VERBOSE KAFKA OUTPUT ===
📤 Message Sent
Topic: test_topic_1756879091
Partition: 0
Offset: 0
Key: test_key_1
Message ID: 1
Message: Hello Kafka!
Timestamp: 1756879093.057634

📥 Message Consumed #1
Topic: test_topic_1756879091
Partition: 0
Offset: 0
Key: test_key_1
Message ID: 1
Message: Hello Kafka!
Timestamp: 1756879093174

```

### TestKafkaOperations::test_send_multiple_messages

- **Status**: PASSED
- **Duration**: 11.83 seconds
- **Timestamp**: 2025-09-03T11:28:29.324534

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

============================== 1 passed in 11.43s ===============================


=== VERBOSE KAFKA OUTPUT ===
📤 Message Sent #1
Topic: test_topic_1756879105
Partition: 0
Offset: 0
Key: key_1
Message ID: 1
Message: First message
Timestamp: 1756879105.233622

📤 Message Sent #2
Topic: test_topic_1756879105
Partition: 0
Offset: 1
Key: key_2
Message ID: 2
Message: Second message
Timestamp: 1756879105.233629

📤 Message Sent #3
Topic: test_topic_1756879105
Partition: 0
Offset: 2
Key: key_3
Message ID: 3
Message: Third message
Timestamp: 1756879105.23364

📥 Message Consumed #1
Topic: test_topic_1756879105
Partition: 0
Offset: 0
Key: key_1
Message ID: 1
Message: First message
Timestamp: 1756879105349

📥 Message Consumed #2
Topic: test_topic_1756879105
Partition: 0
Offset: 1
Key: key_2
Message ID: 2
Message: Second message
Timestamp: 1756879105380

📥 Message Consumed #3
Topic: test_topic_1756879105
Partition: 0
Offset: 2
Key: key_3
Message ID: 3
Message: Third message
Timestamp: 1756879105384

```

### TestKafkaOperations::test_consume_messages

- **Status**: PASSED
- **Duration**: 10.44 seconds
- **Timestamp**: 2025-09-03T11:28:39.766780

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

============================== 1 passed in 10.20s ===============================


=== VERBOSE KAFKA OUTPUT ===
📤 Message Sent #1
Topic: test_topic_1756879114
Partition: 0
Offset: 0
Key: None
Message ID: 1
Message: Test message 1
Timestamp: N/A

📤 Message Sent #2
Topic: test_topic_1756879114
Partition: 0
Offset: 1
Key: None
Message ID: 2
Message: Test message 2
Timestamp: N/A

📤 Message Sent #3
Topic: test_topic_1756879114
Partition: 0
Offset: 2
Key: None
Message ID: 3
Message: Test message 3
Timestamp: N/A

📥 Message Consumed #1
Topic: test_topic_1756879114
Partition: 0
Offset: 0
Key: None
Message ID: 1
Message: Test message 1
Timestamp: 1756879115779

📥 Message Consumed #2
Topic: test_topic_1756879114
Partition: 0
Offset: 1
Key: None
Message ID: 2
Message: Test message 2
Timestamp: 1756879115810

📥 Message Consumed #3
Topic: test_topic_1756879114
Partition: 0
Offset: 2
Key: None
Message ID: 3
Message: Test message 3
Timestamp: 1756879115814

```

### TestKafkaOperations::test_consume_messages_with_group_id

- **Status**: PASSED
- **Duration**: 10.53 seconds
- **Timestamp**: 2025-09-03T11:28:50.298691

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

============================== 1 passed in 10.26s ===============================


=== VERBOSE KAFKA OUTPUT ===
📤 Message Sent
Topic: test_topic_1756879124
Partition: 0
Offset: 0
Key: None
Message ID: 1
Message: Group test message
Timestamp: N/A

📥 Message Consumed #1
Topic: test_topic_1756879124
Partition: 0
Offset: 0
Key: None
Message ID: 1
Message: Group test message
Timestamp: 1756879126263

```

### TestKafkaOperations::test_get_topic_info

- **Status**: PASSED
- **Duration**: 8.28 seconds
- **Timestamp**: 2025-09-03T11:28:58.582211

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

=============================== 1 passed in 8.05s ===============================

```

### TestKafkaOperations::test_get_partition_count

- **Status**: PASSED
- **Duration**: 10.09 seconds
- **Timestamp**: 2025-09-03T11:29:08.672308

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

=============================== 1 passed in 9.84s ===============================

```

### TestKafkaOperations::test_message_ordering

- **Status**: PASSED
- **Duration**: 10.60 seconds
- **Timestamp**: 2025-09-03T11:29:19.276720

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

============================== 1 passed in 10.38s ===============================


=== VERBOSE KAFKA OUTPUT ===
📤 Message Sent #1
Topic: test_topic_1756879153
Partition: 0
Offset: 0
Key: None
Message ID: 1
Message: N/A
Timestamp: N/A

📤 Message Sent #2
Topic: test_topic_1756879153
Partition: 0
Offset: 1
Key: None
Message ID: 2
Message: N/A
Timestamp: N/A

📤 Message Sent #3
Topic: test_topic_1756879153
Partition: 0
Offset: 2
Key: None
Message ID: 3
Message: N/A
Timestamp: N/A

📤 Message Sent #4
Topic: test_topic_1756879153
Partition: 0
Offset: 3
Key: None
Message ID: 4
Message: N/A
Timestamp: N/A

📥 Message Consumed #1
Topic: test_topic_1756879153
Partition: 0
Offset: 0
Key: None
Message ID: 1
Message: N/A
Timestamp: 1756879154882

📥 Message Consumed #2
Topic: test_topic_1756879153
Partition: 0
Offset: 1
Key: None
Message ID: 2
Message: N/A
Timestamp: 1756879154912

📥 Message Consumed #3
Topic: test_topic_1756879153
Partition: 0
Offset: 2
Key: None
Message ID: 3
Message: N/A
Timestamp: 1756879154916

📥 Message Consumed #4
Topic: test_topic_1756879153
Partition: 0
Offset: 3
Key: None
Message ID: 4
Message: N/A
Timestamp: 1756879154920

```

### TestKafkaOperations::test_message_without_key

- **Status**: PASSED
- **Duration**: 11.77 seconds
- **Timestamp**: 2025-09-03T11:29:31.044062

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

============================== 1 passed in 11.43s ===============================


=== VERBOSE KAFKA OUTPUT ===
📤 Message Sent
Topic: test_topic_1756879166
Partition: 0
Offset: 0
Key: None
Message ID: 1
Message: No key message
Timestamp: N/A

📥 Message Consumed #1
Topic: test_topic_1756879166
Partition: 0
Offset: 0
Key: None
Message ID: 1
Message: No key message
Timestamp: 1756879166998

```

### TestKafkaOperations::test_large_message

- **Status**: PASSED
- **Duration**: 10.39 seconds
- **Timestamp**: 2025-09-03T11:29:41.439581

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

============================== 1 passed in 10.16s ===============================


=== VERBOSE KAFKA OUTPUT ===
📤 Message Sent
Topic: test_topic_1756879176
Partition: 0
Offset: 0
Key: None
Message ID: 1
Message: N/A
Timestamp: 1756879177.335808

📥 Message Consumed #1
Topic: test_topic_1756879176
Partition: 0
Offset: 0
Key: None
Message ID: 1
Message: N/A
Timestamp: 1756879177454

```

### TestKafkaQueueLength::test_queue_length_after_sending

- **Status**: PASSED
- **Duration**: 13.99 seconds
- **Timestamp**: 2025-09-03T11:29:55.434387

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

============================== 1 passed in 13.74s ===============================


=== VERBOSE KAFKA OUTPUT ===
📤 Message Sent #1
Topic: queue_test_topic_1756879186
Partition: 0
Offset: 0
Key: None
Message ID: 1
Message: Message 1
Timestamp: N/A

📤 Message Sent #2
Topic: queue_test_topic_1756879186
Partition: 0
Offset: 1
Key: None
Message ID: 2
Message: Message 2
Timestamp: N/A

📤 Message Sent #3
Topic: queue_test_topic_1756879186
Partition: 0
Offset: 2
Key: None
Message ID: 3
Message: Message 3
Timestamp: N/A

📤 Message Sent #4
Topic: queue_test_topic_1756879186
Partition: 0
Offset: 3
Key: None
Message ID: 4
Message: Message 4
Timestamp: N/A

📤 Message Sent #5
Topic: queue_test_topic_1756879186
Partition: 0
Offset: 4
Key: None
Message ID: 5
Message: Message 5
Timestamp: N/A

📥 Message Consumed #1
Topic: queue_test_topic_1756879186
Partition: 0
Offset: 0
Key: None
Message ID: 1
Message: Message 1
Timestamp: 1756879188194

📥 Message Consumed #2
Topic: queue_test_topic_1756879186
Partition: 0
Offset: 1
Key: None
Message ID: 2
Message: Message 2
Timestamp: 1756879188227

📥 Message Consumed #3
Topic: queue_test_topic_1756879186
Partition: 0
Offset: 2
Key: None
Message ID: 3
Message: Message 3
Timestamp: 1756879188231

📥 Message Consumed #4
Topic: queue_test_topic_1756879186
Partition: 0
Offset: 3
Key: None
Message ID: 4
Message: Message 4
Timestamp: 1756879188234

📥 Message Consumed #5
Topic: queue_test_topic_1756879186
Partition: 0
Offset: 4
Key: None
Message ID: 5
Message: Message 5
Timestamp: 1756879188239

```

### TestKafkaQueueLength::test_partition_distribution

- **Status**: PASSED
- **Duration**: 10.49 seconds
- **Timestamp**: 2025-09-03T11:30:05.924709

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

============================== 1 passed in 10.23s ===============================


=== VERBOSE KAFKA OUTPUT ===
📤 Message Sent #1
Topic: queue_test_topic_1756879200
Partition: 0
Offset: 0
Key: None
Message ID: 1
Message: Message 1
Timestamp: N/A

📤 Message Sent #2
Topic: queue_test_topic_1756879200
Partition: 2
Offset: 0
Key: None
Message ID: 2
Message: Message 2
Timestamp: N/A

📤 Message Sent #3
Topic: queue_test_topic_1756879200
Partition: 2
Offset: 1
Key: None
Message ID: 3
Message: Message 3
Timestamp: N/A

📤 Message Sent #4
Topic: queue_test_topic_1756879200
Partition: 2
Offset: 2
Key: None
Message ID: 4
Message: Message 4
Timestamp: N/A

📤 Message Sent #5
Topic: queue_test_topic_1756879200
Partition: 0
Offset: 1
Key: None
Message ID: 5
Message: Message 5
Timestamp: N/A

📥 Message Consumed #1
Topic: queue_test_topic_1756879200
Partition: 0
Offset: 0
Key: None
Message ID: 1
Message: Message 1
Timestamp: 1756879201922

📥 Message Consumed #2
Topic: queue_test_topic_1756879200
Partition: 0
Offset: 1
Key: None
Message ID: 5
Message: Message 5
Timestamp: 1756879201966

📥 Message Consumed #3
Topic: queue_test_topic_1756879200
Partition: 2
Offset: 0
Key: None
Message ID: 2
Message: Message 2
Timestamp: 1756879201955

📥 Message Consumed #4
Topic: queue_test_topic_1756879200
Partition: 2
Offset: 1
Key: None
Message ID: 3
Message: Message 3
Timestamp: 1756879201959

📥 Message Consumed #5
Topic: queue_test_topic_1756879200
Partition: 2
Offset: 2
Key: None
Message ID: 4
Message: Message 4
Timestamp: 1756879201963

```

### TestKafkaQueueLength::test_queue_length_verbose

- **Status**: PASSED
- **Duration**: 11.66 seconds
- **Timestamp**: 2025-09-03T11:30:17.586658

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

============================== 1 passed in 11.38s ===============================


=== VERBOSE KAFKA OUTPUT ===
📤 Message Sent #1
Topic: queue_test_topic_1756879211
Partition: 0
Offset: 0
Key: None
Message ID: 1
Message: Message 1
Timestamp: N/A

📤 Message Sent #2
Topic: queue_test_topic_1756879211
Partition: 0
Offset: 1
Key: None
Message ID: 2
Message: Message 2
Timestamp: N/A

📤 Message Sent #3
Topic: queue_test_topic_1756879211
Partition: 0
Offset: 2
Key: None
Message ID: 3
Message: Message 3
Timestamp: N/A

📊 Queue Length Information
Topic: queue_test_topic_1756879211
Total Messages: 3
Read Messages: 0
Queue Length: 3

📥 Message Consumed #1
Topic: queue_test_topic_1756879211
Partition: 0
Offset: 0
Key: None
Message ID: 1
Message: Message 1
Timestamp: 1756879212424

📥 Message Consumed #2
Topic: queue_test_topic_1756879211
Partition: 0
Offset: 1
Key: None
Message ID: 2
Message: Message 2
Timestamp: 1756879212455

📊 Queue Length Information
Topic: queue_test_topic_1756879211
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
- **Report Generated**: 2025-09-03 11:30:17


## Recommendations

🎉 **All tests passed successfully!**

