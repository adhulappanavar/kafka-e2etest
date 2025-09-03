# 🚀 Kafka E2E Test Report ⚠️

🔴 **Some Tests Failed** | ![Test Status](https://img.shields.io/badge/Tests-4%2F13-red) | ![Coverage](https://img.shields.io/badge/Coverage-30.8%25-red) | ![Duration](https://img.shields.io/badge/Duration-145.1s-blue)

---

## 📊 Executive Summary

| Metric | Value | Status |
|--------|-------|--------|
| 🕐 **Test Session** | 2025-09-03 11:48:54 → 2025-09-03 11:51:19 | 📅 |
| ⏱️ **Total Duration** | 145.12 seconds | ⏰ |
| 🧪 **Total Tests** | 13 | 🔢 |
| ✅ **Passed** | 4 | 🟢 |
| ❌ **Failed** | 9 | 🔴 |
| 📈 **Success Rate** | 30.8% | 🔴 |

## 🧪 Test Results Overview

| 🏷️ Test Name | 📊 Status | ⏱️ Duration | 📋 Details |
|--------------|-----------|-------------|------------|
| TestKafkaOperations::test_create_topic | ✅ PASSED | ⚡ 3.63s | test_index: 1; category: Topic Management; verbose_mode: True |
| TestKafkaOperations::test_send_single_message | ❌ FAILED | ⏱️ 9.23s | test_index: 2; category: Send Operations; verbose_mode: True |
| TestKafkaOperations::test_send_multiple_messages | ❌ FAILED | ⏱️ 13.22s | test_index: 3; category: Send Operations; verbose_mode: True |
| TestKafkaOperations::test_consume_messages | ❌ FAILED | ⏱️ 12.88s | test_index: 4; category: Consume Operations; verbose_mode: True |
| TestKafkaOperations::test_consume_messages_with_group_id | ✅ PASSED | ⏱️ 11.04s | test_index: 5; category: Consume Operations; verbose_mode: True |
| TestKafkaOperations::test_get_topic_info | ✅ PASSED | ⏱️ 9.53s | test_index: 6; category: Topic Management; verbose_mode: True |
| TestKafkaOperations::test_get_partition_count | ✅ PASSED | ⏱️ 11.07s | test_index: 7; category: Other; verbose_mode: True |
| TestKafkaOperations::test_message_ordering | ❌ FAILED | ⏱️ 12.21s | test_index: 8; category: Other; verbose_mode: True |
| TestKafkaOperations::test_message_without_key | ❌ FAILED | ⏱️ 10.92s | test_index: 9; category: Other; verbose_mode: True |
| TestKafkaOperations::test_large_message | ❌ FAILED | ⏱️ 9.84s | test_index: 10; category: Other; verbose_mode: True |
| TestKafkaQueueLength::test_queue_length_after_sending | ❌ FAILED | ⏱️ 13.57s | test_index: 11; category: Send Operations; verbose_mode: True |
| TestKafkaQueueLength::test_partition_distribution | ❌ FAILED | ⏱️ 11.13s | test_index: 12; category: Queue Length Operations; verbose_mode: True |
| TestKafkaQueueLength::test_queue_length_verbose | ❌ FAILED | ⏱️ 10.90s | test_index: 13; category: Queue Length Operations; verbose_mode: True |

---

## 🔍 Detailed Test Information

### 1. 🏗️ TestKafkaOperations::test_create_topic ✅

<details>
<summary><strong>📋 Test Information</strong></summary>

| Property | Value |
|----------|-------|
| 🏷️ **Test Name** | `TestKafkaOperations::test_create_topic` |
| 📊 **Status** | ✅ PASSED |
| ⏱️ **Duration** | 3.63 seconds |
| 🕐 **Timestamp** | 2025-09-03T11:49:03.613751 |
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

================================================== 1 passed in 2.26s ==================================================

```

</details>

### 2. 📤 TestKafkaOperations::test_send_single_message ❌

<details>
<summary><strong>📋 Test Information</strong></summary>

| Property | Value |
|----------|-------|
| 🏷️ **Test Name** | `TestKafkaOperations::test_send_single_message` |
| 📊 **Status** | ❌ FAILED |
| ⏱️ **Duration** | 9.23 seconds |
| 🕐 **Timestamp** | 2025-09-03T11:49:12.844563 |
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
================================================= test session starts =================================================
platform darwin -- Python 3.12.2, pytest-8.4.1, pluggy-1.5.0 -- /Users/anidhula/.pyenv/versions/3.12.2/bin/python
cachedir: .pytest_cache
rootdir: /Users/anidhula/learn/kafka-e2etest
configfile: pytest.ini
plugins: asyncio-1.1.0, cov-4.1.0, anyio-4.10.0, dash-2.14.2
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collecting ... collected 1 item

test_kafka.py::TestKafkaOperations::test_send_single_message FAILED                                             [100%]

====================================================== FAILURES =======================================================
____________________________________ TestKafkaOperations.test_send_single_message _____________________________________
test_kafka.py:76: in test_send_single_message
    assert success is True
E   assert False is True
------------------------------------------------ Captured stdout setup ------------------------------------------------
Starting Kafka with docker-compose...
Kafka is ready!
------------------------------------------------ Captured stderr setup ------------------------------------------------
 Network kafka-e2etest_default  Creating
 Network kafka-e2etest_default  Created
 Container zookeeper  Creating
 Container zookeeper  Created
 Container kafka  Creating
 Container kafka  Created
 Container zookeeper  Starting
 Container zookeeper  Started
 Container kafka  Starting
 Container kafka  Started
------------------------------------------------- Captured log setup --------------------------------------------------
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:1163 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: socket disconnected
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: socket disconnected
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.06 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:1163 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: socket disconnected
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: socket disconnected
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.12 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:1163 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: socket disconnected
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: socket disconnected
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.23 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:1163 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: socket disconnected
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: socket disconnected
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.48 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:1163 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: socket disconnected
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: socket disconnected
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.72 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:1163 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: socket disconnected
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: socket disconnected
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.36 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
------------------------------------------------ Captured stdout call -------------------------------------------------
           📤 Message Sent            
┏━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Property   ┃ Value                 ┃
┡━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━┩
│ Topic      │ test_topic_1756880348 │
│ Partition  │ 0                     │
│ Offset     │ 0                     │
│ Key        │ test_key_1            │
│ Message ID │ 1                     │
│ Message    │ Hello Kafka!          │
│ Timestamp  │ 1756880350.082719     │
└────────────┴───────────────────────┘
Error sending message: 'Row' object has no attribute 'cells'
-------------------------------------------------- Captured log call --------------------------------------------------
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-producer-1, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-producer-1, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-producer-1, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-producer-1, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
---------------------------------------------- Captured stdout teardown -----------------------------------------------
Stopping Kafka...
---------------------------------------------- Captured stderr teardown -----------------------------------------------
 Container kafka  Stopping
 Container kafka  Stopped
 Container kafka  Removing
 Container kafka  Removed
 Container zookeeper  Stopping
 Container zookeeper  Stopped
 Container zookeeper  Removing
 Container zookeeper  Removed
 Network kafka-e2etest_default  Removing
 Network kafka-e2etest_default  Removed
=============================================== short test summary info ===============================================
FAILED test_kafka.py::TestKafkaOperations::test_send_single_message - assert False is True
================================================== 1 failed in 9.01s ==================================================

```

</details>

### 3. 📤 TestKafkaOperations::test_send_multiple_messages ❌

<details>
<summary><strong>📋 Test Information</strong></summary>

| Property | Value |
|----------|-------|
| 🏷️ **Test Name** | `TestKafkaOperations::test_send_multiple_messages` |
| 📊 **Status** | ❌ FAILED |
| ⏱️ **Duration** | 13.22 seconds |
| 🕐 **Timestamp** | 2025-09-03T11:49:26.062295 |
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
================================================= test session starts =================================================
platform darwin -- Python 3.12.2, pytest-8.4.1, pluggy-1.5.0 -- /Users/anidhula/.pyenv/versions/3.12.2/bin/python
cachedir: .pytest_cache
rootdir: /Users/anidhula/learn/kafka-e2etest
configfile: pytest.ini
plugins: asyncio-1.1.0, cov-4.1.0, anyio-4.10.0, dash-2.14.2
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collecting ... collected 1 item

test_kafka.py::TestKafkaOperations::test_send_multiple_messages FAILED                                          [100%]

====================================================== FAILURES =======================================================
___________________________________ TestKafkaOperations.test_send_multiple_messages ___________________________________
test_kafka.py:111: in test_send_multiple_messages
    assert len(messages) == 3
E   AssertionError: assert 1 == 3
E    +  where 1 = len([{'key': 'key_1', 'offset': 0, 'partition': 0, 'timestamp': 1756880361541, ...}])
------------------------------------------------ Captured stdout setup ------------------------------------------------
Starting Kafka with docker-compose...
Kafka is ready!
------------------------------------------------ Captured stderr setup ------------------------------------------------
 Network kafka-e2etest_default  Creating
 Network kafka-e2etest_default  Created
 Container zookeeper  Creating
 Container zookeeper  Created
 Container kafka  Creating
 Container kafka  Created
 Container zookeeper  Starting
 Container zookeeper  Started
 Container kafka  Starting
 Container kafka  Started
------------------------------------------------- Captured log setup --------------------------------------------------
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.06 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.10 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.23 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.45 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.79 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.35 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:1163 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: socket disconnected
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: socket disconnected
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.04 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:1163 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: socket disconnected
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: socket disconnected
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.10 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:1163 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: socket disconnected
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: socket disconnected
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.19 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:1163 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: socket disconnected
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: socket disconnected
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.41 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
WARNING  kafka.client:client_async.py:794 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]> timed out after 62.5 ms. Closing connection.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. [Error 7] RequestTimedOutError: Request timed out after 62.5 ms
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.89 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
------------------------------------------------ Captured stdout call -------------------------------------------------

