# Elastic Load Balancing
[link](https://docs.aws.amazon.com/elasticloadbalancing/)
> **Elastic Load Balancing**은 들어오는 트래픽(요청)을 여러 대상(EC2, 컨테이너, IP 등)에 자동으로 분산하여  
> 가용성과 확장성을 높여주는 AWS의 **트래픽 분산 서비스**입니다.

| 구분             | **GWLB**         | **NLB**        | **ALB**          |
| -------------- | ---------------- | -------------- | ---------------- |
| **계층**         | L3 (Network)     | L4 (Transport) | L7 (Application) |
| **라우팅 기준**     | 모든 IP 트래픽        | IP/Port        | Host/Path/Query  |
| **주요 용도**      | 방화벽, IDS, 트래픽 검사 | TCP/UDP 서비스    | 웹 애플리케이션         |
| **고정 IP 지원**   | ✅                | ✅              | ❌                |
| **암호화 처리**     | ❌ (어플라이언스 자체 처리) | ✅ (TLS)        | ✅ (HTTPS)        |
| **WAF 연동**     | ❌                | ❌              | ✅                |
| **대상(Target)** | 어플라이언스 EC2       | EC2/IP/Lambda  | EC2/IP/Lambda    |
| **통신 프로토콜**    | GENEVE (6081)    | TCP/UDP/TLS    | HTTP/HTTPS/gRPC  |
| **트래픽 유형**     | 내부 네트워크 트래픽      | 클라이언트–서버       | 웹/REST API       |
## Application Load Balancer

- **서비스명:** Elastic Load Balancing (ELB)
- **타입 중 하나:** Application Load Balancer (ALB)
- **계층:** OSI 7계층 (Application Layer, HTTP/HTTPS)
- **주요 기능:** HTTP 헤더, 경로, 호스트, 쿼리 문자열 등 요청 내용 기반 라우팅
-  **주요 목적:** 여러 EC2, ECS, Lambda 등으로 트래픽을 분산해 가용성과 확장성 확보

| 구성 요소            | 역할                                        | 시험 포인트                              |
| ---------------- | ----------------------------------------- | ----------------------------------- |
| **Listener**     | 요청 수신 (포트+프로토콜 정의, 예: HTTP:80, HTTPS:443) | 리스너 규칙(Rules) 기반으로 트래픽 분배           |
| **Rule**         | 라우팅 조건 + 동작 정의 (조건: 경로, 호스트, 헤더, 쿼리 등)    | Path-based, Host-based routing      |
| **Target Group** | 트래픽이 향할 대상 집합 (EC2, IP, Lambda 등)         | 대상 상태 확인(Health Check) 가능           |
| **Target**       | 실제 트래픽을 받는 엔드포인트                          | EC2 인스턴스, ECS 태스크, IP, Lambda 함수 가능 |

|라우팅 유형|설명|예시|
|---|---|---|
|**Host-based routing**|요청의 Host 헤더(도메인)에 따라|`api.example.com` → API 서버|
|**Path-based routing**|URL 경로에 따라|`/admin/*` → Admin 서버|
|**Query string / Header routing**|요청의 쿼리나 헤더값에 따라|`?version=beta`|
|**HTTP → HTTPS Redirect**|보안 강화용|80 → 443 자동 리다이렉션|
|**Fixed Response**|커스텀 응답 반환|403 Forbidden 등|
|**Forward Action**|대상 그룹으로 트래픽 전달|기본적인 라우팅 방식|

**Health Check (헬스 체크)
- 각 Target Group 단위로 설정
- ALB는 _Healthy 대상만_ 트래픽 전달
- 기본 경로: `/`
- 주기(Interval), 실패 허용 횟수, 타임아웃 등 세부 설정 가능
- 시험 포인트: "비정상 인스턴스 자동 제외"

**지원 대상 (Targets)
- EC2 인스턴스 
- ECS (컨테이너 자동 등록 지원)
- Lambda 함수 (서버리스 지원)
- IP 주소 (VPC 내부/외부 모두 가능)

**보안 및 암호화
- HTTPS 사용 시 **ACM(AWS Certificate Manager)** 으로 SSL/TLS 인증서 관리
- ALB는 TLS 종료(Offloading) 지원
- **AWS WAF**와 통합 가능 (웹 방화벽 기능)

**모니터링 및 로깅
- **Amazon CloudWatch**: 지표(Metric) 모니터링
- **Access Logs**: S3에 저장 가능 (요청/응답 로그)
- **Request Tracing**: X-Amzn-Trace-Id 헤더로 추적

## Network Load Balancer

**1️⃣개요
- **서비스명:** Elastic Load Balancing (ELB)
- **타입:** Network Load Balancer (NLB)
- **계층:** OSI 4계층 (Transport Layer)
- **주요 프로토콜:** TCP, UDP, TLS
- **특징:**
    - **초고성능, 초저지연, 수백만 개 연결** 처리 가능
    - IP 주소 단위 트래픽 분산
    - **고정 IP(Static IP)** 제공 (각 AZ별 Elastic IP 할당 가능)
    - 높은 처리량이 필요한 실시간 서비스(예: 게임 서버, 금융 트래픽)에 적합


**2️⃣ 주요 구성요소

| 구성 요소            | 설명                              | 시험 포인트             |
| ---------------- | ------------------------------- | ------------------ |
| **Listener**     | 포트+프로토콜(TCP/UDP/TLS)을 정의        | 예: TCP:443         |
| **Target Group** | 트래픽이 향할 대상 그룹 (EC2, IP, Lambda) | 헬스체크 단위            |
| **Target**       | 실제 트래픽을 받는 엔드포인트                | EC2, IP, Lambda 가능 |

**3️⃣동작 방식
- **Connection-level Routing (L4)**  
    → 패킷의 헤더(IP, Port) 기반으로 트래픽을 분산
- **Flow hash 알고리즘** 사용  
    → 한 연결은 동일 대상에 유지 (세션 일관성)
- **Cross-Zone Load Balancing** (옵션)  
    → 모든 AZ의 대상에 균등 분산 가능
- **Elastic IP** (선택)  
    → 각 AZ별 고정 IP 제공 (방화벽 정책 설정에 유용)


**4️⃣지원 대상 및 통합
- **EC2 인스턴스**
- **ECS 서비스** (포트 자동 등록 지원)
- **Lambda 함수** (서버리스 트래픽 분산)
- **IP 주소 기반 대상 등록 가능 (VPC 외부도 가능)**
**Auto Scaling Group**과 자동 연동되어 인스턴스 추가/삭제 시 Target Group 자동 업데이트.

**5️⃣ Health Check
- Target Group 단위로 수행
- 프로토콜: TCP, HTTP, HTTPS
- 정상 상태의 대상만 트래픽 수신
- 비정상 대상 자동 제외
- 
**6️⃣ 보안 및 암호화
- **TLS 리스너 지원** (4계층 암호화)
- **서버 인증서 관리:** **AWS Certificate Manager(ACM)**
- ALB처럼 WAF 직접 연동은 ❌ (L7 전용이기 때문)

**7️⃣ 모니터링 및 로깅

| 항목              | 서비스                              |
| --------------- | -------------------------------- |
| **지표(Metrics)** | Amazon CloudWatch                |
| **접근 로그**       | S3 저장 가능                         |
| **상태 확인**       | CloudWatch + Target Group Health |

**8️⃣ 비용 구조
- **시간당 로드 밸런서 사용 요금**
- **LCU (Load Balancer Capacity Unit)** 기준 청구
    - 초당 처리된 연결 수
    - 활성 연결 수
    - 처리된 바이트 수 기준

## Gateway Load Balancer

**1️⃣ 개요

- **서비스명:** Elastic Load Balancing (ELB)
- **타입:** Gateway Load Balancer (GWLB)
- **계층:** OSI 3계층 (Network Layer)
- **주요 프로토콜:** 모든 IP 패킷 (포트/프로토콜 무관)
- **주요 용도:**
    
    - **방화벽, IDS/IPS, 패킷 검사 등 서드파티 네트워크 어플라이언스 앞단 트래픽 분산**
        
    - VPC 간 트래픽을 **프라이빗하게 전달 및 중앙화된 보안 정책 적용**
        
    - “Bump-in-the-Wire” 형태로 네트워크 트래픽을 **투명하게 중계 및 검사**


**2️⃣ 주요 구성요소

| 구성 요소                                      | 역할                                      | 시험 포인트                 |
| ------------------------------------------ | --------------------------------------- | ---------------------- |
| **Listener**                               | 모든 IP 패킷 수신 (포트 구분 없이 작동)               | L3 수준에서 트래픽 수신         |
| **Target Group**                           | 어플라이언스 인스턴스 그룹 (방화벽, IDS 등)             | 헬스 체크 수행               |
| **Gateway Load Balancer Endpoint (GWLBe)** | VPC Endpoint 형태로, 다른 VPC의 트래픽을 GWLB로 전달 | 다중 VPC, 계정 간 트래픽 검사 핵심 |
| **Flow Stickiness**                        | 동일 세션(Flow)을 같은 어플라이언스에 유지              | 상태 기반 방화벽에 중요          |
| **GENEVE 프로토콜**                            | GWLB ↔ 어플라이언스 간 캡슐화 통신 (포트 6081)        | 시험 단골 포인트 🔥           |
**3️⃣ 동작 방식

- **IP 패킷 단위 라우팅 (L3)**  
    → ALB(L7)나 NLB(L4)보다 더 낮은 계층에서 작동. 
- **트래픽 캡슐화:**
    
    - GENEVE(포트 6081)로 트래픽을 어플라이언스로 전달
        
    - 어플라이언스가 검사 후 응답을 되돌려주면 GWLB가 원본 트래픽으로 복원
        
- **Flow Hash 기반 라우팅**  
    → 같은 트래픽 흐름은 동일 대상에 유지 (스티키 처리)
    
- **GWLBe (Endpoint)**  
    → 다른 VPC의 트래픽을 PrivateLink를 통해 GWLB로 전달  
    → 다계정 보안 서비스 구축 시 핵심 구성

**4️⃣ 지원 대상 및 통합
- **Virtual Appliances**: 방화벽, IDS/IPS, DLP, 트래픽 분석기 등    
- **EC2 기반 어플라이언스 인스턴스**
- **Auto Scaling Group**으로 스케일 아웃 가능
- **Cross-VPC / Cross-Account 트래픽 인스펙션** 지원 (GWLBe 이용)

**5️⃣ Health Check
- Target Group 단위로 수행
- **프로토콜:** TCP, HTTP, HTTPS (L3 수준에서 설정 가능)
- 비정상 어플라이언스 자동 제외
- 헬스체크 실패 시 다른 어플라이언스로 트래픽 자동 재분배

**6️⃣ 보안 및 암호화

- **암호화 자체 기능은 없음** (L3 계층이라 TLS 종단 아님) 
- 대신 보안 어플라이언스(방화벽, IDS)가 자체 암호화/복호화  
- **VPC 내부 트래픽을 PrivateLink(GWLBe)** 로 전달하므로 외부 노출 최소화
- **보안 정책 중앙화**에 유리 (한 곳에서 트래픽 모니터링 및 필터링 가능)

**7️⃣ 모니터링 및 로깅

| 항목              | 서비스                       |
| --------------- | ------------------------- |
| **지표(Metrics)** | Amazon CloudWatch         |
| **Access Logs** | S3 저장 가능                  |
| **Trace ID**    | X-Amzn-Trace-Id 등으로 흐름 추적 |


**8️⃣ 비용 구조
- **로드 밸런서 사용 시간** + **데이터 처리량** 기반 과금
- **GWLBe** 사용 시 엔드포인트 처리 요금 별도 부과

### **Classic Load Balancer (CLB)**: 

AWS에서 제공하는 초기 로드 밸런서로, 4계층(TCP)과 7계층 (HTTP/HTTPS) 로드 밸런싱을 모두 지원합니다. 기본적인 로드 밸런싱 기능을 제공합니다.


- **로드 밸런서 트래픽 암호화**
    - **AWS Certificate Manager (ACM)**: SSL/TLS 인증서를 손쉽게 생성, 관리 및 배포할 수 있도록 도와주는 서비스입니다. ACM은 AWS 서비스를 위한 SSL/TLS 인증서를 자동으로 갱신하고, 손쉽게 관리할 수 있게 해줌으로써 보안 프로토콜을 구현하는 복잡성과 비용을 줄여줍니다.
---
