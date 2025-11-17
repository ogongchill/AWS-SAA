# Q601 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/121210-exam-aws-certified-sol
utions-architect-associate-saa-c03/

---

# Q602 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/121212-exam-aws-certified-sol
utions-architect-associate-saa-c03/

---

# Q603 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/121211-exam-aws-certified-sol
utions-architect-associate-saa-c03/

---

# Q604 

**정답: D**

https://www.examtopics.com/discussions/amazon/view/121186-exam-aws-certified-sol
utions-architect-associate-saa-c03/

---

# Q605 

**정답: D**

https://www.examtopics.com/discussions/amazon/view/121170-exam-aws-certified-sol
utions-architect-associate-saa-c03/

---

# Q606 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/121214-exam-aws-certified-sol
utions-architect-associate-saa-c03/

---

# Q607 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/121215-exam-aws-certified-sol
utions-architect-associate-saa-c03/

---

# Q608 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/121216-exam-aws-certified-sol
utions-architect-associate-saa-c03/

---

# Q609 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/121162-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
이 옵션은 Lake Formation 과 통합된 엔진 및 쿼리 결과의 특정 데이터에 대한 액세스를
제한하는 사양인 데이터 필터를 사용하기 때문에 가장 효율적입니다. 데이터 필터는 중요한
정보가 포함된 데이터 부분에 대한 액세스를 방지하는 기술인 행 수준 보안 및 셀 수준
보안을 구현하는 데 사용할 수 있습니다. Data Catalog 테이블에 대한 Lake Formation
권한을 부여할 때 데이터 필터를 적용할 수 있으며 PartiQL 표현식을 사용하여 조건에 따라
데이터를 필터링할 수 있습니다. 이 솔루션은 중요한 정보가 포함된 데이터 부분에 대한
액세스를 방지하는 보안 솔루션을 제공해야 한다는 요구 사항을 충족합니다.
옵션 A 는 IAM 정책을 사용하여 Lake Formation 의 데이터에 대한 액세스 권한을 부여하는
방법인 Lake Formation 테이블에 대한 액세스 권한이 포함된 IAM 역할을 사용하기 때문에
효율성이 떨어집니다. 그러나 이것은 중요한 정보가 포함된 데이터 부분에 대한 액세스를
방지하는 방법을 제공하지 않습니다.
옵션 C 는 Lake Formation 이 데이터를 수집하기 전에 민감한 정보를 제거하는 AWS
Lambda 함수를 사용하기 때문에 효율성이 떨어집니다. 이는 서버리스 함수를 사용하여
데이터 정리 또는 변환을 수행하는 방법입니다. 그러나 여기에는 애플리케이션 코드 및
논리에 대한 상당한 변경이 포함될 수 있으며 데이터 손실 또는 불일치가 발생할 수도
있습니다.
옵션 D 는 서버리스 함수를 사용하여 데이터 정리 또는 변환을 수행하는 방법인 Lake
Formation 테이블에서 민감한 정보를 주기적으로 쿼리하고 제거하는 AWS Lambda 함수를
사용하기 때문에 효율성이 떨어집니다. 그러나 여기에는 애플리케이션 코드 및 논리에 대한
상당한 변경이 포함될 수 있으며 데이터 손실 또는 불일치가 발생할 수도 있습니다.

---

# Q610 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/121217-exam-aws-certified-sol
utions-architect-associate-saa-c03/

---

# Q611 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/121218-exam-aws-certified-sol
utions-architect-associate-saa-c03/

---

# Q612 

**정답: D**

https://www.examtopics.com/discussions/amazon/view/121159-exam-aws-certified-sol
utions-architect-associate-saa-c03/

---

# Q613 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/121158-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
이를 통해 회사는 최소한의 운영 오버헤드로 EKS 클러스터의 Kubernetes 비밀 개체를
암호화할 수 있습니다. EKS 클러스터에서 비밀 암호화를 활성화함으로써 회사는 AWS Key
Management Service(AWS KMS)를 사용하여 저장된 비밀을 암호화하고 해독하기 위한
암호화 키를 생성하고 관리할 수 있습니다. 이는 EKS 클러스터의 중요한 정보를 보호하는
간단하고 안전한 방법입니다.

---

# Q614 

**정답: D**

https://www.examtopics.com/discussions/amazon/view/121157-exam-aws-certified-sol
utions-architect-associate-saa-c03/

---

# Q615 

**정답: D**

https://www.examtopics.com/discussions/amazon/view/121154-exam-aws-certified-sol
utions-architect-associate-saa-c03/

---

# Q616 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/121177-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
Amazon GuardDuty 는 AWS 계정과 워크로드 전체에서 악의적인 활동과 무단 행동을
지속적으로 모니터링하는 위협 탐지 서비스입니다. GuardDuty 는 AWS CloudTrail 이벤트
로그, Amazon VPC 흐름 로그 및 DNS 로그와 같은 데이터 소스를 분석하여 손상된
인스턴스, 정찰, 포트 스캐닝 및 데이터 유출과 같은 잠재적인 위협을 식별합니다.
GuardDuty 는 AWS 계정 및 워크로드의 보안 상태에 대한 포괄적인 보기를 제공하는
서비스인 AWS Security Hub에 조사 결과를 보고할 수 있습니다. Security Hub는 여러 AWS
서비스 및 파트너 솔루션의 보안 경고를 집계, 구성 및 우선순위를 지정하여 대시보드에
표시합니다. 이 솔루션은 AWS 계정의 악의적인 활동, 워크로드 및 S3 버킷에 대한 액세스
패턴을 지속적으로 모니터링, 보고 및 시각화할 수 있으므로 요구 사항을 충족합니다.

---

# Q617 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/121176-exam-aws-certified-sol
utions-architect-associate-saa-c03/
102문제와 중복

---

# Q618 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/121219-exam-aws-certified-sol
utions-architect-associate-saa-c03/

---

# Q619 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/121220-exam-aws-certified-sol
utions-architect-associate-saa-c03/

---

# Q620 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/121221-exam-aws-certified-sol
utions-architect-associate-saa-c03/

---

# Q621 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/121222-exam-aws-certified-sol
utions-architect-associate-saa-c03/

---

# Q622 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/121223-exam-aws-certified-sol
utions-architect-associate-saa-c03/

---

# Q623 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/121172-exam-aws-certified-sol
utions-architect-associate-saa-c03/

---

# Q624 

**정답: D**

https://www.examtopics.com/discussions/amazon/view/125336-exam-aws-certified-sol
utions-architect-associate-saa-c03/

---

# Q625 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/125337-exam-aws-certified-sol
utions-architect-associate-saa-c03/

---

# Q626 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/125338-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
이를 통해 회사는 온프레미스 위치에서 Amazon S3 버킷으로 데이터를 마이그레이션하고
전송 후 데이터 무결성을 자동으로 확인할 수 있습니다. AWS DataSync 에이전트를
온프레미스에 배포함으로써 회사는 AWS 에서 대량의 데이터를 쉽게 이동할 수 있는 완전
관리형 데이터 전송 서비스를 사용할 수 있습니다. S3 버킷으로의 온라인 데이터 전송을
수행하도록 DataSync 에이전트를 구성함으로써 회사는 암호화, 압축, 대역폭 조절, 데이터
검증과 같은 DataSync 의 기능을 활용할 수 있습니다. DataSync 는 각 전송 작업 후에
소스와 대상 모두에서 데이터 무결성을 자동으로 확인합니다.

---

# Q627 

**정답: D**

https://www.examtopics.com/discussions/amazon/view/125541-exam-aws-certified-sol
utions-architect-associate-saa-c03/

---

# Q628 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/125459-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
S3 Storage Lens 는 AWS Organizations 의 여러 AWS 계정에 걸친 객체 스토리지 사용 및
활동에 대한 조직 전체의 가시성을 제공하는 클라우드 스토리지 분석 기능입니다. S3
스토리지 렌즈는 수집하여 S3 콘솔의 대화형 대시보드에 표시하는 지표 중 하나로
불완전한 멀티파트 업로드 객체 수를 보고할 수 있습니다. S3 Storage Lens는 추가 분석을
위해 CSV 또는 Parquet 형식의 지표를 S3 버킷으로 내보낼 수도 있습니다. 이 솔루션은
코드 개발이나 정책 변경이 필요하지 않으므로 최소한의 운영 오버헤드로 요구 사항을
충족합니다.

---

# Q629 

**정답: D**

https://www.examtopics.com/discussions/amazon/view/125460-exam-aws-certified-sol
utions-architect-associate-saa-c03/

---

# Q630 

**정답: D**

https://www.examtopics.com/discussions/amazon/view/125541-exam-aws-certified-sol
utions-architect-associate-saa-c03/

---

# Q631 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/125113-exam-aws-certified-sol
utions-architect-associate-saa-c03/
B??

---

# Q632 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/125114-exam-aws-certified-sol
utions-architect-associate-saa-c03/

---

# Q633 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/125513-exam-aws-certified-sol
utions-architect-associate-saa-c03/

---

# Q634 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/125544-exam-aws-certified-sol
utions-architect-associate-saa-c03/

---

# Q635 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/125545-exam-aws-certified-sol
utions-architect-associate-saa-c03/

---

# Q636 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/125546-exam-aws-certified-sol
utions-architect-associate-saa-c03/

---

# Q637 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/125547-exam-aws-certified-sol
utions-architect-associate-saa-c03/

---

# Q638 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/125574-exam-aws-certified-sol
utions-architect-associate-saa-c03/

---

# Q639 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/125575-exam-aws-certified-sol
utions-architect-associate-saa-c03/

---

# Q640 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/125579-exam-aws-certified-sol
utions-architect-associate-saa-c03/
??

---

# Q641 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/125580-exam-aws-certified-sol
utions-architect-associate-saa-c03/

---

# Q642 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/125215-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
이 솔루션은 UDP 패킷을 사용하고 트래픽이 증가 및 감소함에 따라 확장 및 축소하여
데이터를 전송하는 게임 애플리케이션 실행 요구 사항을 충족합니다. Network Load
Balancer 는 매우 낮은 대기 시간으로 높은 처리량을 유지하면서 초당 수백만 건의 요청을
처리할 수 있으며 TCP 및 UDP 프로토콜을 모두 지원합니다. Auto Scaling 그룹은 수요 및
조정 정책에 따라 EC2 인스턴스 수를 자동으로 조정할 수 있습니다.
Application Load Balancer가 UDP 프로토콜을 지원하지 않고 HTTP 및 HTTPS만 지원하기
때문에 옵션 B는 올바르지 않습니다.
Amazon Route 53 은 다양한 정책을 기반으로 트래픽을 라우팅할 수 있는 DNS
서비스이지만 로드 밸런싱 또는 확장 기능을 제공하지 않기 때문에 옵션 C 는 올바르지
않습니다.
옵션 D는
NAT 인스턴스는 프라이빗 서브넷의 인스턴스를 인터넷 또는 다른 AWS 서비스에 연결하는
데 사용되지만 로드 밸런싱 또는 확장 기능을 제공하지 않기 때문에 올바르지 않습니다.
참조:
https://aws.amazon.com/blogs/aws/new-udp-load-balancing-for-network-load-balanc
er/
https://docs.aws.amazon.com/autoscaling/ec2/userguide/AutoScalingGroup.html
A : UDP 패킷을 사용한다고 했으니 네트워크 계층 서비스인 NLB가 적합.

---

# Q643 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/125581-exam-aws-certified-sol
utions-architect-associate-saa-c03/

---

# Q644 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/125582-exam-aws-certified-sol
utions-architect-associate-saa-c03/

---

# Q645 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/125583-exam-aws-certified-sol
utions-architect-associate-saa-c03/

---

# Q646 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/125584-exam-aws-certified-sol
utions-architect-associate-saa-c03/

---

# Q647 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/125212-exam-aws-certified-sol
utions-architect-associate-saa-c03/
C??

---

# Q648 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/125586-exam-aws-certified-sol
utions-architect-associate-saa-c03/

---

# Q649 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/125588-exam-aws-certified-sol
utions-architect-associate-saa-c03/

---

# Q650 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/125589-exam-aws-certified-sol
utions-architect-associate-saa-c03/