📤 Sending 3 messages to topic 'test_topic_1756880361'
          📤 Message Sent #1          
┏━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Property   ┃ Value                 ┃
┡━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━┩
│ Topic      │ test_topic_1756880361 │
│ Partition  │ 0                     │
│ Offset     │ 0                     │
│ Key        │ key_1                 │
│ Message ID │ 1                     │
│ Message    │ First message         │
│ Timestamp  │ 1756880361.427757     │
└────────────┴───────────────────────┘
Error sending message 0: 'Row' object has no attribute 'cells'
          📤 Message Sent #2          
┏━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Property   ┃ Value                 ┃
┡━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━┩
│ Topic      │ test_topic_1756880361 │
│ Partition  │ 0                     │
│ Offset     │ 1                     │
│ Key        │ key_2                 │
│ Message ID │ 2                     │
│ Message    │ Second message        │
│ Timestamp  │ 1756880361.427757     │
└────────────┴───────────────────────┘
Error sending message 1: 'Row' object has no attribute 'cells'
          📤 Message Sent #3          
┏━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Property   ┃ Value                 ┃
┡━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━┩
│ Topic      │ test_topic_1756880361 │
│ Partition  │ 0                     │
│ Offset     │ 2                     │
│ Key        │ key_3                 │
│ Message ID │ 3                     │
│ Message    │ Third message         │
│ Timestamp  │ 1756880361.427758     │
└────────────┴───────────────────────┘
Error sending message 2: 'Row' object has no attribute 'cells'
✓ Successfully sent 3/3 messages


📥 Consuming messages from topic 'test_topic_1756880361' (max: 3)
        📥 Message Consumed #1        
┏━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Property   ┃ Value                 ┃
┡━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━┩
│ Topic      │ test_topic_1756880361 │
│ Partition  │ 0                     │
│ Offset     │ 0                     │
│ Key        │ key_1                 │
│ Message ID │ 1                     │
│ Message    │ First message         │
│ Timestamp  │ 1756880361541         │
└────────────┴───────────────────────┘
Error consuming messages: 'Row' object has no attribute 'cells'
✓ Consumed 1 messages from topic 'test_topic_1756880361'

-------------------------------------------------- Captured log call --------------------------------------------------
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-producer-2, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-producer-2, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-producer-2, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-producer-2, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=coordinator-1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=coordinator-1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
---------------------------------------------- Captured stdout teardown -----------------------------------------------
Stopping Kafka...
---------------------------------------------- Captured stderr teardown -----------------------------------------------
 Container kafka  Stopping
 Container kafka  Stopped
 Container kafka  Removing
 Container kafka  Removed
 Container zookeeper  Stopping
 Container zookeeper  Stopped
 Container zookeeper  Removing
 Container zookeeper  Removed
 Network kafka-e2etest_default  Removing
 Network kafka-e2etest_default  Removed
=============================================== short test summary info ===============================================
FAILED test_kafka.py::TestKafkaOperations::test_send_multiple_messages - AssertionError: assert 1 == 3
================================================= 1 failed in 12.96s ==================================================

