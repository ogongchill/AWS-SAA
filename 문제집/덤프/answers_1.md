# Q1 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/84973-exam-aws-certified-solutions-architect-associate-saa-c03/

**왜 A가 최선인가?**
1. **S3 Transfer Acceleration**
   - CloudFront의 전 세계 엣지 로케이션 활용
   - 엣지 로케이션에서 AWS 백본 네트워크를 통해 S3로 최적화된 경로 사용
   - 장거리 전송 시 50-500% 속도 향상 가능

2. **멀티파트 업로드**
   - 500GB 대용량 파일을 여러 파트로 분할하여 병렬 업로드
   - 네트워크 오류 시 전체 재시작 불필요 (실패한 파트만 재업로드)
   - 5MB 이상 파트 사용 권장, 100MB 이상 파일에 필수적

**다른 옵션들이 부적합한 이유:**
- **B**: 리전별 중간 버킷 관리, CRR 설정, 원본 삭제 작업 등 운영 복잡도 높음
- **C**: 고속 인터넷이 있는데 물리적 디바이스 사용은 비효율적, 배송 시간으로 인한 지연
- **D**: EC2/EBS 인프라 관리 부담, 스냅샷 복사 과정에서 추가 지연 발생

**핵심 키워드:**
- 고속 인터넷 ✓ → 네트워크 전송 가능
- 최대한 빨리 ✓ → Transfer Acceleration
- 운영 복잡성 최소화 ✓ → 직접 업로드 (중간 단계 없음)
- 500GB 대용량 ✓ → 멀티파트 업로드

---

# Q2

**정답: C**

https://www.examtopics.com/discussions/amazon/view/84848-exam-aws-certified-solutions-architect-associate-saa-c03/

## 설명

**핵심 요구사항:**
- S3에 JSON 형식 로그 저장
- 간단한 주문형(on-demand) 쿼리
- 최소한의 아키텍처 변경
- 최소한의 운영 오버헤드

**왜 C (Amazon Athena)인가?**

S3에 쿼리하는 건 Athena.
Athena 가 사용 가능한 모든 리전에서 Amazon Athena 를 사용하여 표준 SQL 로 Amazon S3 인벤토리를 쿼리할 수 있습니다.
https://docs.aws.amazon.com/ko_kr/AmazonS3/latest/userguide/storage-inventory-athena-query.html

Athena로 JSON 쿼리 가능.
Amazon Athena 를 사용하면 JSON 인코딩 값을 구문 분석하고, JSON 에서 데이터를 추출하고, 값을 검색하고, JSON 배열의 길이와 크기를 찾을 수 있습니다.
https://docs.aws.amazon.com/athena/latest/ug/querying-JSON.html

**Athena의 장점:**
- 서버리스 → 인프라 관리 불필요
- S3 데이터 직접 쿼리 → 데이터 이동/로드 불필요
- 사용한 만큼만 과금 (주문형에 최적)
- 표준 SQL 지원
- 기존 S3 아키텍처 변경 없음

**오답 분석:**
- **A (Redshift)**: 데이터 로드 필요, 클러스터 프로비저닝 및 관리 필요 → 운영 오버헤드 높음
- **B (CloudWatch Logs)**: S3 → CloudWatch 데이터 이동 필요 → 아키텍처 변경 큼, CloudWatch는 SQL 쿼리 미지원
- **D (Glue + EMR)**: EMR 클러스터 관리 필요, 복잡한 설정 → 운영 오버헤드 매우 높음

---

# Q3

**정답: A**

https://www.examtopics.com/discussions/amazon/view/84838-exam-aws-certified-solutions-architect-associate-saa-c03/

## 설명

**핵심 요구사항:**
- AWS Organizations 환경에서 여러 계정 관리
- S3 버킷 액세스를 조직 내 계정 사용자로만 제한
- 최소한의 운영 오버헤드

**왜 A (aws:PrincipalOrgID)인가?**

aws:PrincipalOrgID 라는 조건 키를 권한 정책에 사용하여 조직 내의 계정에 해당하는 IAM 보안 주체(사용자 및 역할)만 리소스에 액세스할 수 있도록 합니다.
https://aws.amazon.com/ko/about-aws/whats-new/2018/05/principal-org-id/

aws:PrincipalOrgID 전역 키는 조직의 모든 AWS 계정에 대한 모든 계정 ID를 나열하는 대신 사용할 수 있습니다. 예를 들어 다음 Amazon S3 버킷 정책은 XXX 조직의 모든 계정 구성원이 버킷에 객체를 추가하도록 허용합니다.

```json
{
  "Version": "2020-09-10",
  "Statement": {
    "Sid": "AllowPutObject",
    "Effect": "Allow",
    "Principal": "*",
    "Action": "s3:PutObject",
    "Resource": "arn:aws:s3:::examtopics/*",
    "Condition": {
      "StringEquals": {
        "aws:PrincipalOrgID": ["XXX"]
      }
    }
  }
}
```

https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html

**aws:PrincipalOrgID의 장점:**
- 단일 조직 ID만 명시하면 됨
- 계정 추가/제거 시 정책 수정 불필요
- 간단한 구성 → 최소 운영 오버헤드
- 조직 전체에 자동 적용

**오답 분석:**
- **B (aws:PrincipalOrgPaths)**: 다중 값 조건 키로 OU별 세부 제어에 사용. 조직 전체 제한이 목적인 이 문제에서는 불필요하게 복잡함
  - aws:PrincipalOrgPaths는 특정 OU 경로를 지정해야 하므로 관리 복잡도 증가
  - https://docs.aws.amazon.com/ko_kr/IAM/latest/UserGuide/reference_policies_condition-keys.html
- **C (CloudTrail 모니터링)**: CloudTrail은 리소스 내역 기록/전송 서비스로, 액세스 제어와 무관. 또한 수동으로 정책을 업데이트해야 하므로 운영 오버헤드 높음
- **D (aws:PrincipalTag)**: 각 사용자마다 태그를 달아야 하므로 최소 운영 오버헤드 조건 불충족
  - aws:PrincipalTag/tag-key는 보안 주체에 연결된 태그를 비교하는 방식으로, 사용자 관리 부담 증가
  - https://docs.aws.amazon.com/ko_kr/IAM/latest/UserGuide/reference_policies_condition-keys.html

---

# Q4

**정답: A**

https://www.examtopics.com/discussions/amazon/view/84980-exam-aws-certified-solutions-architect-associate-saa-c03/

## 설명

**핵심 요구사항:**
- VPC 내 EC2 인스턴스에서 S3 버킷 액세스
- 인터넷 연결 없이 S3 접근 필요
- 프라이빗 네트워크 연결 제공

**Gateway VPC Endpoint의 특징:**
- S3와 DynamoDB는 Gateway Endpoint 지원
- 인터넷 게이트웨이 또는 NAT 불필요
- VPC 라우팅 테이블을 통해 트래픽 라우팅
- 추가 비용 없음 (무료)
- 프라이빗 네트워크 내에서 S3 액세스

**Gateway Endpoint vs Interface Endpoint:**
- **Gateway Endpoint**: S3, DynamoDB 전용, 라우팅 테이블 사용, 무료
- **Interface Endpoint**: 기타 AWS 서비스, ENI 사용, 시간당 요금

**오답 분석:**
- **B (CloudWatch Logs → S3)**: 로그를 CloudWatch로 스트리밍 후 S3로 내보내는 방식은 불필요한 우회 경로. 인터넷 없이 직접 S3 접근이 목표이므로 요구사항 불충족
- **C (인스턴스 프로파일)**: IAM 역할/권한 설정일 뿐, 네트워크 연결 문제를 해결하지 못함. 인터넷 없이 S3 접근하려면 네트워크 경로(VPC Endpoint) 필요
- **D (API Gateway + PrivateLink)**: 불필요하게 복잡한 아키텍처. API Gateway는 API 관리 서비스이며, S3 직접 접근에는 Gateway Endpoint가 가장 간단하고 효율적

---

# Q5

**정답: C**

https://www.examtopics.com/discussions/amazon/view/84981-exam-aws-certified-solutions-architect-associate-saa-c03/

## 설명

**핵심 요구사항:**
- 2개 AZ에 걸친 EC2 인스턴스 (ALB 뒤)
- 각 인스턴스는 별도의 EBS 볼륨 사용
- 사용자가 새로고침 시 일부 문서만 보임 (데이터 불일치)
- 모든 문서를 한 번에 볼 수 있어야 함

**문제 원인:**
각 AZ의 EC2 인스턴스가 독립적인 EBS 볼륨을 사용하여 데이터가 공유되지 않음. ALB가 요청을 분산하면서 사용자는 서로 다른 데이터를 보게 됨.

**왜 C (Amazon EFS)인가?**

**EBS vs EFS 핵심 차이:**
- **EBS**: 단일 AZ 내에서만 접근 가능한 블록 스토리지, 단일 EC2 인스턴스에만 연결
- **EFS**: 다중 AZ에서 접근 가능한 공유 파일 스토리지, 여러 EC2 인스턴스 동시 마운트

https://docs.aws.amazon.com/efs/latest/ug/how-it-works.html#how-it-works-ec2

**EFS의 장점:**
- 다중 AZ 지원 → 여러 EC2 인스턴스 동시 접근
- 공유 파일 시스템 → 데이터 일관성 보장
- 자동 확장 → 용량 관리 불필요
- NFSv4 프로토콜 지원

**오답 분석:**
- **A (두 EBS 볼륨에 데이터 복사)**: 수동 동기화 필요, 실시간 업데이트 시 데이터 불일치 발생. EBS는 여전히 독립적이므로 근본적 해결 안 됨
- **B (사용자를 특정 서버로 안내)**: Sticky Session을 의미하는데, 이는 특정 사용자를 같은 서버로 고정하는 것일 뿐 모든 문서를 볼 수 있게 하지 못함. 각 서버에 다른 문서가 있으면 여전히 일부만 보임
- **D (두 서버 모두에 요청 전송)**: ALB는 단일 서버로 라우팅하는 로드 밸런서이며, 여러 서버에 동시 요청을 보내고 결과를 조합하는 기능이 없음. 아키텍처적으로 불가능하고 비효율적

---

# Q6

**정답: B**

**핵심 요구사항:**
- 70TB 대용량 데이터 마이그레이션
- 최소한의 네트워크 대역폭 사용
- 가능한 빨리 마이그레이션

**Snowball Edge 선택 이유:**
- **용량**: 100TB 제공 (사용 가능: 83TB) → 70TB 데이터를 한 번에 전송 가능
- **네트워크 대역폭**: 물리적 디바이스를 통한 오프라인 전송 → 네트워크 대역폭 사용 최소화
- **속도**: 인터넷 전송 대비 월등히 빠름
- **호환성**: NFS 프로토콜 지원으로 기존 스토리지와 호환

**오답 분석:**
- **A (AWS CLI 복사)**: 70TB를 인터넷으로 전송 시 네트워크 대역폭 과다 사용, 전송 시간 매우 오래 걸림
- **C (S3 File Gateway)**: 인터넷을 통해 데이터 전송하므로 네트워크 대역폭 많이 사용, Snowball보다 느림
- **D (Direct Connect + S3 File Gateway)**: Direct Connect 설정에 시간 소요 (수주~수개월), 높은 초기 비용, 일회성 마이그레이션에 비효율적

**참고:**
- Snowball (구형): 50TB/80TB (사용 가능: 42TB/72TB)
- Snowball Edge (현재): 100TB (사용 가능: 83TB)

---

# Q7

**정답: D**

**핵심 요구사항:**
- 들어오는 메시지를 수집
- 수십 개의 애플리케이션/마이크로서비스가 메시지 소비
- 초당 100,000개까지 급증하는 메시지량
- 솔루션 분리 (Decoupling)
- 확장성 (Scalability)

**SNS + 여러 SQS 구독 선택 이유:**
- **Fan-out 패턴**: SNS 토픽 하나가 여러 SQS 대기열로 메시지 자동 배포 → 수십 개의 마이크로서비스가 각각 독립적으로 소비
- **완전한 분리**: Publisher(메시지 생산자)와 Subscriber(소비자) 완전 분리
- **높은 확장성**: SQS는 거의 무제한 처리량 지원, 초당 100,000개 메시지 처리 가능
- **독립적 소비**: 각 마이크로서비스가 자신의 SQS 대기열에서 독립적으로 메시지 처리, 다른 서비스에 영향 없음
- **관리형 서비스**: 자동 확장, 별도 인프라 관리 불필요

**오답 분석:**
- **A (Kinesis Data Analytics)**: 실시간 **분석** 서비스로 메시지 배포가 아닌 스트림 분석용. 여러 소비자에게 메시지 배포하는 용도 아님
- **B (EC2 Auto Scaling)**: 수집 애플리케이션만 확장할 뿐, 메시지 분리/배포 메커니즘 제공 안 함. 소비자 애플리케이션과의 디커플링 해결 불가
- **C (Kinesis 단일 샤드 + Lambda + DynamoDB)**: 단일 샤드는 초당 1,000레코드/1MB 제한. 초당 100,000개 처리 불가능. 수십 개 소비자에게 독립적 배포 어려움

---

# Q8

**정답: B**

**핵심 요구사항:**
- 레거시: 기본 서버가 여러 컴퓨팅 노드의 작업 조정
- 탄력성(Resilience) 극대화
- 확장성(Scalability) 극대화
- 애플리케이션 현대화

**SQS 대기열 + 대기열 크기 기반 Auto Scaling 선택 이유:**
- **완전한 디커플링**: SQS로 기본 서버(작업 생성자)와 컴퓨팅 노드(작업 소비자) 완전 분리 → 독립적 확장 및 관리 가능
- **높은 탄력성**: 작업이 SQS에 안전하게 보관되므로 컴퓨팅 노드 장애 시에도 작업 손실 없음. 노드 복구 후 처리 재개 가능
- **동적 확장성**: 대기열 크기(ApproximateNumberOfMessages)에 따라 Auto Scaling → 실제 워크로드에 맞춰 실시간 자동 조정
- **비용 최적화**: 작업량 증가 시 인스턴스 추가, 감소 시 자동 축소 → 필요한 만큼만 리소스 사용
- **단일 장애점 제거**: 중앙 집중식 기본 서버 제거 → 아키텍처 현대화

**오답 분석:**
- **A (예약된 조정)**: Scheduled Scaling은 예측 가능한 패턴(예: 매일 오전 9시 트래픽 증가)에만 적합. 실시간 워크로드 변화에 대응 불가. 탄력성 부족
- **C (CloudTrail)**: API 호출 감사/로깅 서비스로 작업 큐 역할 불가능. 작업 대상으로 부적합
- **D (EventBridge + 노드 부하 기반)**: 기본 서버가 여전히 존재하여 단일 장애점(SPOF) 유지. 완전한 디커플링 안 됨. EventBridge는 이벤트 라우팅용이지 작업 큐가 아님

---

# Q9

**정답: B**

**핵심 요구사항:**
- SMB 파일 서버 (온프레미스)
- 대용량 파일, 처음 며칠은 자주 액세스, 7일 후 거의 액세스 안 함
- 저장 공간 부족 문제 해결
- 최근 파일에 대한 저지연 액세스 유지
- 파일 수명 주기 관리 필요

**S3 File Gateway + S3 Lifecycle Policy 선택 이유:**
- **하이브리드 스토리지**: S3 File Gateway로 온프레미스 환경과 AWS 클라우드 통합 → 온프레미스 유지하면서 클라우드 스토리지 활용
- **SMB 호환성**: SMB v2/v3 프로토콜 지원 → 기존 SMB 파일 서버 워크플로우 유지, 애플리케이션 변경 불필요
- **로컬 캐싱**: 자주 액세스하는 파일을 게이트웨이에 캐싱 → 최근 파일에 대한 저지연 액세스 보장
- **무제한 확장**: 모든 파일이 S3로 자동 업로드되어 사실상 무제한 스토리지 확보 → 온프레미스 용량 부족 문제 근본 해결
- **자동 수명 주기 관리**: S3 Lifecycle Policy로 7일 후 Glacier Deep Archive로 자동 전환 → 장기 보관 비용 대폭 절감, 향후 스토리지 문제 방지

**오답 분석:**
- **A (DataSync)**: 7일 지난 데이터만 일회성 복사. 지속적인 저장 공간 증가 문제 해결 안 됨. AWS 측 스토리지 타입 불명확. 하이브리드 아키텍처 아님
- **C (FSx for Windows)**: 온프레미스 저장 공간 문제 해결 안 됨. 완전히 AWS로 마이그레이션 필요. 자동 수명 주기 관리 기능 없음
- **D (각 사용자 PC에 유틸리티)**: SMB 파일 서버 사용 불가능. 기존 워크플로우 완전 변경 필요. 사용자별 유틸리티 설치 및 관리 복잡도 매우 높음

---

# Q10

**정답: B**

**핵심 요구사항:**
- 전자 상거래 웹 애플리케이션
- API Gateway REST API로 주문 정보 수신
- **주문이 접수된 순서대로 처리** (순서 보장 필수)

**SQS FIFO 대기열 + Lambda 선택 이유:**
- **엄격한 순서 보장**: FIFO (First-In-First-Out) 대기열은 메시지 송수신 순서를 정확히 보장 → 첫 번째 주문이 먼저 처리됨
- **정확히 한 번 처리**: FIFO는 중복 메시지 자동 제거 기능 제공 → 동일 주문 중복 처리 방지
- **네이티브 통합**: API Gateway에서 직접 SQS로 메시지 전송 가능 (Lambda 없이도 통합 가능)
- **자동 Lambda 트리거**: SQS FIFO 대기열에서 Lambda를 직접 트리거하여 순차적으로 주문 처리
- **안정성**: 메시지가 대기열에 보관되므로 처리 실패 시 재시도 가능

**오답 분석:**
- **A (SNS + Lambda)**: SNS는 순서 보장 없음. Pub/Sub 패턴으로 여러 구독자에게 동시 메시지 전달 (Fan-out). 순차 처리 불가능
- **C (API Gateway 권한 부여자)**: 권한 부여자(Authorizer)는 인증/인가 전용 기능. 순서 보장이나 메시지 큐잉 기능 없음. 요청 차단만으로 순서 보장 불가능
- **D (SQS 표준 대기열)**: Best-effort ordering으로 순서 보장 없음. 높은 처리량 제공하지만 메시지 순서가 바뀔 수 있어 주문 처리 순서 보장 불가

---

# Q11

**정답: A**

**핵심 요구사항:**
- EC2 인스턴스가 Aurora 데이터베이스에 연결
- 현재: 파일에 로컬로 저장된 사용자 이름과 암호 사용
- **자격 증명 관리의 운영 오버헤드 최소화**

**AWS Secrets Manager + 자동 회전 선택 이유:**
- **중앙 집중식 관리**: 파일 기반 저장 방식 제거 → Secrets Manager에서 자격 증명 안전하게 중앙 관리
- **자동 회전**: 데이터베이스 자격 증명을 자동으로 주기적 교체 (예: 30일마다) → 수동 암호 변경 불필요, 운영 오버헤드 최소화
- **Aurora 네이티브 통합**: Secrets Manager는 Aurora/RDS와 직접 통합 → 자동 회전 시 데이터베이스 암호 자동 업데이트, 애플리케이션 중단 없음
- **자동 암호화**: KMS로 저장 및 전송 중 자격 증명 자동 암호화
- **IAM 통합**: EC2 인스턴스 역할(Instance Profile)로 Secrets Manager 접근 제어 → 자격 증명 노출 방지
- **버전 관리**: 자격 증명 변경 이력 자동 추적