---

# Q651 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/125244-exam-aws-certified-sol
utions-architect-associate-saa-c03/

---

# Q652 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/125591-exam-aws-certified-sol
utions-architect-associate-saa-c03/

---

# Q653 

**정답: C**

설명
Amazon Athena 는 Amazon S3 에 저장된 데이터에 대해 SQL 쿼리를 실행할 수 있는
서비스입니다. 서버리스이므로 인프라를 프로비저닝하거나 관리할 필요가 없습니다. 실행한
쿼리와 스캔한 데이터 양에 대해서만 비용을 지불하면 됩니다.
Amazon Athena를 사용하여 Amazon S3에서 데이터를 쿼리하면 다음과 같은 이점을 얻을
수 있습니다.
* Amazon RDS for MySQL DB 인스턴스의 성능에 영향을 주지 않고 보고서에 대한 쿼리를
실행할 수 있습니다. DB 인스턴스에서 S3 버킷으로 데이터를 내보내고 Athena 를 사용하여
버킷의 데이터를 쿼리할 수 있습니다. 이렇게 하면 DB 인스턴스에서 쿼리를 실행하는
오버헤드와 경합을 피할 수 있습니다.
* 보고서에 대한 쿼리를 실행하는 비용과 복잡성을 줄일 수 있습니다. 추가 요금이
발생하고 유지 관리가 필요한 읽기 전용 복제본이나 DB 인스턴스의 백업을 생성할 필요가
없습니다. 또한 운영 오버헤드를 증가시키는 추가 워크로드를 수용하기 위해 DB
인스턴스의 크기를 조정할 필요가 없습니다.
* Amazon S3 및 Athena 의 확장성과 유연성을 활용할 수 있습니다. 용량이나 성능 제한에
대한 걱정 없이 S3 에 대량의 데이터를 저장하고 Athena 로 쿼리할 수 있습니다. 또한
다양한 형식, 압축 방법 및 파티셔닝 체계를 사용하여 데이터 스토리지 및 쿼리 성능을
최적화할 수 있습니다.

---

# Q654 

**정답: B**

설명
Amazon RDS Proxy 는 Amazon RDS 및 Aurora 데이터베이스를 위한 완전관리형 고가용성
데이터베이스 프록시를 제공하는 서비스입니다. 이를 통해 데이터베이스 연결 풀링 및 공유,
데이터베이스 로드 감소, 애플리케이션 확장성 및 가용성 향상이 가능합니다.
Aurora 데이터베이스 앞에서 Amazon RDS Proxy 를 사용하면 다음과 같은 이점을 얻을 수
있습니다.
* 데이터베이스에 대한 연결 수를 줄이고 너무 많은 연결이 있음을 나타내는 오류를 피할
수 있습니다. Amazon RDS Proxy 는 연결 관리 및 멀티플렉싱을 처리하므로 더 적은 수의
데이터베이스 연결 및 리소스를 사용할 수 있습니다.
* 읽기 복제본이 기본 작성자로 승격되면 장애 조치 시간을 20%까지 줄일 수 있습니다.
Amazon RDS Proxy 는 애플리케이션 코드나 구성을 변경할 필요 없이 장애를 자동으로
감지하고 새로운 기본 인스턴스로 트래픽을 라우팅합니다. 벤치마크 테스트에 따르면
Amazon RDS Proxy 를 사용하면 장애 조치 시간이 66 초에서 53 초로 단축되어 20%
향상되었습니다.
* 데이터베이스 액세스의 보안 및 규정 준수를 향상시킬 수 있습니다. Amazon RDS
Proxy는 AWS Secrets Manager 및 AWS Identity and Access Management(IAM)와 통합되어
데이터베이스 연결에 대한 안전하고 세분화된 인증 및 권한 부여를 지원합니다.

---

# Q655 

**정답: C**

설명
AWS Lambda는 호출 수와 함수 실행 시간에 따라 요금을 부과합니다. 데이터 처리 작업이
상대적으로 작기 때문에(데이터 2MB) Lambda 가 비용 효율적인 선택입니다. 인프라를
프로비저닝하고 유지 관리할 필요 없이 실제 사용량에 대해서만 비용을 지불하면 됩니다.

---

# Q656 

**정답: B**

설명
AWS ParallelCluster는 AWS에서 고성능 컴퓨팅(HPC) 클러스터를 생성하고 관리할 수 있는
서비스입니다. 여러 EC2 인스턴스에서 분산 워크로드를 실행할 수 있는 AWS Batch 를
비롯한 여러 스케줄러를 지원합니다.
MPI 는 병렬 컴퓨팅에서 프로세스 간 메시지 전달을 위한 표준입니다. 데이터 송수신,
프로세스 동기화, 통신 그룹 관리 등의 기능을 제공합니다.
AWS ParallelCluster 및 MPI 라이브러리를 사용하면 다음과 같은 이점을 얻을 수 있습니다.
* 인스턴스 유형, 노드 수, 네트워크 구성 및 스토리지 옵션과 같은 특정 요구 사항을
충족하는 HPC 클러스터를 쉽게 생성하고 구성할 수 있습니다.
* AWS 의 확장성과 탄력성을 활용하여 서버 프로비저닝이나 관리에 대한 걱정 없이 대규모
병렬 워크로드를 실행할 수 있습니다.
* MPI 라이브러리를 사용하여 프로세스 간 통신 및 데이터 교환을 활성화하여 병렬
애플리케이션의 성능과 효율성을 최적화할 수 있습니다.
* Open MPI, Intel MPI 및 MPICH와 같이 AWS ParallelCluster와 호환되는 다양한 MPI 구현
중에서 선택할 수 있습니다.

---

# Q657 

**정답: B**

설명
Application Load Balancer 는 OSI 모델의 애플리케이션 계층(계층 7)에서 작동하는 일종의
Elastic Load Balancer입니다. Amazon EC2 인스턴스, 컨테이너, IP 주소 및 Lambda 함수와
같은 여러 대상에 수신 트래픽을 분산할 수 있습니다. 호스트 이름, 경로 또는 쿼리
매개변수와 같은 요청 내용을 기반으로 요청을 라우팅할 수도 있습니다. AWS 로드 밸런서
컨트롤러는 Kubernetes 클러스터의 Elastic Load Balancer 를 관리하는 데 도움이 되는
컨트롤러입니다. Kubernetes 수신 또는 서비스 리소스를 생성할 때 Application Load
Balancer 또는 Network Load Balancer를 프로비저닝할 수 있습니다.
AWS Load Balancer Controller 를 사용하여 Amazon EKS 클러스터용 Application Load
Balancer를 프로비저닝하면 다음과 같은 이점을 얻을 수 있습니다.
* Ingress 리소스에서 정의한 규칙에 따라 수신 요청을 적절한 마이크로서비스로 라우팅할
수 있습니다. 예를 들어 호스트 이름이나 경로가 다른 요청을 고객과 주문을 처리하는 다른
마이크로 서비스로 라우팅할 수 있습니다.
* 여러 대상에 부하를 분산하고 상태 확인 및 자동 조정을 활성화하여 컨테이너
애플리케이션의 성능과 가용성을 개선할 수 있습니다.
* Amazon EKS 및 Kubernetes 와 통합되는 단일 컨트롤러를 사용하여 로드 밸런서 관리
비용과 복잡성을 줄일 수 있습니다. 로드 밸런서를 수동으로 생성 또는 구성하거나
클러스터가 변경될 때 업데이트할 필요가 없습니다.

---

# Q658 

**정답: A**

설명:
Auto Scaling 그룹은 유사한 특성을 공유하고 수요에 따라 자동으로 확장 또는 축소될 수
있는 EC2 인스턴스 모음입니다. Auto Scaling 그룹은 여러 가용 영역의 여러 대상에 수신
트래픽을 분산시키는 Elastic Load Balancing 로드 밸런서의 일종인 Application Load
Balancer 뒤에 배치될 수 있습니다. 이 솔루션은 고가용성, 확장성 및 내결함성을 제공하여
웹 계층의 복원성을 향상시킵니다. Amazon RDS 다중 AZ 배포는 기본 데이터베이스
인스턴스를 자동으로 생성하고 다른 가용 영역에 있는 대기 인스턴스에 데이터를
동기식으로 복제하는 구성입니다. 오류가 발생하면 Amazon RDS 는 수동 개입 없이
자동으로 대기 인스턴스로 장애 조치됩니다. 이 솔루션은 데이터 중복성, 백업 지원 및
가용성을 제공하여 데이터베이스 계층의 복원성을 향상시킵니다. 이 단계 조합은
마이그레이션 중에 애플리케이션을 최소한으로 변경하여 요구 사항을 충족합니다.

---

# Q659 

**정답: A**

설명:
스팟 인스턴스는 온디맨드 가격에 비해 최대 90% 할인된 가격으로 제공되는 EC2
인스턴스입니다. 스팟 인스턴스는 중단을 허용할 수 있는 상태 비저장, 내결함성 및 유연한
워크로드에 적합합니다. 온디맨드 용량에 대한 수요가 증가하면 스팟 인스턴스를 EC2 에서
회수할 수 있지만 종료되기 2 분 전에 경고를 제공합니다. EKS 관리형 노드 그룹은 EKS
클러스터에 대한 노드의 프로비저닝 및 수명주기 관리를 자동화합니다. 관리형 노드 그룹은
스팟 인스턴스를 사용하여 비용을 절감하고 수요에 따라 클러스터를 확장할 수 있습니다.
관리형 노드 그룹은 스팟 인스턴스의 가용성과 복원력을 향상시키기 위해 용량 재조정 및
용량 최적화 할당 전략과 같은 기능도 지원합니다. 이 솔루션은 가장 저렴한 EC2 용량을
활용하고 수동 개입이 필요하지 않으므로 가장 비용 효율적으로 요구 사항을 충족합니다.

---

# Q660 

**정답: B**

설명:
Amazon S3 파일 게이트웨이는 네트워크 파일 공유로 표시되는 Amazon S3 에 파일 기반
인터페이스를 제공하는 서비스입니다. SMB 와 같은 표준 파일 스토리지 프로토콜을 통해
Amazon S3 객체를 저장하고 검색할 수 있습니다. S3 파일 게이트웨이는 짧은 액세스
지연을 위해 자주 액세스하는 데이터를 로컬로 캐시할 수도 있습니다. S3 수명 주기 정책은
수명 주기 전반에 걸쳐 객체 관리를 자동화하는 규칙을 정의할 수 있는 기능입니다. S3
수명 주기 정책을 사용하면 객체의 수명과 액세스 패턴에 따라 객체를 다양한 스토리지
클래스로 전환할 수 있습니다. S3 Glacier Deep Archive 는 검색 시간이 12 시간 또는
48 시간으로 가장 저렴한 장기 데이터 보관 비용을 제공하는 스토리지 클래스입니다. 이
솔루션은 회사가 SMB 파일 액세스를 통해 S3 에 대용량 파일을 저장하고, 비용 절감 및
규정 준수를 위해 7 일 후에 파일을 S3 Glacier Deep Archive 로 이동할 수 있도록 하므로
요구 사항을 충족합니다.

---

# Q661 

**정답: A**

설명:
AWS DataSync 는 AWS 스토리지 서비스와 온프레미스 스토리지 시스템 간에 대량의
데이터를 쉽게 이동할 수 있게 해주는 서비스입니다. AWS DataSync 는 S3 버킷에서 EFS
파일 시스템 및 다른 S3 버킷으로 파일을 지속적으로 복사할 수 있을 뿐만 아니라
소스에서 변경된 파일만 덮어쓸 수 있습니다. 이 솔루션은 코드 개발이나 수동 개입이
필요하지 않으므로 최소한의 운영 오버헤드로 요구 사항을 충족합니다.

---

# Q663 

**정답: B**