```

</details>

### 4. 📥 TestKafkaOperations::test_consume_messages ❌

<details>
<summary><strong>📋 Test Information</strong></summary>

| Property | Value |
|----------|-------|
| 🏷️ **Test Name** | `TestKafkaOperations::test_consume_messages` |
| 📊 **Status** | ❌ FAILED |
| ⏱️ **Duration** | 12.88 seconds |
| 🕐 **Timestamp** | 2025-09-03T11:49:38.941466 |
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
================================================= test session starts =================================================
platform darwin -- Python 3.12.2, pytest-8.4.1, pluggy-1.5.0 -- /Users/anidhula/.pyenv/versions/3.12.2/bin/python
cachedir: .pytest_cache
rootdir: /Users/anidhula/learn/kafka-e2etest
configfile: pytest.ini
plugins: asyncio-1.1.0, cov-4.1.0, anyio-4.10.0, dash-2.14.2
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collecting ... collected 1 item

test_kafka.py::TestKafkaOperations::test_consume_messages FAILED                                                [100%]

====================================================== FAILURES =======================================================
______________________________________ TestKafkaOperations.test_consume_messages ______________________________________
test_kafka.py:139: in test_consume_messages
    assert len(messages) >= 3
E   AssertionError: assert 1 >= 3
E    +  where 1 = len([{'key': None, 'offset': 0, 'partition': 0, 'timestamp': 1756880374803, ...}])
------------------------------------------------ Captured stdout setup ------------------------------------------------
Starting Kafka with docker-compose...
Kafka is ready!
------------------------------------------------ Captured stderr setup ------------------------------------------------
 Network kafka-e2etest_default  Creating
 Network kafka-e2etest_default  Created
 Container zookeeper  Creating
 Container zookeeper  Created
 Container kafka  Creating
 Container kafka  Created
 Container zookeeper  Starting
 Container zookeeper  Started
 Container kafka  Starting
 Container kafka  Started
------------------------------------------------- Captured log setup --------------------------------------------------
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.06 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.12 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.18 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.35 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.75 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.51 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:1163 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: socket disconnected
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: socket disconnected
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.05 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:1163 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: socket disconnected
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: socket disconnected
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.09 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:1163 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: socket disconnected
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: socket disconnected
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.16 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:1163 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: socket disconnected
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: socket disconnected
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.48 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
WARNING  kafka.client:client_async.py:794 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]> timed out after 62.5 ms. Closing connection.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. [Error 7] RequestTimedOutError: Request timed out after 62.5 ms
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.85 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
------------------------------------------------ Captured stdout call -------------------------------------------------

📤 Sending 3 messages to topic 'test_topic_1756880374'
          📤 Message Sent #1          
┏━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Property   ┃ Value                 ┃
┡━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━┩
│ Topic      │ test_topic_1756880374 │
│ Partition  │ 0                     │
│ Offset     │ 0                     │
│ Key        │ None                  │
│ Message ID │ 1                     │
│ Message    │ Test message 1        │
│ Timestamp  │ N/A                   │
└────────────┴───────────────────────┘
Error sending message 0: 'Row' object has no attribute 'cells'
          📤 Message Sent #2          
┏━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Property   ┃ Value                 ┃
┡━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━┩
│ Topic      │ test_topic_1756880374 │
│ Partition  │ 0                     │
│ Offset     │ 1                     │
│ Key        │ None                  │
│ Message ID │ 2                     │
│ Message    │ Test message 2        │
│ Timestamp  │ N/A                   │
└────────────┴───────────────────────┘
Error sending message 1: 'Row' object has no attribute 'cells'
          📤 Message Sent #3          
┏━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Property   ┃ Value                 ┃
┡━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━┩
│ Topic      │ test_topic_1756880374 │
│ Partition  │ 0                     │
│ Offset     │ 2                     │
│ Key        │ None                  │
│ Message ID │ 3                     │
│ Message    │ Test message 3        │
│ Timestamp  │ N/A                   │
└────────────┴───────────────────────┘
Error sending message 2: 'Row' object has no attribute 'cells'
✓ Successfully sent 3/3 messages


📥 Consuming messages from topic 'test_topic_1756880374' (max: 5)
        📥 Message Consumed #1        
┏━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Property   ┃ Value                 ┃
┡━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━┩
│ Topic      │ test_topic_1756880374 │
│ Partition  │ 0                     │
│ Offset     │ 0                     │
│ Key        │ None                  │
│ Message ID │ 1                     │
│ Message    │ Test message 1        │
│ Timestamp  │ 1756880374803         │
└────────────┴───────────────────────┘
Error consuming messages: 'Row' object has no attribute 'cells'
✓ Consumed 1 messages from topic 'test_topic_1756880374'

-------------------------------------------------- Captured log call --------------------------------------------------
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-producer-3, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-producer-3, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-producer-3, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-producer-3, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=coordinator-1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=coordinator-1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
---------------------------------------------- Captured stdout teardown -----------------------------------------------
Stopping Kafka...
---------------------------------------------- Captured stderr teardown -----------------------------------------------
 Container kafka  Stopping
 Container kafka  Stopped
 Container kafka  Removing
 Container kafka  Removed
 Container zookeeper  Stopping
 Container zookeeper  Stopped
 Container zookeeper  Removing
 Container zookeeper  Removed
 Network kafka-e2etest_default  Removing
 Network kafka-e2etest_default  Removed
=============================================== short test summary info ===============================================
FAILED test_kafka.py::TestKafkaOperations::test_consume_messages - AssertionError: assert 1 >= 3
================================================= 1 failed in 12.61s ==================================================

```

</details>

### 5. 📥 TestKafkaOperations::test_consume_messages_with_group_id ✅

<details>
<summary><strong>📋 Test Information</strong></summary>

| Property | Value |
|----------|-------|
| 🏷️ **Test Name** | `TestKafkaOperations::test_consume_messages_with_group_id` |
| 📊 **Status** | ✅ PASSED |
| ⏱️ **Duration** | 11.04 seconds |
| 🕐 **Timestamp** | 2025-09-03T11:49:49.978457 |
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
================================================= test session starts =================================================
platform darwin -- Python 3.12.2, pytest-8.4.1, pluggy-1.5.0 -- /Users/anidhula/.pyenv/versions/3.12.2/bin/python
cachedir: .pytest_cache
rootdir: /Users/anidhula/learn/kafka-e2etest
configfile: pytest.ini
plugins: asyncio-1.1.0, cov-4.1.0, anyio-4.10.0, dash-2.14.2
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collecting ... collected 1 item

test_kafka.py::TestKafkaOperations::test_consume_messages_with_group_id PASSED                                  [100%]

================================================= 1 passed in 10.78s ==================================================

```

</details>

### 6. 🏗️ TestKafkaOperations::test_get_topic_info ✅

<details>
<summary><strong>📋 Test Information</strong></summary>

| Property | Value |
|----------|-------|
| 🏷️ **Test Name** | `TestKafkaOperations::test_get_topic_info` |
| 📊 **Status** | ✅ PASSED |
| ⏱️ **Duration** | 9.53 seconds |
| 🕐 **Timestamp** | 2025-09-03T11:49:59.504470 |
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

================================================== 1 passed in 9.29s ==================================================

```

</details>

### 7. 🔧 TestKafkaOperations::test_get_partition_count ✅

<details>
<summary><strong>📋 Test Information</strong></summary>

| Property | Value |
|----------|-------|
| 🏷️ **Test Name** | `TestKafkaOperations::test_get_partition_count` |
| 📊 **Status** | ✅ PASSED |
| ⏱️ **Duration** | 11.07 seconds |
| 🕐 **Timestamp** | 2025-09-03T11:50:10.574430 |
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

================================================= 1 passed in 10.84s ==================================================

