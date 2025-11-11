#ApplicationIntegration

# AWS B2B Data Interchange

> _EDI (전자 문서 교환) 데이터를 JSON/XML 등 공통 형식으로 자동 변환하는 서비스._

`거래처/공급망/물류 시스템 간 EDI 형식이 서로 달라 변환 자동화가 필요할 때 기존 레거시 EDI 매핑 작업을 수작업에서 자동화하려고 할 때 대량 주문/송장 데이터를 표준 포맷으로 맞춰야 할 때`

---

# Amazon Managed Workflows for Apache Airflow (MWAA)

> _Apache Airflow 워크플로우를 완전 관리형으로 운영 가능하게 하는 서비스._

`ETL/데이터 파이프라인/스케줄링 작업을 Airflow DAG로 구성하고 안정적으로 운영하고 싶을 때 서버 패치/운영/확장 없이 Airflow만 사용하고 싶을 때 데이터 엔지니어가 Airflow 기반 DevOps 부담을 줄이고 싶을 때`

---

# Amazon EventBridge

> _서버리스 이벤트 버스로, 서비스/애플리케이션 간 이벤트 기반 연동을 지원._

`서로 다른 마이크로서비스가 이벤트를 통해 비동기적으로 동작해야 할 때 SaaS 서비스(Webhooks)와 AWS 내부 서비스를 연결해야 할 때 로직을 느슨하게 결합해서 유지보수를 쉽게 하고 싶을 때`

---

# Amazon Simple Notification Service (SNS)

> _Pub/Sub 메시징, SMS/이메일/푸시 알림 전송 서비스._

`여러 구독자에게 동시에 알림을 전달해야 할 때 S3 업로드 → SNS → Lambda 같은 이벤트 기반 알림 구조가 필요할 때 긴급 알림, 장애 알림, 사용자 알림 시스템 구현 시`

---

# Amazon MQ

> _RabbitMQ / ActiveMQ 를 관리형으로 운영할 수 있는 메시지 브로커 서비스._

`기존 시스템이 JMS, RabbitMQ, ActiveMQ 등 메시지 브로커 표준 프로토콜을 이미 사용 중일 때 메시지 브로커는 유지하되 운영 부담(클러스터, 패치)을 줄이고 싶을 때 레거시 시스템과 클라우드 시스템을 메시지 큐로 연결해야 할 때`

---

# AWS Step Functions

> _분산 애플리케이션의 작업 순서를 상태 기계(State Machine)로 조정하는 서비스._

`Lambda, ECS, SQS 작업을 “순서/조건분기/재시도” 로 조립해야 할 때 서버리스 워크플로우를 코드 없이 시각적으로 설계하고 싶을 때 시스템 통합 로직을 코드가 아니라 상태 다이어그램으로 관리하고 싶을 때`

---

# Amazon AppFlow

> _SaaS ↔ AWS 간 데이터 통합을 코드 없이 자동화하는 서비스._

`Salesforce → S3 로 고객 데이터를 동기화해야 할 때 Slack, Zendesk, Google Workspace 등 SaaS 데이터를 분석 파이프라인으로 가져올 때 현업 팀이 ETL 없이 클릭 기반으로 데이터 연동하고 싶을 때`

---

# Amazon Simple Queue Service (SQS)

> _완전 관리형 메시지 큐 서비스._

`생산자/소비자 작업을 분리하고 시스템을 느슨하게 결합하고 싶을 때 버스트 트래픽을 완충하여 안정적인 처리량을 유지해야 할 때 백엔드 처리량이 순간 부하에 영향을 받지 않도록 큐에 저장 후 처리할 때`

---