설명:
게이트웨이 엔드포인트는 지원되는 AWS 서비스로 향하는 트래픽에 사용되는 라우팅
테이블의 지정된 경로에 대한 대상인 게이트웨이입니다. Amazon S3 는 게이트웨이
엔드포인트를 지원하지 않고 인터페이스 엔드포인트만 지원합니다. 따라서 선택지 A 는
올바르지 않습니다.
인터페이스 엔드포인트는 지원되는 서비스로 향하는 트래픽의 진입점 역할을 하는 개인 IP
주소가 있는 탄력적 네트워크 인터페이스입니다. 인터페이스 엔드포인트는 지역 내에서
Amazon S3 에 대한 보안 액세스를 제공할 수 있지만 온프레미스 위치에서는 제공할 수
없습니다. 따라서 선택지 C는 올바르지 않습니다.
AWS Key Management Service(AWS KMS)는 데이터를 보호하기 위해 암호화 키를 생성하고
관리할 수 있는 서비스입니다. AWS KMS 는 인터넷을 통과하지 않고 Amazon S3 의
데이터에 액세스할 수 있는 방법을 제공하지 않습니다. 따라서 옵션 D 가 올바르지
않습니다.
AWS Transit Gateway는 Amazon Virtual Private Cloud(VPC)와 온프레미스 네트워크를 단일
게이트웨이에 연결할 수 있게 해주는 서비스입니다. AWS Transit Gateway 에서
게이트웨이를 생성하면 AWS Direct Connect를 사용하여 리전과 온프레미스 위치 모두에서
Amazon S3에 안전하게 액세스할 수 있습니다. 따라서 선택 B가 맞습니다.

---

# Q663 

**정답: A**

설명:
DynamoDB Accelerator(DAX)는 Amazon DynamoDB 용으로 구축된 완전 관리형 고가용성
캐싱 서비스입니다. DAX 는 초당 수백만 건의 요청에서도 밀리초에서 마이크로초로 최대
10 배의 성능 향상을 제공합니다. DAX 는 개발자가 캐시 무효화, 데이터 채우기 또는
클러스터 관리를 관리할 필요 없이 DynamoDB 테이블에 인 메모리 가속을 추가하는 데
필요한 모든 무거운 작업을 수행합니다. 이제 대규모 성능에 대한 걱정 없이 고객을 위한
훌륭한 애플리케이션을 구축하는 데 집중할 수 있습니다. DAX 는 기존 DynamoDB API
호출과 호환되므로 애플리케이션 로직을 수정할 필요가 없습니다. 이 솔루션은 코드
개발이나 수동 개입이 필요하지 않으므로 최소한의 운영 오버헤드로 요구 사항을
충족합니다.

---

# Q664 

**정답: A**

설명:
클러스터 배치 그룹은 네트워크 지연 시간을 최소화하기 위해 서로 가깝게 배치되는 단일
가용 영역 내 EC2 인스턴스의 논리적 그룹입니다. 이는 높은 네트워크 성능이 요구되는
대기 시간에 민감한 HPC 워크로드에 적합합니다. 컴퓨팅 최적화 EC2 인스턴스는 vCPU 대
메모리 비율이 높은 인스턴스 유형으로, 컴퓨팅 집약적인 애플리케이션에 이상적입니다.
NetApp ONTAP 용 Amazon FSx 는 파일 시스템에서 NFS 및 SMB 다중 프로토콜 액세스는
물론 데이터 중복 제거, 압축, 씬 프로비저닝, 스냅샷과 같은 기능을 제공하는 완전관리형
서비스입니다. 이 솔루션은 AWS 의 짧은 지연 시간 네트워크 및 스토리지 성능을
활용하므로 가장 짧은 지연 시간으로 요구 사항을 충족합니다.

---

# Q665 

**정답: A**

설명:
Microsoft SQL Server용 Amazon RDS는 SQL Server 2014, 2016, 2017 및 2019 에디션을
제공하는 동시에 백업, 패치, 확장과 같은 데이터베이스 관리 작업을 오프로드하는
완전관리형 서비스입니다. Amazon RDS는 온라인 애플리케이션의 성능에 영향을 주지 않고
보고 목적으로 사용할 수 있는 기본 데이터베이스의 읽기 전용 복사본인 읽기 전용
복제본을 지원합니다.
이 솔루션은 코드 변경이나 수동 개입이 필요하지 않으므로 최소한의 운영 오버헤드로 요구
사항을 충족합니다.

---

# Q666 

**정답: B**

설명:
AWS Lambda 는 서버를 프로비저닝하거나 관리하지 않고도 코드를 실행할 수 있는
서버리스 컴퓨팅 서비스입니다. Lambda 를 사용하면 사용자를 비용 센터에 매핑하는 RDS
데이터베이스를 쿼리하여 리소스를 생성한 사용자의 비용 센터 ID 로 리소스에 태그를
지정할 수 있습니다. Amazon EventBridge 는 이벤트 중심 아키텍처를 지원하는 서버리스
이벤트 버스 서비스입니다. EventBridge 는 AWS 계정에 의해 또는 AWS 계정을 대신하여
이루어진 기록된 API 호출인 AWS CloudTrail 이벤트에 반응하도록 구성할 수 있습니다.
EventBridge 는 특정 AWS 계정에 리소스가 생성될 때 Lambda 함수를 호출하여 사용자
자격 증명 및 리소스 정보를 매개 변수로 전달할 수 있습니다. 이 솔루션은 사용자 및 비용
센터 매핑을 기반으로 리소스에 자동으로 태그를 지정할 수 있으므로 요구 사항을
충족합니다.

---

# Q667 

**정답: D**

설명:
EBS 스냅샷은 데이터를 복원하거나 새 볼륨을 생성하는 데 사용할 수 있는 EBS 볼륨의
특정 시점 백업입니다. EBS 스냅샷 잠금이라는 기능을 사용하여 실수로 삭제되는 것을
방지하기 위해 EBS 스냅샷을 잠글 수 있습니다. 스냅샷이 잠겨 있으면 잠금이 해제될
때까지 루트 사용자를 포함한 어떤 사용자도 삭제할 수 없습니다. 잠금 정책은 스냅샷을
삭제할 수 있는 보존 기간을 지정할 수도 있습니다. 이 솔루션은 코드 개발이나 정책
변경이 필요하지 않으므로 최소한의 관리 노력으로 요구 사항을 충족합니다.

---

# Q668 

**정답: D**

설명:
요구 사항을 충족하는 솔루션은 AWS Security Token Service(AWS STS)를 사용하여 단기
자격 증명을 얻는 온프레미스 사용자 지정 자격 증명 브로커 애플리케이션 또는 프로세스를
개발하는 것입니다. 이 솔루션을 사용하면 회사는 SAML 호환성 없이도 기존 LDAP
디렉터리 서비스를 사용하여 AWS Management Console 에 사용자를 인증할 수 있습니다.
사용자 지정 자격 증명 브로커 애플리케이션 또는 프로세스는 LDAP 디렉터리 서비스와
AWS STS 간의 프록시 역할을 할 수 있으며 LDAP 속성 및 역할을 기반으로 사용자에 대한
임시 보안 자격 증명을 요청할 수 있습니다. 그런 다음 사용자는 이러한 자격 증명을
사용하여 자격 증명 브로커가 생성한 로그인 URL 을 통해 AWS Management Console 에
액세스할 수 있습니다. 또한 이 솔루션은 지정된 기간 후에 만료되는 단기 자격 증명을
사용하여 보안을 강화합니다.
다른 솔루션은 SAML 호환성이 필요하거나 AWS Management Console 에 대한 액세스를
제공하지 않기 때문에 요구 사항을 충족하지 않습니다. AWS 와 온프레미스 LDAP 간에
AWS IAM Identity Center(AWS Single Sign-On)를 활성화하려면 SAML 2.0을 지원하는 LDAP
디렉터리 서비스가 필요하지만 이 시나리오에서는 그렇지 않습니다. AWS 자격 증명을
사용하는 IAM 정책을 생성하고 정책을 LDAP 에 통합하면 AWS Management Console 에
대한 액세스가 제공되지 않고 AWS API 에만 액세스할 수 있습니다. LDAP 자격 증명이
업데이트될 때마다 IAM 자격 증명을 교체하는 프로세스를 설정하면 AWS Management
콘솔에 대한 액세스가 제공되지 않고 AWS CLI 에만 액세스할 수 있습니다. 따라서 이러한
솔루션은 주어진 요구 사항에 적합하지 않습니다.

---

# Q669 

**정답: B**

설명:
AWS WAF 는 애플리케이션 가용성에 영향을 미치거나 보안을 손상시키거나 과도한
리소스를 소비할 수 있는 일반적인 웹 공격으로부터 웹 애플리케이션을 보호하는 데 도움이
되는 웹 애플리케이션 방화벽입니다. AWS WAF 를 통해 사용자는 사용자 정의 가능한 웹
보안 규칙을 기반으로 웹 요청을 차단, 허용 또는 계산하는 규칙을 생성할 수 있습니다.
생성할 수 있는 규칙 유형 중 하나는 사용자가 허용하거나 차단하려는 IP 주소 또는 IP
주소 범위 목록을 지정할 수 있는 IP 일치 규칙입니다. 악의적인 IP 주소를 차단하는 IP
일치 조건을 추가하도록 AWS WAF 의 구성을 수정함으로써 솔루션 아키텍트는 공격자가
CloudFront 배포 및 ALB를 통해 웹 사이트에 액세스하는 것을 방지할 수 있습니다.
다른 옵션은 악성 IP 주소의 웹 사이트 액세스를 효과적으로 차단하지 못하기 때문에
올바르지 않습니다. CloudFront 배포의 네트워크 ACL 또는 ALB 뒤의 대상 그룹에 있는
EC2 인스턴스를 수정하는 것은 네트워크 ACL 이 상태 비저장이고 애플리케이션 계층에서
트래픽을 평가하지 않기 때문에 작동하지 않습니다. 보안 그룹은 상태 저장형이고 로드
밸런서 수준이 아닌 인스턴스 수준에서만 트래픽을 평가하기 때문에 ALB 뒤의 대상 그룹에
있는 EC2 인스턴스에 대한 보안 그룹을 수정하면 작동하지 않습니다.

---

# Q670 

**정답: C**

설명:
요구 사항을 충족하는 솔루션은 Amazon Elastic Container Service(Amazon ECS)에서
서비스 자동 확장 기능을 갖춘 마이크로서비스로 애플리케이션을 실행하는 것입니다. 이
솔루션을 사용하면 애플리케이션을 유연하고 확장 가능하며 점진적으로 개선할 수 있을
뿐만 아니라 애플리케이션 가동 중지 시간도 최소화할 수 있습니다. 모놀리식
애플리케이션을 마이크로서비스로 분할함으로써 회사는 전체 애플리케이션에 영향을 주지
않고 모듈을 분리하고 독립적으로 업데이트할 수 있습니다. Amazon ECS 에서
마이크로서비스를 실행함으로써 회사는 이식성, 효율성, 격리와 같은 컨테이너화의 이점을
활용할 수 있습니다. 서비스 자동 확장을 활성화함으로써 회사는 수요에 따라 각
마이크로서비스에 대해 실행되는 컨테이너 수를 조정하여 최적의 성능과 비용을 보장할 수
있습니다. 또한 Amazon ECS는 업데이트 중 가동 중지 시간을 줄이거나 없앨 수 있는 롤링
업데이트 또는 블루/그린 배포와 같은 다양한 배포 전략을 지원합니다.
다른 솔루션은 요구 사항을 충족하지 않거나 새로운 문제를 야기하기 때문에 첫 번째
솔루션만큼 효과적이지 않습니다. 최대 동시성 프로비저닝을 통해 AWS Lambda 에서
애플리케이션을 단일 함수로 실행하면 모놀리스를 마이크로서비스로 분해하지도 않고 유지
관리의 복잡성을 줄여주지도 않기 때문에 요구 사항을 충족하지 못합니다. 또한 Lambda
함수는 실행 시간(15 분), 메모리 크기(10GB) 및 동시성 할당량에 의해 제한되는데, 이는
보고서 생성 애플리케이션에 충분하지 않을 수 있습니다. 스팟 집합 기본 할당 전략을
사용하여 Amazon EC2 스팟 인스턴스에서 마이크로서비스로 애플리케이션을 실행하면 현물
가격 변동으로 인해 중단될 위험이 있으므로 요구 사항을 충족하지 못합니다. 스팟
인스턴스는 가용성이나 안정성이 보장되지 않으며 AWS 에서 언제든지 2 분 경고 후 회수할
수 있습니다.
이로 인해 보고서 생성이 실패하거나 처음부터 다시 시작될 수 있습니다. 한꺼번에 배포
전략을 사용하는 단일 애플리케이션 환경으로 AWS Elastic Beanstalk 에서 애플리케이션을
실행하면 모놀리스를 마이크로서비스로 분해하지도 않고 애플리케이션 가동 중지 시간을
최소화하지도 않기 때문에 요구 사항을 충족하지 못합니다. 일괄 배포 전략은 업데이트를
모든 인스턴스에 동시에 배포하므로 애플리케이션이 잠시 중단됩니다.