```

</details>

### 8. 🔧 TestKafkaOperations::test_message_ordering ❌

<details>
<summary><strong>📋 Test Information</strong></summary>

| Property | Value |
|----------|-------|
| 🏷️ **Test Name** | `TestKafkaOperations::test_message_ordering` |
| 📊 **Status** | ❌ FAILED |
| ⏱️ **Duration** | 12.21 seconds |
| 🕐 **Timestamp** | 2025-09-03T11:50:22.789444 |
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
================================================= test session starts =================================================
platform darwin -- Python 3.12.2, pytest-8.4.1, pluggy-1.5.0 -- /Users/anidhula/.pyenv/versions/3.12.2/bin/python
cachedir: .pytest_cache
rootdir: /Users/anidhula/learn/kafka-e2etest
configfile: pytest.ini
plugins: asyncio-1.1.0, cov-4.1.0, anyio-4.10.0, dash-2.14.2
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collecting ... collected 1 item

test_kafka.py::TestKafkaOperations::test_message_ordering FAILED                                                [100%]

====================================================== FAILURES =======================================================
______________________________________ TestKafkaOperations.test_message_ordering ______________________________________
test_kafka.py:227: in test_message_ordering
    assert len(consumed_messages) == 4
E   AssertionError: assert 1 == 4
E    +  where 1 = len([{'key': None, 'offset': 0, 'partition': 0, 'timestamp': 1756880418367, ...}])
------------------------------------------------ Captured stdout setup ------------------------------------------------
Starting Kafka with docker-compose...
Kafka is ready!
------------------------------------------------ Captured stderr setup ------------------------------------------------
 Network kafka-e2etest_default  Creating
 Network kafka-e2etest_default  Created
 Container zookeeper  Creating
 Container zookeeper  Created
 Container kafka  Creating
 Container kafka  Created
 Container zookeeper  Starting
 Container zookeeper  Started
 Container kafka  Starting
 Container kafka  Started
------------------------------------------------- Captured log setup --------------------------------------------------
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.04 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.11 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.20 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.46 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.93 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.23 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:1163 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: socket disconnected
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: socket disconnected
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.05 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:1163 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: socket disconnected
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: socket disconnected
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.10 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:1163 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: socket disconnected
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: socket disconnected
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.22 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
WARNING  kafka.client:client_async.py:794 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]> timed out after 125.0 ms. Closing connection.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. [Error 7] RequestTimedOutError: Request timed out after 125.0 ms
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.31 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
------------------------------------------------ Captured stdout call -------------------------------------------------

📤 Sending 4 messages to topic 'test_topic_1756880418'
          📤 Message Sent #1          
┏━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Property   ┃ Value                 ┃
┡━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━┩
│ Topic      │ test_topic_1756880418 │
│ Partition  │ 0                     │
│ Offset     │ 0                     │
│ Key        │ None                  │
│ Message ID │ 1                     │
│ Message    │ N/A                   │
│ Timestamp  │ N/A                   │
└────────────┴───────────────────────┘
Error sending message 0: 'Row' object has no attribute 'cells'
          📤 Message Sent #2          
┏━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Property   ┃ Value                 ┃
┡━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━┩
│ Topic      │ test_topic_1756880418 │
│ Partition  │ 0                     │
│ Offset     │ 1                     │
│ Key        │ None                  │
│ Message ID │ 2                     │
│ Message    │ N/A                   │
│ Timestamp  │ N/A                   │
└────────────┴───────────────────────┘
Error sending message 1: 'Row' object has no attribute 'cells'
          📤 Message Sent #3          
┏━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Property   ┃ Value                 ┃
┡━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━┩
│ Topic      │ test_topic_1756880418 │
│ Partition  │ 0                     │
│ Offset     │ 2                     │
│ Key        │ None                  │
│ Message ID │ 3                     │
│ Message    │ N/A                   │
│ Timestamp  │ N/A                   │
└────────────┴───────────────────────┘
Error sending message 2: 'Row' object has no attribute 'cells'
          📤 Message Sent #4          
┏━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Property   ┃ Value                 ┃
┡━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━┩
│ Topic      │ test_topic_1756880418 │
│ Partition  │ 0                     │
│ Offset     │ 3                     │
│ Key        │ None                  │
│ Message ID │ 4                     │
│ Message    │ N/A                   │
│ Timestamp  │ N/A                   │
└────────────┴───────────────────────┘
Error sending message 3: 'Row' object has no attribute 'cells'
✓ Successfully sent 4/4 messages


📥 Consuming messages from topic 'test_topic_1756880418' (max: 4)
        📥 Message Consumed #1        
┏━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Property   ┃ Value                 ┃
┡━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━┩
│ Topic      │ test_topic_1756880418 │
│ Partition  │ 0                     │
│ Offset     │ 0                     │
│ Key        │ None                  │
│ Message ID │ 1                     │
│ Message    │ N/A                   │
│ Timestamp  │ 1756880418367         │
└────────────┴───────────────────────┘
Error consuming messages: 'Row' object has no attribute 'cells'
✓ Consumed 1 messages from topic 'test_topic_1756880418'

-------------------------------------------------- Captured log call --------------------------------------------------
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-producer-5, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-producer-5, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-producer-5, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-producer-5, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=coordinator-1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=coordinator-1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
---------------------------------------------- Captured stdout teardown -----------------------------------------------
Stopping Kafka...
---------------------------------------------- Captured stderr teardown -----------------------------------------------
 Container kafka  Stopping
 Container kafka  Stopped
 Container kafka  Removing
 Container kafka  Removed
 Container zookeeper  Stopping
 Container zookeeper  Stopped
 Container zookeeper  Removing
 Container zookeeper  Removed
 Network kafka-e2etest_default  Removing
 Network kafka-e2etest_default  Removed
=============================================== short test summary info ===============================================
FAILED test_kafka.py::TestKafkaOperations::test_message_ordering - AssertionError: assert 1 == 4
================================================= 1 failed in 11.92s ==================================================

```

</details>

### 9. 🔧 TestKafkaOperations::test_message_without_key ❌

<details>
<summary><strong>📋 Test Information</strong></summary>

| Property | Value |
|----------|-------|
| 🏷️ **Test Name** | `TestKafkaOperations::test_message_without_key` |
| 📊 **Status** | ❌ FAILED |
| ⏱️ **Duration** | 10.92 seconds |
| 🕐 **Timestamp** | 2025-09-03T11:50:33.706920 |
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
================================================= test session starts =================================================
platform darwin -- Python 3.12.2, pytest-8.4.1, pluggy-1.5.0 -- /Users/anidhula/.pyenv/versions/3.12.2/bin/python
cachedir: .pytest_cache
rootdir: /Users/anidhula/learn/kafka-e2etest
configfile: pytest.ini
plugins: asyncio-1.1.0, cov-4.1.0, anyio-4.10.0, dash-2.14.2
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collecting ... collected 1 item

test_kafka.py::TestKafkaOperations::test_message_without_key FAILED                                             [100%]

====================================================== FAILURES =======================================================
____________________________________ TestKafkaOperations.test_message_without_key _____________________________________
test_kafka.py:239: in test_message_without_key
    assert success is True
