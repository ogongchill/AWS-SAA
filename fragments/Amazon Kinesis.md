| Kinesis 서비스                      | 설명                                     | 용도                    |
| -------------------------------- | -------------------------------------- | --------------------- |
| **Kinesis Data Streams (KDS)**   | 실시간 스트림 처리 플랫폼. 샤드 단위 확장. Replay 가능.   | Kafka 대체, 실시간 처리      |
| **Kinesis Data Firehose (KDF)**  | 실시간 데이터 적재 서비스. 완전 관리형. 자동 확장.         | S3/Redshift/ES에 자동 저장 |
| **Kinesis Data Analytics (KDA)** | KDS/Firehose 데이터에 SQL 또는 Flink로 실시간 분석 | 실시간 ETL/집계/모니터링       |
| **Kinesis Video Streams (KVS)**  | 영상/오디오 스트림을 실시간으로 ingest               | 보안 카메라, IoT 영상 처리     |

---

# Kinesis Data Streams

> Kafka 같은 스트림 처리

- 초저지연(200~300ms)
- Producer → Stream → Consumer
- Consumer(Dynamo, Lambda, EC2 등)는 **직접 작성**
- 샤드(Shard) 수를 직접 관리
- 데이터 보존: 최대 365일
- 재처리(Replay) 가능 (Reset iterator)
- Exactly-once 아님 → at-least once

```
- 실시간 로그 분석
    
- 시계열 모니터링
    
- Fraud detection
    
- 실시간 감정 분석
    
- ML inference pipeline
```

---

# Kinesis Data Firehose

> 자동으로 S3/Redshift로 전송

- **완전 관리형** → 샤드 없음, 확장 자동
- 실시간은 아니고 약간의 버퍼링 발생 (기본 1~5분)
- 실시간 “처리”는 아님 → **수집/적재용**
- Lambda Transform으로 간단한 전처리는 가능
- S3, Redshift, OpenSearch, Splunk에 자동 전송
- Replay 불가 (왜냐면 데이터를 저장하는 것이 목적이라)

```
 - S3로 로그 적재
    
- Redshift로 분석 데이터 적재
    
- Athena로 S3 로그 쿼리
    
- ETL 파이프라인 자동화
```

---

# Kinesis Data Analytics

> 실시간 SQL/Flink 분석

- Stream + Analytics + Output
- 예: 5초 이동평균, 이상 탐지
- KDS / Firehose input 가능

---

# Kinesis Video Streams

> 영상 스트리밍 ingest

- 보안 카메라
- 차량 블랙박스
- ML 기반 영상 분석과 결합 가능

---