---

# Q671 

**정답: A**

설명:
이 회사는 고가용성과 애플리케이션 변경을 최소화하면서 3 개의 가용 영역에 걸쳐
컨테이너화된 애플리케이션 워크로드를 VPC 에 배포하려고 합니다. 최소한의 운영
오버헤드로 이러한 요구 사항을 충족하는 솔루션은 다음과 같습니다.
Amazon Elastic Container Service(Amazon ECS)를 사용하세요. Amazon ECS는 AWS에서
컨테이너화된 애플리케이션을 실행하고 확장할 수 있는 완전관리형 컨테이너
오케스트레이션 서비스입니다. Amazon ECS를 사용하면 자체 클러스터 관리 인프라를 설치,
운영 및 확장할 필요가 없습니다. Amazon ECS는 VPC, ELB, CloudFormation, CloudWatch,
IAM 등과 같은 다른 AWS 서비스와도 통합됩니다.
대상 추적 조정을 사용하도록 Amazon ECS 서비스 Auto Scaling 을 구성합니다. Amazon
ECS 서비스 Auto Scaling 을 사용하면 수요 또는 사용자 지정 지표를 기반으로 서비스의
작업 수를 자동으로 조정할 수 있습니다. 목표 추적 조정은 지정된 지표를 목표 값으로
유지하기 위해 서비스의 작업 수를 조정하는 정책 유형입니다. 예를 들어, 목표 추적
조정을 사용하여 서비스에 대한 목표 CPU 사용률 또는 작업당 요청 수를 유지할 수
있습니다.
최소 용량을 3 으로 설정합니다. 이렇게 하면 서비스가 항상 3 개의 가용 영역에서 3 개
이상의 작업을 실행하여 애플리케이션에 고가용성과 내결함성을 제공할 수 있습니다.
가용 영역 속성을 사용하여 분산되도록 작업 배치 전략 유형을 설정합니다. 이렇게 하면
작업이 클러스터의 가용 영역에 고르게 분산되어 서비스 가용성이 극대화됩니다.
이 솔루션은 가용 영역 전반에 걸쳐 고가용성을 제공하고 애플리케이션 변경을 최소화하며
자체 클러스터 인프라 관리에 따른 운영 오버헤드를 줄입니다.

---

# Q672 

**정답: D**

설명:
회사는 메시지 대기열에서 지속적으로 증가하는 메시지 수를 처리하는 Lambda 함수에
대해 컴퓨팅 비용을 줄이고 서비스 지연 시간을 유지하려고 합니다.
Lambda 함수는 CPU 집약적인 코드를 사용하여 메시지를 처리합니다. 이러한 요구 사항을
충족하려면 솔루션 설계자는 다음 솔루션을 권장해야 합니다.
Lambda 함수에 대해 프로비저닝된 동시성을 구성합니다. 프로비저닝된 동시성은 Lambda
함수에 할당된 사전 초기화된 실행 환경의 수입니다.
이러한 실행 환경은 들어오는 기능 요청에 즉시 응답하여 콜드 스타트 대기 시간을
줄입니다. 프로비저닝된 동시성을 구성하면 Lambda 서비스의 동시성 한도 도달로 인한
조절 오류를 방지하는 데도 도움이 됩니다.
AWS Compute Optimizer 권장 사항에 따라 메모리를 늘리십시오. AWS Compute
Optimizer 는 사용률 데이터를 기반으로 최적의 AWS 리소스 구성에 대한 권장 사항을
제공하는 서비스입니다. Lambda 함수에 할당된 메모리를 늘려 CPU 성능을 높이고 CPU
집약적인 코드의 성능을 향상시킬 수도 있습니다. AWS Compute Optimizer 는 워크로드
특성 및 성능 목표를 기반으로 Lambda 함수에 대한 최적의 메모리 크기를 찾는 데 도움이
됩니다.
이 솔루션은 메모리 및 CPU 리소스의 불필요한 과잉 프로비저닝을 방지하여 컴퓨팅
비용을 절감하고, 프로비저닝된 동시성 및 Lambda 함수에 대한 최적의 메모리 크기를
사용하여 서비스 대기 시간을 유지합니다.

---

# Q673 

**정답: B**

설명:
현재 Amazon S3 버킷에 저장된 기록 값을 사용하여 매월 제조 프로세스에 필요한
리소스를 예측하려면 솔루션 설계자는 Amazon SageMaker 를 사용하여 S3 버킷의 기록
데이터를 사용하여 모델을 훈련하고 Amazon SageMaker 모델을 배포해야 합니다. 추론을
위해 SageMaker 엔드포인트를 생성합니다. Amazon SageMaker 는 기계 학습(ML) 모델을
쉽게 구축, 교육 및 배포할 수 있는 방법을 제공하는 완전관리형 서비스입니다. 솔루션
아키텍트는 SageMaker 에서 제공하는 기본 제공 알고리즘 또는 프레임워크를 사용하거나
자체 사용자 지정 코드를 가져와 S3 버킷의 기록 데이터를 입력으로 사용하여 모델을
교육할 수 있습니다. 그런 다음 훈련된 모델을 애플리케이션의 예측 요청을 처리할 수 있는
확장 가능하고 안전한 웹 서비스인 SageMaker 엔드포인트에 배포할 수 있습니다. 솔루션
아키텍트는 SageMaker 를 사용하기 위해 ML 경험이 있거나 인프라를 관리할 필요가
없습니다.

---

# Q674 

**정답: A**

설명:
회사는 애플리케이션의 가용성과 성능을 향상하는 동시에 일반적인 웹 공격으로부터
애플리케이션을 보호하기를 원합니다. 회사에는 애플리케이션에 대한 고정 IP 주소도
필요합니다. 이러한 요구 사항을 충족하려면 솔루션 설계자는 다음 솔루션을 권장해야
합니다.
각 리전의 NLB(Network Load Balancer) 뒤에 EC2 인스턴스를 배치합니다. NLB 는 매우
짧은 대기 시간으로 높은 처리량을 유지하면서 초당 수백만 개의 요청을 처리하도록
설계되었습니다. NLB 는 각 가용 영역에 대한 고정 IP 주소도 지원하는데, 이는
화이트리스트 작성이나 방화벽 목적에 유용할 수 있습니다.
NLB 에 AWS WAF 를 배포합니다. AWS WAF 는 가용성, 보안 또는 성능에 영향을 미칠 수
있는 일반적인 웹 공격으로부터 웹 애플리케이션을 보호하는 데 도움이 되는 웹
애플리케이션 방화벽입니다. AWS WAF 를 사용하면 웹 애플리케이션에 대해 허용하거나
차단할 트래픽을 제어하는 사용자 지정 가능한 웹 보안 규칙을 정의할 수 있습니다.
AWS Global Accelerator 를 사용하여 액셀러레이터를 생성하고 NLB 를 엔드포인트로
등록합니다.
AWS Global Accelerator 는 로컬 또는 글로벌 사용자를 대상으로 애플리케이션의 가용성과
성능을 향상시키는 서비스입니다. 모든 AWS 리전의 애플리케이션 엔드포인트에 대한 고정
진입점 역할을 하는 고정 IP 주소를 제공합니다. AWS 글로벌 네트워크를 사용하여
사용자에서 애플리케이션까지의 경로를 최적화하여 TCP 및 UDP 트래픽의 성능을
향상시킵니다.
이 솔루션은 가용 영역 및 지역 전반에 걸쳐 고가용성을 제공하고, AWS 글로벌 네트워크를
통해 트래픽을 라우팅하여 성능을 향상시키며, 일반적인 웹 공격으로부터 애플리케이션을
보호하고, 애플리케이션에 고정 IP 주소를 제공합니다.

---

# Q675 

**정답: D**



---

# Q676 

**정답: B**

설명:
AWS WAF 는 애플리케이션 가용성에 영향을 미치거나 보안을 손상시키거나 과도한
리소스를 소비할 수 있는 일반적인 웹 공격으로부터 웹 애플리케이션을 보호하는 데 도움이
되는 웹 애플리케이션 방화벽입니다. AWS WAF 를 통해 사용자는 사용자 정의 가능한 웹
보안 규칙을 기반으로 웹 요청을 차단, 허용 또는 계산하는 규칙을 생성할 수 있습니다.
생성할 수 있는 규칙 유형 중 하나는 사용자가 허용하거나 차단할 IP 주소 또는 IP 주소
범위 목록을 지정할 수 있는 SQL 삽입 규칙입니다. AWS WAF 를 사용하여 애플리케이션을
보호함으로써 회사는 SQL 주입 및 기타 웹 기반 공격이 애플리케이션과 데이터베이스에
도달하는 것을 방지할 수 있습니다.
RDS 파라미터 그룹은 데이터베이스 인스턴스 작동 방식을 정의하는 파라미터 모음입니다.
사용자는 매개변수 그룹의 매개변수를 수정하여 데이터베이스의 동작과 성능을 변경할 수
있습니다. RDS 매개변수 그룹을 사용하여 보안 설정을 구성함으로써 회사는 원격 루트
로그인 비활성화, SSL 연결 요구, 최대 연결 수 제한과 같은 모범 사례를 적용할 수
있습니다.
다른 옵션은 SQL 주입 및 기타 웹 기반 공격으로부터 애플리케이션과 데이터베이스를
효과적으로 보호하지 못하기 때문에 올바르지 않습니다. 보안 그룹과 네트워크 ACL 을
사용하여 데이터베이스와 애플리케이션 서버를 보호하는 것만으로는 충분하지 않습니다.
왜냐하면 애플리케이션 계층이 아닌 네트워크 계층에서만 트래픽을 필터링하기 때문입니다.
AWS 네트워크 방화벽을 사용하여 애플리케이션과 데이터베이스를 보호할 필요는 없습니다.
이는 개별 애플리케이션이나 데이터베이스가 아닌 VPC 에 대한 네트워크 보호를 제공하는
상태 저장 방화벽 서비스이기 때문입니다. 서로 다른 기능을 위해 애플리케이션 코드에서
서로 다른 데이터베이스 계정을 사용하는 것은 좋은 습관이지만 SQL 주입 공격이
애플리케이션 코드의 취약점을 악용하는 것을 방지할 수는 없습니다.

---

# Q677 

**정답: B**