E   assert False is True
------------------------------------------------ Captured stdout setup ------------------------------------------------
Starting Kafka with docker-compose...
Kafka is ready!
------------------------------------------------ Captured stderr setup ------------------------------------------------
 Network kafka-e2etest_default  Creating
 Network kafka-e2etest_default  Created
 Container zookeeper  Creating
 Container zookeeper  Created
 Container kafka  Creating
 Container kafka  Created
 Container zookeeper  Starting
 Container zookeeper  Started
 Container kafka  Starting
 Container kafka  Started
------------------------------------------------- Captured log setup --------------------------------------------------
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.06 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.08 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.24 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.47 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.71 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.40 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:1163 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: socket disconnected
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: socket disconnected
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.03 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:1163 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: socket disconnected
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: socket disconnected
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.08 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:1163 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: socket disconnected
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: socket disconnected
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.22 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:1163 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: socket disconnected
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: socket disconnected
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.37 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
WARNING  kafka.client:client_async.py:794 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]> timed out after 62.5 ms. Closing connection.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. [Error 7] RequestTimedOutError: Request timed out after 62.5 ms
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.76 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
------------------------------------------------ Captured stdout call -------------------------------------------------
           📤 Message Sent            
┏━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Property   ┃ Value                 ┃
┡━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━┩
│ Topic      │ test_topic_1756880431 │
│ Partition  │ 0                     │
│ Offset     │ 0                     │
│ Key        │ None                  │
│ Message ID │ 1                     │
│ Message    │ No key message        │
│ Timestamp  │ N/A                   │
└────────────┴───────────────────────┘
Error sending message: 'Row' object has no attribute 'cells'
-------------------------------------------------- Captured log call --------------------------------------------------
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-producer-6, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-producer-6, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-producer-6, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-producer-6, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
---------------------------------------------- Captured stdout teardown -----------------------------------------------
Stopping Kafka...
---------------------------------------------- Captured stderr teardown -----------------------------------------------
 Container kafka  Stopping
 Container kafka  Stopped
 Container kafka  Removing
 Container kafka  Removed
 Container zookeeper  Stopping
 Container zookeeper  Stopped
 Container zookeeper  Removing
 Container zookeeper  Removed
 Network kafka-e2etest_default  Removing
 Network kafka-e2etest_default  Removed
=============================================== short test summary info ===============================================
FAILED test_kafka.py::TestKafkaOperations::test_message_without_key - assert False is True
================================================= 1 failed in 10.67s ==================================================

```

</details>

### 10. 🔧 TestKafkaOperations::test_large_message ❌

<details>
<summary><strong>📋 Test Information</strong></summary>

| Property | Value |
|----------|-------|
| 🏷️ **Test Name** | `TestKafkaOperations::test_large_message` |
| 📊 **Status** | ❌ FAILED |
| ⏱️ **Duration** | 9.84 seconds |
| 🕐 **Timestamp** | 2025-09-03T11:50:43.546152 |
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
================================================= test session starts =================================================
platform darwin -- Python 3.12.2, pytest-8.4.1, pluggy-1.5.0 -- /Users/anidhula/.pyenv/versions/3.12.2/bin/python
cachedir: .pytest_cache
rootdir: /Users/anidhula/learn/kafka-e2etest
configfile: pytest.ini
plugins: asyncio-1.1.0, cov-4.1.0, anyio-4.10.0, dash-2.14.2
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collecting ... collected 1 item

test_kafka.py::TestKafkaOperations::test_large_message FAILED                                                   [100%]

====================================================== FAILURES =======================================================
_______________________________________ TestKafkaOperations.test_large_message ________________________________________
test_kafka.py:263: in test_large_message
    assert success is True
E   assert False is True
------------------------------------------------ Captured stdout setup ------------------------------------------------
Starting Kafka with docker-compose...
Kafka is ready!
------------------------------------------------ Captured stderr setup ------------------------------------------------
 Network kafka-e2etest_default  Creating
 Network kafka-e2etest_default  Created
 Container zookeeper  Creating
 Container zookeeper  Created
 Container kafka  Creating
 Container kafka  Created
 Container zookeeper  Starting
 Container zookeeper  Started
 Container kafka  Starting
 Container kafka  Started
------------------------------------------------- Captured log setup --------------------------------------------------
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:1163 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: socket disconnected
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: socket disconnected
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.06 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:1163 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: socket disconnected
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: socket disconnected
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.08 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:1163 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: socket disconnected
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: socket disconnected
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.22 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:1163 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: socket disconnected
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: socket disconnected
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.44 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:1163 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: socket disconnected
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: socket disconnected
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.77 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:1163 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: socket disconnected
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: socket disconnected
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.39 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:1163 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: socket disconnected
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: socket disconnected
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.05 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:1163 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: socket disconnected
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: socket disconnected
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.12 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:1163 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: socket disconnected
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: socket disconnected
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.22 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
WARNING  kafka.client:client_async.py:794 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]> timed out after 125.0 ms. Closing connection.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. [Error 7] RequestTimedOutError: Request timed out after 125.0 ms
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.28 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
------------------------------------------------ Captured stdout call -------------------------------------------------
           📤 Message Sent            
┏━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Property   ┃ Value                 ┃
┡━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━┩
│ Topic      │ test_topic_1756880441 │
│ Partition  │ 0                     │
│ Offset     │ 0                     │
│ Key        │ None                  │
│ Message ID │ 1                     │
│ Message    │ N/A                   │
│ Timestamp  │ 1756880441.297477     │
└────────────┴───────────────────────┘
Error sending message: 'Row' object has no attribute 'cells'
-------------------------------------------------- Captured log call --------------------------------------------------
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-producer-7, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-producer-7, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-producer-7, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-producer-7, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
---------------------------------------------- Captured stdout teardown -----------------------------------------------
Stopping Kafka...
---------------------------------------------- Captured stderr teardown -----------------------------------------------
 Container kafka  Stopping
 Container kafka  Stopped
 Container kafka  Removing
 Container kafka  Removed
 Container zookeeper  Stopping
 Container zookeeper  Stopped
 Container zookeeper  Removing
 Container zookeeper  Removed
 Network kafka-e2etest_default  Removing
 Network kafka-e2etest_default  Removed
=============================================== short test summary info ===============================================
FAILED test_kafka.py::TestKafkaOperations::test_large_message - assert False is True
================================================== 1 failed in 9.60s ==================================================

```

</details>

### 11. 📤 TestKafkaQueueLength::test_queue_length_after_sending ❌

<details>
<summary><strong>📋 Test Information</strong></summary>

| Property | Value |
|----------|-------|
| 🏷️ **Test Name** | `TestKafkaQueueLength::test_queue_length_after_sending` |
| 📊 **Status** | ❌ FAILED |
| ⏱️ **Duration** | 13.57 seconds |
| 🕐 **Timestamp** | 2025-09-03T11:50:57.112677 |
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
================================================= test session starts =================================================
platform darwin -- Python 3.12.2, pytest-8.4.1, pluggy-1.5.0 -- /Users/anidhula/.pyenv/versions/3.12.2/bin/python
cachedir: .pytest_cache
rootdir: /Users/anidhula/learn/kafka-e2etest
configfile: pytest.ini
plugins: asyncio-1.1.0, cov-4.1.0, anyio-4.10.0, dash-2.14.2
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collecting ... collected 1 item

