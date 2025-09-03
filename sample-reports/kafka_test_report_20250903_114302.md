# 🚀 Kafka E2E Test Report 🎉

🟢 **All Tests Passed** | ![Test Status](https://img.shields.io/badge/Tests-13%2F13-brightgreen) | ![Coverage](https://img.shields.io/badge/Coverage-100.0%25-brightgreen) | ![Duration](https://img.shields.io/badge/Duration-146.6s-blue)

---

## 📊 Executive Summary

| Metric | Value | Status |
|--------|-------|--------|
| 🕐 **Test Session** | 2025-09-03 11:40:35 → 2025-09-03 11:43:02 | 📅 |
| ⏱️ **Total Duration** | 146.57 seconds | ⏰ |
| 🧪 **Total Tests** | 13 | 🔢 |
| ✅ **Passed** | 13 | 🟢 |
| ❌ **Failed** | 0 | 🟢 |
| 📈 **Success Rate** | 100.0% | 🟢 |

## 🧪 Test Results Overview

| 🏷️ Test Name | 📊 Status | ⏱️ Duration | 📋 Details |
|--------------|-----------|-------------|------------|
| TestKafkaOperations::test_create_topic | ✅ PASSED | ⚡ 3.51s | test_index: 1; category: Topic Management; verbose_mode: True |
| TestKafkaOperations::test_send_single_message | ✅ PASSED | ⏱️ 11.85s | test_index: 2; category: Send Operations; verbose_mode: True |
| TestKafkaOperations::test_send_multiple_messages | ✅ PASSED | ⏱️ 10.74s | test_index: 3; category: Send Operations; verbose_mode: True |
| TestKafkaOperations::test_consume_messages | ✅ PASSED | ⏱️ 10.86s | test_index: 4; category: Consume Operations; verbose_mode: True |
| TestKafkaOperations::test_consume_messages_with_group_id | ✅ PASSED | ⏱️ 11.94s | test_index: 5; category: Consume Operations; verbose_mode: True |
| TestKafkaOperations::test_get_topic_info | ✅ PASSED | ⏱️ 9.56s | test_index: 6; category: Topic Management; verbose_mode: True |
| TestKafkaOperations::test_get_partition_count | ✅ PASSED | ⏱️ 10.29s | test_index: 7; category: Other; verbose_mode: True |
| TestKafkaOperations::test_message_ordering | ✅ PASSED | ⏱️ 10.64s | test_index: 8; category: Other; verbose_mode: True |
| TestKafkaOperations::test_message_without_key | ✅ PASSED | ⏱️ 10.68s | test_index: 9; category: Other; verbose_mode: True |
| TestKafkaOperations::test_large_message | ✅ PASSED | ⏱️ 11.77s | test_index: 10; category: Other; verbose_mode: True |
| TestKafkaQueueLength::test_queue_length_after_sending | ✅ PASSED | ⏱️ 14.99s | test_index: 11; category: Send Operations; verbose_mode: True |
| TestKafkaQueueLength::test_partition_distribution | ✅ PASSED | ⏱️ 10.98s | test_index: 12; category: Queue Length Operations; verbose_mode: True |
| TestKafkaQueueLength::test_queue_length_verbose | ✅ PASSED | ⏱️ 12.79s | test_index: 13; category: Queue Length Operations; verbose_mode: True |

---

## 🔍 Detailed Test Information

### 1. 🏗️ TestKafkaOperations::test_create_topic ✅

<details>
<summary><strong>📋 Test Information</strong></summary>

| Property | Value |
|----------|-------|
| 🏷️ **Test Name** | `TestKafkaOperations::test_create_topic` |
| 📊 **Status** | ✅ PASSED |
| ⏱️ **Duration** | 3.51 seconds |
| 🕐 **Timestamp** | 2025-09-03T11:40:44.973822 |
| 📂 **Category** | Topic Management |
| 🔢 **Test Index** | 1 |

</details>

<details>
<summary><strong>⚙️ Test Configuration</strong></summary>

**verbose_mode**: `True`

</details>

<details>
<summary><strong>🔍 Verbose Output</strong></summary>

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

=============================== 1 passed in 2.09s ===============================

```

</details>

### 2. 📤 TestKafkaOperations::test_send_single_message ✅

<details>
<summary><strong>📋 Test Information</strong></summary>

| Property | Value |
|----------|-------|
| 🏷️ **Test Name** | `TestKafkaOperations::test_send_single_message` |
| 📊 **Status** | ✅ PASSED |
| ⏱️ **Duration** | 11.85 seconds |
| 🕐 **Timestamp** | 2025-09-03T11:40:56.825715 |
| 📂 **Category** | Send Operations |
| 🔢 **Test Index** | 2 |

</details>

<details>
<summary><strong>⚙️ Test Configuration</strong></summary>

**verbose_mode**: `True`

</details>

<details>
<summary><strong>🔍 Verbose Output</strong></summary>

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

============================== 1 passed in 11.63s ===============================


=== VERBOSE KAFKA OUTPUT ===
📤 Message Sent
Topic: test_topic_1756879852
Partition: 0
Offset: 0
Key: test_key_1
Message ID: 1
Message: Hello Kafka!
Timestamp: 1756879852.463448

📥 Message Consumed #1
Topic: test_topic_1756879852
Partition: 0
Offset: 0
Key: test_key_1
Message ID: 1
Message: Hello Kafka!
Timestamp: 1756879852576

```

</details>

### 3. 📤 TestKafkaOperations::test_send_multiple_messages ✅

<details>
<summary><strong>📋 Test Information</strong></summary>

| Property | Value |
|----------|-------|
| 🏷️ **Test Name** | `TestKafkaOperations::test_send_multiple_messages` |
| 📊 **Status** | ✅ PASSED |
| ⏱️ **Duration** | 10.74 seconds |
| 🕐 **Timestamp** | 2025-09-03T11:41:07.569766 |
| 📂 **Category** | Send Operations |
| 🔢 **Test Index** | 3 |

</details>

<details>
<summary><strong>⚙️ Test Configuration</strong></summary>

**verbose_mode**: `True`

</details>

<details>
<summary><strong>🔍 Verbose Output</strong></summary>

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

============================== 1 passed in 10.50s ===============================


=== VERBOSE KAFKA OUTPUT ===
📤 Message Sent #1
Topic: test_topic_1756879861
Partition: 0
Offset: 0
Key: key_1
Message ID: 1
Message: First message
Timestamp: 1756879863.376702

📤 Message Sent #2
Topic: test_topic_1756879861
Partition: 0
Offset: 1
Key: key_2
Message ID: 2
Message: Second message
Timestamp: 1756879863.376708

📤 Message Sent #3
Topic: test_topic_1756879861
Partition: 0
Offset: 2
Key: key_3
Message ID: 3
Message: Third message
Timestamp: 1756879863.37671

📥 Message Consumed #1
Topic: test_topic_1756879861
Partition: 0
Offset: 0
Key: key_1
Message ID: 1
Message: First message
Timestamp: 1756879863494

📥 Message Consumed #2
Topic: test_topic_1756879861
Partition: 0
Offset: 1
Key: key_2
Message ID: 2
Message: Second message
Timestamp: 1756879863526

📥 Message Consumed #3
Topic: test_topic_1756879861
Partition: 0
Offset: 2
Key: key_3
Message ID: 3
Message: Third message
Timestamp: 1756879863530

```

</details>

### 4. 📥 TestKafkaOperations::test_consume_messages ✅

<details>
<summary><strong>📋 Test Information</strong></summary>

| Property | Value |
|----------|-------|
| 🏷️ **Test Name** | `TestKafkaOperations::test_consume_messages` |
| 📊 **Status** | ✅ PASSED |
| ⏱️ **Duration** | 10.86 seconds |
| 🕐 **Timestamp** | 2025-09-03T11:41:18.432170 |
| 📂 **Category** | Consume Operations |
| 🔢 **Test Index** | 4 |

</details>

<details>
<summary><strong>⚙️ Test Configuration</strong></summary>

**verbose_mode**: `True`

</details>

<details>
<summary><strong>🔍 Verbose Output</strong></summary>

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

============================== 1 passed in 10.62s ===============================


=== VERBOSE KAFKA OUTPUT ===
📤 Message Sent #1
Topic: test_topic_1756879872
Partition: 0
Offset: 0
Key: None
Message ID: 1
Message: Test message 1
Timestamp: N/A

📤 Message Sent #2
Topic: test_topic_1756879872
Partition: 0
Offset: 1
Key: None
Message ID: 2
Message: Test message 2
Timestamp: N/A

📤 Message Sent #3
Topic: test_topic_1756879872
Partition: 0
Offset: 2
Key: None
Message ID: 3
Message: Test message 3
Timestamp: N/A

📥 Message Consumed #1
Topic: test_topic_1756879872
Partition: 0
Offset: 0
Key: None
Message ID: 1
Message: Test message 1
Timestamp: 1756879874164

📥 Message Consumed #2
Topic: test_topic_1756879872
Partition: 0
Offset: 1
Key: None
Message ID: 2
Message: Test message 2
Timestamp: 1756879874197

📥 Message Consumed #3
Topic: test_topic_1756879872
Partition: 0
Offset: 2
Key: None
Message ID: 3
Message: Test message 3
Timestamp: 1756879874201

```

</details>

### 5. 📥 TestKafkaOperations::test_consume_messages_with_group_id ✅

<details>
<summary><strong>📋 Test Information</strong></summary>

| Property | Value |
|----------|-------|
| 🏷️ **Test Name** | `TestKafkaOperations::test_consume_messages_with_group_id` |
| 📊 **Status** | ✅ PASSED |
| ⏱️ **Duration** | 11.94 seconds |
| 🕐 **Timestamp** | 2025-09-03T11:41:30.377721 |
| 📂 **Category** | Consume Operations |
| 🔢 **Test Index** | 5 |

</details>

<details>
<summary><strong>⚙️ Test Configuration</strong></summary>

**verbose_mode**: `True`

</details>

<details>
<summary><strong>🔍 Verbose Output</strong></summary>

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

============================== 1 passed in 11.69s ===============================


=== VERBOSE KAFKA OUTPUT ===
📤 Message Sent
Topic: test_topic_1756879885
Partition: 0
Offset: 0
Key: None
Message ID: 1
Message: Group test message
Timestamp: N/A

📥 Message Consumed #1
Topic: test_topic_1756879885
Partition: 0
Offset: 0
Key: None
Message ID: 1
Message: Group test message
Timestamp: 1756879886097

```

</details>

### 6. 🏗️ TestKafkaOperations::test_get_topic_info ✅

<details>
<summary><strong>📋 Test Information</strong></summary>

| Property | Value |
|----------|-------|
| 🏷️ **Test Name** | `TestKafkaOperations::test_get_topic_info` |
| 📊 **Status** | ✅ PASSED |
| ⏱️ **Duration** | 9.56 seconds |
| 🕐 **Timestamp** | 2025-09-03T11:41:39.941570 |
| 📂 **Category** | Topic Management |
| 🔢 **Test Index** | 6 |

</details>

<details>
<summary><strong>⚙️ Test Configuration</strong></summary>

**verbose_mode**: `True`

</details>

<details>
<summary><strong>🔍 Verbose Output</strong></summary>

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

=============================== 1 passed in 9.32s ===============================

```

</details>

### 7. 🔧 TestKafkaOperations::test_get_partition_count ✅

<details>
<summary><strong>📋 Test Information</strong></summary>

| Property | Value |
|----------|-------|
| 🏷️ **Test Name** | `TestKafkaOperations::test_get_partition_count` |
| 📊 **Status** | ✅ PASSED |
| ⏱️ **Duration** | 10.29 seconds |
| 🕐 **Timestamp** | 2025-09-03T11:41:50.230574 |
| 📂 **Category** | Other |
| 🔢 **Test Index** | 7 |

</details>

<details>
<summary><strong>⚙️ Test Configuration</strong></summary>

**verbose_mode**: `True`

</details>

<details>
<summary><strong>🔍 Verbose Output</strong></summary>

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

============================== 1 passed in 10.09s ===============================

```

</details>

### 8. 🔧 TestKafkaOperations::test_message_ordering ✅

<details>
<summary><strong>📋 Test Information</strong></summary>

| Property | Value |
|----------|-------|
| 🏷️ **Test Name** | `TestKafkaOperations::test_message_ordering` |
| 📊 **Status** | ✅ PASSED |
| ⏱️ **Duration** | 10.64 seconds |
| 🕐 **Timestamp** | 2025-09-03T11:42:00.869272 |
| 📂 **Category** | Other |
| 🔢 **Test Index** | 8 |

</details>

<details>
<summary><strong>⚙️ Test Configuration</strong></summary>

**verbose_mode**: `True`

</details>

<details>
<summary><strong>🔍 Verbose Output</strong></summary>

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

============================== 1 passed in 10.43s ===============================


=== VERBOSE KAFKA OUTPUT ===
📤 Message Sent #1
Topic: test_topic_1756879915
Partition: 0
Offset: 0
Key: None
Message ID: 1
Message: N/A
Timestamp: N/A

📤 Message Sent #2
Topic: test_topic_1756879915
Partition: 0
Offset: 1
Key: None
Message ID: 2
Message: N/A
Timestamp: N/A

📤 Message Sent #3
Topic: test_topic_1756879915
Partition: 0
Offset: 2
Key: None
Message ID: 3
Message: N/A
Timestamp: N/A

📤 Message Sent #4
Topic: test_topic_1756879915
Partition: 0
Offset: 3
Key: None
Message ID: 4
Message: N/A
Timestamp: N/A

📥 Message Consumed #1
Topic: test_topic_1756879915
Partition: 0
Offset: 0
Key: None
Message ID: 1
Message: N/A
Timestamp: 1756879916758

📥 Message Consumed #2
Topic: test_topic_1756879915
Partition: 0
Offset: 1
Key: None
Message ID: 2
Message: N/A
Timestamp: 1756879916792

📥 Message Consumed #3
Topic: test_topic_1756879915
Partition: 0
Offset: 2
Key: None
Message ID: 3
Message: N/A
Timestamp: 1756879916796

📥 Message Consumed #4
Topic: test_topic_1756879915
Partition: 0
Offset: 3
Key: None
Message ID: 4
Message: N/A
Timestamp: 1756879916800

```

</details>

### 9. 🔧 TestKafkaOperations::test_message_without_key ✅

<details>
<summary><strong>📋 Test Information</strong></summary>

| Property | Value |
|----------|-------|
| 🏷️ **Test Name** | `TestKafkaOperations::test_message_without_key` |
| 📊 **Status** | ✅ PASSED |
| ⏱️ **Duration** | 10.68 seconds |
| 🕐 **Timestamp** | 2025-09-03T11:42:11.550516 |
| 📂 **Category** | Other |
| 🔢 **Test Index** | 9 |

</details>

<details>
<summary><strong>⚙️ Test Configuration</strong></summary>

**verbose_mode**: `True`

</details>

<details>
<summary><strong>🔍 Verbose Output</strong></summary>

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

============================== 1 passed in 10.44s ===============================


=== VERBOSE KAFKA OUTPUT ===
📤 Message Sent
Topic: test_topic_1756879926
Partition: 0
Offset: 0
Key: None
Message ID: 1
Message: No key message
Timestamp: N/A

📥 Message Consumed #1
Topic: test_topic_1756879926
Partition: 0
Offset: 0
Key: None
Message ID: 1
Message: No key message
Timestamp: 1756879927601

```

</details>

### 10. 🔧 TestKafkaOperations::test_large_message ✅

<details>
<summary><strong>📋 Test Information</strong></summary>

| Property | Value |
|----------|-------|
| 🏷️ **Test Name** | `TestKafkaOperations::test_large_message` |
| 📊 **Status** | ✅ PASSED |
| ⏱️ **Duration** | 11.77 seconds |
| 🕐 **Timestamp** | 2025-09-03T11:42:23.323953 |
| 📂 **Category** | Other |
| 🔢 **Test Index** | 10 |

</details>

<details>
<summary><strong>⚙️ Test Configuration</strong></summary>

**verbose_mode**: `True`

</details>

<details>
<summary><strong>🔍 Verbose Output</strong></summary>

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

============================== 1 passed in 11.55s ===============================


=== VERBOSE KAFKA OUTPUT ===
📤 Message Sent
Topic: test_topic_1756879936
Partition: 0
Offset: 0
Key: None
Message ID: 1
Message: N/A
Timestamp: 1756879938.6424682

📥 Message Consumed #1
Topic: test_topic_1756879936
Partition: 0
Offset: 0
Key: None
Message ID: 1
Message: N/A
Timestamp: 1756879938762

```

</details>

### 11. 📤 TestKafkaQueueLength::test_queue_length_after_sending ✅

<details>
<summary><strong>📋 Test Information</strong></summary>

| Property | Value |
|----------|-------|
| 🏷️ **Test Name** | `TestKafkaQueueLength::test_queue_length_after_sending` |
| 📊 **Status** | ✅ PASSED |
| ⏱️ **Duration** | 14.99 seconds |
| 🕐 **Timestamp** | 2025-09-03T11:42:38.314477 |
| 📂 **Category** | Send Operations |
| 🔢 **Test Index** | 11 |

</details>

<details>
<summary><strong>⚙️ Test Configuration</strong></summary>

**verbose_mode**: `True`

</details>

<details>
<summary><strong>🔍 Verbose Output</strong></summary>

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

============================== 1 passed in 14.73s ===============================


=== VERBOSE KAFKA OUTPUT ===
📤 Message Sent #1
Topic: queue_test_topic_1756879950
Partition: 0
Offset: 0
Key: None
Message ID: 1
Message: Message 1
Timestamp: N/A

📤 Message Sent #2
Topic: queue_test_topic_1756879950
Partition: 0
Offset: 1
Key: None
Message ID: 2
Message: Message 2
Timestamp: N/A

📤 Message Sent #3
Topic: queue_test_topic_1756879950
Partition: 0
Offset: 2
Key: None
Message ID: 3
Message: Message 3
Timestamp: N/A

📤 Message Sent #4
Topic: queue_test_topic_1756879950
Partition: 0
Offset: 3
Key: None
Message ID: 4
Message: Message 4
Timestamp: N/A

📤 Message Sent #5
Topic: queue_test_topic_1756879950
Partition: 0
Offset: 4
Key: None
Message ID: 5
Message: Message 5
Timestamp: N/A

📥 Message Consumed #1
Topic: queue_test_topic_1756879950
Partition: 0
Offset: 0
Key: None
Message ID: 1
Message: Message 1
Timestamp: 1756879951042

📥 Message Consumed #2
Topic: queue_test_topic_1756879950
Partition: 0
Offset: 1
Key: None
Message ID: 2
Message: Message 2
Timestamp: 1756879951077

📥 Message Consumed #3
Topic: queue_test_topic_1756879950
Partition: 0
Offset: 2
Key: None
Message ID: 3
Message: Message 3
Timestamp: 1756879951081

📥 Message Consumed #4
Topic: queue_test_topic_1756879950
Partition: 0
Offset: 3
Key: None
Message ID: 4
Message: Message 4
Timestamp: 1756879951084

📥 Message Consumed #5
Topic: queue_test_topic_1756879950
Partition: 0
Offset: 4
Key: None
Message ID: 5
Message: Message 5
Timestamp: 1756879951088

```

</details>

### 12. 📊 TestKafkaQueueLength::test_partition_distribution ✅

<details>
<summary><strong>📋 Test Information</strong></summary>

| Property | Value |
|----------|-------|
| 🏷️ **Test Name** | `TestKafkaQueueLength::test_partition_distribution` |
| 📊 **Status** | ✅ PASSED |
| ⏱️ **Duration** | 10.98 seconds |
| 🕐 **Timestamp** | 2025-09-03T11:42:49.291301 |
| 📂 **Category** | Queue Length Operations |
| 🔢 **Test Index** | 12 |

</details>

<details>
<summary><strong>⚙️ Test Configuration</strong></summary>

**verbose_mode**: `True`

</details>

<details>
<summary><strong>🔍 Verbose Output</strong></summary>

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

============================== 1 passed in 10.75s ===============================


=== VERBOSE KAFKA OUTPUT ===
📤 Message Sent #1
Topic: queue_test_topic_1756879963
Partition: 0
Offset: 0
Key: None
Message ID: 1
Message: Message 1
Timestamp: N/A

📤 Message Sent #2
Topic: queue_test_topic_1756879963
Partition: 2
Offset: 0
Key: None
Message ID: 2
Message: Message 2
Timestamp: N/A

📤 Message Sent #3
Topic: queue_test_topic_1756879963
Partition: 2
Offset: 1
Key: None
Message ID: 3
Message: Message 3
Timestamp: N/A

📤 Message Sent #4
Topic: queue_test_topic_1756879963
Partition: 0
Offset: 1
Key: None
Message ID: 4
Message: Message 4
Timestamp: N/A

📤 Message Sent #5
Topic: queue_test_topic_1756879963
Partition: 2
Offset: 2
Key: None
Message ID: 5
Message: Message 5
Timestamp: N/A

📥 Message Consumed #1
Topic: queue_test_topic_1756879963
Partition: 0
Offset: 0
Key: None
Message ID: 1
Message: Message 1
Timestamp: 1756879964995

📥 Message Consumed #2
Topic: queue_test_topic_1756879963
Partition: 0
Offset: 1
Key: None
Message ID: 4
Message: Message 4
Timestamp: 1756879965046

📥 Message Consumed #3
Topic: queue_test_topic_1756879963
Partition: 2
Offset: 0
Key: None
Message ID: 2
Message: Message 2
Timestamp: 1756879965037

📥 Message Consumed #4
Topic: queue_test_topic_1756879963
Partition: 2
Offset: 1
Key: None
Message ID: 3
Message: Message 3
Timestamp: 1756879965041

📥 Message Consumed #5
Topic: queue_test_topic_1756879963
Partition: 2
Offset: 2
Key: None
Message ID: 5
Message: Message 5
Timestamp: 1756879965049

```

</details>

### 13. 📊 TestKafkaQueueLength::test_queue_length_verbose ✅

<details>
<summary><strong>📋 Test Information</strong></summary>

| Property | Value |
|----------|-------|
| 🏷️ **Test Name** | `TestKafkaQueueLength::test_queue_length_verbose` |
| 📊 **Status** | ✅ PASSED |
| ⏱️ **Duration** | 12.79 seconds |
| 🕐 **Timestamp** | 2025-09-03T11:43:02.082855 |
| 📂 **Category** | Queue Length Operations |
| 🔢 **Test Index** | 13 |

</details>

<details>
<summary><strong>⚙️ Test Configuration</strong></summary>

**verbose_mode**: `True`

</details>

<details>
<summary><strong>🔍 Verbose Output</strong></summary>

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

============================== 1 passed in 12.54s ===============================


=== VERBOSE KAFKA OUTPUT ===
📤 Message Sent #1
Topic: queue_test_topic_1756879976
Partition: 0
Offset: 0
Key: None
Message ID: 1
Message: Message 1
Timestamp: N/A

📤 Message Sent #2
Topic: queue_test_topic_1756879976
Partition: 0
Offset: 1
Key: None
Message ID: 2
Message: Message 2
Timestamp: N/A

📤 Message Sent #3
Topic: queue_test_topic_1756879976
Partition: 0
Offset: 2
Key: None
Message ID: 3
Message: Message 3
Timestamp: N/A

📊 Queue Length Information
Topic: queue_test_topic_1756879976
Total Messages: 3
Read Messages: 0
Queue Length: 3

📥 Message Consumed #1
Topic: queue_test_topic_1756879976
Partition: 0
Offset: 0
Key: None
Message ID: 1
Message: Message 1
Timestamp: 1756879976960

📥 Message Consumed #2
Topic: queue_test_topic_1756879976
Partition: 0
Offset: 1
Key: None
Message ID: 2
Message: Message 2
Timestamp: 1756879976990

📊 Queue Length Information
Topic: queue_test_topic_1756879976
Total Messages: 3
Read Messages: 0
Queue Length: 3

```

</details>

---

## 📊 Test Categories Summary

### 📤 Send Operations 🟢

| Metric | Value |
|--------|-------|
| 🧪 **Total Tests** | 3 |
| ✅ **Passed** | 3 |
| ❌ **Failed** | 0 |
| 📈 **Success Rate** | 100.0% |

### 📥 Consume Operations 🟢

| Metric | Value |
|--------|-------|
| 🧪 **Total Tests** | 2 |
| ✅ **Passed** | 2 |
| ❌ **Failed** | 0 |
| 📈 **Success Rate** | 100.0% |

### 📊 Queue Length Operations 🟢

| Metric | Value |
|--------|-------|
| 🧪 **Total Tests** | 2 |
| ✅ **Passed** | 2 |
| ❌ **Failed** | 0 |
| 📈 **Success Rate** | 100.0% |

### 🏗️ Topic Management 🟢

| Metric | Value |
|--------|-------|
| 🧪 **Total Tests** | 2 |
| ✅ **Passed** | 2 |
| ❌ **Failed** | 0 |
| 📈 **Success Rate** | 100.0% |

### 🔧 Other 🟢

| Metric | Value |
|--------|-------|
| 🧪 **Total Tests** | 4 |
| ✅ **Passed** | 4 |
| ❌ **Failed** | 0 |
| 📈 **Success Rate** | 100.0% |

---

## 🖥️ Environment Information

| Component | Value |
|-----------|-------|
| 🐍 **Python Version** | `3.12.2` |
| 🧪 **Test Framework** | pytest |
| 🔊 **Verbose Mode** | ✅ Enabled |
| 📅 **Report Generated** | 2025-09-03 11:43:02 |

---

## 💡 Recommendations & Next Steps

### 🎉 Excellent Work!

✅ **All tests passed successfully!**

**What this means:**
- 🚀 Your Kafka infrastructure is working correctly
- 📤 Message sending operations are functional
- 📥 Message consumption is working as expected
- 📊 Queue length monitoring is accurate
- 🏗️ Topic management operations are successful

### 📈 Performance Insights

| Metric | Value |
|--------|-------|
| ⚡ **Average Duration** | 10.82s |
| 🐌 **Slow Tests (>15s)** | 0 |
| ⚡ **Fast Tests (<5s)** | 1 |

---

## 📝 Report Footer

<div align="center">

**Generated by Kafka E2E Testing Suite** 🚀

*Report generated on September 03, 2025 at 11:43:02*

![Kafka](https://img.shields.io/badge/Apache-Kafka-231F20?style=flat&logo=apache-kafka&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-6.0+-0A9EDC?style=flat&logo=pytest&logoColor=white)

</div>