설명:
회사의 요구 사항에 가장 적합한 솔루션은 AWS Migration Hub 에서 홈 AWS 리전을
설정하고 AWS Application Discovery Service를 사용하여 온프레미스 서버에 대한 데이터를
수집하는 것입니다. 이 솔루션을 통해 회사는 온프레미스 서버 및 워크로드의 사용량 및
구성 데이터를 수집하고 AWS로의 마이그레이션을 계획할 수 있습니다.
AWS Migration Hub 는 마이그레이션 상태 정보를 단일 콘솔에 집계하여 마이그레이션
추적을 단순화하고 가속화하는 서비스입니다. 사용자는 검색된 서버를 보고, 이를
애플리케이션으로 그룹화하고, 홈 리전의 Migration Hub 콘솔에서 각 애플리케이션의
마이그레이션 상태를 추적할 수 있습니다. 홈 리전은 마이그레이션하는 리전과 관계없이
사용자가 마이그레이션 데이터를 저장하는 AWS 리전입니다.
AWS Application Discovery Service는 온프레미스 서버 및 데이터베이스에 대한 사용량 및
구성 데이터를 수집하여 사용자가 AWS 로의 마이그레이션을 계획하는 데 도움을 주는
서비스입니다.
Application Discovery Service 는 AWS Migration Hub 와 통합되어 에이전트 없는 검색과
에이전트 기반 검색이라는 두 가지 검색 수행 방법을 지원합니다. 가상 머신(VM) 및
데이터베이스에 대한 정적 구성 데이터와 활용도 데이터를 수집하는 VMware vCenter 를
통해 Application Discovery Service Agentless Collector를 배포하여 에이전트 없는 검색을
수행할 수 있습니다. 에이전트 기반 검색은 정적 구성 데이터, 상세한 시계열 시스템 성능
정보, 인바운드 및 아웃바운드 네트워크 연결, 실행 중인 프로세스를 수집하는 AWS
Application Discovery Agent를 각 VM 및 물리적 서버에 배포하여 수행할 수 있습니다.
다른 옵션은 요구 사항을 충족하지 않거나 사용 사례와 관련이 없기 때문에 올바르지
않습니다. AWS Schema Conversion Tool(AWS SCT)을 사용하여 관련 템플릿을 생성하고
AWS Trusted Advisor 를 사용하여 온프레미스 서버에 대한 데이터를 수집하는 것은
올바르지 않습니다. 이 솔루션은 온프레미스 서버의 사용 및 구성 데이터를 수집하는 데
적합하지 않기 때문입니다. 작업 부하. AWS SCT 는 사용자가 데이터베이스 스키마와 코드
객체를 한 데이터베이스 엔진에서 다른 데이터베이스 엔진(예: Oracle 에서
PostgreSQL 로)으로 변환하는 데 도움이 되는 도구입니다. AWS Trusted Advisor 는 비용
최적화, 성능, 보안, 내결함성 및 서비스 제한에 대한 모범 사례 권장 사항을 제공하는
서비스입니다. AWS Schema Conversion Tool(AWS SCT)을 사용하여 관련 템플릿을
생성하고 AWS Database Migration Service(AWS DMS)를 사용하여 온프레미스 서버에 대한
데이터를 수집하는 것은 올바르지 않습니다. 이 솔루션은 사용 및 구성 데이터를 수집하는
데 적합하지 않기 때문입니다. 온프레미스 서버 및 워크로드. 위에서 언급한 것처럼 AWS
SCT 는 사용자가 데이터베이스 스키마와 코드 객체를 한 데이터베이스 엔진에서 다른
데이터베이스 엔진으로 변환하는 데 도움이 되는 도구입니다. AWS DMS 는 사용자가 가동
중지 시간을 최소화하면서 관계형 데이터베이스, 비관계형 데이터베이스 및 기타 유형의
데이터 스토어를 AWS로 마이그레이션하는 데 도움이 되는 서비스입니다.

---

# Q678 

**정답: C**

설명:
자체 계정 권한을 포기하지 않고 다른 회사에 SQS 대기열에 대한 액세스를 제공하려면
솔루션 설계자는 SQS 대기열에 대한 다른 회사 액세스를 제공하는 SQS 액세스 정책을
생성해야 합니다. SQS 액세스 정책은 대기열에 액세스할 수 있는 사람과 그들이 수행할 수
있는 작업을 정의하는 리소스 기반 정책입니다. 정책은 상대 회사의 AWS 계정 ID 를
주체로 지정하고 sqs:ReceiveMessage, sqs:DeleteMessage 및 sqs:GetQueueAttributes 와
같은 작업에 대한 권한을 부여할 수 있습니다. 이렇게 하면 다른 회사가 역할을 맡거나
교차 계정 액세스 키를 사용할 필요 없이 자체 자격 증명을 사용하여 대기열을 폴링할 수
있습니다.

---

# Q679 

**정답: B**

설명:
요구 사항을 충족하는 솔루션은 캐시된 볼륨을 사용하여 AWS Storage Gateway를 배포하고
Storage Gateway 를 사용하여 자주 액세스하는 데이터 하위 집합의 복사본을 로컬에서
유지하면서 Amazon S3 에 데이터를 저장하는 것입니다. 이 솔루션을 사용하면 회사는
로컬에 캐시되지 않은 데이터만 전송하므로 대역폭 비용을 최소화하면서 스토리지 인프라를
AWS 로 마이그레이션할 수 있습니다. 또한 이 솔루션을 사용하면 캐시된 볼륨이 가장
최근에 사용한 데이터에 대한 짧은 대기 시간 액세스를 제공하므로 추가 비용 없이
데이터를 즉시 검색할 수 있습니다. Amazon S3 에 저장된 데이터는 내구성, 확장성 및
보안이 유지됩니다.
다른 솔루션은 요구 사항을 충족하지 못하거나 추가 비용이나 복잡성이 발생하기 때문에 첫
번째 솔루션만큼 효과적이지 않습니다. Amazon S3 Glacier Vault 를 배포하고 빠른 검색을
활성화하면 저장 및 검색 모두에 추가 비용이 발생하므로 요구 사항을 충족하지 못합니다.
Amazon S3 Glacier는 데이터 보관 및 백업을 위한 저렴한 스토리지 서비스이지만 Amazon
S3 보다 검색 시간이 더 깁니다. 신속 검색은 데이터에 더 빠르게 액세스할 수 있는
기능이지만 검색된 GB당 더 높은 요금을 청구합니다.
프로비저닝된 검색 용량은 신속한 검색을 위해 전용 용량을 예약하는 기능이지만,
프로비저닝된 용량 단위당 월별 요금도 청구합니다. 저장된 볼륨을 사용하여 데이터를
로컬에 저장하고 Storage Gateway를 사용하여 데이터의 특정 시점 스냅샷을 Amazon S3에
비동기적으로 백업하는 AWS Storage Gateway 를 배포하면 스토리지 인프라를 AWS 로
마이그레이션하지 않고 요구 사항을 충족하지 못합니다. 백업을 만듭니다. 저장 볼륨은
기본 데이터를 로컬에 저장하고 스냅샷을 Amazon S3에 백업하는 볼륨입니다. 이 솔루션은
온프레미스에 필요한 스토리지 용량을 줄이지 않으며 클라우드 스토리지의 이점을
활용하지도 않습니다. 온프레미스 데이터 센터에 연결하기 위해 AWS Direct Connect 를
배포하고 데이터를 로컬에 저장하고 Storage Gateway 를 사용하여 데이터의 특정 시점
스냅샷을 Amazon S3에 비동기식으로 백업하도록 AWS Storage Gateway를 구성하는 것은
요구 사항을 충족하지 않습니다. 또한 스토리지 인프라를 AWS 로 마이그레이션하지 않고
백업만 생성합니다. AWS Direct Connect 는 온프레미스 데이터 센터와 AWS 간에 전용
네트워크 연결을 설정하는 서비스로, 이를 통해 네트워크 비용을 절감하고 대역폭을 늘릴
수 있습니다. 그러나 이 솔루션은 온프레미스에 필요한 스토리지 용량을 줄이지 않으며
클라우드 스토리지의 이점을 활용하지도 않습니다.

---

# Q680 

**정답: C**

설명:
다음 테스트 단계에서 애플리케이션 시작 시간을 줄이는 솔루션은 최대 절전 모드가 설정된
EC2 온디맨드 인스턴스를 시작하고 EC2 Auto Scaling 웜 풀을 구성하는 것입니다. 이
솔루션을 사용하면 애플리케이션을 처음부터 시작하는 대신 최대 절전 모드에서 다시
시작할 수 있으므로 시간과 리소스를 절약할 수 있습니다. 최대 절전 모드는 EC2
인스턴스의 메모리(RAM) 상태를 루트 EBS 볼륨에 유지한 다음 인스턴스를 중지합니다.
인스턴스가 재개되면 EBS 볼륨에서 메모리 상태를 복원하고 빠르게 생산성을 발휘합니다.
EC2 Auto Scaling 웜 풀은 필요할 때 확장할 준비가 되어 있는 사전 초기화된 인스턴스
풀을 유지하는 데 사용할 수 있습니다. Warm 풀은 최대 절전 모드 인스턴스를 지원할 수도
있으므로 시작 시간과 확장 비용을 더욱 줄일 수 있습니다.
다른 솔루션은 시작 시간을 단축하지 않거나, 가용성을 보장하지 않거나, 필요에 따라
온디맨드 인스턴스를 사용하지 않기 때문에 첫 번째 솔루션만큼 효과적이지 않습니다.
Auto Scaling 기능이 있는 두 개 이상의 EC2 온디맨드 인스턴스를 시작해도 각 인스턴스가
여전히 초기화 프로세스를 거쳐야 하므로 애플리케이션의 시작 시간이 줄어들지 않습니다.
EC2 스팟 인스턴스를 시작한다고 해서 가용성이 보장되는 것은 아닙니다. 용량에 대한
수요가 높아지면 언제든지 AWS 가 스팟 인스턴스를 중단할 수 있기 때문입니다. 용량
예약을 통해 EC2 온디맨드 인스턴스를 시작하면 인스턴스에 사용할 수 있는 용량이
충분한지 확인만 할 뿐 사전 초기화는 하지 않으므로 애플리케이션 시작 시간이 줄어들지
않습니다.

---

# Q681 

**정답: D**

설명:
보안 요구 사항을 충족하려면 솔루션 아키텍트는 AWS 에서 제공하는 루트 인증서를
다운로드하고 RDS 인스턴스에 대한 모든 연결에 인증서를 제공해야 합니다. 이렇게 하면
애플리케이션과 RDS 인스턴스 간에 전송되는 데이터에 대해 SSL/TLS 암호화가
활성화됩니다.
SSL/TLS 암호화는 클라이언트와 서버 간에 이동하는 데이터를 암호화하여 보안 계층을
제공합니다. Amazon RDS 는 SSL 인증서를 생성하고 인스턴스가 프로비저닝되면 DB
인스턴스에 인증서를 설치합니다. 애플리케이션은 AWS 가 제공한 루트 인증서를 사용하여
DB 인스턴스의 신원을 확인하고 보안 연결을 설정할 수 있습니다.
다른 옵션은 전송 중인 데이터에 대한 암호화를 활성화하지 않거나 사용 사례와 관련이
없기 때문에 올바르지 않습니다. 데이터베이스에서 IAM 데이터베이스 인증을 활성화하는
것은 올바르지 않습니다. 이 옵션은 암호화가 아닌 인증 방법만 제공하기 때문입니다. IAM
데이터베이스 인증을 통해 사용자는 데이터베이스 사용자 이름과 암호를 사용하는 대신
AWS Identity and Access Management(IAM) 사용자 및 역할을 사용하여 데이터베이스에
액세스할 수 있습니다. 이 옵션은 안전하지 않거나 신뢰할 수 없기 때문에 자체 서명된
인증서를 제공하는 것은 올바르지 않습니다. 자체 서명 인증서는 신뢰할 수 있는 인증
기관(CA)이 아닌 이를 발급한 동일한 엔터티에 의해 서명된 인증서입니다. 자체 서명된
인증서는 쉽게 위조되거나 손상될 수 있으며 대부분의 브라우저 및 애플리케이션에서
인식되지 않습니다.
RDS 인스턴스의 스냅샷을 찍어 암호화가 활성화된 새 인스턴스로 복원하는 것은 올바르지
않습니다. 이 옵션은 전송 중 암호화가 아닌 유휴 암호화만 활성화하기 때문입니다. 미사용
암호화는 디스크에 저장된 데이터를 보호하지만 클라이언트와 서버 간에 이동하는 데이터는
보호하지 않습니다.

---

# Q682 

**정답: D**