test_kafka.py::TestKafkaQueueLength::test_queue_length_after_sending FAILED                                     [100%]

====================================================== FAILURES =======================================================
________________________________ TestKafkaQueueLength.test_queue_length_after_sending _________________________________
test_kafka.py:328: in test_queue_length_after_sending
    assert len(consumed_messages) == 5
E   AssertionError: assert 1 == 5
E    +  where 1 = len([{'key': None, 'offset': 0, 'partition': 0, 'timestamp': 1756880451950, ...}])
------------------------------------------------ Captured stdout setup ------------------------------------------------
Starting Kafka with docker-compose...
Kafka is ready!
------------------------------------------------ Captured stderr setup ------------------------------------------------
 Network kafka-e2etest_default  Creating
 Network kafka-e2etest_default  Created
 Container zookeeper  Creating
 Container zookeeper  Created
 Container kafka  Creating
 Container kafka  Created
 Container zookeeper  Starting
 Container zookeeper  Started
 Container kafka  Starting
 Container kafka  Started
------------------------------------------------- Captured log setup --------------------------------------------------
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.06 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.08 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.21 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.47 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.77 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.37 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:1163 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: socket disconnected
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: socket disconnected
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.04 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:1163 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: socket disconnected
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: socket disconnected
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.11 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:1163 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: socket disconnected
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: socket disconnected
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.21 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:1163 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: socket disconnected
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: socket disconnected
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.33 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
WARNING  kafka.client:client_async.py:794 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]> timed out after 62.5 ms. Closing connection.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. [Error 7] RequestTimedOutError: Request timed out after 62.5 ms
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.62 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
------------------------------------------------ Captured stdout call -------------------------------------------------

📤 Sending 5 messages to topic 'queue_test_topic_1756880451'
             📤 Message Sent #1             
┏━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Property   ┃ Value                       ┃
┡━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Topic      │ queue_test_topic_1756880451 │
│ Partition  │ 0                           │
│ Offset     │ 0                           │
│ Key        │ None                        │
│ Message ID │ 1                           │
│ Message    │ Message 1                   │
│ Timestamp  │ N/A                         │
└────────────┴─────────────────────────────┘
Error sending message 0: 'Row' object has no attribute 'cells'
             📤 Message Sent #2             
┏━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Property   ┃ Value                       ┃
┡━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Topic      │ queue_test_topic_1756880451 │
│ Partition  │ 0                           │
│ Offset     │ 1                           │
│ Key        │ None                        │
│ Message ID │ 2                           │
│ Message    │ Message 2                   │
│ Timestamp  │ N/A                         │
└────────────┴─────────────────────────────┘
Error sending message 1: 'Row' object has no attribute 'cells'
             📤 Message Sent #3             
┏━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Property   ┃ Value                       ┃
┡━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Topic      │ queue_test_topic_1756880451 │
│ Partition  │ 0                           │
│ Offset     │ 2                           │
│ Key        │ None                        │
│ Message ID │ 3                           │
│ Message    │ Message 3                   │
│ Timestamp  │ N/A                         │
└────────────┴─────────────────────────────┘
Error sending message 2: 'Row' object has no attribute 'cells'
             📤 Message Sent #4             
┏━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Property   ┃ Value                       ┃
┡━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Topic      │ queue_test_topic_1756880451 │
│ Partition  │ 0                           │
│ Offset     │ 3                           │
│ Key        │ None                        │
│ Message ID │ 4                           │
│ Message    │ Message 4                   │
│ Timestamp  │ N/A                         │
└────────────┴─────────────────────────────┘
Error sending message 3: 'Row' object has no attribute 'cells'
             📤 Message Sent #5             
┏━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Property   ┃ Value                       ┃
┡━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Topic      │ queue_test_topic_1756880451 │
│ Partition  │ 0                           │
│ Offset     │ 4                           │
│ Key        │ None                        │
│ Message ID │ 5                           │
│ Message    │ Message 5                   │
│ Timestamp  │ N/A                         │
└────────────┴─────────────────────────────┘
Error sending message 4: 'Row' object has no attribute 'cells'
✓ Successfully sent 5/5 messages


📥 Consuming messages from topic 'queue_test_topic_1756880451' (max: 10)
           📥 Message Consumed #1           
┏━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Property   ┃ Value                       ┃
┡━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Topic      │ queue_test_topic_1756880451 │
│ Partition  │ 0                           │
│ Offset     │ 0                           │
│ Key        │ None                        │
│ Message ID │ 1                           │
│ Message    │ Message 1                   │
│ Timestamp  │ 1756880451950               │
└────────────┴─────────────────────────────┘
Error consuming messages: 'Row' object has no attribute 'cells'
✓ Consumed 1 messages from topic 'queue_test_topic_1756880451'

-------------------------------------------------- Captured log call --------------------------------------------------
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-producer-8, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-producer-8, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-producer-8, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-producer-8, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=coordinator-1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=coordinator-1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
---------------------------------------------- Captured stdout teardown -----------------------------------------------
Stopping Kafka...
---------------------------------------------- Captured stderr teardown -----------------------------------------------
 Container kafka  Stopping
 Container kafka  Stopped
 Container kafka  Removing
 Container kafka  Removed
 Container zookeeper  Stopping
 Container zookeeper  Stopped
 Container zookeeper  Removing
 Container zookeeper  Removed
 Network kafka-e2etest_default  Removing
 Network kafka-e2etest_default  Removed
=============================================== short test summary info ===============================================
FAILED test_kafka.py::TestKafkaQueueLength::test_queue_length_after_sending - AssertionError: assert 1 == 5
================================================= 1 failed in 13.24s ==================================================

