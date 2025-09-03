# 🚀 Kafka E2E Test Report 🎉

🟢 **All Tests Passed** | ![Test Status](https://img.shields.io/badge/Tests-13%2F13-brightgreen) | ![Coverage](https://img.shields.io/badge/Coverage-100.0%25-brightgreen) | ![Duration](https://img.shields.io/badge/Duration-162.6s-blue)

---

## 📊 Executive Summary

| Metric | Value | Status |
|--------|-------|--------|
| 🕐 **Test Session** | 2025-09-03 11:59:06 → 2025-09-03 12:01:49 | 📅 |
| ⏱️ **Total Duration** | 162.63 seconds | ⏰ |
| 🧪 **Total Tests** | 13 | 🔢 |
| ✅ **Passed** | 13 | 🟢 |
| ❌ **Failed** | 0 | 🟢 |
| 📈 **Success Rate** | 100.0% | 🟢 |

## 🧪 Test Results Overview

| 🏷️ Test Name | 📊 Status | ⏱️ Duration | 📋 Details |
|--------------|-----------|-------------|------------|
| TestKafkaOperations::test_create_topic | ✅ PASSED | ⚡ 3.54s | test_index: 1; category: Topic Management; verbose_mode: True |
| TestKafkaOperations::test_send_single_message | ✅ PASSED | ⏱️ 13.10s | test_index: 2; category: Send Operations; verbose_mode: True |
| TestKafkaOperations::test_send_multiple_messages | ✅ PASSED | ⏱️ 12.12s | test_index: 3; category: Send Operations; verbose_mode: True |
| TestKafkaOperations::test_consume_messages | ✅ PASSED | ⏱️ 12.11s | test_index: 4; category: Consume Operations; verbose_mode: True |
| TestKafkaOperations::test_consume_messages_with_group_id | ✅ PASSED | ⏱️ 11.33s | test_index: 5; category: Consume Operations; verbose_mode: True |
| TestKafkaOperations::test_get_topic_info | ✅ PASSED | ⏱️ 9.63s | test_index: 6; category: Topic Management; verbose_mode: True |
| TestKafkaOperations::test_get_partition_count | ✅ PASSED | ⏱️ 13.44s | test_index: 7; category: Other; verbose_mode: True |
| TestKafkaOperations::test_message_ordering | ✅ PASSED | ⏱️ 14.29s | test_index: 8; category: Other; verbose_mode: True |
| TestKafkaOperations::test_message_without_key | ✅ PASSED | ⏱️ 13.04s | test_index: 9; category: Other; verbose_mode: True |
| TestKafkaOperations::test_large_message | ✅ PASSED | ⏱️ 12.87s | test_index: 10; category: Other; verbose_mode: True |
| TestKafkaQueueLength::test_queue_length_after_sending | ✅ PASSED | 🐌 15.32s | test_index: 11; category: Send Operations; verbose_mode: True |
| TestKafkaQueueLength::test_partition_distribution | ✅ PASSED | ⏱️ 12.75s | test_index: 12; category: Queue Length Operations; verbose_mode: True |
| TestKafkaQueueLength::test_queue_length_verbose | ✅ PASSED | ⏱️ 13.11s | test_index: 13; category: Queue Length Operations; verbose_mode: True |

---

## 🔍 Detailed Test Information

### 1. 🏗️ TestKafkaOperations::test_create_topic ✅

<details>
<summary><strong>📋 Test Information</strong></summary>

| Property | Value |
|----------|-------|
| 🏷️ **Test Name** | `TestKafkaOperations::test_create_topic` |
| 📊 **Status** | ✅ PASSED |
| ⏱️ **Duration** | 3.54 seconds |
| 🕐 **Timestamp** | 2025-09-03T11:59:16.453898 |
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
================================================= test session starts =================================================
platform darwin -- Python 3.12.2, pytest-8.4.1, pluggy-1.5.0 -- /Users/anidhula/.pyenv/versions/3.12.2/bin/python
cachedir: .pytest_cache
rootdir: /Users/anidhula/learn/kafka-e2etest
configfile: pytest.ini
plugins: asyncio-1.1.0, cov-4.1.0, anyio-4.10.0, dash-2.14.2
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collecting ... collected 1 item

test_kafka.py::TestKafkaOperations::test_create_topic PASSED                                                    [100%]

================================================== 1 passed in 2.12s ==================================================

```

</details>

### 2. 📤 TestKafkaOperations::test_send_single_message ✅

<details>
<summary><strong>📋 Test Information</strong></summary>

| Property | Value |
|----------|-------|
| 🏷️ **Test Name** | `TestKafkaOperations::test_send_single_message` |
| 📊 **Status** | ✅ PASSED |
| ⏱️ **Duration** | 13.10 seconds |
| 🕐 **Timestamp** | 2025-09-03T11:59:29.550853 |
| 📂 **Category** | Send Operations |
| 🔢 **Test Index** | 2 |

</details>

<details>
<summary><strong>⚙️ Test Configuration</strong></summary>

**verbose_mode**: `True`

</details>

<details>
<summary><strong>🔍 Verbose Output</strong></summary>

================================================= test session starts =================================================
platform darwin -- Python 3.12.2, pytest-8.4.1, pluggy-1.5.0 -- /Users/anidhula/.pyenv/versions/3.12.2/bin/python
cachedir: .pytest_cache
rootdir: /Users/anidhula/learn/kafka-e2etest
configfile: pytest.ini
plugins: asyncio-1.1.0, cov-4.1.0, anyio-4.10.0, dash-2.14.2
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collecting ... collected 1 item

test_kafka.py::TestKafkaOperations::test_send_single_message PASSED                                             [100%]

================================================= 1 passed in 12.85s ==================================================


=== VERBOSE KAFKA OUTPUT ===
**📤 Message Sent**

| Property | Value |
|----------|-------|
| Topic | test_topic_1756880964 |
| Partition | 0 |
| Offset | 0 |
| Key | test_key_1 |
| Message ID | 1 |
| Message | Hello Kafka! |
| Timestamp | 1756880965.071274 |


**📥 Message Consumed #1**

| Property | Value |
|----------|-------|
| Topic | test_topic_1756880964 |
| Partition | 0 |
| Offset | 0 |
| Key | test_key_1 |
| Message ID | 1 |
| Message | Hello Kafka! |
| Timestamp | 1756880965186 |


</details>

### 3. 📤 TestKafkaOperations::test_send_multiple_messages ✅

<details>
<summary><strong>📋 Test Information</strong></summary>

| Property | Value |
|----------|-------|
| 🏷️ **Test Name** | `TestKafkaOperations::test_send_multiple_messages` |
| 📊 **Status** | ✅ PASSED |
| ⏱️ **Duration** | 12.12 seconds |
| 🕐 **Timestamp** | 2025-09-03T11:59:41.675185 |
| 📂 **Category** | Send Operations |
| 🔢 **Test Index** | 3 |

</details>

<details>
<summary><strong>⚙️ Test Configuration</strong></summary>

**verbose_mode**: `True`

</details>

<details>
<summary><strong>🔍 Verbose Output</strong></summary>

================================================= test session starts =================================================
platform darwin -- Python 3.12.2, pytest-8.4.1, pluggy-1.5.0 -- /Users/anidhula/.pyenv/versions/3.12.2/bin/python
cachedir: .pytest_cache
rootdir: /Users/anidhula/learn/kafka-e2etest
configfile: pytest.ini
plugins: asyncio-1.1.0, cov-4.1.0, anyio-4.10.0, dash-2.14.2
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collecting ... collected 1 item

test_kafka.py::TestKafkaOperations::test_send_multiple_messages PASSED                                          [100%]

================================================= 1 passed in 11.86s ==================================================


=== VERBOSE KAFKA OUTPUT ===
**📤 Message Sent #1**

| Property | Value |
|----------|-------|
| Topic | test_topic_1756880977 |
| Partition | 0 |
| Offset | 0 |
| Key | key_1 |
| Message ID | 1 |
| Message | First message |
| Timestamp | 1756880977.315875 |


**📤 Message Sent #2**

| Property | Value |
|----------|-------|
| Topic | test_topic_1756880977 |
| Partition | 0 |
| Offset | 1 |
| Key | key_2 |
| Message ID | 2 |
| Message | Second message |
| Timestamp | 1756880977.315876 |


**📤 Message Sent #3**

| Property | Value |
|----------|-------|
| Topic | test_topic_1756880977 |
| Partition | 0 |
| Offset | 2 |
| Key | key_3 |
| Message ID | 3 |
| Message | Third message |
| Timestamp | 1756880977.315876 |


**📥 Message Consumed #1**

| Property | Value |
|----------|-------|
| Topic | test_topic_1756880977 |
| Partition | 0 |
| Offset | 0 |
| Key | key_1 |
| Message ID | 1 |
| Message | First message |
| Timestamp | 1756880977430 |


**📥 Message Consumed #2**

| Property | Value |
|----------|-------|
| Topic | test_topic_1756880977 |
| Partition | 0 |
| Offset | 1 |
| Key | key_2 |
| Message ID | 2 |
| Message | Second message |
| Timestamp | 1756880977466 |


**📥 Message Consumed #3**

| Property | Value |
|----------|-------|
| Topic | test_topic_1756880977 |
| Partition | 0 |
| Offset | 2 |
| Key | key_3 |
| Message ID | 3 |
| Message | Third message |
| Timestamp | 1756880977474 |


</details>

### 4. 📥 TestKafkaOperations::test_consume_messages ✅

<details>
<summary><strong>📋 Test Information</strong></summary>

| Property | Value |
|----------|-------|
| 🏷️ **Test Name** | `TestKafkaOperations::test_consume_messages` |
| 📊 **Status** | ✅ PASSED |
| ⏱️ **Duration** | 12.11 seconds |
| 🕐 **Timestamp** | 2025-09-03T11:59:53.787424 |
| 📂 **Category** | Consume Operations |
| 🔢 **Test Index** | 4 |

</details>

<details>
<summary><strong>⚙️ Test Configuration</strong></summary>

**verbose_mode**: `True`

</details>

<details>
<summary><strong>🔍 Verbose Output</strong></summary>

================================================= test session starts =================================================
platform darwin -- Python 3.12.2, pytest-8.4.1, pluggy-1.5.0 -- /Users/anidhula/.pyenv/versions/3.12.2/bin/python
cachedir: .pytest_cache
rootdir: /Users/anidhula/learn/kafka-e2etest
configfile: pytest.ini
plugins: asyncio-1.1.0, cov-4.1.0, anyio-4.10.0, dash-2.14.2
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collecting ... collected 1 item

test_kafka.py::TestKafkaOperations::test_consume_messages PASSED                                                [100%]

================================================= 1 passed in 11.88s ==================================================


=== VERBOSE KAFKA OUTPUT ===
**📤 Message Sent #1**

| Property | Value |
|----------|-------|
| Topic | test_topic_1756880989 |
| Partition | 0 |
| Offset | 0 |
| Key | None |
| Message ID | 1 |
| Message | Test message 1 |
| Timestamp | N/A |


**📤 Message Sent #2**

| Property | Value |
|----------|-------|
| Topic | test_topic_1756880989 |
| Partition | 0 |
| Offset | 1 |
| Key | None |
| Message ID | 2 |
| Message | Test message 2 |
| Timestamp | N/A |


**📤 Message Sent #3**

| Property | Value |
|----------|-------|
| Topic | test_topic_1756880989 |
| Partition | 0 |
| Offset | 2 |
| Key | None |
| Message ID | 3 |
| Message | Test message 3 |
| Timestamp | N/A |


**📥 Message Consumed #1**

| Property | Value |
|----------|-------|
| Topic | test_topic_1756880989 |
| Partition | 0 |
| Offset | 0 |
| Key | None |
| Message ID | 1 |
| Message | Test message 1 |
| Timestamp | 1756880989411 |


**📥 Message Consumed #2**

| Property | Value |
|----------|-------|
| Topic | test_topic_1756880989 |
| Partition | 0 |
| Offset | 1 |
| Key | None |
| Message ID | 2 |
| Message | Test message 2 |
| Timestamp | 1756880989441 |


**📥 Message Consumed #3**

| Property | Value |
|----------|-------|
| Topic | test_topic_1756880989 |
| Partition | 0 |
| Offset | 2 |
| Key | None |
| Message ID | 3 |
| Message | Test message 3 |
| Timestamp | 1756880989445 |


</details>

### 5. 📥 TestKafkaOperations::test_consume_messages_with_group_id ✅

<details>
<summary><strong>📋 Test Information</strong></summary>

| Property | Value |
|----------|-------|
| 🏷️ **Test Name** | `TestKafkaOperations::test_consume_messages_with_group_id` |
| 📊 **Status** | ✅ PASSED |
| ⏱️ **Duration** | 11.33 seconds |
| 🕐 **Timestamp** | 2025-09-03T12:00:05.116608 |
| 📂 **Category** | Consume Operations |
| 🔢 **Test Index** | 5 |

</details>

<details>
<summary><strong>⚙️ Test Configuration</strong></summary>

**verbose_mode**: `True`

</details>

<details>
<summary><strong>🔍 Verbose Output</strong></summary>

================================================= test session starts =================================================
platform darwin -- Python 3.12.2, pytest-8.4.1, pluggy-1.5.0 -- /Users/anidhula/.pyenv/versions/3.12.2/bin/python
cachedir: .pytest_cache
rootdir: /Users/anidhula/learn/kafka-e2etest
configfile: pytest.ini
plugins: asyncio-1.1.0, cov-4.1.0, anyio-4.10.0, dash-2.14.2
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collecting ... collected 1 item

test_kafka.py::TestKafkaOperations::test_consume_messages_with_group_id PASSED                                  [100%]

================================================= 1 passed in 11.05s ==================================================


=== VERBOSE KAFKA OUTPUT ===
**📤 Message Sent**

| Property | Value |
|----------|-------|
| Topic | test_topic_1756880998 |
| Partition | 0 |
| Offset | 0 |
| Key | None |
| Message ID | 1 |
| Message | Group test message |
| Timestamp | N/A |


**📥 Message Consumed #1**

| Property | Value |
|----------|-------|
| Topic | test_topic_1756880998 |
| Partition | 0 |
| Offset | 0 |
| Key | None |
| Message ID | 1 |
| Message | Group test message |
| Timestamp | 1756881000823 |


</details>

### 6. 🏗️ TestKafkaOperations::test_get_topic_info ✅

<details>
<summary><strong>📋 Test Information</strong></summary>

| Property | Value |
|----------|-------|
| 🏷️ **Test Name** | `TestKafkaOperations::test_get_topic_info` |
| 📊 **Status** | ✅ PASSED |
| ⏱️ **Duration** | 9.63 seconds |
| 🕐 **Timestamp** | 2025-09-03T12:00:14.747749 |
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
================================================= test session starts =================================================
platform darwin -- Python 3.12.2, pytest-8.4.1, pluggy-1.5.0 -- /Users/anidhula/.pyenv/versions/3.12.2/bin/python
cachedir: .pytest_cache
rootdir: /Users/anidhula/learn/kafka-e2etest
configfile: pytest.ini
plugins: asyncio-1.1.0, cov-4.1.0, anyio-4.10.0, dash-2.14.2
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collecting ... collected 1 item

test_kafka.py::TestKafkaOperations::test_get_topic_info PASSED                                                  [100%]

================================================== 1 passed in 9.37s ==================================================

```

</details>

### 7. 🔧 TestKafkaOperations::test_get_partition_count ✅

<details>
<summary><strong>📋 Test Information</strong></summary>

| Property | Value |
|----------|-------|
| 🏷️ **Test Name** | `TestKafkaOperations::test_get_partition_count` |
| 📊 **Status** | ✅ PASSED |
| ⏱️ **Duration** | 13.44 seconds |
| 🕐 **Timestamp** | 2025-09-03T12:00:28.185738 |
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
================================================= test session starts =================================================
platform darwin -- Python 3.12.2, pytest-8.4.1, pluggy-1.5.0 -- /Users/anidhula/.pyenv/versions/3.12.2/bin/python
cachedir: .pytest_cache
rootdir: /Users/anidhula/learn/kafka-e2etest
configfile: pytest.ini
plugins: asyncio-1.1.0, cov-4.1.0, anyio-4.10.0, dash-2.14.2
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collecting ... collected 1 item

test_kafka.py::TestKafkaOperations::test_get_partition_count PASSED                                             [100%]

================================================= 1 passed in 13.04s ==================================================

```

</details>

### 8. 🔧 TestKafkaOperations::test_message_ordering ✅

<details>
<summary><strong>📋 Test Information</strong></summary>

| Property | Value |
|----------|-------|
| 🏷️ **Test Name** | `TestKafkaOperations::test_message_ordering` |
| 📊 **Status** | ✅ PASSED |
| ⏱️ **Duration** | 14.29 seconds |
| 🕐 **Timestamp** | 2025-09-03T12:00:42.472898 |
| 📂 **Category** | Other |
| 🔢 **Test Index** | 8 |

</details>

<details>
<summary><strong>⚙️ Test Configuration</strong></summary>

**verbose_mode**: `True`

</details>

<details>
<summary><strong>🔍 Verbose Output</strong></summary>

================================================= test session starts =================================================
platform darwin -- Python 3.12.2, pytest-8.4.1, pluggy-1.5.0 -- /Users/anidhula/.pyenv/versions/3.12.2/bin/python
cachedir: .pytest_cache
rootdir: /Users/anidhula/learn/kafka-e2etest
configfile: pytest.ini
plugins: asyncio-1.1.0, cov-4.1.0, anyio-4.10.0, dash-2.14.2
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collecting ... collected 1 item

test_kafka.py::TestKafkaOperations::test_message_ordering PASSED                                                [100%]

================================================= 1 passed in 13.86s ==================================================


=== VERBOSE KAFKA OUTPUT ===
**📤 Message Sent #1**

| Property | Value |
|----------|-------|
| Topic | test_topic_1756881037 |
| Partition | 0 |
| Offset | 0 |
| Key | None |
| Message ID | 1 |
| Message | N/A |
| Timestamp | N/A |


**📤 Message Sent #2**

| Property | Value |
|----------|-------|
| Topic | test_topic_1756881037 |
| Partition | 0 |
| Offset | 1 |
| Key | None |
| Message ID | 2 |
| Message | N/A |
| Timestamp | N/A |


**📤 Message Sent #3**

| Property | Value |
|----------|-------|
| Topic | test_topic_1756881037 |
| Partition | 0 |
| Offset | 2 |
| Key | None |
| Message ID | 3 |
| Message | N/A |
| Timestamp | N/A |


**📤 Message Sent #4**

| Property | Value |
|----------|-------|
| Topic | test_topic_1756881037 |
| Partition | 0 |
| Offset | 3 |
| Key | None |
| Message ID | 4 |
| Message | N/A |
| Timestamp | N/A |


**📥 Message Consumed #1**

| Property | Value |
|----------|-------|
| Topic | test_topic_1756881037 |
| Partition | 0 |
| Offset | 0 |
| Key | None |
| Message ID | 1 |
| Message | N/A |
| Timestamp | 1756881038009 |


**📥 Message Consumed #2**

| Property | Value |
|----------|-------|
| Topic | test_topic_1756881037 |
| Partition | 0 |
| Offset | 1 |
| Key | None |
| Message ID | 2 |
| Message | N/A |
| Timestamp | 1756881038040 |


**📥 Message Consumed #3**

| Property | Value |
|----------|-------|
| Topic | test_topic_1756881037 |
| Partition | 0 |
| Offset | 2 |
| Key | None |
| Message ID | 3 |
| Message | N/A |
| Timestamp | 1756881038043 |


**📥 Message Consumed #4**

| Property | Value |
|----------|-------|
| Topic | test_topic_1756881037 |
| Partition | 0 |
| Offset | 3 |
| Key | None |
| Message ID | 4 |
| Message | N/A |
| Timestamp | 1756881038047 |


</details>

### 9. 🔧 TestKafkaOperations::test_message_without_key ✅

<details>
<summary><strong>📋 Test Information</strong></summary>

| Property | Value |
|----------|-------|
| 🏷️ **Test Name** | `TestKafkaOperations::test_message_without_key` |
| 📊 **Status** | ✅ PASSED |
| ⏱️ **Duration** | 13.04 seconds |
| 🕐 **Timestamp** | 2025-09-03T12:00:55.515712 |
| 📂 **Category** | Other |
| 🔢 **Test Index** | 9 |

</details>

<details>
<summary><strong>⚙️ Test Configuration</strong></summary>

**verbose_mode**: `True`

</details>

<details>
<summary><strong>🔍 Verbose Output</strong></summary>

================================================= test session starts =================================================
platform darwin -- Python 3.12.2, pytest-8.4.1, pluggy-1.5.0 -- /Users/anidhula/.pyenv/versions/3.12.2/bin/python
cachedir: .pytest_cache
rootdir: /Users/anidhula/learn/kafka-e2etest
configfile: pytest.ini
plugins: asyncio-1.1.0, cov-4.1.0, anyio-4.10.0, dash-2.14.2
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collecting ... collected 1 item

test_kafka.py::TestKafkaOperations::test_message_without_key PASSED                                             [100%]

================================================= 1 passed in 12.69s ==================================================


=== VERBOSE KAFKA OUTPUT ===
**📤 Message Sent**

| Property | Value |
|----------|-------|
| Topic | test_topic_1756881050 |
| Partition | 0 |
| Offset | 0 |
| Key | None |
| Message ID | 1 |
| Message | No key message |
| Timestamp | N/A |


**📥 Message Consumed #1**

| Property | Value |
|----------|-------|
| Topic | test_topic_1756881050 |
| Partition | 0 |
| Offset | 0 |
| Key | None |
| Message ID | 1 |
| Message | No key message |
| Timestamp | 1756881051132 |


</details>

### 10. 🔧 TestKafkaOperations::test_large_message ✅

<details>
<summary><strong>📋 Test Information</strong></summary>

| Property | Value |
|----------|-------|
| 🏷️ **Test Name** | `TestKafkaOperations::test_large_message` |
| 📊 **Status** | ✅ PASSED |
| ⏱️ **Duration** | 12.87 seconds |
| 🕐 **Timestamp** | 2025-09-03T12:01:08.388360 |
| 📂 **Category** | Other |
| 🔢 **Test Index** | 10 |

</details>

<details>
<summary><strong>⚙️ Test Configuration</strong></summary>

**verbose_mode**: `True`

</details>

<details>
<summary><strong>🔍 Verbose Output</strong></summary>

================================================= test session starts =================================================
platform darwin -- Python 3.12.2, pytest-8.4.1, pluggy-1.5.0 -- /Users/anidhula/.pyenv/versions/3.12.2/bin/python
cachedir: .pytest_cache
rootdir: /Users/anidhula/learn/kafka-e2etest
configfile: pytest.ini
plugins: asyncio-1.1.0, cov-4.1.0, anyio-4.10.0, dash-2.14.2
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collecting ... collected 1 item

test_kafka.py::TestKafkaOperations::test_large_message PASSED                                                   [100%]

================================================= 1 passed in 12.55s ==================================================


=== VERBOSE KAFKA OUTPUT ===
**📤 Message Sent**

| Property | Value |
|----------|-------|
| Topic | test_topic_1756881063 |
| Partition | 0 |
| Offset | 0 |
| Key | None |
| Message ID | 1 |
| Message | N/A |
| Timestamp | 1756881063.899107 |


**📥 Message Consumed #1**

| Property | Value |
|----------|-------|
| Topic | test_topic_1756881063 |
| Partition | 0 |
| Offset | 0 |
| Key | None |
| Message ID | 1 |
| Message | N/A |
| Timestamp | 1756881064015 |


</details>

### 11. 📤 TestKafkaQueueLength::test_queue_length_after_sending ✅

<details>
<summary><strong>📋 Test Information</strong></summary>

| Property | Value |
|----------|-------|
| 🏷️ **Test Name** | `TestKafkaQueueLength::test_queue_length_after_sending` |
| 📊 **Status** | ✅ PASSED |
| ⏱️ **Duration** | 15.32 seconds |
| 🕐 **Timestamp** | 2025-09-03T12:01:23.712791 |
| 📂 **Category** | Send Operations |
| 🔢 **Test Index** | 11 |

</details>

<details>
<summary><strong>⚙️ Test Configuration</strong></summary>

**verbose_mode**: `True`

</details>

<details>
<summary><strong>🔍 Verbose Output</strong></summary>

================================================= test session starts =================================================
platform darwin -- Python 3.12.2, pytest-8.4.1, pluggy-1.5.0 -- /Users/anidhula/.pyenv/versions/3.12.2/bin/python
cachedir: .pytest_cache
rootdir: /Users/anidhula/learn/kafka-e2etest
configfile: pytest.ini
plugins: asyncio-1.1.0, cov-4.1.0, anyio-4.10.0, dash-2.14.2
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collecting ... collected 1 item

test_kafka.py::TestKafkaQueueLength::test_queue_length_after_sending PASSED                                     [100%]

================================================= 1 passed in 15.07s ==================================================


=== VERBOSE KAFKA OUTPUT ===
**📤 Message Sent #1**

| Property | Value |
|----------|-------|
| Topic | queue_test_topic_1756881075 |
| Partition | 0 |
| Offset | 0 |
| Key | None |
| Message ID | 1 |
| Message | Message 1 |
| Timestamp | N/A |


**📤 Message Sent #2**

| Property | Value |
|----------|-------|
| Topic | queue_test_topic_1756881075 |
| Partition | 0 |
| Offset | 1 |
| Key | None |
| Message ID | 2 |
| Message | Message 2 |
| Timestamp | N/A |


**📤 Message Sent #3**

| Property | Value |
|----------|-------|
| Topic | queue_test_topic_1756881075 |
| Partition | 0 |
| Offset | 2 |
| Key | None |
| Message ID | 3 |
| Message | Message 3 |
| Timestamp | N/A |


**📤 Message Sent #4**

| Property | Value |
|----------|-------|
| Topic | queue_test_topic_1756881075 |
| Partition | 0 |
| Offset | 3 |
| Key | None |
| Message ID | 4 |
| Message | Message 4 |
| Timestamp | N/A |


**📤 Message Sent #5**

| Property | Value |
|----------|-------|
| Topic | queue_test_topic_1756881075 |
| Partition | 0 |
| Offset | 4 |
| Key | None |
| Message ID | 5 |
| Message | Message 5 |
| Timestamp | N/A |


**📥 Message Consumed #1**

| Property | Value |
|----------|-------|
| Topic | queue_test_topic_1756881075 |
| Partition | 0 |
| Offset | 0 |
| Key | None |
| Message ID | 1 |
| Message | Message 1 |
| Timestamp | 1756881076088 |


**📥 Message Consumed #2**

| Property | Value |
|----------|-------|
| Topic | queue_test_topic_1756881075 |
| Partition | 0 |
| Offset | 1 |
| Key | None |
| Message ID | 2 |
| Message | Message 2 |
| Timestamp | 1756881076119 |


**📥 Message Consumed #3**

| Property | Value |
|----------|-------|
| Topic | queue_test_topic_1756881075 |
| Partition | 0 |
| Offset | 2 |
| Key | None |
| Message ID | 3 |
| Message | Message 3 |
| Timestamp | 1756881076124 |


**📥 Message Consumed #4**

| Property | Value |
|----------|-------|
| Topic | queue_test_topic_1756881075 |
| Partition | 0 |
| Offset | 3 |
| Key | None |
| Message ID | 4 |
| Message | Message 4 |
| Timestamp | 1756881076127 |


**📥 Message Consumed #5**

| Property | Value |
|----------|-------|
| Topic | queue_test_topic_1756881075 |
| Partition | 0 |
| Offset | 4 |
| Key | None |
| Message ID | 5 |
| Message | Message 5 |
| Timestamp | 1756881076130 |


</details>

### 12. 📊 TestKafkaQueueLength::test_partition_distribution ✅

<details>
<summary><strong>📋 Test Information</strong></summary>

| Property | Value |
|----------|-------|
| 🏷️ **Test Name** | `TestKafkaQueueLength::test_partition_distribution` |
| 📊 **Status** | ✅ PASSED |
| ⏱️ **Duration** | 12.75 seconds |
| 🕐 **Timestamp** | 2025-09-03T12:01:36.465113 |
| 📂 **Category** | Queue Length Operations |
| 🔢 **Test Index** | 12 |

</details>

<details>
<summary><strong>⚙️ Test Configuration</strong></summary>

**verbose_mode**: `True`

</details>

<details>
<summary><strong>🔍 Verbose Output</strong></summary>

================================================= test session starts =================================================
platform darwin -- Python 3.12.2, pytest-8.4.1, pluggy-1.5.0 -- /Users/anidhula/.pyenv/versions/3.12.2/bin/python
cachedir: .pytest_cache
rootdir: /Users/anidhula/learn/kafka-e2etest
configfile: pytest.ini
plugins: asyncio-1.1.0, cov-4.1.0, anyio-4.10.0, dash-2.14.2
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collecting ... collected 1 item

test_kafka.py::TestKafkaQueueLength::test_partition_distribution PASSED                                         [100%]

================================================= 1 passed in 12.49s ==================================================


=== VERBOSE KAFKA OUTPUT ===
**📤 Message Sent #1**

| Property | Value |
|----------|-------|
| Topic | queue_test_topic_1756881091 |
| Partition | 2 |
| Offset | 0 |
| Key | None |
| Message ID | 1 |
| Message | Message 1 |
| Timestamp | N/A |


**📤 Message Sent #2**

| Property | Value |
|----------|-------|
| Topic | queue_test_topic_1756881091 |
| Partition | 1 |
| Offset | 0 |
| Key | None |
| Message ID | 2 |
| Message | Message 2 |
| Timestamp | N/A |


**📤 Message Sent #3**

| Property | Value |
|----------|-------|
| Topic | queue_test_topic_1756881091 |
| Partition | 2 |
| Offset | 1 |
| Key | None |
| Message ID | 3 |
| Message | Message 3 |
| Timestamp | N/A |


**📤 Message Sent #4**

| Property | Value |
|----------|-------|
| Topic | queue_test_topic_1756881091 |
| Partition | 2 |
| Offset | 2 |
| Key | None |
| Message ID | 4 |
| Message | Message 4 |
| Timestamp | N/A |


**📤 Message Sent #5**

| Property | Value |
|----------|-------|
| Topic | queue_test_topic_1756881091 |
| Partition | 2 |
| Offset | 3 |
| Key | None |
| Message ID | 5 |
| Message | Message 5 |
| Timestamp | N/A |


**📥 Message Consumed #1**

| Property | Value |
|----------|-------|
| Topic | queue_test_topic_1756881091 |
| Partition | 1 |
| Offset | 0 |
| Key | None |
| Message ID | 2 |
| Message | Message 2 |
| Timestamp | 1756881092245 |


**📥 Message Consumed #2**

| Property | Value |
|----------|-------|
| Topic | queue_test_topic_1756881091 |
| Partition | 2 |
| Offset | 0 |
| Key | None |
| Message ID | 1 |
| Message | Message 1 |
| Timestamp | 1756881092214 |


**📥 Message Consumed #3**

| Property | Value |
|----------|-------|
| Topic | queue_test_topic_1756881091 |
| Partition | 2 |
| Offset | 1 |
| Key | None |
| Message ID | 3 |
| Message | Message 3 |
| Timestamp | 1756881092249 |


**📥 Message Consumed #4**

| Property | Value |
|----------|-------|
| Topic | queue_test_topic_1756881091 |
| Partition | 2 |
| Offset | 2 |
| Key | None |
| Message ID | 4 |
| Message | Message 4 |
| Timestamp | 1756881092253 |


**📥 Message Consumed #5**

| Property | Value |
|----------|-------|
| Topic | queue_test_topic_1756881091 |
| Partition | 2 |
| Offset | 3 |
| Key | None |
| Message ID | 5 |
| Message | Message 5 |
| Timestamp | 1756881092257 |


</details>

### 13. 📊 TestKafkaQueueLength::test_queue_length_verbose ✅

<details>
<summary><strong>📋 Test Information</strong></summary>

| Property | Value |
|----------|-------|
| 🏷️ **Test Name** | `TestKafkaQueueLength::test_queue_length_verbose` |
| 📊 **Status** | ✅ PASSED |
| ⏱️ **Duration** | 13.11 seconds |
| 🕐 **Timestamp** | 2025-09-03T12:01:49.573315 |
| 📂 **Category** | Queue Length Operations |
| 🔢 **Test Index** | 13 |

</details>

<details>
<summary><strong>⚙️ Test Configuration</strong></summary>

**verbose_mode**: `True`

</details>

<details>
<summary><strong>🔍 Verbose Output</strong></summary>

================================================= test session starts =================================================
platform darwin -- Python 3.12.2, pytest-8.4.1, pluggy-1.5.0 -- /Users/anidhula/.pyenv/versions/3.12.2/bin/python
cachedir: .pytest_cache
rootdir: /Users/anidhula/learn/kafka-e2etest
configfile: pytest.ini
plugins: asyncio-1.1.0, cov-4.1.0, anyio-4.10.0, dash-2.14.2
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collecting ... collected 1 item

test_kafka.py::TestKafkaQueueLength::test_queue_length_verbose PASSED                                           [100%]

================================================= 1 passed in 12.84s ==================================================


=== VERBOSE KAFKA OUTPUT ===
**📤 Message Sent #1**

| Property | Value |
|----------|-------|
| Topic | queue_test_topic_1756881104 |
| Partition | 0 |
| Offset | 0 |
| Key | None |
| Message ID | 1 |
| Message | Message 1 |
| Timestamp | N/A |


**📤 Message Sent #2**

| Property | Value |
|----------|-------|
| Topic | queue_test_topic_1756881104 |
| Partition | 0 |
| Offset | 1 |
| Key | None |
| Message ID | 2 |
| Message | Message 2 |
| Timestamp | N/A |


**📤 Message Sent #3**

| Property | Value |
|----------|-------|
| Topic | queue_test_topic_1756881104 |
| Partition | 0 |
| Offset | 2 |
| Key | None |
| Message ID | 3 |
| Message | Message 3 |
| Timestamp | N/A |


**📊 Queue Length Information**

| Metric | Value |
|--------|-------|
| Topic | queue_test_topic_1756881104 |
| Total Messages | 3 |
| Read Messages | 0 |
| Queue Length | 3 |


**📥 Message Consumed #1**

| Property | Value |
|----------|-------|
| Topic | queue_test_topic_1756881104 |
| Partition | 0 |
| Offset | 0 |
| Key | None |
| Message ID | 1 |
| Message | Message 1 |
| Timestamp | 1756881104292 |


**📥 Message Consumed #2**

| Property | Value |
|----------|-------|
| Topic | queue_test_topic_1756881104 |
| Partition | 0 |
| Offset | 1 |
| Key | None |
| Message ID | 2 |
| Message | Message 2 |
| Timestamp | 1756881104323 |


**📊 Queue Length Information**

| Metric | Value |
|--------|-------|
| Topic | queue_test_topic_1756881104 |
| Total Messages | 3 |
| Read Messages | 0 |
| Queue Length | 3 |


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
| 📅 **Report Generated** | 2025-09-03 12:01:49 |

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
| ⚡ **Average Duration** | 12.05s |
| 🐌 **Slow Tests (>15s)** | 1 |
| ⚡ **Fast Tests (<5s)** | 1 |

**Slow tests that might need optimization:**
- 🐌 `TestKafkaQueueLength::test_queue_length_after_sending` (15.32s)

---

## 📝 Report Footer

<div align="center">

**Generated by Kafka E2E Testing Suite** 🚀

*Report generated on September 03, 2025 at 12:01:49*

![Kafka](https://img.shields.io/badge/Apache-Kafka-231F20?style=flat&logo=apache-kafka&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-6.0+-0A9EDC?style=flat&logo=pytest&logoColor=white)

</div>