설명:
데이터 계층의 성능을 향상시키는 솔루션은 기존 DB 인스턴스 앞에 Redis 용 Amazon
ElastiCache 클러스터를 배포하고 Redis를 사용하도록 게임을 수정하는 것입니다. Redis는
지리공간 데이터 유형과 명령을 지원하는 메모리 내 데이터 저장소이므로 이 솔루션을
사용하면 게임에서 빠르고 확장 가능한 방식으로 플레이어의 위치 데이터를 저장하고
검색할 수 있습니다. Redis 용 ElastiCache 를 사용하면 게임에서 빈도가 높은 업데이트 및
위치 데이터 쿼리에 최적화되지 않은 PostgreSQL DB 인스턴스용 RDS 의 로드를 줄일 수
있습니다. Redis 용 ElastiCache 는 증가하는 게임 사용자 기반을 처리하기 위해 복제, 샤딩
및 자동 크기 조정도 지원합니다.
다른 솔루션은 성능을 향상시키지 않거나 지리공간 데이터를 지원하지 않거나 캐싱을
활용하지 않기 때문에 첫 번째 솔루션만큼 효과적이지 않습니다. 기존 DB 인스턴스의
스냅샷을 생성하고 다중 AZ 가 활성화된 상태로 복원하면 데이터 계층의 성능이 향상되지
않습니다. 이는 높은 가용성과 내구성만 제공할 뿐 확장성이나 짧은 지연 시간은 제공하지
않기 때문입니다. OpenSearch Dashboards 를 사용하여 Amazon RDS 에서 Amazon
OpenSearch Service 로 마이그레이션해도 데이터 계층의 성능은 향상되지 않습니다.
OpenSearch Service 는 주로 실시간 위치 추적이 아닌 전체 텍스트 검색 및 분석을 위해
설계되었기 때문입니다. OpenSearch 서비스는 Redis 와 달리 기본적으로 지리공간 데이터
유형 및 명령을 지원하지 않습니다. 기존 DB 인스턴스 앞에 Amazon DynamoDB
Accelerator(DAX)를 배포하고 DAX 를 사용하도록 게임을 수정해도 데이터 계층의 성능은
향상되지 않습니다. 왜냐하면 DAX 는 PostgreSQL 용 RDS 가 아닌 DynamoDB 하고만
호환되기 때문입니다. DAX는 지리공간 데이터 유형 및 명령도 지원하지 않습니다.

---

# Q683 

**정답: B**

설명:
회사의 규정 준수 정책에 가장 적합한 솔루션은 제한된 SSH AWS Config 관리형 규칙을
활성화하고 비준수 규칙이 생성될 때 Amazon Simple 알림 서비스(Amazon SNS) 알림을
생성하는 것입니다. 이 솔루션은 사용자가 AWS 리소스의 구성을 평가, 감사 및 평가할 수
있는 서비스인 AWS Config 에서 이미 사용 가능한 사전 정의된 규칙을 사용하기 때문에
운영 오버헤드가 가장 적습니다. 제한된 SSH 규칙은 사용 중인 보안 그룹에 0.0.0.0/0
주소에서 SSH를 허용하는 인바운드 규칙이 있는지 확인하고 이를 비준수로 보고합니다.
사용자는 규정을 준수하지 않는 변경 사항이 발생할 때 Amazon SNS 주제에 알림을
보내도록 규칙을 구성하고 주제를 구독하여 이메일, SMS 또는 기타 방법을 통해 알림을
받을 수 있습니다.
다른 옵션은 운영 오버헤드가 더 많거나 요구 사항을 충족하지 않기 때문에 올바르지
않습니다. 0.0.0.0/0 주소에 열려 있는 SSH 에 대한 보안 그룹을 모니터링하고 잘못된
주소를 발견할 때마다 알림을 생성하는 AWS Lambda 스크립트를 작성하려면 사용자 지정
코드 개발 및 유지 관리가 필요하므로 솔루션에 복잡성과 비용이 추가됩니다. 전역적으로
보안 그룹 및 네트워크 ACL 을 열 수 있는 권한이 있는 IAM 역할을 생성하고 사용자가
역할을 맡을 때마다 알림을 생성하는 Amazon SNS 주제를 생성하는 것은 올바르지
않습니다. 이는 비준수 규칙 생성을 방지하거나 감지하지 못하기 때문입니다. 다른 사용자
또는 역할과 관련이 있으며 정책을 위반할 수 있는 기존 규칙을 다루지 않습니다. 관리자가
아닌 사용자가 보안 그룹을 생성하거나 편집하는 것을 방지하는 서비스 제어 정책(SCP)을
구성하고, 사용자가 관리자 권한이 필요한 규칙을 요청할 때 티켓팅 시스템에서 알림을
생성하는 것은 자동화된 솔루션을 제공하지 않기 때문에 올바르지 않습니다. 정책 집행 및
통지를 위해 사용자의 유연성과 생산성을 제한할 수 있습니다.

---

# Q684 

**정답: D**

설명:
고가용성, 성능, 보안 및 고정 IP 주소 요구 사항을 충족하는 솔루션은 Amazon CloudFront,
ALB(Application Load Balancer), Amazon Route 53 및 AWS WAF를 사용하는 것입니다. 이
솔루션을 통해 회사는 엣지 로케이션에 콘텐츠를 캐시하고 각 엣지 로케이션에 고정 IP
주소를 제공하는 CDN(콘텐츠 전송 네트워크) 서비스인 CloudFront 를 사용하여 HTTP 기반
애플리케이션을 전 세계적으로 배포할 수 있습니다. 또한 회사는 Route 53 지연 시간 기반
라우팅을 사용하여 각 지역에서 가장 가까운 ALB 로 요청을 라우팅하여 EC2 인스턴스
전체에 로드 균형을 맞출 수 있습니다. 또한 회사는 정의된 조건에 따라 웹 요청을 허용,
차단 또는 계산하는 규칙을 생성하여 일반적인 웹 공격으로부터 애플리케이션을 보호하기
위해 CloudFront 배포에 AWS WAF 를 배포할 수도 있습니다. 다른 솔루션은 HTTP 기반
애플리케이션을 지원하지 않는 NLB(Network Load Balancer)를 사용하거나 AWS Global
Accelerator 보다 더 나은 성능과 보안을 제공하는 CloudFront 를 사용하지 않기 때문에
모든 요구 사항을 충족하지 못합니다.

---

# Q685 

**정답: C**

설명:
온라인 비디오 게임 회사를 위한 가장 비용 효율적인 솔루션은 인터넷 트래픽에 필요한
프로토콜과 포트로 Network Load Balancer를 구성하고 EC2 인스턴스를 대상으로 지정하는
것입니다. 이 솔루션을 통해 회사는 매우 짧은 대기 시간과 고성능으로 초당 수백만 개의
UDP 요청을 처리할 수 있습니다.
Network Load Balancer는 연결 수준(계층 4)에서 작동하고 IP 프로토콜 데이터를 기반으로
Amazon VPC 내의 대상(EC2 인스턴스, 마이크로서비스 또는 컨테이너)으로 트래픽을
라우팅하는 Elastic Load Balancing의 한 유형입니다. Network Load Balancer는 매우 짧은
대기 시간으로 높은 처리량을 유지하면서 초당 수백만 개의 요청을 처리할 수 있으므로
TCP 및 UDP 트래픽의 로드 밸런싱에 이상적입니다. 또한 Network Load Balancer 는
백엔드 애플리케이션에 대한 클라이언트의 소스 IP 주소를 보존하므로 로깅이나 보안
목적으로 유용할 수 있습니다.

---

# Q686 

**정답: B**

설명:
요구 사항을 충족하는 솔루션은 Amazon Rekognition 을 사용하여 원치 않는 콘텐츠를
감지하는 AWS Lambda 함수를 생성하고 새 사진이 업로드될 때 웹 애플리케이션이
호출하는 Lambda 함수 URL 을 생성하는 것입니다. Amazon Rekognition 은 이미지 및
비디오 분석을 위해 사전 훈련된 컴퓨터 비전 모델을 제공하는 완전 관리형 서비스이므로
이 솔루션에는 기계 학습 모델 훈련이 포함되지 않습니다. Amazon Rekognition 은
노골적이거나 외설적인 성인 콘텐츠, 폭력, 무기, 마약 등과 같은 원치 않는 콘텐츠를
탐지할 수 있습니다. AWS Lambda 를 사용하여 회사는 웹 애플리케이션의 HTTP 요청에
의해 트리거될 수 있는 서버리스 기능을 생성할 수 있습니다. Lambda 함수는 Amazon
Rekognition API 를 사용하여 업로드된 사진을 분석하고 원치 않는 콘텐츠가 포함되어
있는지 여부를 나타내는 응답을 반환할 수 있습니다.
다른 솔루션은 기계 학습 모델 교육이 포함되거나 이미지 분석을 지원하지 않거나 사진
작업을 수행하지 않기 때문에 첫 번째 솔루션만큼 효과적이지 않습니다. Amazon
SageMaker Autopilot 을 사용하여 모델을 생성하고 배포하려면 기계 학습 모델을 훈련해야
하는데, 이는 시나리오에 필요하지 않습니다. Amazon SageMaker Autopilot 은 사용자가
제공한 데이터를 기반으로 분류 또는 회귀를 위한 최고의 기계 학습 모델을 자동으로 생성,
교육 및 조정하는 서비스입니다. Amazon Comprehend 를 사용하여 원치 않는 콘텐츠를
감지하는 Amazon CloudFront 함수를 생성하면 이미지 분석이 지원되지 않습니다. Amazon
Comprehend 는 이미지가 아닌 텍스트를 분석하는 자연어 처리 서비스이기 때문입니다.
Amazon Comprehend 는 언어, 감정, 항목, 주제 등과 같은 텍스트에서 통찰력과 관계를
추출할 수 있습니다. Amazon Rekognition Video 를 사용하여 원치 않는 콘텐츠를 감지하는
AWS Lambda 함수를 생성하는 것은 사진에서는 작동하지 않습니다. Amazon Rekognition
Video 는 정적 이미지가 아닌 비디오 스트림을 분석하도록 설계되었기 때문입니다. Amazon
Rekognition Video 는 비디오 스트림에서 활동, 객체, 얼굴, 유명인, 텍스트 등을 감지할 수
있습니다.

---

# Q687 

**정답: C**

설명:
회사의 애플리케이션에 가장 적합한 디자인 변경은 테이블에 대해 강력하고 일관된 읽기를
요청하는 것입니다. 이렇게 변경하면 테이블에 대한 요청이 모든 이전 쓰기 작업의
업데이트를 반영하여 최신 데이터를 반환하게 됩니다.
Amazon DynamoDB 는 원활한 확장성과 함께 빠르고 예측 가능한 성능을 제공하는 완전
관리형 NoSQL 데이터베이스 서비스입니다. DynamoDB 는 최종적 일관된 읽기와 강력한
일관된 읽기라는 두 가지 유형의 읽기 일관성을 지원합니다. 기본적으로 DynamoDB 는
사용자가 달리 지정하지 않는 한 최종적 일관된 읽기를 사용합니다.
최종 일관성 읽기는 최근 완료된 쓰기 작업의 결과를 반영하지 않을 수 있는 읽기입니다.
모든 복제본에 데이터를 전파하는 데 지연이 발생하기 때문에 응답에 변경 사항이 포함되지
않을 수 있습니다. 사용자가 잠시 후에 읽기 요청을 반복하면 응답은 업데이트된 데이터를
반환해야 합니다. 최종 일관성 읽기는 최신 데이터가 필요하지 않거나 최종 일관성을
허용할 수 있는 애플리케이션에 적합합니다. Strongly Consistency 읽기는 읽기 전에
성공적인 응답을 받은 모든 쓰기를 반영하는 결과를 반환하는 읽기입니다. 사용자는
GetItem, Query 또는 Scan 과 같은 읽기 작업에서 ConsistencyRead 매개 변수를 true 로
설정하여 강력한 일관된 읽기를 요청할 수 있습니다. 강력한 일관된 읽기는 최신 데이터가
필요하거나 최종 일관성을 허용할 수 없는 애플리케이션에 적합합니다.
다른 옵션은 읽기 일관성 문제를 해결하지 않거나 사용 사례와 관련이 없기 때문에
올바르지 않습니다. 이 옵션은 DynamoDB 에서 지원되지 않으므로 테이블에 읽기 전용
복제본을 추가하는 것은 올바르지 않습니다. 읽기 복제본은 읽기 전용 트래픽을 제공하고
가용성과 성능을 향상시킬 수 있는 기본 데이터베이스 인스턴스의 복사본입니다. 읽기 전용
복제본은 Amazon RDS 또는 Amazon Aurora 와 같은 일부 관계형 데이터베이스 서비스에
사용할 수 있지만 DynamoDB2 에는 사용할 수 없습니다. GSI(Global Secondary Index)를
사용하는 것은 올바르지 않습니다. 이 옵션은 읽기 일관성과 관련이 없기 때문입니다.
GSI 는 기본 테이블의 것과 다른 파티션 키와 선택적 정렬 키가 있는 인덱스입니다. GSI 를
사용하면 사용자는 최종 일관성을 유지하면서 다양한 방식으로 데이터를 쿼리할 수
있습니다. 테이블에 대한 최종적 일관된 읽기 요청은 올바르지 않습니다. 이 옵션은 이미
DynamoDB 의 기본 동작이고 최신 데이터를 반환하지 않는 요청 문제를 해결하지 못하기
때문입니다.