```

</details>

### 12. 📊 TestKafkaQueueLength::test_partition_distribution ❌

<details>
<summary><strong>📋 Test Information</strong></summary>

| Property | Value |
|----------|-------|
| 🏷️ **Test Name** | `TestKafkaQueueLength::test_partition_distribution` |
| 📊 **Status** | ❌ FAILED |
| ⏱️ **Duration** | 11.13 seconds |
| 🕐 **Timestamp** | 2025-09-03T11:51:08.241867 |
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
================================================= test session starts =================================================
platform darwin -- Python 3.12.2, pytest-8.4.1, pluggy-1.5.0 -- /Users/anidhula/.pyenv/versions/3.12.2/bin/python
cachedir: .pytest_cache
rootdir: /Users/anidhula/learn/kafka-e2etest
configfile: pytest.ini
plugins: asyncio-1.1.0, cov-4.1.0, anyio-4.10.0, dash-2.14.2
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collecting ... collected 1 item

test_kafka.py::TestKafkaQueueLength::test_partition_distribution FAILED                                         [100%]

====================================================== FAILURES =======================================================
__________________________________ TestKafkaQueueLength.test_partition_distribution ___________________________________
test_kafka.py:355: in test_partition_distribution
    assert len(consumed_messages) == 5
E   AssertionError: assert 1 == 5
E    +  where 1 = len([{'key': None, 'offset': 0, 'partition': 0, 'timestamp': 1756880464093, ...}])
------------------------------------------------ Captured stdout setup ------------------------------------------------
Starting Kafka with docker-compose...
Kafka is ready!
------------------------------------------------ Captured stderr setup ------------------------------------------------
 Network kafka-e2etest_default  Creating
 Network kafka-e2etest_default  Created
 Container zookeeper  Creating
 Container zookeeper  Created
 Container kafka  Creating
 Container kafka  Created
 Container zookeeper  Starting
 Container zookeeper  Started
 Container kafka  Starting
 Container kafka  Started
------------------------------------------------- Captured log setup --------------------------------------------------
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:1163 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: socket disconnected
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: socket disconnected
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.06 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:1163 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: socket disconnected
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: socket disconnected
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.08 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:1163 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: socket disconnected
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: socket disconnected
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.22 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:1163 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: socket disconnected
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: socket disconnected
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.38 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:1163 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: socket disconnected
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: socket disconnected
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.83 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:1163 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: socket disconnected
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: socket disconnected
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.40 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:1163 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: socket disconnected
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <checking_api_versions_recv> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: socket disconnected
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.05 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
------------------------------------------------ Captured stdout call -------------------------------------------------

📤 Sending 5 messages to topic 'queue_test_topic_1756880462'
             📤 Message Sent #1             
┏━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Property   ┃ Value                       ┃
┡━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Topic      │ queue_test_topic_1756880462 │
│ Partition  │ 1                           │
│ Offset     │ 0                           │
│ Key        │ None                        │
│ Message ID │ 1                           │
│ Message    │ Message 1                   │
│ Timestamp  │ N/A                         │
└────────────┴─────────────────────────────┘
Error sending message 0: 'Row' object has no attribute 'cells'
             📤 Message Sent #2             
┏━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Property   ┃ Value                       ┃
┡━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Topic      │ queue_test_topic_1756880462 │
│ Partition  │ 2                           │
│ Offset     │ 0                           │
│ Key        │ None                        │
│ Message ID │ 2                           │
│ Message    │ Message 2                   │
│ Timestamp  │ N/A                         │
└────────────┴─────────────────────────────┘
Error sending message 1: 'Row' object has no attribute 'cells'
             📤 Message Sent #3             
┏━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Property   ┃ Value                       ┃
┡━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Topic      │ queue_test_topic_1756880462 │
│ Partition  │ 0                           │
│ Offset     │ 0                           │
│ Key        │ None                        │
│ Message ID │ 3                           │
│ Message    │ Message 3                   │
│ Timestamp  │ N/A                         │
└────────────┴─────────────────────────────┘
Error sending message 2: 'Row' object has no attribute 'cells'
             📤 Message Sent #4             
┏━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Property   ┃ Value                       ┃
┡━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Topic      │ queue_test_topic_1756880462 │
│ Partition  │ 1                           │
│ Offset     │ 1                           │
│ Key        │ None                        │
│ Message ID │ 4                           │
│ Message    │ Message 4                   │
│ Timestamp  │ N/A                         │
└────────────┴─────────────────────────────┘
Error sending message 3: 'Row' object has no attribute 'cells'
             📤 Message Sent #5             
┏━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Property   ┃ Value                       ┃
┡━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Topic      │ queue_test_topic_1756880462 │
│ Partition  │ 1                           │
│ Offset     │ 2                           │
│ Key        │ None                        │
│ Message ID │ 5                           │
│ Message    │ Message 5                   │
│ Timestamp  │ N/A                         │
└────────────┴─────────────────────────────┘
Error sending message 4: 'Row' object has no attribute 'cells'
✓ Successfully sent 5/5 messages


📥 Consuming messages from topic 'queue_test_topic_1756880462' (max: 10)
           📥 Message Consumed #1           
┏━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Property   ┃ Value                       ┃
┡━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Topic      │ queue_test_topic_1756880462 │
│ Partition  │ 0                           │
│ Offset     │ 0                           │
│ Key        │ None                        │
│ Message ID │ 3                           │
│ Message    │ Message 3                   │
│ Timestamp  │ 1756880464093               │
└────────────┴─────────────────────────────┘
Error consuming messages: 'Row' object has no attribute 'cells'
✓ Consumed 1 messages from topic 'queue_test_topic_1756880462'

-------------------------------------------------- Captured log call --------------------------------------------------
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-producer-9, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-producer-9, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-producer-9, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-producer-9, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=coordinator-1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=coordinator-1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
---------------------------------------------- Captured stdout teardown -----------------------------------------------
Stopping Kafka...
---------------------------------------------- Captured stderr teardown -----------------------------------------------
 Container kafka  Stopping
 Container kafka  Stopped
 Container kafka  Removing
 Container kafka  Removed
 Container zookeeper  Stopping
 Container zookeeper  Stopped
 Container zookeeper  Removing
 Container zookeeper  Removed
 Network kafka-e2etest_default  Removing
 Network kafka-e2etest_default  Removed
=============================================== short test summary info ===============================================
FAILED test_kafka.py::TestKafkaQueueLength::test_partition_distribution - AssertionError: assert 1 == 5
================================================= 1 failed in 10.90s ==================================================

```

</details>

### 13. 📊 TestKafkaQueueLength::test_queue_length_verbose ❌

<details>
<summary><strong>📋 Test Information</strong></summary>

| Property | Value |
|----------|-------|
| 🏷️ **Test Name** | `TestKafkaQueueLength::test_queue_length_verbose` |
| 📊 **Status** | ❌ FAILED |
| ⏱️ **Duration** | 10.90 seconds |
| 🕐 **Timestamp** | 2025-09-03T11:51:19.141469 |
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
================================================= test session starts =================================================
platform darwin -- Python 3.12.2, pytest-8.4.1, pluggy-1.5.0 -- /Users/anidhula/.pyenv/versions/3.12.2/bin/python
cachedir: .pytest_cache
rootdir: /Users/anidhula/learn/kafka-e2etest
configfile: pytest.ini
plugins: asyncio-1.1.0, cov-4.1.0, anyio-4.10.0, dash-2.14.2
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collecting ... collected 1 item

test_kafka.py::TestKafkaQueueLength::test_queue_length_verbose FAILED                                           [100%]

====================================================== FAILURES =======================================================
___________________________________ TestKafkaQueueLength.test_queue_length_verbose ____________________________________
test_kafka.py:381: in test_queue_length_verbose
    queue_length_before = kafka_client.get_queue_length(test_topic)
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
kafka_client.py:287: in get_queue_length
    table_markdown = self._table_to_markdown(table)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
kafka_client.py:307: in _table_to_markdown
    for cell in row.cells:
                ^^^^^^^^^
E   AttributeError: 'Row' object has no attribute 'cells'
------------------------------------------------ Captured stdout setup ------------------------------------------------
Starting Kafka with docker-compose...
Kafka is ready!
------------------------------------------------ Captured stderr setup ------------------------------------------------
 Network kafka-e2etest_default  Creating
 Network kafka-e2etest_default  Created
 Container zookeeper  Creating
 Container zookeeper  Created
 Container kafka  Creating
 Container kafka  Created
 Container zookeeper  Starting
 Container zookeeper  Started
 Container kafka  Starting
 Container kafka  Started
