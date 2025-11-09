#Database

# 전체 요약 테이블

|서비스|유형|핵심 특징|대표 사용 사례|
|---|---|---|---|
|RDS MySQL zero-ETL → Redshift|분석 통합|ETL 제거, 자동 동기화|운영 DB → 분석 자동화|
|RDS for Db2|RDB|Db2 관리형|금융/레거시 마이그레이션|
|DocumentDB|Document Store|MongoDB 호환|JSON 문서 모델|
|Redshift|DWH|MPP 분석 엔진|BI / 대시보드 / 분석|
|DynamoDB|NoSQL|초저지연/고확장|로그인/세션/게임/IoT|
|Timestream|Time-Series|시간축 분석 최적화|IoT/알림/모니터링|
|RDS|RDB|관리형관계DB|일반 OLTP|
|Keyspaces|NoSQL|Cassandra 호환|분산 Key-Value|
|Aurora|RDB|높은 성능+가용성|MySQL/PostgreSQL 향상판|
|MemoryDB|In-Memory DB|Redis + 내구성|세션 + 영속 필요|
|ElastiCache|Cache|Redis/Memcached|캐싱/순위표/속도 개선|
|Neptune|Graph DB|관계 탐색 최적화|추천/그래프 모델|

---

# Amazon RDS for MySQL zero-ETL integration with Amazon Redshift (Preview)

> _RDS MySQL 데이터를 Redshift로 실시간/자동 적재하여 ETL 파이프라인 없이 분석할 수 있게 하는 통합 기능._

`RDS(MySQL)에 저장된 운영 데이터가 매일 빠르게 커지고, 그 데이터를 Redshift로 옮겨 BI/대시보드/ML 분석해야 할 때 별도의 ETL 코드, Glue, Spark 파이프라인 없이 자동 동기화를 하고 싶을 때`

---

# Amazon RDS for Db2

> _IBM Db2 데이터베이스를 AWS에서 관리형으로 운영할 수 있게 해주는 서비스._

`기존 온프레미스 Db2 환경을 유지해야 하지만 서버 운영 부담을 줄이고 싶을 때 레거시 금융/제조 업무 DB를 클라우드로 이전해야 할 때`

---

# Amazon DocumentDB (with MongoDB compatibility)

> _MongoDB API와 호환되는 완전관리형 문서(Document) DB._

`MongoDB 기반 애플리케이션을 유지하면서 운영/백업/스케일링 부담을 줄이고 싶을 때 JSON 문서 기반 데이터 모델을 쓰는 서비스에서`

---

# Amazon Redshift

> _대규모 데이터 웨어하우스 분석을 위한 고성능 MPP 분석 엔진._

`BI 대시보드, 리포트, 정형 분석 쿼리를 빠르게 수행해야 할 때 데이터 레이크(S3) + 분석 클러스터 구성을 함께 사용하고 싶을 때`

---

# Amazon DynamoDB

> _완전 관리형 NoSQL Key-Value / Document 데이터베이스._

`짧은 지연시간으로 대규모 트래픽을 처리해야 하는 서비스(로그인, 세션, 게임 순위 등) 스키마가 자주 변경되거나 유연한 구조가 필요할 때`

[[Dynamo DB]]

---

# Amazon Timestream

> _시계열 데이터(Time-Series) 저장 및 분석을 위한 완전관리형 DB._

`IoT 센서 데이터, 애플리케이션 메트릭, 장비 상태 변화 기록 등 시간축 기반의 분석·집계가 많은 경우`

---

# Amazon RDS

> _MySQL, PostgreSQL, Oracle, SQL Server, MariaDB 를 관리형으로 제공하는 관계형 DB._

`전통적인 OLTP 트랜잭션 애플리케이션에서 백업/패치/복구/확장 관리를 자동화하고 싶을 때`

---

# Amazon Keyspaces (for Apache Cassandra)

> _Cassandra와 호환되는 완전관리형 NoSQL 서비스._

`Cassandra Query Language(CQL) 그대로 가져가고 싶을 때 운영·클러스터 관리 비용 없이 글로벌 분산 Key-Value 데이터를 저장하고자 할 때`

---

# Amazon Aurora

> _RDS 기반의 고성능/고가용성 관계형 DB (MySQL·PostgreSQL 호환)._

`MySQL/PostgreSQL 애플리케이션을 그대로 사용하면서 성능과 복구속도는 더 높은 DB가 필요할 때`

---

# Amazon MemoryDB

> _Valkey/Redis 오픈소스와 호환되는, 내구성 보장형 인메모리 DB._

`Redis 캐시의 속도는 유지하면서, 데이터 손실 없는 지속성(Durability)까지 필요한 경우`

---

# Amazon ElastiCache

> _Redis 또는 Memcached 기반의 관리형 인메모리 캐시 서비스._

`DB 조회를 줄여 애플리케이션 응답속도를 빠르게 해야 할 때 세션 저장소, 순위표, 캐시 계층이 필요한 경우`

---

# Amazon Neptune

> _그래프 데이터(연결 관계)를 효율적으로 저장·탐색하기 위한 관리형 그래프 DB._

`소셜 네트워크, 추천 엔진, 지식 그래프, 연결관계 탐색 로직이 많은 시스템에서 관계형 DB Join을 수십~수백번 수행하는 것을 피하고 싶을 때`

---