---

# Q688 

**정답: C**

설명:
회사의 요구 사항에 가장 적합한 솔루션은 DataBrew 레시피를 사용하여 데이터를 변환하고
변환 단계를 직원과 공유하도록 AWS Glue DataBrew 를 구성하는 것입니다. 이 솔루션은
코드가 필요하지 않은 데이터 변환을 위해 사전 구축된 솔루션을 제공하고 데이터 계보 및
데이터 프로파일링도 제공합니다. 회사는 DataBrew 레시피를 사용하여 회사 전체의 직원과
데이터 변환 단계를 쉽게 공유할 수 있습니다.
AWS Glue DataBrew 는 데이터 분석가와 데이터 과학자가 분석 또는 기계 학습을 위해
데이터를 최대 80% 더 빠르게 정리하고 정규화할 수 있게 해주는 시각적 데이터 준비
도구입니다. 사용자는 Amazon S3, Amazon RDS, Amazon Redshift, Amazon Aurora 또는
Glue Data Catalog 와 같은 다양한 소스에서 데이터를 업로드하고 포인트 앤 클릭
인터페이스를 사용하여 250 개 이상의 기본 제공 변환을 적용할 수 있습니다. 사용자는 각
변환 단계의 결과를 미리 보고 이것이 데이터의 품질과 분포에 어떤 영향을 미치는지
확인할 수도 있습니다.
DataBrew 레시피는 하나 이상의 데이터세트에 적용할 수 있는 재사용 가능한 변환 단계
세트입니다. 사용자는 처음부터 레시피를 생성하거나 DataBrew 레시피 라이브러리의 기존
레시피를 사용할 수 있습니다. 사용자는 또한 AWS 계정 또는 조직 내의 다른 사용자 또는
그룹과 레시피를 내보내거나 가져오거나 공유할 수도 있습니다.
DataBrew 는 또한 사용자가 데이터 품질을 이해하고 개선하는 데 도움이 되는 데이터 계보
및 데이터 프로파일링 기능을 제공합니다. 데이터 계보는 각 데이터세트의 소스와 대상,
그리고 각 레시피 단계에서 데이터가 변환되는 방식을 보여줍니다. 데이터 프로파일링은
열과 같은 각 데이터세트에 대한 다양한 통계 및 측정항목을 표시합니다.

---

# Q689 

**정답: A**

설명:
가장 안전한 방식으로 웹 애플리케이션의 요구 사항을 충족하려면 회사는 Route 53
Resolver 아웃바운드 엔드포인트를 생성하고, 확인자 규칙을 생성하고, 확인자 규칙을
VPC 와 연결해야 합니다. 이 솔루션을 사용하면 애플리케이션이 프라이빗 DNS 레코드를
사용하여 VPC 의 온프레미스 서비스와 통신할 수 있습니다. Route 53 Resolver 는
온프레미스 네트워크와 AWS VPC 간의 DNS 확인을 가능하게 하는 서비스입니다.
아웃바운드 엔드포인트는 확인자가 VPC 에서 온프레미스 네트워크의 확인자로 DNS 쿼리를
전달하는 데 사용하는 IP 주소 집합입니다. 확인자 규칙은 확인자가 규칙에 지정한 IP
주소로 DNS 쿼리를 전달하는 도메인 이름을 지정하는 규칙입니다. 아웃바운드
엔드포인트와 확인자 규칙을 생성하고 이를 VPC 와 연결함으로써 회사는 프라이빗 DNS
레코드를 사용하여 온프레미스 서비스에 대한 DNS 쿼리를 안전하게 확인할 수 있습니다.
다른 옵션은 요구 사항을 충족하지 않거나 안전하지 않기 때문에 올바르지 않습니다. Route
53 Resolver 인바운드 엔드포인트 생성, 해석기 규칙 생성 및 해석기 규칙을 VPC 와
연결하는 것은 올바르지 않습니다. 왜냐하면 이 솔루션은 온프레미스 네트워크의 DNS
쿼리가 VPC 의 리소스에 액세스하도록 허용하고 그 반대의 경우는 허용하지 않기
때문입니다. 인바운드 엔드포인트는 확인자가 온프레미스 네트워크의 확인자로부터 DNS
쿼리를 수신하는 데 사용하는 IP 주소 집합입니다. Route 53 프라이빗 호스팅 영역을
생성하고 이를 VPC 와 연결하는 것은 올바르지 않습니다. 이 솔루션은 동일한 호스팅
영역과 연결된 VPC 또는 다른 VPC 내의 리소스에 대해서만 DNS 확인을 허용하기
때문입니다.
프라이빗 호스팅 영역은 하나 이상의 VPC 에서만 액세스할 수 있는 DNS 레코드의
컨테이너입니다. Route 53 퍼블릭 호스팅 영역을 생성하고 서비스 통신을 허용하기 위해 각
서비스에 대한 레코드를 생성하는 것은 올바르지 않습니다. 이 솔루션은 온프레미스
서비스를 안전하지 않은 퍼블릭 인터넷에 노출시키기 때문입니다. 퍼블릭 호스팅 영역은
인터넷 어디에서나 액세스할 수 있는 DNS 레코드의 컨테이너입니다.

---

# Q690 

**정답: C**

설명:
임의 IP 주소에서 발생하는 DDoS 공격으로부터 웹 애플리케이션을 보호하려면 솔루션
아키텍트가 AWS Shield Advanced를 구독하고 AWS DDoS 대응 팀(DRT)과 협력하여 완화
제어 기능을 서비스에 통합해야 합니다. AWS Shield Advanced는 DRT의 연중무휴 지원 및
대응을 통해 대규모의 정교한 DDoS 공격에 대한 보호를 제공하는 관리형 서비스입니다.
DRT 는 도시에서 AWS WAF 규칙, 속도 기반 규칙 및 네트워크 ACL 과 같은 사전 및 사후
보호 장치를 구성하여 악성 트래픽을 차단하고 애플리케이션의 복원력을 향상시키는 데
도움을 줄 수 있습니다.
또한 이 서비스는 자세한 공격 보고서와 Amazon CloudWatch 지표를 통해 DDoS 소스에
대한 감사 추적을 제공합니다.

---

# Q691 

**정답: B**

설명:
Amazon EFS 는 여러 컨테이너 간에 공유할 수 있는 탄력적이고 확장 가능한 완전관리형
파일 시스템입니다. 여러 가용 영역에 걸쳐 데이터를 복제하여 고가용성과 내결함성을
제공합니다. Amazon EFS 는 Amazon EKS 및 AWS Fargate 와 호환되며 EKS 클러스터의
StorageClass 객체에 등록할 수 있습니다. Amazon EBS 볼륨은 AWS Fargate에서 지원되지
않으며 EBS 다중 연결을 사용하지 않고는 여러 컨테이너 간에 공유할 수 없습니다. 이는
제한 사항과 성능에 영향을 미칩니다. 또한 EBS 다중 연결에서는 볼륨이 작업자 노드와
동일한 가용 영역에 있어야 하므로 가용성과 내결함성이 줄어듭니다. AWS Lambda 를
사용하여 여러 EFS 파일 시스템 간에 데이터를 동기화하는 것은 불필요하고 복잡하며
오류가 발생하기 쉽습니다.

---

# Q692 

**정답: C**

설명:
최소한의 운영 오버헤드로 요구 사항을 충족하는 솔루션은 웹 계층을 퍼블릭 서브넷의
Amazon EC2 인스턴스로 마이그레이션하고, 애플리케이션 계층을 프라이빗 서브넷의 EC2
인스턴스로 마이그레이션하고, 데이터베이스 계층을 프라이빗 서브넷의 Amazon RDS for
MySQL 로 마이그레이션하는 것입니다. 이 솔루션을 사용하면 회사는 동일한 웹,
애플리케이션 및 데이터베이스 계층을 유지하고 동일한 MySQL 데이터베이스 엔진을
사용하므로 아키텍처를 최소한으로 변경하여 3계층 애플리케이션을 AWS로 마이그레이션할
수 있습니다. 또한 이 솔루션은 Amazon RDS for MySQL이 자동 백업 및 특정 시점 복구를
지원하므로 데이터를 특정 시점으로 복원할 수 있는 데이터베이스 솔루션도 제공합니다.
또한 이 솔루션은 프로비저닝, 패치, 확장, 모니터링과 같은 작업을 처리하는 Amazon EC2
및 Amazon RDS와 같은 관리형 서비스를 사용하여 운영 오버헤드를 줄입니다.
다른 솔루션은 아키텍처에 더 많은 변경이 필요하거나 특정 시점 복구를 제공하지 않거나
보안 및 가용성에 대한 모범 사례를 따르지 않기 때문에 첫 번째 솔루션과 마찬가지로 요구
사항을 충족하지 않습니다. 데이터베이스 계층을 Amazon Aurora MySQL 로
마이그레이션하려면 데이터베이스 엔진을 변경하고 잠재적으로 호환성을 보장하기 위해
애플리케이션 코드를 수정해야 합니다. 웹 계층과 애플리케이션 계층을 퍼블릭 서브넷으로
마이그레이션하면 더 많은 보안 위험에 노출되고 서브넷 오류가 발생할 경우 가용성이
줄어듭니다. 데이터베이스 계층을 퍼블릭 서브넷으로 마이그레이션하면 보안과 성능이
손상될 수도 있습니다.

---

# Q693 

**정답: B**

설명:
콘텐츠 업로드에 대한 지연 시간을 최소화하여 사용자 경험을 최적화하는 가장 적합한
솔루션은 Amazon S3에 콘텐츠를 업로드 및 저장하고 업로드에 S3 Transfer Acceleration을
사용하는 것입니다. 이 솔루션을 통해 회사는 AWS 글로벌 네트워크와 엣지 로케이션을
활용하여 사용자와 S3 버킷 간의 데이터 전송 속도를 높일 수 있습니다.
Amazon S3는 모든 유형의 데이터에 대해 확장 가능하고 내구성이 뛰어나며 가용성이 높은
객체 스토리지를 제공하는 스토리지 서비스입니다. Amazon S3 를 사용하면 사용자는 웹
어디에서나 데이터를 저장하고 검색할 수 있으며 암호화, 버전 관리, 수명 주기 관리 및
복제와 같은 다양한 기능을 제공합니다.
S3 Transfer Acceleration 은 사용자가 S3 버킷과 더 빠르게 데이터를 주고받는 데 도움이
되는 Amazon S3 의 기능입니다. S3 Transfer Acceleration 은 최적화된 네트워크 경로와
Amazon의 백본 네트워크를 사용하여 데이터 전송 속도를 가속화하는 방식으로 작동합니다.
사용자는 버킷에 대해 S3 Transfer Acceleration 을 활성화하고
<bucket>.s3-accelerate.amazonaws.com 과 같은 고유한 URL 을 사용하여 버킷에
액세스할 수 있습니다.
다른 옵션은 가장 낮은 대기 시간을 제공하지 않거나 사용 사례에 적합하지 않기 때문에
올바르지 않습니다. Amazon S3 에 콘텐츠를 업로드 및 저장하고 업로드에 Amazon
CloudFront 를 사용하는 것은 올바르지 않습니다. 이 솔루션은 업로드 최적화가 아니라
다운로드 최적화를 위해 설계되었기 때문입니다. Amazon CloudFront는 사용자가 짧은 지연
시간과 높은 전송 속도로 콘텐츠를 전 세계에 배포할 수 있도록 지원하는 콘텐츠 전송
네트워크(CDN)입니다. CloudFront 는 전 세계 엣지 로케이션에서 콘텐츠를 캐싱하는
방식으로 작동하므로 사용자는 어디에서나 빠르고 쉽게 콘텐츠에 액세스할 수 있습니다 3.
사용자에게 가장 가까운 지역의 Amazon EC2 인스턴스에 콘텐츠를 업로드하고 Amazon
S3 에 데이터를 복사하는 것은 프로세스에 불필요한 복잡성과 비용을 추가하므로 올바르지
않습니다. Amazon EC2 는 클라우드에서 확장 가능하고 안전한 가상 서버를 제공하는
컴퓨팅 서비스입니다. 사용자는 필요에 따라 EC2 인스턴스를 시작, 중지 또는 종료할 수
있으며 다양한 인스턴스 유형, 운영 체제 및 구성 중에서 선택할 수 있습니다4. 사용자에게
가장 가까운 지역의 Amazon S3 에 콘텐츠를 업로드하고 저장하며 Amazon CloudFront 의
여러 배포를 사용하는 것은 사용 사례에 비해 비용 효율적이거나 효율적이지 않기 때문에
올바르지 않습니다. 위에서 언급했듯이 Amazon CloudFront 는 사용자가 짧은 지연 시간과
높은 전송 속도로 콘텐츠를 전 세계에 배포할 수 있도록 지원하는 CDN 입니다. 그러나 각
지역에 대해 여러 CloudFront 배포를 생성하면 추가 비용과 관리 오버헤드가 발생하고
콘텐츠의 90%가 업로드된 동일한 지역 내에서 소비되므로 필요하지 않습니다.