------------------------------------------------- Captured log setup --------------------------------------------------
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.06 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.12 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.20 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.36 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.73 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
WARNING  kafka.client:client_async.py:1049 No node available during check_version; sleeping 0.51 secs
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
------------------------------------------------ Captured stdout call -------------------------------------------------

📤 Sending 3 messages to topic 'queue_test_topic_1756880473'
             📤 Message Sent #1             
┏━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Property   ┃ Value                       ┃
┡━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Topic      │ queue_test_topic_1756880473 │
│ Partition  │ 0                           │
│ Offset     │ 0                           │
│ Key        │ None                        │
│ Message ID │ 1                           │
│ Message    │ Message 1                   │
│ Timestamp  │ N/A                         │
└────────────┴─────────────────────────────┘
Error sending message 0: 'Row' object has no attribute 'cells'
             📤 Message Sent #2             
┏━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Property   ┃ Value                       ┃
┡━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Topic      │ queue_test_topic_1756880473 │
│ Partition  │ 0                           │
│ Offset     │ 1                           │
│ Key        │ None                        │
│ Message ID │ 2                           │
│ Message    │ Message 2                   │
│ Timestamp  │ N/A                         │
└────────────┴─────────────────────────────┘
Error sending message 1: 'Row' object has no attribute 'cells'
             📤 Message Sent #3             
┏━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Property   ┃ Value                       ┃
┡━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Topic      │ queue_test_topic_1756880473 │
│ Partition  │ 0                           │
│ Offset     │ 2                           │
│ Key        │ None                        │
│ Message ID │ 3                           │
│ Message    │ Message 3                   │
│ Timestamp  │ N/A                         │
└────────────┴─────────────────────────────┘
Error sending message 2: 'Row' object has no attribute 'cells'
✓ Successfully sent 3/3 messages


📊 Checking queue length for topic 'queue_test_topic_1756880473'
          📊 Queue Length Information           
┏━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric         ┃ Value                       ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Topic          │ queue_test_topic_1756880473 │
│ Total Messages │ 3                           │
│ Read Messages  │ 0                           │
│ Queue Length   │ 3                           │
└────────────────┴─────────────────────────────┘
✓ Queue length: 3 messages

-------------------------------------------------- Captured log call --------------------------------------------------
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-producer-10, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-producer-10, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-producer-10, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-producer-10, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
ERROR    kafka.conn:conn.py:429 <BrokerConnection client_id=kafka-python-2.2.15, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connect attempt returned error 61. Disconnecting.
ERROR    kafka.conn:conn.py:945 <BrokerConnection client_id=kafka-python-2.2.15, node_id=1 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection. KafkaConnectionError: 61 ECONNREFUSED
---------------------------------------------- Captured stdout teardown -----------------------------------------------
Stopping Kafka...
---------------------------------------------- Captured stderr teardown -----------------------------------------------
 Container kafka  Stopping
 Container kafka  Stopped
 Container kafka  Removing
 Container kafka  Removed
 Container zookeeper  Stopping
 Container zookeeper  Stopped
 Container zookeeper  Removing
 Container zookeeper  Removed
 Network kafka-e2etest_default  Removing
 Network kafka-e2etest_default  Removed
=============================================== short test summary info ===============================================
FAILED test_kafka.py::TestKafkaQueueLength::test_queue_length_verbose - AttributeError: 'Row' object has no attribut...
================================================= 1 failed in 10.67s ==================================================

```

</details>

---

## 📊 Test Categories Summary

### 📤 Send Operations 🔴

| Metric | Value |
|--------|-------|
| 🧪 **Total Tests** | 3 |
| ✅ **Passed** | 0 |
| ❌ **Failed** | 3 |
| 📈 **Success Rate** | 0.0% |

### 📥 Consume Operations 🔴

| Metric | Value |
|--------|-------|
| 🧪 **Total Tests** | 2 |
| ✅ **Passed** | 1 |
| ❌ **Failed** | 1 |
| 📈 **Success Rate** | 50.0% |

### 📊 Queue Length Operations 🔴

| Metric | Value |
|--------|-------|
| 🧪 **Total Tests** | 2 |
| ✅ **Passed** | 0 |
| ❌ **Failed** | 2 |
| 📈 **Success Rate** | 0.0% |

### 🏗️ Topic Management 🟢

| Metric | Value |
|--------|-------|
| 🧪 **Total Tests** | 2 |
| ✅ **Passed** | 2 |
| ❌ **Failed** | 0 |
| 📈 **Success Rate** | 100.0% |

### 🔧 Other 🔴

| Metric | Value |
|--------|-------|
| 🧪 **Total Tests** | 4 |
| ✅ **Passed** | 1 |
| ❌ **Failed** | 3 |
| 📈 **Success Rate** | 25.0% |

---

## 🖥️ Environment Information

| Component | Value |
|-----------|-------|
| 🐍 **Python Version** | `3.12.2` |
| 🧪 **Test Framework** | pytest |
| 🔊 **Verbose Mode** | ✅ Enabled |
| 📅 **Report Generated** | 2025-09-03 11:51:19 |

---

## 💡 Recommendations & Next Steps

### ❌ Failed Tests (9)

1. 🔧 **Review and fix**: `TestKafkaOperations::test_send_single_message`
2. 🔧 **Review and fix**: `TestKafkaOperations::test_send_multiple_messages`
3. 🔧 **Review and fix**: `TestKafkaOperations::test_consume_messages`
4. 🔧 **Review and fix**: `TestKafkaOperations::test_message_ordering`
5. 🔧 **Review and fix**: `TestKafkaOperations::test_message_without_key`
6. 🔧 **Review and fix**: `TestKafkaOperations::test_large_message`
7. 🔧 **Review and fix**: `TestKafkaQueueLength::test_queue_length_after_sending`
8. 🔧 **Review and fix**: `TestKafkaQueueLength::test_partition_distribution`
9. 🔧 **Review and fix**: `TestKafkaQueueLength::test_queue_length_verbose`

### ⚠️ Attention Required

🔴 **9 test(s) failed and need attention.**

**Recommended actions:**
- 🔍 Review the verbose output for failed tests
- 🐳 Ensure Kafka infrastructure is running properly
- 🔧 Check network connectivity and configuration
- 📝 Review test logs for specific error messages

### 📈 Performance Insights

| Metric | Value |
|--------|-------|
| ⚡ **Average Duration** | 10.70s |
| 🐌 **Slow Tests (>15s)** | 0 |
| ⚡ **Fast Tests (<5s)** | 1 |

---

## 📝 Report Footer

<div align="center">

**Generated by Kafka E2E Testing Suite** 🚀

*Report generated on September 03, 2025 at 11:51:19*

![Kafka](https://img.shields.io/badge/Apache-Kafka-231F20?style=flat&logo=apache-kafka&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-6.0+-0A9EDC?style=flat&logo=pytest&logoColor=white)

</div>