**오답 분석:**
- **B (Systems Manager Parameter Store)**: **자동 회전 기능 없음**. 구성 데이터 저장 용도이지 자격 증명 자동 관리 부적합. 암호 교체 시 수동 업데이트 필요 → 운영 오버헤드 증가
- **C (S3 + KMS 암호화)**: 자동 회전 기능 없음. 파일 기반 저장 방식 그대로 유지. 암호 변경 시 수동으로 S3 객체 업데이트 및 EC2에 배포 필요 → 운영 오버헤드 매우 높음
- **D (암호화된 EBS)**: 자동 회전 기능 없음. 여전히 파일 기반 저장. EBS 암호화는 디스크 보호일 뿐 자격 증명 라이프사이클 관리 아님 → 운영 오버헤드 해결 안 됨

---

# Q12

**정답: A**

**핵심 요구사항:**
- 글로벌 회사 (전 세계 사용자)
- 웹 애플리케이션: ALB 뒤 EC2 (동적 데이터) + S3 버킷 (정적 데이터)
- **정적 및 동적 데이터의 성능 개선 및 대기 시간 감소**
- Route 53에 등록된 자체 도메인 사용

**CloudFront (S3 + ALB 오리진) + Route 53 선택 이유:**
- **단일 엔드포인트**: CloudFront 하나로 정적(S3)과 동적(ALB) 데이터 모두 제공 → 단일 도메인으로 간편하게 관리
- **글로벌 엣지 캐싱**: CloudFront의 전 세계 400+ 엣지 로케이션에서 콘텐츠 캐싱 → 사용자와 가까운 위치에서 제공, 대기 시간 대폭 감소
- **다중 오리진 지원**: CloudFront는 여러 오리진(S3, ALB 등) 동시 지원 → 경로 패턴별로 다른 오리진 라우팅 가능 (예: /static/* → S3, /api/* → ALB)
- **정적 콘텐츠 최적화**: S3 오리진으로 이미지, CSS, JS 등 정적 파일 빠르게 제공, 엣지에서 캐싱
- **동적 콘텐츠 가속**: ALB 오리진으로 동적 요청도 CloudFront를 통해 TCP 연결 최적화, Gzip 압축 등 성능 향상
- **Route 53 통합**: 자체 도메인(예: www.example.com)을 CloudFront 배포로 A/AAAA 레코드 라우팅 → 사용자 경험 일관성

**오답 분석:**
- **B (CloudFront + Global Accelerator)**: Global Accelerator는 TCP/UDP 계층(L4) 가속화 서비스로 캐싱 기능 없음. S3를 Global Accelerator 엔드포인트로 사용하는 것은 부적절하고 비효율적. 불필요한 복잡성 추가
- **C (CloudFront + Global Accelerator 혼합)**: 아키텍처 과도하게 복잡. Global Accelerator는 HTTP/HTTPS 캐싱 미지원. CloudFront만으로 정적/동적 데이터 모두 처리 가능
- **D (두 개의 도메인 이름)**: 정적/동적 콘텐츠에 각각 다른 도메인 사용 → 사용자 경험 나쁨 (두 도메인 관리 필요), CORS 문제 발생 가능, 관리 복잡도 증가. 단일 엔드포인트가 Best Practice

---

# Q13

**정답: A**

**핵심 요구사항:**
- 월별 유지 관리 활동
- **여러 AWS 리전**에서 MySQL용 RDS 데이터베이스 자격 증명 교체
- **최소한의 운영 오버헤드**

**Secrets Manager + 다중 리전 복제 + 자동 회전 선택 이유:**
- **다중 리전 비밀 복제**: Secrets Manager의 네이티브 기능으로 기본 리전의 비밀을 여러 리전에 자동 복제 → 각 리전마다 개별 관리 불필요
- **일정 기반 자동 회전**: 월별 일정에 따라 자동 회전 설정 가능 (예: 매월 1일) → 수동 작업 완전 제거, 운영 오버헤드 최소화
- **RDS 네이티브 통합**: Secrets Manager는 RDS/Aurora와 직접 통합 → 자동 회전 시 데이터베이스 암호를 Secrets Manager가 자동 업데이트
- **자동 동기화**: 기본 리전에서 비밀 회전 시 복제된 모든 리전의 비밀도 자동 동기화 → 리전별 개별 작업 불필요
- **완전 관리형**: AWS가 복제, 암호화(KMS), 회전 로직 모두 관리 → 인프라 관리 불필요
- **감사 로깅**: CloudTrail과 통합되어 비밀 액세스 및 회전 이력 자동 기록

**오답 분석:**
- **B (Systems Manager Parameter Store)**: **다중 리전 복제 기능 없음**. 각 리전마다 개별 파라미터 생성 및 수동 동기화 필요. **자동 회전 기능 없음** → 월별 수동 교체 필요, 운영 오버헤드 매우 높음
- **C (S3 + EventBridge + Lambda)**: 사용자 정의 솔루션으로 아키텍처 복잡도 높음. Lambda 함수로 자격 증명 교체 로직 직접 개발 및 유지보수 필요. 여러 리전 동기화 로직 구현 필요 → 운영 오버헤드 높음
- **D (KMS + DynamoDB Global Tables + Lambda)**: 과도하게 복잡한 아키텍처. Lambda로 RDS API 호출하여 비밀 교체 로직 직접 구현 필요. DynamoDB 테이블 관리, KMS 키 관리 등 추가 운영 부담. Secrets Manager의 네이티브 기능 대비 매우 비효율적 → 운영 오버헤드 매우 높음

---

# Q14

**정답: C**

**핵심 요구사항:**
- 전자 상거래 애플리케이션 (ALB + EC2 Auto Scaling, 여러 AZ)
- 현재: EC2 인스턴스 호스팅 MySQL 8.0 데이터베이스
- 로드 증가 시 데이터베이스 성능 저하
- **읽기 요청 >> 쓰기 트랜잭션** (읽기 집약적 워크로드)
- **고가용성 유지**
- **예측할 수 없는 읽기 워크로드에 자동 확장**

**Aurora 다중 AZ + Aurora 복제본 + Aurora Auto Scaling 선택 이유:**
- **자동 스토리지 확장**: Aurora는 10GB에서 시작하여 128TB까지 10GB 단위로 자동 확장 → 스토리지 관리 불필요
- **다중 AZ 고가용성**: 3개 AZ에 6개 복제본 자동 생성 → 최대 2개 복제본 손실에도 쓰기 가용성, 3개 복제본 손실에도 읽기 가용성 유지. 자동 장애 조치
- **읽기 확장성**: Aurora 복제본(최대 15개)으로 읽기 트래픽 분산 → 읽기 집약적 워크로드에 최적화
- **Aurora Auto Scaling**: 읽기 워크로드 메트릭(CPU, 연결 수 등)에 따라 Aurora 복제본 자동 추가/제거 → 예측 불가능한 읽기 워크로드에 자동 대응
- **MySQL 호환성**: MySQL 8.0과 완벽 호환 → 기존 애플리케이션 코드 변경 최소화, 마이그레이션 용이
- **고성능**: 표준 MySQL 대비 최대 5배 빠른 읽기/쓰기 성능 → 성능 저하 문제 해결

**오답 분석:**
- **A (Redshift 단일 노드)**: Redshift는 OLAP 데이터 웨어하우스로 OLTP 트랜잭션 처리 부적합. 단일 노드는 고가용성 미지원. MySQL과 호환되지 않아 애플리케이션 재작성 필요
- **B (RDS 단일 AZ + 리더 인스턴스)**: 단일 AZ 배포는 고가용성 요구사항 미충족. 기본 인스턴스 장애 시 가용성 손실. 읽기 복제본 수동 추가 필요 → 자동 확장 아님
- **D (ElastiCache + EC2 스팟)**: ElastiCache는 캐싱 계층일 뿐 트랜잭션 데이터베이스 대체 불가 (데이터 영속성 없음). 스팟 인스턴스는 언제든 중단 가능 → 고가용성 미지원. 다중 AZ 언급 없음

---

# Q15

**정답: C**

**핵심 요구사항:**
- AWS로 마이그레이션한 회사
- 프로덕션 VPC로 들어오고 나가는 트래픽 보호
- 온프레미스: 검사 서버로 **트래픽 흐름 검사** 및 **트래픽 필터링** 수행
- AWS 클라우드에서 동일한 기능 필요

**AWS Network Firewall 선택 이유:**
- **트래픽 검사**: Stateful(상태 유지) 및 Stateless(무상태) 검사 엔진으로 VPC 인바운드/아웃바운드 트래픽 검사
- **트래픽 필터링**: 방화벽 규칙 기반으로 트래픽 차단(DROP), 허용(PASS), 알림(ALERT) → 온프레미스 검사 서버와 동일한 기능 제공
- **VPC 경계 보호**: VPC로 들어오고 나가는 모든 트래픽을 네트워크 레벨에서 제어
- **심층 패킷 검사 (DPI)**: 애플리케이션 계층(L7)까지 검사 가능, HTTP, DNS, TLS 등 프로토콜 분석
- **침입 방지 시스템 (IPS)**: Suricata 호환 IPS 규칙 지원 → 알려진 위협 패턴 차단
- **완전 관리형**: AWS가 인프라 관리, 자동 확장, 고가용성 보장

**오답 분석:**
- **A (GuardDuty)**: 위협 탐지 서비스로 AWS 계정 및 워크로드의 악의적 활동 모니터링 및 알림. 실시간 트래픽 검사 및 필터링 기능 없음. 사후 탐지만 가능, 사전 차단 불가
- **B (트래픽 미러링)**: ENI에서 네트워크 트래픽을 복사하여 다른 위치(분석 도구)로 전송하는 기능. 자체적으로 검사/필터링 수행 안 함. 별도 검사 솔루션 필요 → 불완전한 솔루션
- **D (Firewall Manager)**: 여러 AWS 계정과 리소스에 걸쳐 방화벽 규칙(WAF, Shield, Network Firewall 등)을 중앙 관리하는 서비스. 실제 트래픽 검사/필터링을 수행하지 않음. 관리 도구일 뿐

---

# Q16

**정답: B**

**핵심 요구사항:**
- 데이터 레이크: Amazon S3 + PostgreSQL용 RDS
- **데이터 시각화** 및 보고 솔루션 필요
- **모든 데이터 소스 포함** (S3 + RDS)
- **관리팀**: 모든 시각화에 대한 전체 액세스
- **나머지 회사**: 제한된 액세스

**QuickSight → 사용자(User) & 그룹(Group) 기반 공유 구조

- Admin 그룹: 전체 접근
- 일반 그룹: 제한된 접근
- Row-level Security(RLS)도 QuickSight 내부 기능

>*QuickSight 사용 권한과 시각화 공유는 오직 QuickSight User/Group 기반*

**오답 분석:**
- **A (IAM 역할과 공유)**: QuickSight 대시보드는 **IAM 역할과 공유 불가능**. QuickSight 사용자 및 그룹과만 공유 가능. IAM 역할은 QuickSight 서비스 자체의 AWS 리소스 액세스 제어용이지 대시보드 공유 메커니즘 아님
- **C (Glue + ETL + S3 보고서)**: Glue는 ETL(추출/변환/적재) 서비스로 데이터 변환 용도. S3에 정적 보고서 게시는 시각화가 아닌 파일 저장. 대화형 시각화 불가능. RDS 데이터 통합 방법 언급 없음
- **D (Glue + Athena + S3)**: Athena는 SQL 쿼리 엔진이지 시각화 도구 아님. S3에 정적 보고서 게시는 대화형 대시보드 제공 불가. 사용자별 세분화된 액세스 제어 어려움. 시각화 기능 없음

---

# Q17

**정답: A**

**핵심 요구사항:**
- 새로운 비즈니스 애플리케이션
- 두 개의 EC2 인스턴스에서 실행
- S3 버킷을 문서 저장용으로 사용
- **EC2 인스턴스가 S3 버킷에 액세스 가능하도록 보장**

**IAM 역할 생성 및 EC2 인스턴스에 연결 선택 이유:**
- **Instance Profile**: IAM 역할을 EC2 인스턴스에 연결(Instance Profile을 통해) → AWS Best Practice
- **임시 자격 증명**: EC2 메타데이터 서비스를 통해 임시 보안 자격 증명 자동 관리, 주기적 자동 로테이션 → 수동 관리 불필요
- **보안 강화**: 액세스 키 하드코딩 불필요 → 자격 증명 노출 위험 제거, 코드 저장소에 비밀 유출 방지
- **자동 관리**: AWS SDK 및 CLI가 메타데이터 서비스에서 자격 증명 자동 획득 → 애플리케이션 코드 변경 불필요
- **최소 권한 원칙**: 필요한 S3 버킷 및 작업(예: s3:GetObject, s3:PutObject)에만 권한 부여 가능
- **확장성**: 여러 EC2 인스턴스에 동일한 역할 적용 가능

**오답 분석:**
- **B (IAM 정책)**: IAM 정책은 독립적으로 EC2 인스턴스에 직접 연결 불가능. 정책은 반드시 역할, 사용자, 또는 그룹에 첨부되어야 함. 정책 자체는 권한 정의일 뿐 자격 증명 제공 안 함
- **C (IAM 그룹)**: IAM 그룹은 IAM 사용자들을 그룹화하는 용도로만 사용. EC2 인스턴스(AWS 리소스)에 연결 불가능. 그룹은 사람 사용자 관리 전용
- **D (IAM 사용자)**: 사용자 액세스 키를 EC2 인스턴스에 하드코딩해야 함 → 보안 위험 매우 높음, 키 노출 가능, 수동 로테이션 필요, AWS Best Practice 위반. 장기 자격 증명 사용은 보안 취약점

---

# Q18

**정답: A, B**

**핵심 요구사항:**
- 큰 이미지를 압축 이미지로 변환하는 마이크로서비스
- 사용자 이미지 업로드 → S3 저장 → Lambda 처리/압축 → 다른 S3 저장
- **내구성이 있는 상태 비저장(Stateless) 구성 요소 사용**
- **이미지를 자동으로 처리**
- **(2개 선택)**

**A + B 조합 선택 이유:**

**A (S3 이벤트 알림 → SQS 대기열):**
- S3 이벤트 알림으로 이미지 업로드(ObjectCreated) 시 SQS로 자동 메시지 전송
- **내구성**: SQS가 메시지를 안전하게 보관 (기본 4일, 최대 14일)
- **디커플링**: S3와 Lambda 사이에 SQS 큐로 분리 → 독립적 확장 가능

**B (Lambda가 SQS를 이벤트 소스로 사용):**
- Lambda가 SQS 대기열에서 메시지 자동 폴링 및 처리
- **상태 비저장**: Lambda는 stateless, 모든 처리 정보는 SQS 메시지에 포함
- **자동 삭제**: 성공적으로 처리된 메시지는 SQS에서 자동 삭제
- **재시도**: 처리 실패 시 메시지가 큐에 남아 자동 재시도 → 내구성 보장

**통합 장점:**
- **완전 자동화**: S3 → SQS → Lambda 플로우 완전 자동, 사람 개입 불필요
- **확장성**: Lambda 자동 확장으로 대량 이미지 업로드 처리 가능
- **간단한 아키텍처**: 최소 구성 요소로 운영 및 비용 효율적
- **장애 복원력**: Lambda 장애 시에도 SQS에 메시지 보관 → 처리 보장

**오답 분석:**
- **C (메모리의 텍스트 파일)**: 메모리에 상태 저장 → **상태 비저장 요구사항 위반**. Lambda 종료 시 데이터 손실 → **내구성 없음**
- **D (EC2 + 텍스트 파일)**: 텍스트 파일에 상태 저장 → **상태 비저장 위반**. EC2 인스턴스 관리 필요 → 운영 오버헤드 증가, 서버리스 아님
- **E (EventBridge → SNS → 이메일)**: 이메일로 알림만 전송, 사람이 수동 처리 → **자동 처리 아님**. 내구성 및 상태 비저장과 무관

---

# Q19

**정답: D**

**핵심 요구사항:**
- 3계층 웹 애플리케이션 (웹 서버: 퍼블릭 서브넷, 앱/DB 서버: 프라이빗 서브넷)
- 타사 가상 방화벽 어플라이언스가 검사 VPC에 배포됨
- IP 패킷을 수락할 수 있는 IP 인터페이스
- **트래픽이 웹 서버 도달 전에 모든 트래픽 검사**
- **최소한의 운영 오버헤드**

**Gateway Load Balancer + GWLB 엔드포인트 선택 이유:**
- **타사 어플라이언스 통합**: GWLB는 타사 가상 어플라이언스(방화벽, IDS/IPS, 심층 패킷 검사 등) 통합을 위해 특별히 설계된 L3 게이트웨이 + L4 로드 밸런서
- **투명한 트래픽 삽입/반환**: GWLB 엔드포인트를 통해 트래픽을 투명하게 검사 VPC로 라우팅 → 어플라이언스 검사 → 원래 경로로 반환 (Bump-in-the-wire 방식)
- **자동 확장 및 고가용성**: 여러 어플라이언스 인스턴스에 트래픽 자동 분산, 장애 시 자동 failover, 헬스 체크 제공
- **VPC 간 트래픽 교환**: PrivateLink 기반 GWLB 엔드포인트로 검사 VPC ↔ 애플리케이션 VPC 간 안전한 트래픽 교환
- **GENEVE 프로토콜**: IP 패킷을 GENEVE 캡슐화하여 어플라이언스로 전달 → 원본 IP 정보 보존
- **최소 운영 오버헤드**: 완전 관리형 서비스, 자동 확장, 복잡한 수동 라우팅 설정 불필요

**아키텍처 플로우:**
1. 인터넷 → 애플리케이션 VPC IGW → GWLB 엔드포인트 (인그레스 라우팅)
2. GWLB 엔드포인트 → 검사 VPC의 GWLB → 타사 방화벽 어플라이언스 (검사)
3. 어플라이언스 → GWLB → GWLB 엔드포인트 → 웹 서버 (허용된 트래픽만)

**오답 분석:**
- **A (NLB)**: L4 로드 밸런서로 백엔드 타겟으로 트래픽 분산 용도. 패킷 검사 후 원래 경로로 투명하게 반환하는 기능 없음. 타사 어플라이언스 통합 미지원
- **B (ALB)**: L7 로드 밸런서로 HTTP/HTTPS 트래픽 분산 전용. 가상 어플라이언스 통합 불가능. 모든 IP 패킷 처리 불가 (HTTP/HTTPS만)
- **C (Transit Gateway만)**: VPC 간 연결 허브 제공하지만 GWLB 없이는 타사 어플라이언스로 트래픽을 투명하게 삽입/검사/반환 불가능. 복잡한 라우팅 테이블 구성 및 유지 필요 → 운영 오버헤드 높음

---

# Q20

**정답: D**

**핵심 요구사항:**
- 동일 AWS 리전에서 대량 프로덕션 데이터를 테스트 환경으로 복제
- 데이터는 EBS 볼륨에 저장
- **복제된 데이터 수정 시 프로덕션 환경에 영향 없음**
- **일관되게 높은 I/O 성능 요구**
- **복제 시간 최소화**

**EBS 스냅샷 + Fast Snapshot Restore + 새 EBS 볼륨 선택 이유:**
- **독립적인 볼륨**: 스냅샷에서 새로운 독립적인 EBS 볼륨 생성 → 테스트 환경에서 데이터 수정해도 프로덕션 환경에 전혀 영향 없음
- **빠른 스냅샷 복원 (FSR)**: 스냅샷에서 볼륨 생성 시 **즉시 전체 성능 제공** → 초기화 대기 시간(lazy loading) 제거
- **높은 I/O 성능 보장**: FSR로 생성된 볼륨은 생성 즉시 프로비저닝된 IOPS/처리량 완전 사용 가능 → 일관되게 높은 I/O 성능 제공
- **복제 시간 최소화**: FSR 없이는 처음 액세스하는 블록을 S3에서 가져오는 지연(latency penalty) 발생. FSR은 블록을 미리 로드하여 즉시 사용 가능
- **스냅샷 효율성**: 증분 스냅샷으로 변경된 블록만 저장 → 스냅샷 생성 시간 및 저장 비용 절감

**Fast Snapshot Restore (FSR) 작동 원리:**
- FSR 활성화 시: 스냅샷 데이터를 S3에서 미리 로드하여 완전히 초기화된 볼륨 생성
- FSR 비활성화 시: 볼륨 생성 후 처음 액세스하는 블록마다 S3에서 가져오는 지연 발생 (성능 저하)

**오답 분석:**
- **A (인스턴스 스토어)**: 인스턴스 스토어는 **휘발성** 임시 스토리지. EC2 중지/종료 시 데이터 완전 손실. 영구 데이터 저장 불가능. 스냅샷을 인스턴스 스토어로 복원 불가능
- **B (EBS 다중 연결)**: 동일 EBS 볼륨을 프로덕션과 테스트 인스턴스에 동시 연결 → 테스트에서 수정 시 프로덕션에도 즉시 영향 → **요구사항 위반**. 데이터 독립성 없음
- **C (볼륨 생성 후 복원)**: EBS는 스냅샷에서 **직접 볼륨 생성**하는 방식. 빈 볼륨 생성 후 스냅샷을 복원하는 절차는 존재하지 않음. **잘못된 프로세스**

---

# Q21 

**정답: D**

https://www.examtopics.com/discussions/amazon/view/85195-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:・
A(X) : 전체 웹사이트를 호스팅하기에는 동적인 요소들이 들어가 있을 수 있는데
S3+CloudFront 조합은 정적 웹사이트 호스팅을 위한 것임.
B(X) : RDS 는 기본적으로 Auto Scaling 을 사용하지 않음. 따로 켜야하는데 해당 선택지엔
Auto Scaling을 사용한단 언급이 없음.
워크로드를 예측할 수 없는 경우 Amazon RDS DB 인스턴스에 대해 스토리지
Autoscaling을 활성화할 수 있습니다.
https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIOPS.StorageTypes.
html#USER_PIOPS.Autoscaling
C(X) : B와 동일한 이유로 오답.
D(O) : 정적인 웹사이트 요소들은 S3 + CloudFront로 빠르게 제공하고, API Gateway에서
Lambda 함수를 호출해 DynamoDB에 데이터 저장 가능. DynamoDB는 확장성이 뛰어나고
밀리초 단위 액세스를 지원하는 데이터베이스 유형.
・S3 + CloudFront 조합의 정적 웹사이트 호스팅 :
https://aws.amazon.com/ko/premiumsupport/knowledge-center/cloudfront-serve-static-
website/
・즉, HTTPS 엔드포인트를 통해 API 를 호출하면 API Gateway 가 Lambda 함수를
호출합니다.
https://docs.aws.amazon.com/ko_kr/lambda/latest/dg/services-apigateway-tutorial.html
・개발자는 DynamoDB 를 사용해 최신 서버리스 애플리케이션을 구축하여 우선 작은
규모에서 시작했다가 전역적으로 확장하여 초당 페타바이트 단위의 데이터와 수천만 건의
읽기 및 쓰기 요청을 지원하도록 할 수 있습니다.....DynamoDB 는 용량에 맞게 테이블을
자동으로 조정하므로 별도로 관리하지 않아도 성능을 유지합니다.
https://aws.amazon.com/ko/dynamodb/features/#Enterprise_ready
설명2:
사용량이 많은 시간 동안 지연 시간이 밀리초이고 운영 오버헤드가 최소인 AWS 에서 하루
1 회 거래 웹 사이트를 시작하려면 가장 좋은 옵션은 Amazon S3 버킷을 사용하여 웹
사이트의 정적 콘텐츠를 호스팅하고 Amazon CloudFront 배포를 배포하는 것입니다.
S3 버킷을 오리진으로 설정하고 백엔드 API 에 Amazon API Gateway 및 AWS Lambda
함수를 사용하고 데이터를 Amazon DynamoDB에 저장합니다.
이 옵션은 최소한의 운영 오버헤드가 필요하며 사용량이 많은 시간 동안 밀리초 대기
시간으로 시간당 수백만 건의 요청을 처리할 수 있습니다. 따라서 보기 D가 정답입니다.

---

# Q22 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/84943-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:・
S3 Intelligent-Tiering - 액세스 빈도 또는 불규칙한 사용 패턴을 모를 때 완벽한 사용
사례입니다.
Amazon S3 는 다양한 사용 사례를 위해 설계된 다양한 스토리지 클래스를 제공합니다.
여기에는 자주 액세스하는 데이터의 범용 스토리지를 위한 S3 Standard 가 포함됩니다.
액세스 패턴을 알 수 없거나 변경하는 데이터를 위한 S3 Intelligent-Tiering; S3
Standard-Infrequent Access(S3 Standard-IA) 및 S3 One Zone-Infrequent Access(S3 One
Zone-IA)는 수명이 길지만 액세스 빈도가 낮은 데이터를 위한 것입니다. 장기 아카이브 및
디지털 보존을 위한 Amazon S3 Glacier(S3 Glacier) 및 Amazon S3 Glacier Deep Archive(S3
Glacier Deep Archive). 기존 AWS 리전에서 충족할 수 없는 데이터 레지던시 요구 사항이
있는 경우 S3 Outposts 스토리지 클래스를 사용하여 S3 데이터를 온프레미스에 저장할 수
있습니다.
Amazon S3는 수명 주기 동안 데이터를 관리하는 기능도 제공합니다. S3 수명 주기 정책이
설정되면 애플리케이션을 변경하지 않고도 데이터가 자동으로 다른 스토리지 클래스로
전송됩니다.
https://aws.amazon.com/getting-started/hands-on/getting-started-using-amazon-s3-in
telligent-tiering/?nc1=h_ls
예측할 수 없는 패턴 = S3 Intelligent Tiering.

---

# Q23 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/85092-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:・
이러한 요구 사항을 가장 비용 효율적으로 충족하는 스토리지 솔루션은 B입니다.
1 개월 후에 객체를 S3 Standard 에서 S3 Glacier Deep Archive 로 전환하는 S3 수명 주기
구성을 생성합니다. Amazon S3 Glacier Deep Archive 는 거의 액세스하지 않고 몇 시간의
검색 시간이 허용되는 데이터의 장기 보존을 위한 안전하고 내구성이 있으며 매우 저렴한
Amazon S3 스토리지 클래스입니다. Amazon S3 에서 가장 저렴한 스토리지 옵션이므로
1 개월 후에 액세스하지 않는 백업 파일을 저장하는 데 비용 효율적인 선택입니다. S3 수명
주기 구성을 사용하여 1 개월 후에 객체를 S3 Standard 에서 S3 Glacier Deep Archive 로
자동 전환할 수 있습니다. 이렇게 하면 자주 액세스하지 않는 백업 파일의 저장 비용이
최소화됩니다.
1개월 이후 파일에 접근하지 않음 = S3 Glacier Deep Archive. 답은 B.

---

# Q24 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/85038-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명
AWS Cost Explorer는 비용과 사용량을 보고 분석할 수 있는 도구입니다. 기본 그래프, Cost
Explorer 비용 및 사용량 보고서 또는 Cost Explorer RI 보고서를 사용하여 사용량 및
비용을 탐색할 수 있습니다. 최대 지난 12 개월 동안의 데이터를 보고 향후 12 개월 동안
지출할 가능성이 있는 금액을 예측하고 구매할 예약 인스턴스에 대한 추천을 받을 수
있습니다. 비용 탐색기를 사용하여 추가 조사가 필요한 영역을 식별하고 비용을 이해하는
데 사용할 수 있는 추세를 볼 수 있습니다.
https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html

---

# Q25 

**정답: D**

https://www.examtopics.com/discussions/amazon/view/85197-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:・
대기열(SQS)로 병목 현상을 방지할 수 있습니다.
대량의 데이터 처리 + 확장성 개선 = SQS queue + Lambda 조합.

---

# Q26 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/84940-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:・
AWS Config는 AWS 리소스 구성을 측정, 감사 및 평가할 수 있는 서비스입니다. Config는
AWS 리소스 구성을 지속적으로 모니터링 및 기록하고, 원하는 구성을 기준으로 기록된
구성을 자동으로 평가해 줍니다.
https://aws.amazon.com/ko/config/
설명2:
Amazon S3 버킷에 무단 구성 변경이 없도록 하려면 솔루션 설계자가 적절한 규칙으로
AWS Config를 켜야 합니다. AWS Config는 사용자가 업계 표준 및 내부 정책을 준수하는지
AWS 리소스 구성을 감사하고 평가할 수 있는 서비스입니다. 리소스가 서로 어떻게
관련되어 있는지에 대한 정보를 포함하여 리소스 및 해당 구성에 대한 자세한 보기를
제공합니다. 적절한 규칙으로 AWS Config 를 켜면 사용자는 Amazon S3 버킷에 대한 무단
구성 변경을 식별하고 수정할 수 있습니다.

---

# Q27 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/85227-exam-aws-certified-solut
ions-architect-associate-saa-c03/
해설:・
AWS 계정에 직접 액세스할 수 없는 사람들과 CloudWatch 대시보드를 공유할 수 있습니다.
대시보드를 공유할 때 다음 세 가지 방법으로 대시보드를 볼 수 있는 사람을 지정할 수
있습니다.
◎하나의 대시보드를 공유하고 대시보드를 볼 수 있는 사람들의 특정 이메일 주소를
지정합니다. 이러한 각 사용자는 대시보드를 보기 위해 입력해야 하는 고유한 암호를
만듭니다.
◎링크가 있는 모든 사용자가 대시보드를 볼 수 있도록 단일 대시보드를 공개적으로
공유합니다.
◎계정의 모든 CloudWatch 대시보드를 공유하고 대시보드 액세스를 위한 타사 SSO(Single
Sign-On) 공급자를 지정합니다. 이 SSO 공급자 목록의 구성원인 모든 사용자는 계정의
모든 대시보드에 액세스할 수 있습니다. 이를 활성화하려면 SSO 공급자를 Amazon
Cognito 와 통합합니다. SSO 공급자는 SAML(Security Assertion Markup Language)을
지원해야 합니다.
https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-dashbo
ard-sharing.html

---

# Q28 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/85231-exam-aws-certified-solut
ions-architect-associate-saa-c03/
해설:・
・AWS Organizations로 SSO 설정하여 Active Directory 사용 가능.
AWS IAM Identity Center(AWS SSO 의 후속 서비스)를 설정하여 Active Directory 를 통해
AWS 계정 및 리소스에 대한 액세스를 제공하며, 별도의 작업 역할에 따라 권한을 사용자
지정합니다. https://aws.amazon.com/ko/organizations/features/
・AWS Directory Service를 사용하여 AWS Managed Microsoft AD 디렉터리에 연결 가능.
IAM Identity Center 는 AWS Identity and Access Management(IAM)를 기반으로 구축된
서비스로, 여러 AWS 계정, AWS 애플리케이션 및 다른 SAML 사용 클라우드
애플리케이션에 대한 액세스 관리를 간소화합니다. AWS Directory Service를 사용하여 IAM
Identity Center 를 온프레미스 Active Directory(AD) 또는 AWS Managed Microsoft AD
디렉터리에 연결할 수 있습니다. https://aws.amazon.com/ko/iam/identity-center/faqs/
A(X) : SSO, AWS 관리 콘솔에는 양방향 트러스트가 필요.
AWS Managed Microsoft AD는 수신, 발신 및 양방향(양방향)의 세 가지 신뢰 관계 방향을
모두 지원합니다. AWS Managed Microsoft AD 는 외부 및 포리스트 트러스트를 모두
지원합니다. Amazon Chime, Amazon Connect, Amazon QuickSight, AWS IAM Identity
Center(AWS Single Sign-On의 후속 제품), Amazon WorkDocs, Amazon WorkMail, Amazon
WorkSpaces 및 AWS Management Console 과 같은 AWS 엔터프라이즈 앱에는 양방향
신뢰가 필요합니다. Amazon EC2, Amazon RDS 및 Amazon FSx 는 단방향 또는 양방향
신뢰로 작동합니다.
https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_setup_trust.ht
ml
B(O) : A와 같은 이유로 정답.
C(X) : SSO는 온프레미스 Active Directory나 AWS 관리형 Microsoft AD Directory에 연결할
수 있지, 온프레미스 Microsoft AD Direcotry에 연결할 수는 없음. ▲위의 설명 참고
D(X) : IdP는 외부 자격 증명 서비스.
자격 증명 공급자(IdP)를 사용하면 AWS 외부의 사용자 자격 증명을 관리할 수 있고 이
외부 사용자 자격 증명에 계정의 AWS 리소스에 대한 사용 권한을 부여할 수 있습니다.
https://docs.aws.amazon.com/ko_kr/IAM/latest/UserGuide/id_roles_providers.html

---

# Q29 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/85029-exam-aws-certified-solut
ions-architect-associate-saa-c03/
해설:・
UDP 연결을 사용한다고 했으므로 NLB. 대기 시간이 가장 짧은 리전으로 라우팅 + UDP
사용 = AWS Global Accelerator.
AWS Global Accelerator에서 제공하는 고정 IP 주소와 AWS 엣지 로케이션의 애니캐스트를
리전별 AWS 리소스 또는 엔드포인트(예: Network Load Balancer, Application Load Balancer
EC2 인스턴스 및 탄력적 IP 주소)에 연결할 수 있습니다. IP 주소는 AWS 엣지
로케이션에서 애니캐스트 되므로 사용자와 가까운 AWS 글로벌 네트워크에 온보딩 기능을
제공합니다.
https://aws.amazon.com/ko/global-accelerator/faqs/
https://aws.amazon.com/global-accelerator/faqs/
HTTP /HTTPS - ALB ; TCP and UDP - NLB; Lowest latency routing and more throughput.
Also supports failover, uses Anycast Ip addressing - Global Accelerator Caching at Egde
Locations - CloudFront WS Global Accelerator automatically checks the health of your
applications and routes user traffic only to healthy application endpoints. If the health status
changes or you make configuration updates, AWS Global Accelerator reacts instantaneously
to route your users to the next available endpoint.

---

# Q30 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/85030-exam-aws-certified-solut
ions-architect-associate-saa-c03/
해설:・
한 달에 한 번 48 시간 동안만 사용하고, 가장 비용 효율적인 방법을 사용해야하므로
스냅샷이 제일 저렴.
A(X) : DB 인스턴스를 중지해도 DB 인스턴스가 돌아가는 EBS 볼륨이나 이런 건 사용하지
않아도 보유 중인 용량에 따라 요금이 부과됨.
B(X) : Auto Scaling을 사용하게 되면 사용하지 않을 때에도 인스턴스가 실행 상태가 되므로
스냅샷 보관보다 비용이 더 부과됨
C(O) : 스냅샷으로 보관해서 저장하면 스냅샷 용량만큼만 비용이 부과됨.
D(X) : 사용 중이 아닐 때도 인스턴스가 실행 상태이므로 스냅샷 보관보다 비용이 더
부과됨

---

# Q31 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/85198-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:・
사후 대응적 거버넌스는 Resource Groups Tagging API, AWS Config Rules, 사용자 지정
스크립트 등의 도구를 사용하여 제대로 태그가 지정되지 않은 리소스를 찾습니다.
https://docs.aws.amazon.com/ko_kr/general/latest/gr/aws_tagging.html
설명2:
모든 Amazon EC2 인스턴스, Amazon RDS DB 인스턴스 및 Amazon Redshift 클러스터가
태그로 구성되도록 하려면 솔루션 설계자가 AWS Config 규칙을 사용하여 적절하게 태그가
지정되지 않은 리소스를 정의하고 감지해야 합니다. AWS Config 규칙은 AWS Config 가
모범 사례 및 회사 정책을 준수하는지 AWS 리소스 구성을 평가하는 데 사용하는 사용자
지정 가능한 규칙 세트입니다. AWS Config 규칙을 사용하면 비준수 리소스를 식별하고
담당 팀에 알리는 프로세스를 자동화하므로 이 검사를 구성하고 운영하는 노력을 최소화할
수 있습니다.
참조: AWS Config 규칙:
(https://docs.aws.amazon.com/ko_kr/config/latest/developerguide/evaluate-config_use-
managed-rules.html)

---

# Q32 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/85199-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:・
정적 웹 사이트에서 웹 페이지는 사전 구축된 서버에 의해 반환됩니다. HTML, CSS 또는
JavaScript 와 같은 간단한 언어를 사용합니다. 정적 웹 사이트에서는 서버에서(사용자에
따라) 콘텐츠를 처리하지 않습니다. 웹 페이지는 변경 없이 서버에 의해 반환되므로 정적
웹 사이트는 빠릅니다. 데이터베이스와의 상호 작용이 없습니다.
또한 호스트가 다른 언어로 서버 측 처리를 지원할 필요가 없기 때문에 비용이 적게 듭니다.
동적 웹 사이트에서 웹 페이지는 런타임 중에 처리되는 서버에 의해 반환됩니다. 즉, 사전
구축된 웹 페이지가 아니라 사용자의 요구에 따라 런타임 중에 구축됩니다. 이들은 PHP,
Node.js, ASP.NET 및 서버에서 지원하는 더 많은 것과 같은 서버 측 스크립팅 언어를
사용합니다. 따라서 정적 웹 사이트보다 느리지만 업데이트 및 데이터베이스와의 상호
작용이 가능합니다.
설명2:
모두 정적 웹사이트 콘텐츠 유형에 해당.
Amazon S3 를 사용하여 웹 서버를 구성하거나 관리할 필요 없이 정적 웹 사이트를
호스팅할 수 있습니다. 다음 단계를 완료하여 웹사이트에 모든 고정 자산을 호스팅할 새
Amazon S3 버킷을 생성합니다. 이 자산에는 HTML, CSS, JavaScript, 이미지 파일이
포함됩니다.
https://aws.amazon.com/ko/getting-started/hands-on/app-onboarding/module-5/

---

# Q33 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/85201-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:・
피크 시간에 수십만 명의 사용자에게 서비스 제공 = Kinesis 사용. B,C 둘 중 하나가 답.
B(X) : Kinesis Data Firehose는 데이터 변환 및 전송 서비스. 데이터 수집을 하려면 Kinesis
Data Streams가 필요.
Kinesis Data Firehose 로 데이터를 보내도록 데이터 생산자를 구성하면 지정한 대상으로
데이터가 자동으로 전달됩니다. 데이터를 전송하기 전에 변환하도록 Kinesis Data
Firehose를 구성할 수도 있습니다.
https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html
C(O) : Amazon Kinesis Data Streams를 사용하면 특수 요구에 맞춰 스트리밍 데이터를 처리
또는 분석하는 사용자 지정 애플리케이션을 구축할 수 있습니다. 수십 만개의 소스에서
클릭 스트림, 애플리케이션 로그, 소셜 미디어와 같은 다양한 유형의 데이터를 Kinesis
데이터 스트림에 추가할 수 있습니다. 그러면 몇 초 안에 애플리케이션에서 스트림의 해당
데이터를 읽고 처리할 수 있습니다.
https://aws.amazon.com/ko/kinesis/data-streams/faqs/?nc=sn&loc=6
설명2:
Kinesis Data Firehose 전송 스트림의 대상입니다. Kinesis Data Firehose는 Amazon Simple
Storage Service(Amazon S3), Amazon을 비롯한 다양한 대상으로 데이터 레코드를 보낼 수
있습니다.
Redshift, Amazon OpenSearch Service 및 귀하 또는 귀하의 제 3 자 서비스 공급자가
소유한 모든 HTTP 엔드포인트.
다음은 지원되는 대상입니다.
* Amazon 오픈서치 서비스(Amazon OpenSearch Service)
* Amazon S3
* 데이터독(Datadog)
* 다이나트레이스(Dynatrace)
* 벌집(Honeycomb)
* HTTP 끝점(Endpoint)
* 로직 모니터(Logic Monitor)
* 몽고디비 클라우드(MongoDB Cloud)
* 새로운 유물(New Relic)
* 스플렁크(Splunk)
* 스모 로직(Sumo Logic)
https://docs.aws.amazon.com/firehose/latest/dev/create-name.html
https://aws.amazon.com/kinesis/data-streams/
Amazon Kinesis Data Streams(KDS)는 확장성과 내구성이 뛰어난 실시간 데이터 스트리밍
서비스입니다.
KDS 는 웹사이트 클릭 스트림, 데이터베이스 이벤트 스트림, 금융 거래, 소셜 미디어 피드,
IT 로그 및 위치 추적 이벤트와 같은 수십만 개의 소스에서 초당 기가바이트의 데이터를
지속적으로 캡처할 수 있습니다.

---

# Q34 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/85202-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:・
리소스 구성 사항 변경 추적 = AWS Config / 리소스 내역 기록 = CloudTrail
AWS Config 는 AWS 리소스 인벤토리, 구성 기록, 구성 변경 알림을 제공하여 보안 및
거버넌스를 실현하는 완벽한 관리형 서비스입니다.
https://aws.amazon.com/ko/config/faq/
AWS Cloudtrail 은 사용자 활동 및 API 사용을 추적하여 감사, 보안 모니터링 및 운영 문제
해결을 지원합니다. CloudTrail 은 AWS 인프라 전체에서 작업과 관련된 계정 활동을
로그하고 지속적으로 모니터링하고 보존하여 스토리지, 분석 및 해결 작업을 제어할 수
있도록 합니다.
https://aws.amazon.com/ko/cloudtrail/faqs/
설명2:
AWS Config 는 회사가 AWS 리소스의 구성을 평가, 감사 및 평가할 수 있는 완전관리형
서비스입니다. 사용 중인 리소스에 대한 자세한 인벤토리를 제공하고 리소스 구성에 대한
변경 사항을 추적합니다. AWS Config 는 구성 변경을 감지하고 변경이 발생하면 회사에
알릴 수 있습니다. 또한 규정 준수 및 거버넌스 목적에 필수적인 변경 기록 보기를
제공합니다. AWS CloudTrail 은 회사의 AWS 리소스에 대한 자세한 API 호출 기록을
제공하는 완전 관리형 서비스입니다. API 호출을 한 사람, 호출한 시간, 호출의 영향을 받은
리소스를 포함하여 AWS 계정의 모든 API 활동을 기록합니다. 이 정보를 통해 회사는 AWS
리소스에서 발생할 수 있는 의심스러운 활동을 조사할 수 있으므로 보안 및 감사 목적에
매우 중요합니다.

---

# Q35 

**정답: D**

https://www.examtopics.com/discussions/amazon/view/85203-exam-aws-certified-solut
ions-architect-associate-saa-c03/
해설:・
A(X) : GuardDuty는 계정 보호 서비스.
Amazon GuardDuty 는 AWS 계정 및 워크로드에서 악의적 활동을 모니터링하고 상세한
보안 결과를 제공하여 가시성 및 해결을 촉진하는 위협 탐지 서비스입니다.
https://aws.amazon.com/ko/guardduty/
B(X) : Amazon Inspector는 취약점 스캔 서비스.
Amazon Inspector는 지속적으로 스캔하는 취약성 관리 서비스입니다.
https://docs.aws.amazon.com/ko_kr/inspector/latest/user/what-is-inspector.html
C(X) : 대규모 DDoS 방어는 AWS Shield Advanced가 더 적합.
D(O) : AWS Shield Advanced 는 정교한 대규모 DDoS 공격에 대한 추가 보호 및 완화,
실시간에 가까운 공격에 대한 가시성, 웹 애플리케이션 방화벽 AWS WAF 와의 통합을
제공합니다. DDoS 관련 급증 시 Amazon Elastic Compute Cloud(EC2), Elastic Load
Balancing(ELB), Amazon CloudFront, AWS Global Accelerator 및 Amazon Route 53 요금
보호를 제공합니다.
https://aws.amazon.com/ko/shield/?whats-new-cards.sort-by=item.additionalFields.post
DateTime&whats-new-cards.sort-order=desc

---

# Q36 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/84747-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.ht
ml
대부분의 사용자는 FIPS 140-2 인증 암호화 모듈로 보호되는 기본 AWS KMS 키 스토어가
보안 요구 사항을 충족합니다. 추가 유지 관리 책임 계층이나 추가 서비스에 대한 종속성을
추가할 필요가 없습니다. 그러나 조직에 다음과 같은 요구 사항이 있는 경우 사용자 지정
키 스토어 생성을 고려할 수 있습니다. 키 자료는 공유 환경에 저장할 수 없습니다. 키
자료는 독립적인 보조 감사 경로를 따라야 합니다. 키 자료를 생성하고 저장하는 HSM 은
FIPS 140-2 레벨 3에서 인증을 받아야 합니다.
https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.ht
ml
https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.ht
ml
설명2:
A(X) : SSE-S3은 AWS에서 데이터 키와 마스터 키 모두 관리하기 때문에 고객 관리형 키가
사용되지 않음.
참고: AWS KMS 키로 암호화된 개체를 업로드하려면 키와 S3 버킷이 동일한 AWS 리전에
있어야 합니다.
Note: To upload an object encrypted by an AWS KMS key, the key and the S3 bucket must be
in the same AWS Region.
https://aws.amazon.com/ko/premiumsupport/knowledge-center/s3-bucket-store-kms-e
ncrypted-objects/
B(O) : 고객 관리형 다중 리전 KMS 키 생성. 각 리전에 S3 버킷 생성. S3 버킷 간 복제
설정. 클라이언트 측 암호화로 KMS키 사용하도록 애플리케이션 설정
C(X) : A와 같은 이유로 오답.
D(X) : 각 리전에 고객 관리형 KMS 키 및 S3 버킷 생성. AWS KMS keys(SSE-KMS)로 KMS
키(SSE-KMS)로 서버 측 암호화 사용하도록 S3 버킷 설정. S3 버킷 간 복제 설정.

---

# Q37 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/85037-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:・
A(X) : 물리적으로 케이블 갖다 꽂는 것이기 때문에 원격 접속이 아님.
B(O) : 세션 관리자는 사용자 인스턴스에 SSH 키 또는 인증서를 유지하거나 인바운드
포트를 열도록 요구하지 않고 보안 태세를 강화합니다. 또한, AWS IAM 을 사용하여
인스턴스 액세스를 중앙에서 관리합니다. 세션 관리자를 사용하면 Linux 또는 Windows
EC2 인스턴스와 연결하여 각 인스턴스에서 세션을 시작한 각 사용자를 추적할 수 있습니다.
인스턴스에 액세스한 사용자와 AWS CloudTrail 을 사용한 시점을 감사할 수 있으며,
인스턴스에서 실행된 각 명령을 Amazon S3 또는 Amazon CloudWatch Logs 에 기록할 수
있습니다. 끝으로 Session Manager 를 사용하면 배스쳔 호스트를 운영하고 관리하기 위한
초기 투자 비용이 들지 않습니다. https://aws.amazon.com/ko/systems-manager/faq/
C(X) : SSH키 쌍이 필요하므로 B보다 운영 오버헤드가 많이 발생함.
D(X) : C와 동일한 이유로 오답.
참고
https://docs.aws.amazon.com/ko_kr/systems-manager/latest/userguide/setup-instance-
permissions.html

---

# Q38 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/85238-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:・
A(X) : S3 버킷을 각 리전마다 복제하면 콘텐츠가 업로드될 때마다 각 리전의 버킷에
복제해야하므로 낭비임. CloudFront를 사용하는 것이 훨씬 더 효율적이고 경제적.
B(X) : AWS Global Accelerator 는 TCP/UDP 를 사용하는 네트워크 계층에서 동작하는데,
지문에서 사용된 Route 53은 DNS 서비스로서, 애플리케이션 계층에서 동작.
C(O) : Route 53으로 CloudFront 배포를 가리킬 수 있음.
S3 를 사용해 정적 콘텐츠를 저장하면 다양한 이점이 있습니다. 하지만 비용을 효과적으로
관리하는 동시에 애플리케이션의 성능과 보안까지 최적화하려면 Amazon CloudFront 를
설정해 S3 버킷과 함께 사용하면서 콘텐츠를 제공하고 보호하는 것이 좋습니다.
CloudFront는 전 세계의 정적/동적 웹 콘텐츠, 비디오 스트림 및 API를 안전하게 대규모로
전송할 수 있는 콘텐츠 전송 네트워크(CDN) 서비스입니다. CloudFront 에서 데이터를
전송하면 설계상 S3에서 직접 사용자에게 전송하는 것보다 더욱 비용 효율적입니다.
https://aws.amazon.com/ko/blogs/korea/amazon-s3-amazon-cloudfront-a-match-mad
e-in-the-cloud/
자체 도메인 이름을 사용하려는 경우 Amazon Route 53 을 사용하여 CloudFront 배포를
가리키는 별칭 레코드(alias record)를 생성합니다
https://docs.aws.amazon.com/ko_kr/Route53/latest/DeveloperGuide/routing-to-cloudfro
nt-distribution.html
D(X) : S3 Transfer Acceleration은 각지에서 중앙 S3 버킷으로 업로드하는 서비스.
S3 Transfer Acceleration 은 전 세계에서 S3 버킷으로 전송되는 속도를 최적화하도록
설계되었습니다. 지리적으로 분산된 위치에서 중앙 집중식 버킷으로 데이터를 업로드하거나,
대륙 간에 GB 또는 TB 규모의 데이터를 정기적으로 전송하는 경우, S3 Transfer
Acceleration을 사용하면 몇 시간 또는 며칠의 데이터 전송 시간을 절약할 수 있습니다.
https://aws.amazon.com/ko/s3/faqs/#s3ta
설명2:
Amazon CloudFront는 전 세계 엣지 로케이션에서 콘텐츠를 캐싱하여 콘텐츠에 액세스하는
사용자에게 짧은 지연 시간과 빠른 전송 속도를 제공하는 콘텐츠 전송
네트워크(CDN)입니다. S3 버킷 앞에 CloudFront 배포를 추가하면 전 세계 엣지 위치에서
정적 웹 사이트의 콘텐츠를 캐싱하여 웹 사이트에 액세스하는 사용자의 지연 시간을
줄입니다. 또한 이 솔루션은 CloudFront 엣지 로케이션에서 콘텐츠에 액세스하는 사용자의
데이터 전송 및 요청에 대해서만 비용을 청구하므로 비용 효율적입니다. 또한 이 솔루션은
CloudFront 가 자동으로 확장하여 수요 증가를 처리하고 웹 사이트에 고가용성을 제공할 수
있으므로 확장성과 안정성 이점을 제공합니다.

---

# Q39 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/84748-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:・
https://aws.amazon.com/ebs/features/
프로비저닝된 IOPS 볼륨은 솔리드 스테이트 드라이브(SSD)로 지원되며 중요한 I/O
집약적인 데이터베이스 애플리케이션을 위해 설계된 최고 성능의 EBS 볼륨입니다.
이러한 볼륨은 극히 짧은 대기 시간이 필요한 IOPS 집약적 워크로드와 처리량 집약적
워크로드 모두에 이상적입니다.
https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html
설명2:
'삽입' 작업이라고 했으므로 I/O 성능과 관련되어있음을 유추할 수 있음. 그리고 '저장소
성능'이 문제라고 판단했고, 범용 'SSD' 스토리지가 있다고 했으므로 A가 정답.
D(X) : 버스트 가능한 성능 인스턴스는 잠시 I/O 성능을 끌어올리는 것일 뿐 근본적인 I/O
성능 개선은 하지 못함.
획득한 크레딧이 남아 있지 않으면 인스턴스가 기준 CPU 사용률로 점진적으로 저하되고
크레딧이 더 많이 적립될 때까지 기준 이상으로 버스트할 수 없습니다.
https://docs.aws.amazon.com/ko_kr/AWSEC2/latest/UserGuide/burstable-credits-baselin
e-concepts.html

---

# Q40 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/85204-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:・
수 천 개의 Edge 장치로부터 경고 수집 및 저장 = Kinesis. A,C 둘 중 하나가 답.
A(O) : 정답.
・Kinesis Firehose Delivery Stream에서 데이터 수집
다양한 유형의 소스를 사용하여 Kinesis Data Firehose 전송 스트림으로 데이터를 보낼 수
있습니다. https://docs.aws.amazon.com/firehose/latest/dev/basic-write.html
・Kinesis Firehose에서 S3로 데이터 전송
Kinesis Data Firehose 전송 스트림을 설정할 때 데이터의 최종 대상을 선택합니다. 대상
옵션은 Amazon Simple Storage Service(Amazon S3), Amazon OpenSearch Service 및
Amazon Redshift입니다.
https://docs.aws.amazon.com/ko_kr/ses/latest/dg/event-publishing-kinesis-analytics-fir
ehose-stream.html
・S3에서 Life Cycle Policy를 사용해 S3 Glacier로 객체 이전
수명 주기 규칙을 사용하여 객체 수명 주기 동안 Amazon S3 에서 수행하려는 작업을
정의할 수 있습니다(예: 객체를 다른 스토리지 클래스로 이전, 객체 보관, 지정된 기간이
경과한 후 객체 삭제).
https://docs.aws.amazon.com/ko_kr/AmazonS3/latest/userguide/how-to-set-lifecycle-c
onfiguration-intro.html)
C(X) : 14일이 지난 데이터를 보관하길 원한다고 했는데 삭제해버리므로 오답.
참고:
https://aws.amazon.com/ko/kinesis/data-firehose/features/?nc=sn&loc=2#:~:text=into%
20Amazon%20S3%2C%20

---

# Q41 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/85446-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:・
Amazon AppFlow 는 Salesforce, SAP, Zendesk, Slack 및 ServiceNow 와 같은
SaaS(Software-as-a-Service) 애플리케이션과 Amazon S3 및 Amazon Redshift 와 같은
AWS 서비스 간에 데이터를 안전하게 전송할 수 있는 완전 관리형 통합 서비스입니다. 클릭
몇 번이면 됩니다.
https://aws.amazon.com/appflow/
설명2:
SaaS = Appflow. Appflow는 완전 관리형 통합 서비스이기 때문에 운영 오버헤드가 적음.
Amazon AppFlow 는 클릭 몇 번으로 Salesforce, Marketo, Slack 및 ServiceNow 와 같은
SaaS(Software-as-a-Service) 애플리케이션과 Amazon S3 및 Amazon Redshift 와 같은
AWS 서비스 간에 데이터를 안전하게 전송할 수 있게 해 주는 완전관리형 통합 서비스.
https://aws.amazon.com/ko/appflow/faqs/

---

# Q42 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/85205-exam-aws-certified-solut
ions-architect-associate-saa-c03/
해설1:・
데이터 전송 요금이 걱정되니 전용 전송 통로를 뚫으면 됨. VPC-S3 간 전용 통로는 S3
VPC Gateway Endpoint. 답은 C.
해설2:
S3 용 게이트웨이 VPC 엔드포인트를 배포함으로써 회사는 인터넷 게이트웨이나 NAT
게이트웨이를 거치지 않고 VPC 와 S3 사이에 직접 연결을 설정할 수 있습니다. 이렇게
하면 EC2 와 S3 사이의 트래픽이 Amazon 네트워크 내에 머물면서 지역 데이터 전송
요금을 피할 수 있습니다.
A 는 각 AZ 에서 NAT 게이트웨이를 시작할 것을 제안합니다. 이는 가용성과 중복성에
도움이 될 수 있지만 트래픽이 여전히 NAT 게이트웨이를 통과하고 데이터 전송 요금이
발생하므로 데이터 전송 요금 문제를 해결하지 못합니다.
B 는 NAT 게이트웨이를 NAT 인스턴스로 교체할 것을 제안합니다. 그러나 이 솔루션은
여전히 NAT 인스턴스를 통해 인스턴스와 S3 간에 데이터를 전송하므로 데이터 전송
요금이 발생합니다.
D 는 EC2 를 실행하기 위해 EC2 전용 호스트를 프로비저닝할 것을 제안합니다. 이는
인스턴스 전용 하드웨어를 제공할 수 있지만 데이터 전송 요금 문제를 직접적으로
해결하지는 않습니다.

---

# Q43 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/85206-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:・
A(X) : VPN 은 인터넷을 통과하는데다가, VPC Gateway Endpoint 는 VPC-S3,Dynamo 간
전송을 담당.
B(O) : Direct Connect 는 전용선을 통과하기 때문에 인터넷에 전송중인 데이터가 노출되지
않음
C(X) : Snowball Device 는 배송기간까지 합하면 보통 7 일 정도 걸리는데 이를 매일
주문한다는 것은 무리수.
D(X) : 한도 증가만 가능. 한도 제거 옵션은 없음.
https://docs.aws.amazon.com/ko_kr/general/latest/gr/aws_service_limits.html
설명2:
회사의 온프레미스 애플리케이션에 대한 대역폭 제한 문제를 해결하고 내부 사용자 연결에
대한 영향을 최소화하려면 이 새로운 연결을 통해 백업 트래픽을 전달하도록 새로운 AWS
Direct Connect 연결을 설정해야 합니다. 이 솔루션은 회사의 데이터 센터와 AWS 간에
안전한 고속 연결을 제공하여 회사가 인터넷 대역폭을 사용하지 않고 데이터를 빠르게
전송할 수 있도록 합니다.
참조:
AWS Direct Connect 설명서: https://aws.amazon.com/directconnect/

---

# Q44 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/84750-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
A(O) : 버전 관리는 실수로 삭제했을 때 이전 버전의 파일을 불러올 수 있도록 해줌.
Amazon S3 의 버전 관리는 동일 버킷 내에 여러 개의 객체 변형을 보유하는 수단입니다.
S3 버전 관리를 사용하면 버킷에 저장된 모든 버전의 객체를 모두 보존, 검색 및 복원할
수 있습니다.
https://docs.aws.amazon.com/ko_kr/AmazonS3/latest/userguide/Versioning.html
B(O) : MFA Delete는 함부로 삭제하지 못하도록 막음.
MFA Delete 는 다음 작업에 대해 추가 인증을 요구합니다. ◎버킷의 버전 관리 상태 변경
◎객체 버전 영구 삭제
https://docs.aws.amazon.com/ko_kr/AmazonS3/latest/userguide/MultiFactorAuthenticatio
nDelete.html
C(X) : 버킷 정책은 액세스 권한에 관련된 것. 버킷 정책은 버킷과 해당 버킷의 객체에 대한
액세스 권한을 부여할 수 있는 리소스 기반 정책입니다.
https://docs.aws.amazon.com/ko_kr/AmazonS3/latest/userguide/bucket-policies.html
D(X) : 암호화는 파일 내용을 함부로 볼 수 없게하는 등의 기능은 있지만 기본적으로
삭제는 막지 못함. 우리가 직장에서 DRM 걸린 문서는 열람 못해도 액세스 권한이 있다면
삭제할 수 있는 거랑 비슷함.
E(X) : 객체 수명 주기 정책은 객체를 언제 이동하고 삭제할 거냐의 문제.
설명2:
S3 버킷의 데이터를 실수로 삭제하지 않도록 보호하려면 S3 버킷에 있는 모든 객체의 모든
버전을 보존, 검색 및 복원할 수 있는 버전 관리를 활성화해야 합니다.
또한 S3 버킷에서 MFA(다단계 인증) 삭제를 활성화하면 버킷의 객체를 삭제하기 위해
사용자의 액세스 키 외에 인증 토큰을 요구함으로써 추가 보호 계층이 추가됩니다.
참조:
AWS S3 버전 관리 설명서:
https://docs.aws.amazon.com/AmazonS3/latest/dev/Versioning.html
AWS S3 MFA 문서 삭제:
https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMFADelete.html

---

# Q45 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/85408-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:・
네트워크 연결 문제로 데이터 수집이 잠시 실패하는 현상이 일어남. 이런 경우 데이터
손실이 일어날 위험성이 크므로 데이터를 보관해둘 곳이 필요하고, 대책으로는 SQS
Queue가 적절. 또한 SQS Queue에 머물러 있는 작업들은 Lambda로 처리 가능. 답은 BE.
SQS 를 사용하면 메시지 손실 위험을 감수하거나 다른 서비스를 가동할 필요 없이
소프트웨어 구성 요소 간에 모든 볼륨의 메시지를 전송, 저장 및 수신할 수 있습니다.
https://aws.amazon.com/ko/sqs/
Lambda 함수를 사용하여 Amazon Simple Queue Service(Amazon SQS) 대기열의 메시지를
처리할 수 있습니다.
https://docs.aws.amazon.com/ko_kr/lambda/latest/dg/with-sqs.html
설명2:
간헐적인 네트워크 연결 문제에도 불구하고 Lambda 함수가 향후 모든 데이터를
수집하도록 하려면 다음 조치를 취해야 합니다.
Amazon Simple Queue Service(SQS) 대기열을 생성하고 SNS 주제를 구독합니다. 이를
통해 알림과 처리를 분리할 수 있으므로 처리 Lambda 함수가 실패하더라도 나중에 추가
처리를 위해 메시지가 대기열에 남아 있습니다.
SNS 에서 직접 읽지 않고 SQS 대기열에서 읽도록 Lambda 함수를 수정합니다. 이 분리는
재시도 및 내결함성을 허용하고 모든 메시지가 Lambda 함수에 의해 처리되도록 합니다.
참조:
AWS SNS 설명서: https://aws.amazon.com/sns/
AWS SQS 설명서: https://aws.amazon.com/sqs/
AWS Lambda 설명서: https://aws.amazon.com/lambda/

---

# Q46 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/85264-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
Amazon Macie는 AWS에서 PII와 같은 민감한 데이터를 자동으로 검색, 분류 및 보호하는
관리형 서비스입니다. S3 에서 Macie 를 활성화하면 업로드된 객체에서 PII 를 검색할 수
있습니다.
A. Amazon Inspector 를 사용하여 S3 의 객체를 스캔하는 것은 PII 데이터 스캔을 위한
최적의 선택이 아닙니다. Amazon Inspector 는 콘텐츠 스캔이 아닌 호스트 수준 취약성
평가를 위해 설계되었습니다.
C. AWS Lambda 함수에서 사용자 지정 검색 알고리즘을 구현하려면 대용량 파일 검색을
처리하기 위해 상당한 개발 노력이 필요합니다.
D. 알림에 SES 를 사용하고 S3 수명 주기 정책을 트리거하면 솔루션에 불필요한 복잡성이
추가될 수 있습니다.
따라서 최소한의 개발 노력으로 요구 사항을 충족하는 최상의 옵션은 S3 를 안전한 전송
지점으로 사용하고 Amazon Macie 를 PII 스캔에 활용하고 관리자에게 SNS 알림을
트리거하는 것입니다(옵션 B).
설명2:
최소한의 개발 노력으로 PII 가 공유될 때 관리자에게 탐지 및 경고하고 수정을 자동화하는
요구 사항을 충족하려면 Amazon S3 버킷을 안전한 전송 지점으로 사용하고 Amazon
Macie로 버킷의 객체를 스캔하는 것이 가장 좋습니다.
Amazon Macie 는 기계 학습 및 패턴 일치를 사용하여 Amazon S3 에 저장된 중요한
데이터를 검색하고 보호하는 완전 관리형 데이터 보안 및 데이터 개인 정보 보호
서비스입니다. 민감한 데이터를 분류하고, 민감한 데이터에 대한 액세스를 모니터링하고,
수정 작업을 자동화하는 데 사용할 수 있습니다.
이 시나리오에서는 파일을 Amazon S3 버킷에 업로드한 후 Amazon Macie 에서 객체를
스캔하여 PII를 찾을 수 있으며, PII가 감지되면 Amazon Simple Notification Service(SNS)
알림을 트리거하여 관리자에게 제거하도록 알릴 수 있습니다. PII를 포함하는 객체. Amazon
Macie 에는 이미 다양한 형식의 PII 를 탐지할 수 있는 사전 구축된 데이터 분류 규칙이
있으므로 이 접근 방식은 최소한의 개발 노력이 필요합니다.
개인정보 = Macie. 정답은 B.
참조:
html AWS Well-Architected 프레임워크 - 보안 기반:
https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html

---

# Q47 

**정답: D**

https://www.examtopics.com/discussions/amazon/view/85529-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
A(X) : 예약 인스턴스는 1년 또는 3년 단위 약정 방식.
예약 인스턴스(RI)는 1 년 또는 3 년 기간으로 약정하는 경우 EC2 사용 요금을 상당히
할인해 주는 EC2 상품입니다. https://aws.amazon.com/ko/ec2/faqs/
B(X) : 용량 예약을 생성할 때 다음을 지정합니다. ◎용량을 예약할 가용 영역
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-reservations.html
C(X) : 예약 인스턴스는 1년 또는 3년 단위 약정 방식.
D(O) : B번 참조.
설명2:
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-reservations.html
예비 인스턴스: 비용 효율적이지 않은 전체 기간(1 년 또는 3 년)에 대해 비용을 지불해야
합니다.

---

# Q48 

**정답: D**

https://www.examtopics.com/discussions/amazon/view/85119-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
A(X) : ElastiCache는 캐시 서비스.
B(X) : 인스턴스 스토어는 휘발성 스토리지. 내구성 불충족.
C(X) : Amazon S3 Glacier Deep Archive는 콜드 스토리지. 가용성 불충족.
D(O) : 정답.
설명2:
카탈로그를 Amazon Elastic File System(Amazon EFS) 파일 시스템으로 이동하면
고가용성과 내구성이 모두 제공됩니다. Amazon EFS 는 필요에 따라 확장할 수 있도록
구축된 완전 관리형, 가용성 및 내구성이 뛰어난 파일 시스템입니다. Amazon EFS 를
사용하면 다양한 가용 영역에 있는 여러 EC2 인스턴스에서 카탈로그 데이터를 저장하고
액세스할 수 있으므로 고가용성이 보장됩니다. 또한 Amazon EFS는 여러 가용 영역 내에서
파일을 자동으로 중복 저장하므로 내구성 있는 스토리지 옵션이 됩니다.

---

# Q49 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/85211-exam-aws-certified-solut
ions-architect-associate-saa-c03/
해설:
의료 이미지, 뉴스 미디어 자산 또는 유전체학 데이터와 같이 즉각적인 액세스가 필요한
아카이브 데이터의 경우 S3 Glacier Instant Retrieve 스토리지 클래스를 선택하십시오. S3
Glacier Instant Retrieve 스토리지 클래스는 밀리초 검색으로 최저 비용의 스토리지를
제공합니다.
즉각적인 액세스가 필요하지는 않지만 백업 또는 재해 복구 사용 사례와 같이 비용 없이
대용량 데이터 세트를 검색할 수 있는 유연성이 필요한 아카이브 데이터의 경우 S3 Glacier
Flexible Retrieve(이전의 S3 Glacier)를 선택하고, 몇 분 내에 검색하거나 5-12 시간 내에
대량 검색을 무료로 제공합니다.

---

# Q50 

**정답: D**

https://www.examtopics.com/discussions/amazon/view/85026-exam-aws-certified-solut
ions-architect-associate-saa-c03/
해설:・
A(X) : 1000 개의 인스턴스에 일일이 다 Lambda 로 패치 적용한다는 것은 비효율적이고
번거로움
B(X) : 자동 업데이트에는 시간이 좀 걸림. ""패치 관리자는 승인 및 거부된 패치 목록과
함께 릴리스 후 며칠 이내에 패치를 자동 승인하기 위한 규칙을 포함 하는 패치 기준선 을
사용합니다.
https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-pat
ch.html
C(X) : 가능한 빨리 패치해야한다고 했는데 예약을 하고 있어서 안 됨.
D(O) : 리소스 그룹을 통해 한 번에 여러 인스턴스를 업데이트 가능. 리소스 그룹이 명령
대상으로 지원됨에 따라 해당 리소스 그룹에 속한 모든 관리형 인스턴스에서 관리 및 임시
작업을 자동화할 수 있습니다.
https://aws.amazon.com/ko/about-aws/whats-new/2019/08/now-select-resource-group
s-as-targets-for-aws-systems-manager-run-command/
참고:
https://docs.aws.amazon.com/ko_kr/systems-manager/latest/userguide/about-windows-
app-patching.html

---

# Q51 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/85557-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:・
https://docs.aws.amazon.com/ses/latest/dg/send-email-formatted.html
1. 데이터에 대한 애플리케이션의 API 를 쿼리하기 위해 AWS Lambda 함수를 호출하는
Amazon EventBridge(Amazon CloudWatch Events) 예약 이벤트를 생성합니다. 이 단계는
AWS Lambda 를 사용하여 배송 통계를 추출하고 데이터를 HTML 형식으로 구성할 수
있습니다.
2. Amazon Simple Email Service(Amazon SES)를 사용하여 데이터 형식을 지정하고
이메일로 보고서를 보냅니다.
이 단계는 Amazon SES 를 사용하여 매일 아침 동시에 여러 이메일 주소로 보고서를
전송함으로써 수행할 수 있습니다.
따라서 옵션 D와 B는 이 질문에 대한 올바른 선택입니다. Kinesis Data Firehose가 이 사용
사례에 필요하지 않기 때문에 옵션 A 는 올바르지 않습니다. 애플리케이션의 API 를
쿼리하는 데 AWS Glue 가 필요하지 않기 때문에 옵션 C 는 올바르지 않습니다. S3 이벤트
알림을 사용하여 이메일로 보고서를 보낼 수 없기 때문에 옵션 E는 올바르지 않습니다.
설명2:
B(O) : HTML형식의 이메일 요구사항을 충족
D(O) : 매일 아침 일정 이벤트 요구사항 충족

---

# Q52 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/85265-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:・
EFS는 표준 파일 시스템으로 자동 확장되며 가용성이 높습니다.
설명2:
고가용성이므로 Auto Scaling이 들어간 C,D 둘 중 하나가 정답. EFS vs EBS를 비교해보면
보통은 EFS 가 정답인 경우가 많음. 일단 EBS 는 여러 EC2 인스턴스에서 동시 접속할 수
없다는 단점이 치명적이기 때문.
Amazon Elastic File System 은 전체 파일 시스템 액세스 의미 체계를 지원하는 표준 파일
시스템 인터페이스를 제공합니다.
https://docs.aws.amazon.com/efs/latest/ug/using-fs.html
EBS 다중 연결 볼륨에서 표준 파일 시스템 작업은 지원되는 구성이 아닙니다.
https://aws.amazon.com/ko/premiumsupport/knowledge-center/ebs-access-volumes-us
ing-multi-attach/

---

# Q53 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/85532-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:・
A(X) : 1년 동안 즉시 액세스할 수 있어야 한다고 했으므로 액세스 시간이 1분 이상 걸리는
S3 Glacier는 오답.
B(X) : 특정 기간동안 즉시 액세스할 수 있어야 하므로 Intelligent Tiering 이 아니라 Life
Cycle Policy가 적합.
C(O) : S3 Standard = 즉시 액세스 가능 / S3 Glacier Deep Archive = 콜드 스토리지.
보관용으로 사용됨. Object Lock으로 객체 삭제 방지.
S3 객체 잠금을 사용하면 write-once-read-many(WORM) 모델을 사용하여 객체를 저장할
수 있습니다. 객체 잠금은 고정된 시간 동안 또는 무기한으로 객체의 삭제 또는 덮어쓰기를
방지하는 데 도움이 될 수 있습니다.
https://docs.aws.amazon.com/ko_kr/AmazonS3/latest/userguide/object-lock.html
D(X) : 기록은 최대한의 복원력으로 저장해야한다고 했으므로 One Zone-IA 는 적합하지
않음.
설명2:
1 년 동안 즉시 액세스 가능한 레코드의 요구 사항을 충족한 다음 최대 복원력으로 추가
9 년 동안 보관하기 위해 S3 수명 주기 정책을 사용하여 1 년 후 S3 Standard 에서 S3
Glacier Deep Archive 로 레코드를 전환할 수 있습니다. 또한 관리자 및 루트 사용자를
포함하여 누구도 레코드를 삭제할 수 없도록 10 년 동안 규정 준수 모드에서 S3 객체
잠금을 사용할 수 있습니다. 따라서 정답은 옵션 C입니다.

---

# Q54 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/85574-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:・
Windows File 공유가 핵심 키워드. 답은 C.
설명2:
https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/AmazonEFS.html
Amazon FSx for Windows File Server 는 완전히 네이티브로 지원되는 완전히 관리되는
Microsoft Windows 파일 서버를 제공합니다.
윈도우 파일 시스템.
https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html

---

# Q55 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/85409-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:・
프라이빗 서브넷의 인스턴스에 할당된 보안 그룹의 인바운드 트래픽을 허용하는 보안
그룹을 생성하면 프라이빗 서브넷에서 실행되는 EC2 만 RDS 데이터베이스에 액세스할 수
있습니다. 보안 그룹을 DB 와 연결하여 지정된 보안 그룹에 속한 인스턴스로만 접근을
제한합니다.
질문에 설명된 요구 사항을 충족하는 솔루션은 옵션 C 입니다. 프라이빗 서브넷의
인스턴스에 할당된 보안 그룹에서 인바운드 트래픽을 허용하는 보안 그룹을 생성합니다.
보안 그룹을 DB 인스턴스에 연결합니다.
이 솔루션에서 DB 인스턴스에 적용된 보안 그룹은 프라이빗 서브넷의 인스턴스에 할당된
보안 그룹의 인바운드 트래픽을 허용합니다. 이렇게 하면 프라이빗 서브넷에서 실행되는
EC2 인스턴스만 RDS 데이터베이스에 액세스할 수 있습니다.

---

# Q56 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/85266-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:・
사용자 정의 도메인 이름 은 API 사용자에게 제공할 수 있는 더 간단하고 직관적인
URL 입니다. API 를 배포한 후 귀하(및 귀하의 고객)는 다음 형식의 기본 기본 URL 을
사용하여 API를 호출할 수 있습니다.
https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domai
ns.html
리전 사용자 지정 도메인 이름은 API 와 동일한 AWS 리전에 있는 SSL/TLS 인증서를
사용해야 합니다.
https://aws.amazon.com/ko/premiumsupport/knowledge-center/custom-domain-name-
amazon-api-gateway/
・여기서 API Gateway URL 이란, Route 53 에 등록된 도메인 이름으로, 이를 통해 API 를
호출할 수 있음.
・인증서는 HTTPS에 사용됨. HTTPS=HTTL + SSL인데, SSL에 인증서가 필요하기 때문.
인증서는 ACM으로 가져올 수 있음.
1. 리전 API 게이트웨이 엔드포인트 생성 및 회사 도메인 이름과 연결
또한 API Gateway REST API, Amazon CLI 또는 Amazon SDK 중 하나를 호출하여 사용자
지정 도메인 이름을 호스트 이름으로 사용하여 API 의 기본 경로 매핑을 설정할 수
있습니다.
https://docs.amazonaws.cn/en_us/apigateway/latest/developerguide/how-to-edge-opti
mized-custom-domain-name.html#how-to-custom-domains-mapping-console
2. 회사 도메인 이름과 연결된 공인 인증서를 동일 리전의 ACM으로 가져옴
API Gateway 리전 사용자 지정 도메인 이름의 경우 API 와 동일한 리전에서 인증서를
요청하거나 가져와야 합니다......도메인 이름에 대한 인증서를 ACM으로 가져오려면....
https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domai
ns-prerequisites.html
3. API 게이트웨이 엔드포인트에 인증서 연결
ACM 인증서로 리전 사용자 지정 도메인 이름을 생성(또는 마이그레이션)하면 API
Gateway 는 해당 계정에 서비스 연결 역할을 생성합니다(이 역할이 아직 없는 경우).
서비스 연결 역할은 ACM 인증서를 해당 리전 엔드포인트에 연결하는 데 필요합니다.
https://docs.aws.amazon.com/ko_kr/apigateway/latest/developerguide/apigateway-regio
nal-api-custom-domain-create.html
4. API 게이트웨이 엔드포인트로 트래픽 라우팅 하도록 Route 53 설정
API Gateway 리전 사용자 지정 도메인 이름의 경우 API 와 동일한 리전에서 인증서를
요청하거나 가져와야 합니다. 그리하여 회사의 도메인 이름과 연결된 공인 인증서는 동일
리전의 ACM으로 가져와야됩니다. 따라서 정답은 C에 한표 입니다.
도메인 이름을 사용하여 Amazon API Gateway API로 트래픽 라우팅
・리전 API 엔드포인트(Regional API endpoint): 리전 API 엔드포인트로 트래픽을 라우팅하는
Route 53 별칭 레코드를 생성합니다.
https://docs.aws.amazon.com/ko_kr/Route53/latest/DeveloperGuide/routing-to-api-gate
way.html
설명2
회사의 도메인 이름과 해당 인증서로 API Gateway URL 을 설계하려면 회사에서 다음을
수행해야 합니다.
1. 지역 API 게이트웨이 엔드포인트 생성: 이를 통해 회사는 지역에 특정한 엔드포인트를
생성할 수 있습니다.
2. API 게이트웨이 엔드포인트를 회사의 도메인 이름과 연결: 이렇게 하면 회사에서 API
게이트웨이 URL에 자체 도메인 이름을 사용할 수 있습니다.
3. 회사의 도메인 이름과 연결된 공인 인증서를 동일한 리전의 AWS Certificate
Manager(ACM)로 가져옵니다. 이렇게 하면 회사에서 API 와의 보안 통신을 위해 HTTPS 를
사용할 수 있습니다.
4. API Gateway 엔드포인트에 인증서 첨부: 회사에서 API Gateway URL 보안을 위해
인증서를 사용할 수 있습니다.
5. 트래픽을 API 게이트웨이 엔드포인트로 라우팅하도록 Route 53 구성: 이를 통해 회사는
Route 53 을 사용하여 회사의 도메인 이름을 사용하는 API 게이트웨이 URL 로 트래픽을
라우팅할 수 있습니다.

---

# Q57 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/85452-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:・
Amazon Rekognition 을 사용하여 부적절하거나 원치 않거나 불쾌감을 주는 콘텐츠를
감지할 수 있습니다.
https://docs.aws.amazon.com/rekognition/latest/dg/moderation.html
참조
https://docs.aws.amazon.com/rekognition/latest/dg/moderation.html?pg=ln&sec=ft
https://docs.aws.amazon.com/rekognition/latest/dg/a2i-rekognition.html

---

# Q58 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/85453-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
AWS 에서 컨테이너라고 하면 ECS, ECS 라고 하면 일단 Fargate 부터 떠올리면 됨. AWS
Fargate Fargate 는 Amazon EC2 인스턴스의 서버나 클러스터를 관리할 필요 없이
컨테이너를 실행하기 위해 Amazon ECS에 사용할 수 있는 기술입니다.
https://docs.aws.amazon.com/ko_kr/AmazonECS/latest/developerguide/AWS_Fargate.ht
ml
설명2:
요구 사항은 컨테이너화된 워크로드를 실행하기 위해 기본 인프라를 프로비저닝하고 관리할
필요 없이 확장성과 가용성을 위한 것이므로 AWS Fargate에서 AWS ECS를 사용합니다.
https://docs.aws.amazon.com/AmazonECS/latest/userguide/what-is-fargate.html

---

# Q59 

**정답: D**

https://www.examtopics.com/discussions/amazon/view/85793-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:・
대량의 스트림 데이터 수집 = Kinesis Data Streams. 정답은 D.
※실제 사례가 있음.
◎전 세계 300 개 이상의 Hearst 웹사이트에서 스트리밍되는 하루 30 테라바이트 이상의
클릭스트림 데이터를 전송하고 처리하는 클릭스트림 분석 플랫폼을 구축했습니다.
◎Amazon Kinesis Firehose 는 버퍼링된 데이터를 Amazon Kinesis Data Streams 에서
Amazon Simple Storage Service (Amazon S3) 의 영구 스토리지로 자동 이동합니다. 이는
팀이 이전에 관리해야 했던 Amazon Elastic Compute Cloud(Amazon EC2) 인스턴스를
대체합니다.
◎변환된 클릭스트림 데이터는 Hearst 데이터 레이크에서 가져와 분석 쿼리 및 복잡한
데이터 과학 작업을 위해 Amazon Redshift로 전송됩니다.
◎Amazon Redshift 에서 데이터는 API 를 통해 회사의 콘텐츠 관리 시스템으로 최종
사용자에게 푸시됩니다.
https://aws.amazon.com/ko/solutions/case-studies/hearst-data-analytics/

---

# Q60 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/85121-exam-aws-certified-solut
ions-architect-associate-saa-c03/
해설:・
Application Load Balancer 를 위한 리스너…..쿼리 문자열 조건을 사용하여 쿼리 문자열의
키/값 페어 또는 값을 기반으로 요청을 라우팅하는 규칙을 구성할 수 있습니다.
https://docs.aws.amazon.com/ko_kr/elasticloadbalancing/latest/application/load-balance
r-listeners.html
Application Load Balancer 리스너 규칙을 사용하여 HTTP 요청을 HTTPS로 리디렉션하려고
합니다. 어떻게 해야 하나요?
①HTTP 요청을 HTTPS로 리디렉션하는 HTTP 리스너 규칙 생성.
②HTTPS 리스너 생성.
③Application Load Balancer의 보안 그룹이 443의 트래픽을 허용하는지 확인
https://aws.amazon.com/ko/premiumsupport/knowledge-center/elb-redirect-http-to-htt
ps-using-alb/
참조
https://aws.amazon.com/premiumsupport/knowledge-center/elb-redirect-http-to-https-
using-alb/
https://repost.aws/ko/knowledge-center/elb-redirect-http-to-https-using-alb

---

# Q61 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/85580-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:・
애플리케이션에 자격증명 하드코딩 안 됨 = Secrets Manager.
Secrets Manager 를 사용하면 애플리케이션 소스 코드에서 하드 코딩된 자격 증명을
제거하고 애플리케이션 자체에 자격 증명을 저장하지 않음으로써 보안 태세를 개선할 수
있습니다. 사용자의 개입 없이 지정한 일정에 따라 자동으로 보안 암호를 교체하도록
Secrets Manager 를 구성할 수 있습니다. 교체는 AWS Lambda 함수를 사용하여 정하고
실행합니다.
https://docs.aws.amazon.com/ko_kr/secretsmanager/latest/userguide/intro.html
참고:
https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_database_secret.
html

---

# Q62 

**정답: D**

https://www.examtopics.com/discussions/amazon/view/85524-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:・
외부 인증기관에서 발급한 SSL/TLS 인증서가 이미 있고 이를 사용해야하므로 ACM 쪽에서
SSL/TLS 인증서를 발급하는 A,B는 모두 오답.
C(X) : 인증서가 있는데 또 발급받을 필요가 없음.
https://www.amazonaws.cn/en/certificate-manager/faqs/#Managed_renewal_and_deploy
ment

---

# Q63 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/85795-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:・
A(O) : S3에 넣으면 Lambda를 통해 자동으로 처리가 되도록 하는 거라 OK. S3는 저렴함.
B(X) : dynamodb는 이미지 저장용으론…
C(X) : 저렴한 S3가 있는데 굳이... 인스턴스 비용도 나감.
D(x) : C와 마찬가지.
설명2:
Elastic BeanStalk는 비싸고 DocumentDB는 최대 400KB의 파일을 업로드할 수 있습니다.
따라서 Lambda와 S3가 하나여야 합니다.

---

# Q64 

**정답: D**

https://www.examtopics.com/discussions/amazon/view/85173-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:・
Windows File Server + AWS로 이동 = Amazon FSx File Gateway.
Amazon FSx 파일 게이트웨이는 Amazon FSx 의 Windows 파일 공유에 대한 온프레미스
액세스를 최적화하여 사용자가 짧은 지연 시간과 공유 대역폭을 유지하면서 Windows 파일
서버용 FSx 데이터에 쉽게 액세스할 수 있도록 합니다. 사용자는 액세스할 수 있는 자주
사용하는 데이터의 로컬 캐시를 활용하여 성능을 높이고 데이터 전송 트래픽을 줄일 수
있습니다. 파일 읽기 및 쓰기와 같은 파일 시스템 작업은 모두 로컬 캐시에 대해 수행되는
반면 Amazon FSx 파일 게이트웨이는 변경된 데이터를 백그라운드에서 Windows 파일
서버용 FSx 와 동기화합니다. 이러한 기능을 사용하면 Windows 파일 서버용 FSx 에서
AWS 의 모든 온프레미스 파일 공유 데이터를 통합하고 보호되고 탄력적인 완전 관리형
파일 시스템의 이점을 누릴 수 있습니다.
https://aws.amazon.com/storagegateway/faqs/?nc1=h_ls
설명2:
https://docs.aws.amazon.com/filegateway/latest/filefsxw/what-is-file-fsxw.html
대기 시간을 최소화하면서 AWS 와 온프레미스 파일 스토리지 모두에 액세스해야 하는
회사의 요구 사항을 충족하기 위해 하이브리드 클라우드 아키텍처를 사용할 수 있습니다.
한 가지 솔루션은 완벽하게 관리되는 Windows 파일 서버를 제공하는 AWS 에서 Windows
파일 서버용 Amazon FSx를 배포 및 구성하는 것입니다.
온프레미스 파일 데이터는 온프레미스와 AWS 파일 스토리지 간의 브리지 역할을 할 수
있는 FSx 파일 게이트웨이로 이동할 수 있습니다. 클라우드 워크로드는 AWS 에서
Windows File Server 용 FSx 를 사용하도록 구성할 수 있으며 온프레미스 워크로드는 FSx
파일 게이트웨이를 사용하도록 구성할 수 있습니다.
이 솔루션은 운영 오버헤드를 최소화하고 기존 파일 액세스 패턴을 크게 변경할 필요가
없습니다. 온프레미스와 AWS 간의 연결은 AWS Site-to-Site VPN 연결을 사용하여 설정할
수 있습니다.
참조:
Windows 파일 서버용 AWS FSx: https://aws.amazon.com/fsx/windows/
AWS FSx 파일 게이트웨이: https://aws.amazon.com/fsx/file-gateway/
AWS 사이트 간 VPN: https://aws.amazon.com/vpn/site-to-site-vpn/

---

# Q65 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/85367-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:・
・Textract로 텍스트 추출, Comprehend Medical을 통해 식별
A(X) : Textract 와 Comprehend Medical 을 사용하는 것이 파이썬 코드를 별도로 관리할
필요가 없어서 운영하기 편함.
B(X) : SageMaker는 기계 학습 모델 서비스.
Amazon SageMaker 는 완전관리형 인프라, 도구 및 워크플로를 사용하여 모든 사용 사례에
대해 기계 학습(ML) 모델을 구축, 훈련 및 배포하는 완전관리형 서비스입니다.
https://aws.amazon.com/ko/sagemaker/faqs/
C(O) : Textract는 OCR 같은 서비스. Comprehend는 의료용 텍스트 식별 서비스.
Amazon Textract 는 스캔한 문서에서 텍스트, 필기 및 데이터를 자동으로 추출하는 기계
학습(ML) 서비스입니다. 단순한 광학 문자 인식(OCR) 이상으로 양식 및 표의 데이터를
식별하고 이해하며 추출합니다.
https://aws.amazon.com/ko/textract/
Amazon Comprehend Medical 은 HIPAA 적격 자연어 처리(NLP) 서비스로, 미리 학습된
기계 학습을 사용하여 처방전, 처치, 진단과 같은 의료 텍스트에서 의료 데이터를 파악하고
추출합니다.
https://aws.amazon.com/ko/comprehend/medical/
D(X) : Rekognition은 이미지나 비디오 분석 서비스지 텍스트 추출 서비스가 아님.
Amazon Rekognition 은 애플리케이션에 강력한 시각 분석 기능을 쉽게 추가할 수 있게 해
주는 서비스입니다. Rekognition Image를 통해 수백만 개의 이미지를 검색, 확인 및 구성할
수 있는 강력한 애플리케이션을 쉽게 구축할 수 있습니다. Rekognition Video 를 통해
저장된 동영상 또는 실시간 스트림 동영상에서 동작 기반 컨텍스트를 추출하고 이를 분석할
수 있습니다.
https://aws.amazon.com/ko/rekognition/faqs/?nc=sn&loc=7
설명2:
대기 시간을 최소화하면서 AWS 와 온프레미스 파일 스토리지 모두에 액세스해야 하는
회사의 요구 사항을 충족하기 위해 하이브리드 클라우드 아키텍처를 사용할 수 있습니다.
한 가지 솔루션은 완벽하게 관리되는 Windows 파일 서버를 제공하는 AWS 에서 Windows
파일 서버용 Amazon FSx 를 배포 및 구성하는 것입니다. 온프레미스 파일 데이터는
온프레미스와 AWS 파일 스토리지 간의 브리지 역할을 할 수 있는 FSx 파일 게이트웨이로
이동할 수 있습니다. 클라우드 워크로드는 AWS 에서 Windows File Server 용 FSx 를
사용하도록 구성할 수 있으며 온프레미스 워크로드는 FSx 파일 게이트웨이를 사용하도록
구성할 수 있습니다. 이 솔루션은 운영 오버헤드를 최소화하고 기존 파일 액세스 패턴을
크게 변경할 필요가 없습니다. 온프레미스와 AWS 간의 연결은 AWS Site-to-Site VPN
연결을 사용하여 설정할 수 있습니다.
참조:
AWS FSx for Windows File Server: https://aws.amazon.com/fsx/windows/
AWS FSx File Gateway: https://aws.amazon.com/fsx/file-gateway/
AWS Site-to-Site VPN: https://aws.amazon.com/vpn/site-to-site-vpn/

---

# Q66 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/85310-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:・
A(X) : 즉각적인 액세스가 항상 필요하다고 했기 때문에 S3 Glacier 사용은 적합하지 않음.
B(X) : 재생산하기 쉽지 않은 중요한 비즈니스 데이터라고 했기 때문에 One Zone-IA
보다는 S3 Standard-IA가 더 적합
C(O) : 30 일 동안은 자주 액세스하므로 S3 Standard, 30 일 이후에는 자주 액세스하진
않지만 즉각적인 액세스가 필요하므로 S3 Standard-IA, 4 년이 지나면 중요한 비즈니스
데이터므로 함부로 보관해서는 안됨. 따라서 삭제.
D(X) : 중요한 비즈니스 데이터라고 했으므로 보관기간인 4 년이 지나고 나서는 함부로
보관해서는 안되며 삭제해야 함.
참고:
https://aws.amazon.com/ko/s3/storage-classes/?trk=66264cd8-3b73-416c-9693-ea7cf
4fe846a&sc_channel=ps&s_kw

---

# Q67 

**정답: D**

https://www.examtopics.com/discussions/amazon/view/85583-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:・
가시성 제한 시간은 Amazon SQS 가 메시지를 반환할 때 시작됩니다. 이 시간 동안
소비자는 메시지를 처리하고 삭제합니다. 그러나 메시지를 삭제하기 전에 소비자가
실패하고 가시성 제한 시간이 만료되기 전에 시스템에서 해당 메시지에 대한
DeleteMessage 작업을 호출하지 않으면 메시지가 다른 소비자에게 표시되고 메시지가
다시 수신됩니다. 메시지를 한 번만 수신해야 하는 경우 소비자는 가시성 제한 시간 내에
메시지를 삭제해야 합니다.
https://docs.aws.amazon.com/ko_kr/AWSSimpleQueueService/latest/SQSDeveloperGuide
/sqs-visibility-timeout.html
키워드: Amazon RDS 에 대한 SQS 대기열 쓰기 여기에서 옵션 D 최상의 기타 옵션
제외[옵션 A - 기존 대기열에 하나 이상의 대기열을 도입할 수 없습니다. 옵션 B - 권한만
허용; 옵션 C - 메시지만 검색] FIFO 대기열은 중복 메시지를 도입하지 않도록
설계되었습니다. 그러나 메시지 생성자는 특정 시나리오에서 중복을 생성할 수 있습니다.
예를 들어 생성자가 메시지를 보내고 응답을 받지 못한 다음 동일한 메시지를 다시 보내는
경우입니다. Amazon SQS API 는 메시지 생성자가 중복 전송을 방지하는 중복 제거 기능을
제공합니다. 메시지 생성자에 의해 도입된 모든 중복 항목은 5 분 중복 제거 간격 내에
제거됩니다. 표준 대기열의 경우 때때로 메시지의 복제본을 받을 수 있습니다(최소 1 회
전달). 표준 대기열을 사용하는 경우 애플리케이션을 멱등적으로 설계해야 합니다(즉,
동일한 메시지를 두 번 이상 처리할 때 부정적인 영향을 받지 않아야 함).
설명2:
메시지를 수신한 직후에는 메시지가 대기열에 그대로 있습니다. 다른 소비자가 메시지를
다시 처리하지 못하게 Amazon SQS 에서는 다른 소비자가 메시지를 수신하고 처리할 수
없도록 막는 기간인 Visibility timeout을 설정합니다.
https://docs.aws.amazon.com/ko_kr/AWSSimpleQueueService/latest/SQSDeveloperGuide
/sqs-visibility-timeout.html

---

# Q68 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/85593-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:・
어떤 경우에는 이 연결만으로는 충분하지 않습니다. 항상 DX 의 백업으로 폴백 연결을
보장하는 것이 좋습니다. 여러 옵션이 있지만 AWS Site-To-Site VPN 으로 구현하는 것이
비용 효율적입니다. 비용을 줄이기 위해 활용하거나 그 동안 두 번째 DX 설정을 기다릴 수
있는 솔루션입니다.
https://blog.besharp.it/hybrid-cloud-networking-backup-aws-direct-connect-network-c
onnection-with-aws-site-to-site-vpn/
설명2:
VPN과 Direct Connect는 같이 사용할 수 있음.
https://docs.aws.amazon.com/ko_kr/whitepapers/latest/aws-vpc-connectivity-options/a
ws-direct-connect-vpn.html

---

# Q69 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/85594-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:・
A(X) : 다중 AZ 사용이 더 바람직. 게다가 뜬금없이 잘 쓰고 있던 EC2 인스턴스를 다른
AZ도 아니고 다른 리전에 배치하는 건 무리수.
B(O) : 다중 AZ + Auto Scaling으로 고가용성 확보.
C(X) : 하나의 가용영역을 사용하므로 고가용성 불충족.
D(X) : 다중 AZ가 더 바람직할 뿐더러 굳이 불필요하게 S3를 거쳐가고 있음.
설명2:
최소한의 가동 중지 시간과 최소한의 데이터 손실로 고가용성을 달성하려면 단일 장애
지점이 없도록 여러 가용 영역을 사용하도록 Auto Scaling 그룹을 구성해야 합니다. 기본
가용 영역에서 정전이 발생한 경우 자동 장애 조치를 활성화하려면 데이터베이스를 다중
AZ로 구성해야 합니다. 또한 Amazon RDS Proxy 인스턴스를 사용하여 연결 실패를 줄이고
장애 조치 시간을 개선하여 데이터베이스의 확장성과 가용성을 개선할 수 있습니다.

---

# Q70 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/85734-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:・
이 회사는 NLB 가 응용 프로그램에 대한 HTTP 오류를 감지하지 못한다고 알고
있습니다'라는 대목에서 응용프로그램에 대한 HTTP 오류를 감지하려면 ALB(Applicaton
Load Balancer)가 필요함을 유추할 수 있음.
A(X) : 응용프로그램에 대한 HTTP 오류를 감지해야하므로 NLB는 부적절.
B(X) : 자동이 아니라 정기적으로 로그를 확인하는 것이므로 오답.
C(O) : Application Load Balancer 는 등록된 대상으로 요청을 주기적으로 전송하여 상태를
확인합니다. 이러한 테스트를 바로 상태 확인이라고 합니다....◎HealthCheckProtocol :
대상에 대한 상태 확인을 수행할 때 로드 밸런서가 사용하는 프로토콜입니다. HTTP, HTTPS
등의 프로토콜이 여기에 해당됩니다. HTTP 프로토콜이 기본 설정값입니다.
◎HealthCheckPath : 대상에 대한 상태 확인을 위한 대상입니다. 프로토콜 버전이
HTTP/1.1 또는 HTTP/2 인 경우 유효한 URI(/path?query)를 참조하세요. 기본값은 /입니다.
프로토콜 버전이 gRPC 인 경우, 사용자 지정 상태 확인 방법의 경로를
/package.service/method 형식으로 지정합니다. 기본값은 /AWS.ALB/healthcheck입니다.
https://docs.aws.amazon.com/ko_kr/elasticloadbalancing/latest/application/target-group
-health-checks.html
D(X) : A와 같은 이유로 오답.
설명2:
애플리케이션 가용성: NLB 는 애플리케이션의 가용성을 보장할 수 없습니다. 이는 네트워크
및 TCP 계층 변수에만 의존하여 결정을 내리며 애플리케이션을 전혀 인식하지 못하기
때문입니다.
일반적으로 NLB 는 ICMP ping 에 응답하거나 3 방향 TCP 핸드셰이크를 올바르게 완료하는
서버의 기능을 기반으로 가용성을 결정합니다. ALB 는 훨씬 더 깊이 들어가 특정 페이지의
성공적인 HTTP GET 뿐만 아니라 콘텐츠가 입력 매개변수를 기반으로 예상한 대로라는
확인을 기반으로 가용성을 결정할 수 있습니다.

---

# Q71 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/85603-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:・
A(X) : 리전 장애 발생 시 리디렉션에는 탁월하나 데이터 손상에는 취약함. 글로벌
테이블에서 새로 작성된 항목은 1 초 이내에 모든 복제본 테이블에 전파되는데, 이는
데이터를 잘못 건드리면 1 초 이내에 모든 복제본 테이블에 해당 변경 사항이 적용되기
때문.
전역 테이블에서 새로 작성된 항목은 일반적으로 1 초 이내에 모든 복제본 테이블에
전파됩니다.
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/V2globaltables_H
owItWorks.html
B(O) : DynamoDB 는 주문형 백업 기능을 제공합니다. 이를 통해 규정 준수 요구 사항에
대한 장기 보존 및 보관을 위해 테이블의 전체 백업을 생성할 수 있습니다. 주문형 백업을
생성하고 Amazon DynamoDB 테이블에 대한 특정 시점 복구를 활성화할 수 있습니다.
지정 시간 복구는 우발적인 쓰기 또는 삭제 작업으로부터 테이블을 보호하는 데 도움이
됩니다. 특정 시점 복구를 사용하면 지난 35 일 동안의 특정 시점으로 테이블을 복원할 수
있습니다.
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html
C(X) : S3 Glacier는 콜드 스토리지로 액세스 시간이 더 김. 괜히 RTO만 늘어남.
D(X) : DynamoDB 는 서버리스라 EBS 스냅샷을 찍을 수 있는지도 의문이고 애초에
PITR(특정 시점으로 복구)이 더 좋은 옵션임.
참조
https://docs.aws.amazon.com/ko_kr/amazondynamodb/latest/developerguide/PointInTim
eRecovery.html

---

# Q72 

**정답: D**

https://www.examtopics.com/discussions/amazon/view/85604-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:・
A(X) : VPC-온프레미스 간 통신은 이루어지나 VPC 간 통신은 이루어지지 않고 있음.
B(X) : A와 같은 이유로 오답.
C(X) : A와 같은 이유로 오답.
D(O) : Transit Gateway 는 동일한 리전 내에 있는 여러 VPC 들을 연결하는 전송
'허브'이므로 Transit Gateway를 거쳐 VPC끼리 통신이 가능
AWS Transit Gateway는 동일한 리전의 VPC를 상호 연결하여 Amazon VPC 라우팅 구성을
한 곳에 통합하는 네트워크 전송 허브입니다.
https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-dir
ect-connect-aws-transit-gateway.html
설명2:
정답은 옵션 D 입니다. S3 VPC 게이트웨이 엔드포인트를 VPC 에 배포하고 S3 버킷에 대한
액세스를 허용하는 엔드포인트 정책을 연결합니다. S3 VPC 게이트웨이 엔드포인트를
배포하면 애플리케이션이 VPC 내의 프라이빗 네트워크 연결을 통해 S3 버킷에 액세스할
수 있으므로 인터넷을 통한 데이터 전송이 필요하지 않습니다. 이를 통해 데이터 전송
비용을 줄이고 애플리케이션의 성능을 향상시킬 수 있습니다. 엔드포인트 정책을 사용하여
애플리케이션이 액세스할 수 있는 S3 버킷을 지정할 수 있습니다.

---

# Q73 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/85613-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:・
전체적인 프로세스는 사내네트워크 -> 외부 인터넷 -> Bastion Host(퍼블릭서브넷 내에
NAT게이트웨이와 함께 위치) -> Application(프라이빗서브넷 내에 위치)으로 이루어짐.
Bastion Host 는 내부네트워크(여기서는 Application 이 있는 곳)에 접속할 수 있는 유일한
창구로, SSH 접속도 여길 통과해야만 가능함.
일단 Bastion Host 에 오는 트래픽(인바운드 트래픽)은 외부 인터넷을 통해서 온 회사의
IP(즉, 외부 IP)이므로 C가 정답.
그 다음으로는 Bastion Host 로부터 Application 으로 오는 트래픽(인바운드 트래픽)을
허용해야하는데 이미 Bastion Host에서 안쪽의 내부 네트워크와 통신하려고 프라이빗 IP를
들고 온 상태임. 따라서 D가 정답이며 최종적으로는 C,D가 정답.
내부 아이피는 온프레미스 환경 사내 안에서 쓰는 아이피를 보통 뜻하고 인터넷으로 나오는
IP 는 외부 IP 개념이라 사내 네트워크에서 외부인터넷으로 나온 external ip 범위의
대역에서 인바운드 액세스만 허용하는 C가 B보다 더 적절한 답으로 보임.

---

# Q74 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/85346-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:・
전체적인 구조는 EC2 인스턴스에서 실행되는 웹 애플리케이션(퍼블릭 서브넷 내에
위치)---->EC2 인스턴스에서 실행되는 데이터베이스(프라이빗 서브넷 내에 위치)으로
되어있고, 인스턴스 단위의 보안은 보안 그룹이 담당.
보안 그룹은 기본적으로 인바운드 트래픽에 관해서는 허용만 지정할 수 있고, 허용하지
않은 건 기본적으로 모두 차단하기 때문에 외부 인터넷->웹 애플리케이션으로의 액세스를
허용하려면 0.0.0.0/0으로부터 온 포트 443(HTTPS)를 허용해야 함.
그 다음으로 웹 애플리케이션->데이터베이스로의 액세스를 허용하려면 웹 애플리케이션이
있는 웹 계층에서 오는 포트 1433(MySQL) 인바운드 트래픽을 허용하도록 보안 그룹
설정을 해야 함. 따라서 정답은 A,C.
설명2:
"보안 그룹은 모든 인바운드 규칙에 대한 아웃바운드 규칙을 생성합니다." 완전히 옳지
않습니다. Statefull 은 인바운드(또는 아웃바운드) 규칙을 생성하는 경우 아웃바운드(또는
인바운드) 규칙을 생성한다는 의미가 아닙니다. 이것이 의미하는 바는 다음과 같습니다. X
IP 에 대한 포트 443 에서 인바운드 규칙을 생성한다고 가정합니다. 요청이 X ip 에서 포트
443으로 들어오면 포트 443에서 해당 요청에 대한 트래픽 아웃을 허용합니다.
그러나 아웃바운드 규칙을 보면 명시적으로 생성하지 않는 한 포트 443 에 대한 아웃바운드
규칙이 없을 것입니다. 상태 비저장 ACL에서는 들어오는 요청을 허용하는 인바운드 규칙과
애플리케이션이 이러한 들어오는 요청에 응답할 수 있도록 하는 아웃바운드 규칙을
만들어야 합니다.
https://docs.aws.amazon.com/ko_kr/vpc/latest/userguide/VPC_SecurityGroups.html#Sec
urityGroupRules

---

# Q75 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/86120-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:・
AWS Lambda, Amazon API Gateway, AWS Amplify, Amazon DynamoDB 및 Amazon
Cognito를 사용하여 서버리스 웹 애플리케이션을 구축하십시오. 이 예에서는 AWS Lambda,
Amazon API Gateway, AWS Amplify, Amazon DynamoDB 및 Amazon Cognito를 사용하여
서버리스 웹 애플리케이션 구축 질문과 유사한 설정을 보여줍니다.
RESTful API = API Gateway 사용.
트랜잭션 삭제되는 문제 = SQS.

---

# Q76 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/85801-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:・
A(X) : 퍼블릭 인터넷으로 전송하면 노출 위험이 큼. 심지어는 VPN도 안 했음.
B(O) : Direct Connect는 전용선 연결로 온프레미스-AWS 간 통신하는 것이고, DataSync는
데이터 전송/마이그레이션에 사용되는 서비스.
AWS DataSync 는 온프레미스와 AWS 스토리지 서비스 사이에서 데이터 이동을 자동화 및
가속화하는 안전한 온라인 서비스입니다. Amazon Simple Storage Service(S3) 버킷 간에
데이터를 복사할 수 있습니다. https://aws.amazon.com/ko/datasync/
C(X) : A와 마찬가지 이유로 오답.
D(X) : DMS 는 데이터베이스 마이그레이션 서비스로 S3 로 데이터를 전송해야하는 지문
상황과는 맞지 않음.
설명2:
다음은 AWS DataSync 의 주요 사용 사례 중 일부입니다. * 데이터 마이그레이션 - 활성
데이터 세트를 네트워크를 통해 Amazon S3, Amazon EFS 또는 FSx for Windows File
Server 로 빠르게 이동합니다. DataSync 에는 자동 암호화 및 데이터 무결성 검증이
포함되어 데이터가 안전하고 온전하며 사용할 준비가 되었는지 확인하는 데 도움이 됩니다.
"DataSync 에는 암호화 및 무결성 검증이 포함되어 있어 데이터가 안전하고 온전하며
사용할 준비가 되었는지 확인하는 데 도움이 됩니다."
https://aws.amazon.com/datasync/faqs/

---

# Q77 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/85740-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
실시간 데이터 수집 = Kinesis Data Streams. A,C 둘 중 하나가 답.
A(X) : API는 API Gateway를 사용하여 전송.
Amazon API Gateway 는 어떤 규모에서든 개발자가 API 를 손쉽게 생성, 게시, 유지 관리,
모니터링 및 보안 유지할 수 있도록 하는 완전관리형 서비스입니다. API 는 애플리케이션이
백엔드 서비스의 데이터, 비즈니스 로직 또는 기능에 액세스할 수 있는 "정문" 역할을
합니다. https://aws.amazon.com/ko/api-gateway/
C(O) :
・API Gateway API를 Kinesis Data Streams와 같이 사용 가능
API Gateway API를 Kinesis와 통합하려면 API Gateway와 Kinesis 서비스를 모두 사용할 수
있는 리전을 선택해야 합니다.
https://docs.aws.amazon.com/apigateway/latest/developerguide/integrating-api-with-aw
s-services-kinesis.html
・Kinesis Data Streams로 데이터 수집.
Amazon Kinesis Data Streams를 사용하면 특수 요구에 맞춰 스트리밍 데이터를 처리 또는
분석하는 사용자 지정 애플리케이션을 구축할 수 있습니다. 수십 만개의 소스에서 클릭
스트림, 애플리케이션 로그, 소셜 미디어와 같은 다양한 유형의 데이터를 Kinesis 데이터
스트림에 추가할 수 있습니다.
https://aws.amazon.com/ko/kinesis/data-streams/faqs/
・Kinesis Data Streams -> Kinesis Data Firehose
Amazon Kinesis Data Firehose 전송 스트림에 정보를 전송하도록 Amazon Kinesis Data
Streams를 구성할 수 있습니다.
https://docs.aws.amazon.com/ko_kr/firehose/latest/dev/writing-with-kinesis-streams.ht
ml
・Lambda로 데이터 변환
Kinesis Data Firehose Firehose 는 Lambda 함수를 호출하여 수신되는 소스 데이터를
변환하고 변환된 데이터를 대상으로 전송할 수 있습니다.
https://docs.aws.amazon.com/ko_kr/firehose/latest/dev/data-transformation.html
・S3로 전송
Amazon Kinesis Data Firehose는 실시간 스트리밍 데이터를 Amazon S3, Amazon RedShift,
Amazon OpenSearch Service, Splunk 및 사용자 지정 HTTP 엔드포인트 또는 Datadog,
Dynatrace, LogicMonitor, MongoDB, New Relic, Sumo Logic을 포함한 지원되는 서드파티
소유의 HTTP 엔드포인트 대상에 전달하기 위한 완전관리형 서비스입니다.
https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html

---

# Q78 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/85742-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:・
A(X) : 35 일 제한이 있습니다. ""특정 시점으로 복구가 설정되어 있으면 최근 35 일 중
원하는 시점으로 테이블을 복원할 수 있습니다.
https://docs.aws.amazon.com/ko_kr/amazondynamodb/latest/developerguide/PointInTim
eRecovery.html
B(O) : 한 곳에서 백업 현황 모니터링 및 콜드 스토리지에 저장, 예약 저장 가능합니다.
AWS Backup 을 사용하면 백업 정책을 구성하고 AWS 리소스 및 온프레미스 워크로드에
대한 활동을 한 곳에서 모니터링할 수 있습니다. AWS Backup 과 함께 DynamoDB 를
사용하면 AWS 계정 및 리전에서 온디맨드 백업을 복사하고, 온디맨드 백업에 비용 할당
태그를 추가하고, 온디맨드 백업을 콜드 스토리지로 전환하여 비용을 절감할 수 있습니다.
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/BackupRestore.h
tml
AWS Backup 을 사용하여 DynamoDB 온디맨드 백업을 자동으로 예약, 복사, 태그 지정 및
수명 주기를 수행할 수 있습니다. DynamoDB 콘솔에서 이러한 백업을 계속 보고 복원할 수
있습니다.
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/backuprestore_H
owItWorksAWS.html
C(X) : 불가능한 건 아닌데, B 가 더 유리합니다. 운영 측면에서는 한 곳에서 모니터링하는
게 편하고, S3 버킷에 저장한다고 했는데 7 년 동안 보관할 거면 S3 콜드 스토리지에
보관하는 게 비용이 더 저렴합니다.
D(X) : 너무 단계가 많습니다. 아마존에서는 DynamoDB 테이블 백업에 AWS Backup 또는
DynamoDB 콘솔을 사용할 것을 언급하고 있습니다. ""DynamoDB 온디맨드 백업을
생성하고 관리하는 데 사용할 수 있는 두 가지 옵션이 있습니다. AWS 백업 서비스
다이나모DB
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/BackupRestore.h
tml

---

# Q79 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/85743-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:・
사용량 예측이 안 되므로 프로비저닝은 무의미. 따라서 C,D 는 제외되고 A,B 둘 중 하나가
정답.
A(O) : 온디맨드 모드를 사용하는 테이블의 경우 DynamoDB 는 이전에 관찰된 트래픽
수준까지 상승하거나 하락할 때 고객의 워크로드를 즉시 수용할 수 있습니다. 트래픽
수준이 새로운 고점에 도달하면 DynamoDB는 신속하게 대응하여 워크로드를 수용합니다.
https://aws.amazon.com/ko/blogs/korea/amazon-dynamodb-on-demand-no-capacity-
planning-and-pay-per-request-pricing/
B(X) : 고가용성 언급이 없고 비용 최적화를 언급하고 있으므로 B보다는 A가 적합.

---

# Q80 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/85606-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:・
A(X) : '공개적'이라는 키워드가 애초에 보안과는 거리가 멈.
B(O) : 기존 KMS 키는 스냅샷을 암호화하는 데 사용되었기 때문에 MSP 파트너와 공유해도
괜찮음.
C(X) : 파트너의 KMS 키를 신뢰하면 파트너가 해당 키를 가지고 악의적인 용도로 사용할
때 문제가 됨.
D(X) : 파트너와 공유해야 하는데 파트너가 S3 버킷을 암호화하도록 냅둬버리면 파트너가
공유받는 입장이 아니라 내가 공유받는 입장이 되어버리는 역전현상이 벌어짐.
설명2:
AMI 스냅샷을 암호화하는 데 이미 사용되었기 때문에 기존 KMS 키를 MSP 외부 계정과
공유합니다.
https://docs.aws.amazon.com/ko_kr/kms/latest/developerguide/key-policy-modifying-ex
ternal-accounts.html

---

# Q81 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/86621-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:・
"처리해야 하는 작업을 보관할 Amazon SQS 대기열을 생성합니다.
컴퓨팅 애플리케이션에 대한 Amazon EC2 Auto Scaling 그룹을 생성합니다. SQS 대기열의
항목 수에 따라 노드를 추가 및 제거하도록 Auto Scaling 그룹에 대한 조정 정책을
설정합니다.
Amazon SQS 는 이 사용 사례에 이상적이며 대기열에서 대기 중인 작업 수에 따라 동적
조정을 사용하도록 구성할 수 있습니다. 이 조정을 구성하려면 유지 관리할 인스턴스당
허용되는 백로그인 대상 값과 함께 인스턴스당 백로그 메트릭을 사용할 수 있습니다.
이러한 수치는 다음과 같이 계산할 수 있습니다.
인스턴스당 백로그:
인스턴스당 백로그를 계산하려면 ApproximateNumberOfMessages 대기열 속성으로
시작하여 SQS 대기열의 길이를 결정합니다.

---

# Q82 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/85615-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
A(X) : 30일 전에 통보하랬지 맨날 통보하란 이야기는 없었음.
B(O) : AWS Config 를 사용하여 만료 날짜가 가까워지는 인증서를 확인할 수 있습니다.
인증서 만료 날짜가 가까워지면 Amazon EventBridge를 사용하여 이메일 알림을 받을 수도
있습니다.
https://aws.amazon.com/ko/premiumsupport/knowledge-center/acm-certificate-expiratio
n/
C(X) : Trusted Advisor는 ""AWS 환경을 검사한 후 비용 절감, 시스템 가용성 및 성능 향상
또는 보안 격차를 해결할 기회가 있을 때 권장 사항을 제시
https://docs.aws.amazon.com/ko_kr/awssupport/latest/user/trusted-advisor.html
하는 서비스로 이 경우엔 해당 사항이 없음.
D(X) : EventBridge 는 이벤트 발생을 감지해서 뭔가를 하는 서비스이지 이벤트 발생 전에
뭔가 감지해서 하는 게 아님
참고
https://repost.aws/ko/knowledge-center/acm-certificate-expiration
https://aws.amazon.com/ko/premiumsupport/knowledge-center/acm-certificate-expiratio
n/

---

# Q83 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/85902-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:・
https://aws.amazon.com/pt/blogs/aws/amazon-cloudfront-support-for-custom-origins/
이제 사용자 지정 오리진을 사용하여 CloudFront 배포를 생성할 수 있습니다. 각 배포는
S3 또는 사용자 지정 오리진을 가리킬 수 있습니다. 이것은 다른 스토리지 서비스일 수도
있고 EC2 인스턴스 또는 Elastic Load Balancer 와 같이 더 흥미롭고 동적인 것일 수도
있습니다.
설명2:
A(X) : 유럽과 가까워야 하므로 us-east-1은 오답.
B(X) : 동적 웹 사이트라고 했으므로 S3가 들어가지 않음.
C(O) : CloudFront는 사용자 지정 오리진으로 온프레미스 서버를 가리킬 수 있음.
사용자 지정 출처는 웹 서버와 같은 HTTP 서버입니다. HTTP 서버는 Amazon EC2
인스턴스이거나 다른 곳에서 호스팅하는 HTTP 서버일 수 있습니다. 웹 사이트
엔드포인트로 구성된 Amazon S3 오리진도 사용자 지정 오리진으로 간주됩니다.자체 HTTP
서버를 사용자 지정 오리진으로 사용하는 경우 오리진에서 객체를 가져올 때
CloudFront 에서 사용할 HTTP 및 HTTPS 포트 및 프로토콜과 함께 서버의 DNS 이름을
지정합니다.
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DownloadDistS
3AndCustomOrigins.html#concept_CustomOrigin
D(X) : 웹 사이트엔 CDN 서비스인 CloudFront가 필요.

---

# Q84 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/85665-exam-aws-certified-solut
ions-architect-associate-saa-c03/
해설:・
A(X) : 하루 24 시간 실행하는 프로덕션 EC2 인스턴스에 스팟 인스턴스는 적절치 않음.
스팟 인스턴스는 도중에 중지될 가능성이 높은 인스턴스에 더 적합.
B(O) : 1 년 또는 3 년 단위로 예약 인스턴스를 계약해서 사용하면 비용이 절감됨. 개발 및
테스트용 EC2 인스턴스는 매일 최소 8 시간 이상 실행된다고 했으므로 그 이상 사용될 수
있어 Scheduled Reserved 인스턴스보다는 온디맨드 인스턴스를 사용하는 것이 더 적절함
C(X) : 스팟 블록은 기간이 정의된 스팟 인스턴스로 A와 같은 이유로 오답.
""기간이 정의된 스팟 인스턴스(스팟 블록이라고도 함)는 2021년 7월 1일부로 신규 고객이
더 이상 사용할 수 없습니다.
https://aws.amazon.com/ko/blogs/aws/new-ec2-spot-blocks-for-defined-duration-wor
kloads/
D(X) : 24 시간 동안 사용할 EC2 인스턴스에는 예약 인스턴스 방식을 사용해 비용을 더
절감할 수 있음.

---

# Q85 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/85751-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:・
수정하거나 삭제할 수 없음 = S3 Object Lock.
S3 객체 잠금을 사용하면 write-once-read-many(WORM) 모델을 사용하여 객체를 저장할
수 있습니다. 객체 잠금은 고정된 시간 동안 또는 무기한으로 객체의 삭제 또는 덮어쓰기를
방지하는 데 도움이 될 수 있습니다.
https://docs.aws.amazon.com/ko_kr/AmazonS3/latest/userguide/object-lock.html

---

# Q86 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/85753-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:・
AWS Secrets Manager 는 애플리케이션, 서비스 및 IT 리소스에 액세스하는 데 필요한
암호를 보호하는 데 도움이 됩니다. 이 서비스를 사용하면 수명 주기 동안 데이터베이스
자격 증명, API 키 및 기타 암호를 쉽게 교체, 관리 및 검색할 수 있습니다.
https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html
Secrets Manager 를 사용하면 암호를 포함하여 코드의 하드코딩된 자격 증명을 Secrets
Manager 에 대한 API 호출로 대체하여 프로그래밍 방식으로 암호를 검색할 수 있습니다.
이렇게 하면 비밀이 코드에 더 이상 존재하지 않기 때문에 코드를 검사하는 누군가가
비밀을 손상시킬 수 없습니다. 또한 지정된 일정에 따라 암호를 자동으로 교체하도록
Secrets Manager 를 구성할 수 있습니다. 이를 통해 장기 비밀을 단기 비밀로 대체하여
손상 위험을 크게 줄일 수 있습니다.
설명2:
사용자 자격 증명을 자주 바꿈 + 안전한 방법 = Secrets Manager.
Secrets Manager 를 사용하면 애플리케이션 소스 코드에서 하드 코딩된 자격 증명을
제거하고 애플리케이션 자체에 자격 증명을 저장하지 않음으로써 보안 태세를 개선할 수
있습니다. 사용자의 개입 없이 지정한 일정에 따라 자동으로 보안 암호를 교체하도록
Secrets Manager 를 구성할 수 있습니다. 교체는 AWS Lambda 함수를 사용하여 정하고
실행합니다.
https://docs.aws.amazon.com/ko_kr/secretsmanager/latest/userguide/intro.html
또한 여러 리전과 여러 AZ에 걸쳐 작동.
https://docs.aws.amazon.com/ko_kr/secretsmanager/latest/userguide/disaster-recovery-
resiliency.html

---

# Q87 

**정답: D**

https://www.examtopics.com/discussions/amazon/view/85319-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
잠시 고객 데이터를 저장하는 솔루션 = SQS. 손실될 위험이 있는 처리 대상 데이터를 잠시
보관하는 용도로는 SQS가 주로 쓰인다고 보면 됨. 답은 D.
설명2:
https://www.learnaws.org/2020/12/13/aws-rds-proxy-deep-dive/
RDS 프록시는 새 데이터베이스 인스턴스가 작동할 때까지 대기하고 이 시간 동안
애플리케이션에서 받은 모든 요청을 유지함으로써 이러한 상황에서 애플리케이션 가용성을
향상시킬 수 있습니다. 최종 결과는 응용 프로그램이 기본 데이터베이스의 문제에 대해 더
탄력적이라는 것입니다. 이렇게 하면 DB 가 정상으로 돌아올 때까지 솔루션이 데이터를
보유할 수 있습니다. RDS 프록시는 Lambda 와 DB 간의 연결을 최적으로 활용하기 위한
것입니다. Lambda 는 DB 컴퓨팅 리소스에 부담을 줄 수 있는 여러 연결을 동시에 열 수
있습니다.

---

# Q88 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/85738-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
요청자 지불 버킷을 사용하면 버킷 소유자 대신 요청자가 버킷에서 데이터 다운로드 및
요청 비용을 지불합니다. 버킷 소유자는 항상 데이터 저장 비용을 지불합니다.
https://docs.aws.amazon.com/AmazonS3/latest/userguide/RequesterPaysBuckets.html
설명2:
"일반적으로 데이터를 공유하고 싶지만 데이터에 액세스하는 다른 사람과 관련된 요금을
부과하지 않으려면 버킷을 요청자 지불 버킷으로 구성합니다.
예를 들어 우편 번호 디렉터리, 참조 데이터 지리 공간 정보 또는 웹 크롤링 데이터와 같은
대용량 데이터 세트를 만들 때 요청자 지불 버킷을 사용할 수 있습니다."
https://docs.aws.amazon.com/AmazonS3/latest/userguide/RequesterPaysBuckets.html

---

# Q89 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/85808-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:・
・버전 관리는 실수로 삭제했을 때 이전 버전의 파일을 불러올 수 있도록 해줌.
Amazon S3 의 버전 관리는 동일 버킷 내에 여러 개의 객체 변형을 보유하는 수단입니다.
S3 버전 관리를 사용하면 버킷에 저장된 모든 버전의 객체를 모두 보존, 검색 및 복원할
수 있습니다.
https://docs.aws.amazon.com/ko_kr/AmazonS3/latest/userguide/Versioning.html
・MFA Delete는 함부로 삭제하지 못하도록 막음.
MFA Delete 는 다음 작업에 대해 추가 인증을 요구합니다. ◎버킷의 버전 관리 상태 변경
◎객체 버전 영구 삭제
https://docs.aws.amazon.com/ko_kr/AmazonS3/latest/userguide/MultiFactorAuthenticatio
nDelete.html

---

# Q90 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/85339-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:・
・스크립트는 데이터베이스에 추가된 새로운 영화의 수를 기록하기 위해 매일 임의의
간격으로 쿼리를 실행합니다. = 스크립트는 쿼리를 수행하고 있음
・'회사의 개발 팀은 스크립트가 실행 중일 때 데이터베이스 성능이 개발 작업에
부적절하다는 것을 알아차렸습니다.' = 스크립트 때문에 데이터베이스 성능이 떨어지고
있음.
따라서 쿼리가 너무 많이 수행되어서 데이터베이스 성능에 영향이 가는 상황입니다. 이런
경우 read replica를 통해 쿼리 부하를 분산할 수 있습니다.
B(O) : 애플리케이션에서 읽기 전용 복제본으로 읽기 쿼리를 라우팅하여 기본 DB
인스턴스의 로드를 줄일 수 있습니다.
https://docs.aws.amazon.com/ko_kr/AmazonRDS/latest/UserGuide/USER_ReadRepl.html
D(X) : ElastiCache는 웹 애플리케이션 성능 향상 용도로 주로 사용됨.
Amazon ElastiCache 는 더 느린 디스크 기반 데이터베이스에 전적으로 의존하기보다는
신속한 관리형 인 메모리 시스템에서 정보를 검색할 수 있는 기능을 지원함으로써 웹
애플리케이션의 성능을 향상합니다. https://aws.amazon.com/ko/elasticache/faqs/

---

# Q91 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/85667-exam-aws-certified-solut
ions-architect-associate-saa-c03/
해설:・
B. 프라이빗 서브넷에서 S3 를 생성하면 버킷에 대한 직접적인 인터넷 액세스가 제한되지만
EC2 와 S3 간의 직접적이고 안전한 연결은 제공되지 않습니다. 애플리케이션은 여전히 S3
API에 액세스하기 위해 인터넷을 통과해야 합니다.
C. EC2 와 동일한 지역에 S3 를 생성한다고 해서 본질적으로 트래픽이 인터넷을 통과하는
것을 막지는 않습니다.
D. NAT 게이트웨이를 구성하면 프라이빗 서브넷의 리소스에 대한 아웃바운드 인터넷
연결이 허용되지만 S3 서비스에 대한 직접적이고 안전한 연결은 제공되지 않습니다.
EC2에서 S3 API로의 트래픽은 여전히 인터넷을 통과합니다.
가장 적합한 솔루션은 S3 게이트웨이 엔드포인트를 구성하는 것입니다(옵션 A). 트래픽이
인터넷을 통과할 필요 없이 VPC 와 S3 서비스 간에 안전한 비공개 연결을 제공합니다. S3
게이트웨이 엔드포인트를 통해 EC2 는 VPC 내에서 직접 S3 API 에 액세스할 수 있으므로
트래픽이 인터넷을 통해 이동하지 못하도록 하는 보안 요구 사항을 충족합니다.
참고:
https://docs.aws.amazon.com/ko_kr/AmazonS3/latest/userguide/privatelink-interface-en
dpoints.html#types-of-vpc-endpoints-for-s3
https://docs.aws.amazon.com/ko_kr/vpc/latest/privatelink/vpc-endpoints-s3.html

---

# Q92 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/85903-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:・
A(O) : Gateway Endpoint는 퍼블릭 인터넷망을 통과하지 않는 전용 연결.
게이트웨이 엔드포인트는 VPC 용 인터넷 게이트웨이 또는 NAT 디바이스가 없어도 Amazon
S3 및 DynamoDB 에 대한 안정적인 연결을 제공합니다. 게이트웨이 엔드포인트는 AWS
PrivateLink를 활성화하지 않습니다.
https://docs.aws.amazon.com/ko_kr/vpc/latest/privatelink/vpce-gateway.html
B(X) : 객체를 퍼블릭으로 만드는 것은 보안과는 거리가 멈.
C(O) : 버킷 정책으로 버킷에 대한 액세스 제어.
버킷 정책은 버킷과 해당 버킷의 객체에 대한 액세스 권한을 부여할 수 있는 리소스 기반
정책입니다.
https://docs.aws.amazon.com/ko_kr/AmazonS3/latest/userguide/example-bucket-policie
s.html
D(X) : 차라리 IAM 사용자 정책을 사용하는 것이 더 나음.
Amazon S3 에 대한 사용자 액세스를 제어하는 IAM 사용자 정책을 생성하고 구성할 수
있습니다.
https://docs.aws.amazon.com/ko_kr/AmazonS3/latest/userguide/user-policies.html
E(X) : Gateway Endpoint가 더 좋은 선택임.

---

# Q93 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/85729-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:・
RDS 에 비해 Aurora 는 항상 3 개의 AZ 에 6 개의 복제본(Replica)를 보유하고 있으므로
애플리케이션 가용성에 더 유리. A,B 둘 중 하나가 답.여기서 mysqldump가 문젠데,
Q: MySQL에서 Amazon Aurora로 또는 그 반대로 마이그레이션하려면 어떻게 해야 하나요?
여러 가지 옵션이 있습니다. 표준 mysqldump 유틸리티를 사용하여 MySQL 에서 데이터를
내보내고 mysqlimport 유틸리티를 사용하여 Amazon Aurora 로 데이터를 가져올 수
있습니다. 그 반대도 마찬가지입니다. 또한, AWS 관리 콘솔에서 Amazon RDS의 DB 스냅샷
마이그레이션 기능을 이용하여 Amazon RDS for MySQL DB 스냅샷을 Amazon Aurora 로
마이그레이션할 수 있습니다. 대부분 고객은 [1시간 이내]에 마이그레이션을 완료하지만
https://aws.amazon.com/ko/rds/aurora/faqs/
최대 1GB 정도의 소규모 데이터베이스라면 mysqldump를 실행
https://aws.amazon.com/ko/rds/mysql/features/
이걸로 봤을 때 mysqldump 는 데이터백업에 많은 시간이 소요되는 방법으로 보이므로 A
제외. 답은 B.
참고
https://aws.amazon.com/blogs/aws/amazon-aurora-fast-database-cloning/

---

# Q94 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/86676-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:・
A(X) : EMR 은 빅데이터 플랫폼 서비스라 사용 분야가 좀 다르고, 파일을 업로드하지 않는
날이나 업로드가 거의 없는 날에는 과도한 지출이 발생할 우려가 있음.
B(X) : 파일에 일회성 단순 처리가 필요하다고 했으므로 EC2 인스턴스로 처리하는
것보다는 Lambda가 더 지문 요구사항에 부합.
C(O) : 유일하게 마음에 걸리는 게 '업로드 후 최대한 빨리 처리'해야한다는 건데 가장
정답에 가까운 선택지로 보임. 업로드하는 파일 숫자도 변동이 심한데 이를 SQS 대기열에
집어넣음으로서 대처할 수 있고, Lambda 함수로 파일에 일회성 단순 처리가 가능하며
추가적인 SQS->Lambda->DynamoDB 에 저장이라는 단순한 프로세스로 인해 운영
오버헤드도 매우 적음. DynamoDB는 JSON 파일을 지원
DynamoDB 는 JSON 을 사용하여 문서에 대한 기본 지원을 제공합니다. 따라서
DynamoDB 는 Tags 같은 반정형 데이터를 저장하는 데 적합합니다. JSON 문서 안에서
데이터를 가져오고 조작할 수도 있습니다.
https://docs.aws.amazon.com/ko_kr/amazondynamodb/latest/developerguide/SQLtoNoS
QL.WriteData.html
D(X) : 파일에 일회성 단순 처리가 필요하다고 했으므로 Kinesis Data Streams 로 처리하는
것보다는 Lambda 가 더 지문 요구사항에 부합. 또한 파일 업로드가 없거나 거의 없는
날에는 Kinesis 사용은 과도한 지출을 야기할 우려가 있음.
설명2:
Amazon S3 는 S3 버킷(예: 객체 생성, 객체 제거 또는 객체 복원)에 대한 이벤트 알림을
동일한 리전의 SNS 주제로 보냅니다.
SNS 주제는 중앙 리전의 SQS 대기열에 이벤트를 게시합니다.
SQS 대기열은 Lambda 함수의 이벤트 소스로 구성되며 Lambda 함수의 이벤트 메시지를
버퍼링합니다.
Lambda 함수는 메시지에 대한 SQS 대기열을 폴링하고 애플리케이션의 요구 사항에 따라
Amazon S3 이벤트 알림을 처리합니다.
https://docs.aws.amazon.com/ko_kr/prescriptive-guidance/latest/patterns/subscribe-a-l
ambda-function-to-event-notifications-from-s3-buckets-in-different-aws-regions.html

---

# Q95 

**정답: D**

https://www.examtopics.com/discussions/amazon/view/85906-exam-aws-certified-solut
ions-architect-associate-saa-c03/
해설:・
복제가 효과적으로 작동하려면 각 읽기 전용 복제본에 원본 DB 인스턴스와 동일한 양의
컴퓨팅 및 스토리지 리소스가 있어야 합니다. 원본 DB 인스턴스를 확장하는 경우 읽기
전용 복제본도 확장합니다.
https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_MySQL.Replication.R
eadReplicas.html
참조
https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_MySQL.Replication.R
eadReplicas.html

---

# Q96 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/86460-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
Allow문 해석 : 소스 IP가 10.100.100.0/24인 모든 리소스(*)에 대해 ec2 인스턴스 종료를
허용.
Deny 문 해석 : ec2 리전이 us-east-1 이 아닌 모든 리소스(*)에 대해 ec2 의 모든 작업을
불허. 따라서 정답은 C.
설명2:
정책은 us-east-1을 제외한 모든 지역에서 EC2 작업을 수행하는 것을 금지하고 소스 IP가
10.100.100.0/24 인 사용자만 인스턴스를 종료하도록 허용하기 때문입니다. 따라서 소스
IP가 10.100.100.254인 사용자는 us-east-1 지역의 인스턴스를 종료할 수 있습니다.

---

# Q97 

**정답: D**

https://www.examtopics.com/discussions/amazon/view/86626-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
Mcrosoft Active Directory용 AWS Directory Service :
AWS Managed Microsoft AD 에 대한 패치 및 유지 관리. 기본적으로 각 디렉터리는 서로
다른 가용 영역에 설치된 두 개의 DC로 구성됩니다.
https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_key_concepts_
maintenance.html
Windows 파일 서버용 FSx 를 AWS Managed Microsoft AD 와 통합하면 Windows 기반
애플리케이션 및 클라이언트(공유 파일 스토리지 활용)를 AWS 로 쉽게 이동할 수 있는
완전 관리형 기본 Microsoft Windows 기반 서버 메시지 블록(SMB) 프로토콜 파일
시스템을 제공합니다.
https://docs.aws.amazon.com/directoryservice/latest/admin-guide/usecase1.html

---

# Q98 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/85185-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:・
A(X) : 긴 폴링 대기 시간의 최대값은 20초입니다.
https://docs.aws.amazon.com/ko_kr/AWSSimpleQueueService/latest/SQSDeveloperGuide
/working-with-messages.html
B(X) : 솔루션 설계자는 SQS 메시지가 Lambda 함수를 두 번 이상 호출하여 여러 이메일
메시지를 생성하는 것이 문제의 원인이라고 보고 있음. 즉, SQS 쪽 문제이지 이미지 생성
및 업로드까지는 문제가 없다는 것. 중복 ID 제거는 생산자가 중복 메시지를 발생시키는
문제를 SQS FIFO Queue에서 해결하는 서비스 유형이므로 지문의 상황에는 적합하지 않음.
더군다나 모든 이미지 업로드 시마다 같은 문제가 계속 발생한다는 건 가끔 중복 메시지가
유입되는 정도가 아니라 SQS 대기열 쪽에서 처리가 이루어질 때 문제가 발생했을
가능성이 더 높음.
FIFO 대기열은 중복 메시지가 절대 유입되지 않도록 설계되었습니다. 다만 일부
시나리오에서는 메시지 생산자가 중복 메시지를 유입할 수도 있습니다.
https://aws.amazon.com/ko/sqs/faqs/
C(O) : 하지만 소비자가 메시지를 삭제하기 전에 실패할 경우 제한 시간 초과가 만료되기
전에 시스템에서 해당 메시지에 대한 DeleteMessage 작업을 호출하지 않으면 다른
소비자가 메시지를 볼 수 있게 되고 메시지가 다시 수신됩니다. 일반적으로
애플리케이션에서 대기열의 메시지를 처리하고 삭제하는 데 소요되는 최대 시간으로 제한
시간 초과를 설정해야 합니다. 메시지의 제한 시간을 단축하거나 늘리기 위해
ChangeMessageVisibility 작업을 사용하여 새 제한 시간 값을 지정할 수 있습니다.
https://docs.aws.amazon.com/ko_kr/AWSSimpleQueueService/latest/SQSDeveloperGuide
/sqs-visibility-timeout.html#configuring-visibility-timeout
D(X) : Lambda 함수가 메시지 처리 및 삭제까지 담당하게 되므로 Lambda 비용이 추가로
발생하여 다른 방법보다 더 비용이 발생. 굳이 이 방법을 사용할 이유가 없음.

---

# Q99 

**정답: D**

https://www.examtopics.com/discussions/amazon/view/85811-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:・
A. AWS Storage Gateway 파일 게이트웨이는 Lustre 클라이언트 액세스를 지원하지
않습니다.
B. EC2 Windows 인스턴스에서 Windows 파일 공유를 생성하는 것은 Windows 기반 파일
공유에 적합하지만 필요한 Lustre 클라이언트 액세스를 제공하지 않습니다. Lustre는 고성능
컴퓨팅(HPC) 환경에서 주로 사용되는 고성능 병렬 파일 시스템입니다.
C. EFS는 기본적으로 Lustre 클라이언트 액세스를 지원하지 않습니다. EFS는 관리형 파일
스토리지 서비스이지만 범용 파일 스토리지용으로 설계되었으며 Lustre 워크로드에
최적화되어 있지 않습니다.
D. Amazon FSx for Lustre 는 Lustre 클라이언트를 포함하여 고성능 컴퓨팅 워크로드에
최적화된 완전관리형 파일 시스템입니다. Lustre 클라이언트를 사용하여 관리되고 확장
가능한 방식으로 데이터에 액세스할 수 있는 기능을 제공합니다. 이 옵션을 선택함으로써
회사는 Lustre 클라이언트 액세스 요구 사항을 충족하면서 Amazon FSx for Lustre 의 성능
및 관리 용이성으로부터 이점을 얻을 수 있습니다.

---

# Q100 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/85186-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:・
고가용성 저장소 = S3. B,C 둘 중 하나가 답.
Lambda보다 KMS가 암호화 및 해독에 적합. 정답은 C.