---

# Q694 

**정답: B**

설명:
AWS DataSync 는 온프레미스 스토리지와 AWS 스토리지 서비스 간에 대량의 데이터를
온라인으로 쉽게 이동할 수 있게 해주는 서비스입니다. AWS DataSync 는 특별히 구축된
네트워크 프로토콜을 사용하고 데이터 전송을 병렬화하여 오픈 소스 도구보다 최대 10 배
빠른 속도로 데이터를 전송할 수 있습니다. AWS DataSync 는 암호화, 데이터 무결성 확인
및 대역폭 최적화도 처리합니다. AWS DataSync 를 사용하려면 사용자는 NFS 서버에
연결하고 데이터를 Amazon S3 에 동기화하는 온프레미스 서버에 DataSync 에이전트를
배포해야 합니다. 사용자는 정기적 또는 일회성 동기화 작업을 예약하고 전송 진행 상황과
상태를 모니터링할 수 있습니다.
다른 옵션은 비용 효율적이지 않거나 사용 사례에 적합하지 않기 때문에 올바르지 않습니다.
온프레미스 서버에서 Amazon S3로 데이터를 복사하도록 AWS Glue를 설정하는 것은 비용
효율적이지 않습니다. AWS Glue는 단순 작업이 아닌 추출, 변환 및 로드(ETL) 작업에 주로
사용되는 서버리스 데이터 통합 서비스이기 때문입니다. 데이터 백업. 온프레미스에서
Amazon S3 로 데이터를 동기화하기 위해 AWS Transfer for SFTP 를 사용하여 SFTP
동기화를 설정하는 것은 비용 효율적이지 않습니다. 왜냐하면 AWS Transfer for SFTP 는
교환에 더 적합한 SFTP 프로토콜을 사용하여 안전한 파일 전송을 제공하는 완전관리형
서비스이기 때문입니다. 데이터를 백업하는 것보다 제3자에게 데이터를 제공하는 것입니다.
온프레미스 데이터 센터와 VPC 간에 AWS Direct Connect 연결을 설정하고 Amazon S3에
데이터를 복사하는 것은 비용 효율적이지 않습니다. 왜냐하면 AWS Direct Connect 는
AWS 와 온프레미스 위치 간의 전용 네트워크 연결이기 때문입니다. 초기 비용이 높고 추가
구성이 필요합니다.

---

# Q695 

**정답: B**

설명:
예측 가능한 데이터베이스 성능을 유지하고 Lambda 호출이 너무 많은 연결로 인해
데이터베이스에 과부하를 주지 않도록 하려면 솔루션 설계자는 RDS 프록시
엔드포인트에서 클라이언트 드라이버를 가리키고 VPC 내부에 Lambda 함수를 배포해야
합니다. RDS 프록시는 애플리케이션이 데이터베이스에 대한 연결을 공유할 수 있도록 하여
데이터베이스 가용성과 확장성을 향상시키는 완전 관리형 데이터베이스 프록시입니다. RDS
프록시를 사용하면 Lambda 함수는 호출할 때마다 새 연결을 생성하는 대신 기존 연결을
재사용하여 연결 오버헤드와 지연 시간을 줄일 수 있습니다. VPC 내부에 Lambda 함수를
배포하면 퍼블릭 인터넷에 노출하지 않고도 프라이빗 RDS DB 인스턴스에 안전하고
효율적으로 액세스할 수 있습니다. 참조:
AWS Lambda 와 함께 Amazon RDS 프록시 사용 VPC 의 리소스에 액세스하도록 Lambda
함수를 구성합니다.

---

# Q696 

**정답: A**

설명:
요구 사항을 충족하는 솔루션은 데이터 수집을 위한 Amazon Kinesis 데이터 스트림을
생성하고, Kinesis 데이터 스트림을 사용하기 위한 Amazon Kinesis Data Firehose 전송
스트림을 생성하고, S3 버킷을 전송 스트림의 대상으로 지정하는 것입니다.
이 솔루션을 사용하면 회사의 애플리케이션이 타사 애플리케이션에서 실시간 데이터를
수집하고 수집된 원시 데이터를 S3 버킷에 배치할 수 있습니다. Amazon Kinesis 데이터
스트림은 수십만 개의 소스에서 데이터를 캡처하고 저장할 수 있는 확장 가능하고 내구성이
뛰어난 스트림입니다. Amazon Kinesis Data Firehose 는 스트리밍 데이터를 S3, Amazon
Redshift, Amazon OpenSearch Service 및 Splunk 와 같은 대상으로 전달할 수 있는
완전관리형 서비스입니다. Amazon Kinesis Data Firehose는 데이터를 S3에 전달하기 전에
변환하고 압축할 수도 있습니다.
다른 솔루션은 실시간 데이터 수집을 지원하지 않거나, 타사 애플리케이션과 작동하지
않거나, S3 를 대상으로 사용하지 않기 때문에 첫 번째 솔루션만큼 효과적이지 않습니다.
AWS Database Migration Service(AWS DMS)에서 데이터베이스 마이그레이션 작업을
생성하면 실시간 데이터 수집이 지원되지 않습니다. AWS DMS 는 주로 스트리밍 데이터가
아닌 관계형 데이터베이스 마이그레이션을 위해 설계되었기 때문입니다. 또한 AWS
DMS 에서는 복제 인스턴스, 소스 엔드포인트 및 대상 엔드포인트가 특정 데이터베이스
엔진 및 버전과 호환되어야 합니다. AWS DataSync 는 애플리케이션 간이 아닌 온프레미스
스토리지 시스템과 AWS 스토리지 서비스 간에 데이터를 전송하는 서비스이므로 EC2
인스턴스에서 AWS DataSync 에이전트를 생성하고 구성하는 것은 타사 애플리케이션에서
작동하지 않습니다. 또한 AWS DataSync 에서는 소스 또는 대상 서버에 에이전트를
설치해야 합니다. 데이터 수집을 위해 애플리케이션에 대한 AWS Direct Connect 연결을
생성하면 S3 가 대상으로 사용되지 않습니다. AWS Direct Connect 는 애플리케이션과
스토리지 서비스 간이 아니라 온프레미스와 AWS 간에 전용 네트워크 연결을 설정하는
서비스이기 때문입니다.
AWS Direct Connect 를 사용하려면 AWS Direct Connect 위치에 대한 물리적 연결도
필요합니다.

---

# Q697 

**정답: A**

설명:
옵션 A 는 애플리케이션 코드를 크게 변경하지 않고도 복제 지연을 줄이고 지속적인 운영
오버헤드를 최소화하는 데 가장 적합한 솔루션입니다. 데이터베이스를 Amazon Aurora
MySQL 로 마이그레이션하면 Amazon RDS for MySQL 에 비해 복제 성능이 향상되고
확장성이 높아집니다. Aurora 복제본은 더 빠른 복제를 제공하여 복제 지연을 줄이고,
Aurora Auto Scaling 은 들어오는 트래픽을 처리하기에 충분한 Aurora 복제본이 있는지
확인합니다. 또한 Aurora MySQL 기본 기능은 저장 프로시저를 대체하여 데이터베이스의
로드를 줄이고 성능을 향상시킬 수 있습니다.

---

# Q698 

**정답: A**

설명:
가장 운영 효율성이 뛰어나며 요구 사항을 충족하는 솔루션은 기존 VPC 에 퍼블릭
서브넷을 구성하고 퍼블릭 서브넷에 MSK 클러스터를 배포하는 것입니다. 이 솔루션을
사용하면 새 VPC 를 생성하거나 로드 밸런서를 배포하지 않고도 인터넷을 통해 데이터
수집 솔루션을 공개적으로 사용할 수 있습니다. 또한 이 솔루션은 상호 TLS 인증을
활성화하여 전송 중인 데이터가 암호화되도록 보장합니다. 이를 위해서는 클라이언트와
서버 모두 확인을 위해 인증서를 제시해야 합니다. 이 솔루션은 Apache Kafka 2.6.0 이상
버전을 실행하는 클러스터에서 사용할 수 있는 Amazon MSK 의 퍼블릭 액세스 기능을
활용합니다.
다른 솔루션은 불필요한 리소스를 생성하거나 전송 중인 데이터를 암호화하지 않기 때문에
첫 번째 솔루션만큼 효율적이지 않습니다. 퍼블릭 서브넷이 있는 새 VPC 를 생성하면
네트워크 리소스 및 라우팅 관리에 추가 비용과 복잡성이 발생합니다. ALB 또는 NLB 를
배포하면 데이터 수집 솔루션에 더 많은 비용과 대기 시간이 추가됩니다. 또한 ALB 또는
NLB 는 추가 단계와 유지 관리가 필요한 HTTPS 리스너 및 인증서로 구성되지 않는 한
전송 중인 데이터를 자체적으로 암호화하지 않습니다. 따라서 이러한 솔루션은 주어진 요구
사항에 최적이 아닙니다.

---

# Q699 

**정답: B**

설명:
AWS 상태 API 는 AWS Personal Health Dashboard 에 표시되는 AWS 상태 정보에 대한
프로그래밍 방식의 액세스를 제공합니다. API 작업을 사용하여 AWS 서비스 및 리소스에
영향을 미치는 AWS 상태 이벤트에 대한 정보를 얻을 수 있습니다. API 를 사용하여 조직의
상태 기반 통찰력을 활성화하거나 비활성화할 수도 있습니다. 각 배포 시작 시 AWS 상태
API 를 사용하여 AWS 인프라 상태를 확인하고 API 가 문제를 반환하는 경우 모든 새
배포를 일시 중지할 수 있습니다.
참조:
https://docs.aws.amazon.com/health/latest/APIReference/Welcome.html

---

# Q700 

**정답: B**

설명:
Amazon RDS 프록시는 Amazon Relational Database Service(RDS)를 위한 완전 관리형
고가용성 데이터베이스 프록시로, 애플리케이션의 확장성과 데이터베이스 오류에 대한
복원력 및 보안을 더욱 강화합니다. RDS Proxy를 사용하면 애플리케이션이 데이터베이스와
설정된 연결을 풀링하고 공유할 수 있어 데이터베이스 효율성과 애플리케이션 확장성이
향상됩니다. 또한 RDS Proxy 는 Aurora 및 RDS 데이터베이스의 장애 조치 시간을 최대
66%까지 줄이고 데이터베이스 액세스를 위한 IAM 인증 및 Secrets Manager 통합을
지원합니다. 코드 변경 없이 대부분의 애플리케이션에 대해 RDS Proxy 를 활성화할 수
있습니다.