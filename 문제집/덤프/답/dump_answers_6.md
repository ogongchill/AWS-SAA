# Q501 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109421-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q502 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109420-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명
옵션 C는 웹 사이트 이미지를 모든 EC2 인스턴스에 탑재된 Amazon EFS 파일 시스템으로
이동하는 기능을 제공합니다. Amazon EFS 는 여러 EC2 인스턴스에서 동시에 액세스할 수
있는 확장 가능하고 완벽하게 관리되는 파일 스토리지 솔루션을 제공합니다. 이렇게 하면
모든 인스턴스에서 웹 사이트 이미지에 효율적이고 일관되게 액세스할 수 있으므로 옵션
E 에서 성능이 향상됩니다. Auto Scaling 그룹은 최소 2 개의 인스턴스를 유지 관리하여
비정상 인스턴스를 자동으로 교체하여 복원력을 보장합니다.
또한 웹 사이트에 대해 Amazon CloudFront 배포를 구성하면 최종 사용자에게 더 가까운
엣지 위치에서 콘텐츠를 캐싱하여 지연 시간을 줄이고 콘텐츠 전송을 개선하여 성능을 더욱
향상시킵니다.
따라서 이러한 작업을 결합하면 효율적인 이미지 저장 및 콘텐츠 전달을 통해 웹 사이트의
성능이 향상됩니다.
~~~

---

# Q503 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109595-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명
고객이 자신의 계정에서 필요한 권한이 있는 IAM 역할을 생성하도록 함으로써 회사는 AWS
Identity and Access Management(IAM)를 사용하여 교차 계정 액세스를 설정할 수 있습니다.
신뢰 정책은 회사의 AWS 계정이 일시적으로 고객의 IAM 역할을 맡도록 허용하여 고객
계정 내의 지정된 리소스(EC2 인스턴스 및 CloudWatch 지표)에 대한 액세스 권한을
부여합니다. 이 접근 방식은 회사가 필요한 권한만 요청하고 고객의 장기 액세스 키나
사용자 자격 증명을 요구하지 않기 때문에 최소 권한 원칙을 따릅니다.
~~~

---

# Q504 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109690-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명
AWS Transit Gateway 는 여러 VPC, 온프레미스 네트워크 및 원격 네트워크를 연결하기
위한 확장성이 뛰어난 중앙 집중식 허브입니다. 단일 진입점을 제공하고 필요한 연결 수를
줄임으로써 네트워크 연결을 단순화합니다. 이 시나리오에서 네트워킹 팀의 AWS 계정에
AWS Transit Gateway 를 배포하면 여러 VPC 에서 네트워크 연결을 효율적으로 관리하고
제어할 수 있습니다.
~~~

---

# Q505 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109691-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q506 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109692-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q507 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109608-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q508 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109530-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:・
옵션 B 는 EC2 지원 Amazon 머신 이미지(AMI) 수명 주기 정책을 사용하여 백업
프로세스를 자동화할 것을 제안합니다. 하루에 두 번 실행되도록 정책을 구성하고
uswest-2 리전에 대한 복사본을 지정함으로써 회사는 정기적인 백업이 생성되고 대체
리전에 복사되도록 할 수 있습니다.
옵션 D 는 중앙 집중식 백업 관리 솔루션을 제공하는 AWS Backup 사용을 제안합니다.
태그 값을 기반으로 백업 볼트 및 백업 계획을 생성함으로써 회사는 EC2 인스턴스에 대한
백업 프로세스를 자동화할 수 있습니다.
백업 일정은 하루에 두 번 실행되도록 설정할 수 있으며 복사 대상은 us-west-2 리전으로
정의할 수 있습니다.
두 옵션 모두 백업 프로세스를 자동화하고 백업을 us-west-2 리전에 복사하는 것을
포함하여 재해 발생 시 데이터 복원력을 보장합니다. 이러한 솔루션은 AWS 서비스에서
제공하는 자동화된 백업 및 복사 메커니즘을 활용하여 관리 작업을 최소화합니다.
~~~

---

# Q509 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109531-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명
퍼블릭 서브넷의 첫 번째 항목에서 요청을 거부하고 프라이빗 서브넷에 도달하는 것을
허용하지 마십시오.
이 시나리오에서 보안 감사는 애플리케이션이 소수의 IP 주소로부터 수백만 건의 불법
요청을 수신하고 있음을 보여줍니다. 이 문제를 해결하려면 웹 계층 서브넷에 대한
네트워크 ACL(액세스 제어 목록)을 수정하는 것이 좋습니다. 리소스를 소비하는 IP 주소를
특별히 대상으로 하는 인바운드 거부 규칙을 추가함으로써 네트워크 ACL 은 불법 트래픽이
웹 서버에 도달하기 전에 서브넷 수준에서 차단할 수 있습니다. 이는 웹 계층의 과도한
로드를 완화하고 애플리케이션의 성능을 향상시키는 데 도움이 됩니다.
~~~

---

# Q510 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109708-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명
다른 리전에 있는 피어 VPC 의 보안 그룹을 참조할 수 없습니다. 대신 피어 VPC 의 CIDR
블록을 사용하십시오.
https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-securitygroups.html
~~~

---

# Q511 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109532-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q512 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109709-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q513 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109713-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명
Amazon S3와 AWS Lambda를 함께 사용하면 확장성과 가용성이 뛰어난 이미지 크기 조정
기능을 제공하는 서버리스 아키텍처를 생성할 수 있습니다.
솔루션이 작동하는 방식은 다음과 같습니다.
사용자가 업로드한 원본 이미지를 저장하도록 Amazon S3 버킷을 설정합니다.
새 이미지가 업로드될 때마다 AWS Lambda 함수를 호출하도록 S3 버킷에서 이벤트
트리거를 구성합니다.
Lambda 함수는 업로드된 이미지를 검색하고, 장치 요구 사항에 따라 필요한 크기 조정
작업을 수행하고, 크기 조정된 이미지를 S3 버킷 또는 크기 조정된 이미지용으로 지정된
다른 버킷에 다시 저장하도록 설계할 수 있습니다.
사용자에게 제공하기 위해 크기 조정된 이미지에 공개적으로 액세스할 수 있도록 Amazon
S3 버킷을 구성합니다.
~~~

---

# Q514 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109534-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명
클러스터의 VPC 내 Kubernetes API 요청(예: 노드와 컨트롤 플레인 통신)은 프라이빗 VPC
엔드포인트를 사용합니다.
https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html
~~~

---

# Q515 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109535-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q516 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109719-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
Amazon API Gateway 는 개발자가 모든 규모에서 API 를 쉽게 생성, 게시, 유지 관리,
모니터링 및 보호할 수 있게 해주는 완전관리형 서비스입니다. AWS Lambda 는 서버를
프로비저닝하거나 관리하지 않고도 코드를 실행할 수 있는 서버리스 컴퓨팅 서비스입니다.
Lambda 는 들어오는 요청에 따라 자동으로 확장되지만 수요가 갑자기 증가하면 함수의 새
인스턴스를 초기화하는 데 시간이 걸릴 수 있습니다. 이로 인해 API 에 대한 긴 대기 시간
또는 콜드 스타트가 발생할 수 있습니다. 이를 방지하기 위해 함수가 초기화되고 언제든지
응답할 준비가 되도록 프로비저닝된 동시성을 사용할 수 있습니다. 프로비저닝된 동시성은
또한 확장이 성능에 미치는 영향을 줄임으로써 API 의 지연 시간을 일관되게 줄이는 데
도움이 됩니다.
참조:
https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integr
ationslambda.html
https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html
~~~

---

# Q517 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109536-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q518 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109721-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q519 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109722-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q520 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109539-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
웹 애플리케이션을 위한 가장 비용 효율적인 DynamoDB 테이블 구성은 DynamoDB
Standard 테이블 클래스를 사용하여 온디맨드 모드에서 DynamoDB 를 구성하는 것입니다.
이 구성을 사용하면 회사는 애플리케이션 트래픽에 따라 확장하고 애플리케이션이
테이블에서 수행하는 읽기 및 쓰기 요청에 대해서만 비용을 지불할 수 있습니다.
온디맨드 모드는 용량 계획 없이 초당 수천 개의 요청을 처리할 수 있는 유연한 청구
옵션입니다. 온디맨드 모드는 들어오는 트래픽을 기준으로 테이블 용량을 자동으로
조정하고 실제로 수행된 읽기 및 쓰기 요청에 대해서만 요금을 청구합니다. 온디맨드
모드는 예측할 수 없거나 가변적인 워크로드가 있는 애플리케이션 또는 사용한 만큼만
비용을 지불하는 용이성을 선호하는 애플리케이션에 적합합니다.
DynamoDB 표준 테이블 클래스는 대부분의 워크로드에 대한 기본이자 권장 테이블
클래스입니다. DynamoDB Standard 테이블 클래스는 DynamoDB Standard-Infrequent
Access(DynamoDB Standard-IA) 테이블 클래스보다 낮은 처리량 비용을 제공하며
처리량이 주요 비용인 테이블에 대해 더 비용 효율적입니다. DynamoDB Standard 테이블
클래스는 DynamoDB Standard-IA 테이블 클래스와 동일한 성능, 내구성 및 가용성을
제공합니다.
다른 옵션은 비용 효율적이지 않거나 사용 사례에 적합하지 않기 때문에 올바르지 않습니다.
DynamoDB 표준 테이블 클래스를 사용하여 프로비저닝된 읽기 및 쓰기로 DynamoDB 를
구성하고 DynamoDB Auto Scaling 을 정의된 최대 용량으로 설정하는 것은 올바르지
않습니다. 이 구성에는 테이블 용량을 수동으로 예측하고 관리해야 하므로 솔루션에
복잡성과 비용이 추가되기 때문입니다.
프로비저닝 모드는 사용자가 테이블에 대한 읽기 및 쓰기 용량 단위의 양을 지정하고
사용량에 관계없이 예약된 용량에 대해 비용을 청구하도록 요구하는 청구 옵션입니다.
프로비저닝 모드는 예측 가능하거나 안정적인 워크로드가 있는 애플리케이션이나 용량
설정을 보다 세밀하게 제어해야 하는 애플리케이션에 적합합니다.
DynamoDB Standard-Infrequent Access(DynamoDB Standard-IA) 테이블 클래스를
사용하여 DynamoDB 를 프로비저닝된 읽기 및 쓰기로 구성하고 DynamoDB 자동
스케일링을 정의된 최대 용량으로 설정하는 것은 중간에서 높은 처리량의 테이블에서는
비용 효율적이지 않기 때문에 올바르지 않습니다.
DynamoDB Standard-IA 테이블 클래스는 DynamoDB Standard 테이블 클래스보다
스토리지 비용은 낮지만 처리량 비용은 더 높습니다. DynamoDB Standard-IA 테이블
클래스는 자주 액세스하지 않는 데이터를 저장하는 테이블과 같이 스토리지 비용이 가장 큰
테이블에 최적화되어 있습니다. DynamoDB Standard-Infrequent Access(DynamoDB
Standard-IA) 테이블 클래스를 사용하여 온디맨드 모드에서 DynamoDB 를 구성하는 것은
올바르지 않습니다. 왜냐하면 이 구성은 중간에서 높은 처리량을 가진 테이블에 대해서는
비용 효율적이지 않기 때문입니다. 위에서 언급한 것처럼 DynamoDB Standard-IA 테이블
클래스는 DynamoDB Standard 테이블 클래스보다 처리량 비용이 높기 때문에 스토리지
비용 절감으로 인한 절감 효과를 상쇄할 수 있습니다.
~~~

---

# Q521 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109703-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q522 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109702-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
https://docs.aws.amazon.com/eks/latest/userguide/horizontal-pod-autoscaler.html
https://docs.aws.amazon.com/eks/latest/userguide/autoscaling.html
수평적 포드 자동 확장은 해당 리소스의 CPU 사용률을 기반으로 배포, 복제 컨트롤러 또는
복제 세트의 포드 수를 자동으로 확장하는 Kubernetes 의 기능입니다. CPU 사용량
데이터를 제공하려면 Kubernetes Metrics Server 와 같은 메트릭 소스가 필요합니다.
클러스터 자동 크기 조정은 Pod 가 실패하거나 다른 노드로 다시 예약될 때 클러스터의
노드 수를 자동으로 조정하는 Kubernetes 의 기능입니다. 클러스터 2 에 가입하는 EC2
인스턴스를 관리하려면 AWS Auto Scaling 그룹과의 통합이 필요합니다. 이 솔루션은
수평적 포드 자동 확장과 클러스터 자동 확장을 모두 사용하여 Amazon EKS 가 워크로드에
따라 확장 및 축소되도록 할 수 있습니다.
~~~

---

# Q523 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109701-exam-aws-certified-sol
utions-architect-associate-saa-c03/
B??
~~~

---

# Q524 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/111425-exam-aws-certified-sol
utions-architect-associate-saa-c03/
D??
~~~

---

# Q525 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/111278-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q526 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/111245-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q527 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/111428-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
이 옵션은 애플리케이션에 고가용성과 중복성을 제공하는 두 번째 리전에 웹 계층과
애플리케이션 계층을 배포하기 때문에 가장 효율적입니다. 또한 단일 Aurora
데이터베이스가 여러 AWS 지역에 걸쳐 있을 수 있도록 하는 기능인 Amazon Aurora
글로벌 데이터베이스를 사용합니다. 또한 기본 지역과 두 번째 지역에 데이터베이스를
배포하여 지연 시간이 짧은 글로벌 읽기 및 지역 중단 시 빠른 복구를 제공합니다. 또한 두
번째 리전에 대한 장애 조치 라우팅 정책과 함께 Amazon Route 53 상태 확인을 사용하여
다른 리전의 정상적인 엔드포인트로 트래픽을 라우팅하여 데이터 보호를 제공합니다. 또한
필요에 따라 보조를 기본으로 승격하여 한 번에 리전 중 하나에서 쓰기 작업을 허용하여
데이터 일관성을 제공합니다. 이 솔루션은 전 세계적으로 확장하고 해당 애플리케이션의
다운타임을 최소화해야 한다는 요구 사항을 충족합니다.
옵션 A 는 웹 계층 및 애플리케이션 계층에 대한 Auto Scaling 그룹을 확장하여 두 번째
리전의 가용 영역에 인스턴스를 배포하기 때문에 효율성이 떨어집니다. 이렇게 하면 별도로
배포하는 것보다 더 높은 비용과 복잡성이 발생할 수 있습니다. 또한 Aurora 글로벌
데이터베이스를 사용하여 기본 리전과 두 번째 리전에 데이터베이스를 배포합니다. 이는
맞습니다. 그러나 두 번째 리전에 대한 장애 조치 라우팅 정책과 함께 Amazon Route 53
상태 확인을 사용하지 않으므로 트래픽이 비정상 엔드포인트로 라우팅될 수 있습니다.
옵션 B 는 웹 계층과 애플리케이션 계층을 올바른 두 번째 리전에 배포하기 때문에
효율성이 떨어집니다. 또한 두 번째 리전에 Aurora PostgreSQL 교차 리전 Aurora 복제본을
추가하여 리전 간 읽기 확장성을 제공합니다. 그러나 리전 간 복제본보다 더 빠른 복제 및
복구를 제공하는 Aurora 글로벌 데이터베이스를 사용하지 않습니다. 또한 올바른 두 번째
리전에 대한 장애 조치 라우팅 정책과 함께 Amazon Route 53 상태 확인을 사용합니다.
그러나 필요에 따라 보조를 기본으로 승격하지 않으므로 데이터 불일치 또는 손실이 발생할
수 있습니다.
옵션 C 는 웹 계층과 애플리케이션 계층을 올바른 두 번째 리전에 배포하기 때문에
효율성이 떨어집니다.
또한 두 번째 리전에 Aurora PostgreSQL 데이터베이스를 생성하여 리전 간 데이터
중복성을 제공합니다. 그러나 별도의 데이터베이스를 생성하는 것보다 더 빠른 복제 및
복구를 제공하는 Aurora 글로벌 데이터베이스 또는 리전 간 복제본을 사용하지 않습니다.
또한 AWS DMS(AWS Database Migration Service)를 사용하여 기본 데이터베이스를 두 번째
리전에 복제하여 서로 다른 소스와 대상 간에 데이터 마이그레이션을 제공합니다. 그러나
AWS DMS 를 사용하는 것보다 더 빠른 복제 및 복구를 제공하는 Aurora 글로벌
데이터베이스 또는 리전 간 복제본을 사용하지 않습니다. 또한 올바른 두 번째 리전에 대한
장애 조치 라우팅 정책과 함께 Amazon Route 53 상태 확인을 사용합니다.
~~~

---

# Q528 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/111317-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
이 옵션은 AWS Transfer Family 를 사용하여 저비용 고가용성 스토리지 서비스인 Amazon
S3 Standard 에 수신 파일을 저장할 수 있는 FTP 서버를 생성하기 때문에 운영상 가장
효율적입니다. 또한 AWS Lambda 를 사용하여 파일을 처리하고 처리 후 삭제합니다. 이는
배치 스케줄링이나 인프라 관리가 필요하지 않은 확장 가능한 서버리스 솔루션입니다. 또한
S3 이벤트 알림을 사용하여 파일이 도착하면 Lambda 함수를 호출하여 수신 데이터 파일을
거의 실시간으로 처리할 수 있습니다.
옵션 A 는 Amazon S3 Standard 보다 검색 비용이 높고 검색 시간이 긴 콜드 스토리지
클래스인 Amazon S3 Glacier Flexible Retrieval 을 사용하기 때문에 효율성이 떨어집니다.
또한 EventBridge 규칙을 사용하여 야간에 작업을 호출하므로 들어오는 데이터 파일을
가능한 한 빨리 처리해야 한다는 요구 사항을 충족하지 않습니다.
옵션 B 는 EBS 볼륨을 사용하여 수신 파일을 저장하기 때문에 효율성이 떨어집니다. 이는
Amazon S3 보다 비용이 높고 내구성이 낮은 블록 스토리지 서비스입니다. 또한
EventBridge 규칙을 사용하여 야간에 작업을 호출하므로 들어오는 데이터 파일을 가능한
한 빨리 처리해야 한다는 요구 사항을 충족하지 않습니다.
옵션 C 는 EBS 볼륨을 사용하여 수신 파일을 저장하기 때문에 효율성이 떨어집니다. 이는
Amazon S3 보다 비용이 높고 내구성이 낮은 블록 스토리지 서비스입니다. 또한 AWS
Batch를 사용하여 파일을 처리하므로 컴퓨팅 리소스와 작업 대기열을 관리해야 합니다.
~~~

---

# Q529 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/111246-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q530 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/111271-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q531 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/111430-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
함수 URL 은 HTTPS 를 통해 함수를 호출하는 데 사용할 수 있는 Lambda 함수의 고유
식별자입니다. 함수가 배포된 AWS 리전의 API 엔드포인트와 function1 의 이름 또는
ARN 으로 구성됩니다. Lambda 함수에 대한 함수 URL 을 생성함으로써 솔루션은 제 3 자가
Lambda 함수를 가장 효율적으로 호출할 수 있도록 할 수 있습니다.
1. Lambda 함수 앞에 Application Load Balancer(ALB)를 배포합니다. Webhook 에 대한
ALB URL 을 타사에 제공합니다. 이 솔루션은 HTTPS 를 통해 Lambda 함수를 호출하는 데
필요하지 않은 추가 리소스(ALB)를 생성하고 관리하기 때문에 최고의 운영 효율성 요구
사항을 충족하지 않습니다.
2. Amazon Simple Notification Service(Amazon SNS) 주제를 생성합니다. Lambda 함수에
주제를 연결합니다. Webhook 에 대한 제 3 자에게 SNS 주제의 공개 호스트 이름을
제공합니다. Amazon SNS 주제에는 웹훅으로 사용할 수 있는 공개 호스트 이름이 없기
때문에 이 솔루션은 작동하지 않습니다. SNS 주제는 외부 소스로부터 메시지를 받는 것이
아니라 구독자에게 메시지를 게시하는 데 사용됩니다.
3. Amazon Simple Queue Service(Amazon SQS) 대기열을 생성합니다. 대기열을 Lambda
함수에 연결합니다. Webhook 에 대해 타사에 SQS 대기열의 공개 호스트 이름을
제공합니다. Amazon SQS 대기열에는 웹훅으로 사용할 수 있는 공개 호스트 이름이 없기
때문에 이 솔루션은 작동하지 않습니다. SQS 대기열은 외부 소스에서 메시지를 수신하는
것이 아니라 AWS 서비스 간에 메시지를 전송, 저장 및 수신하는 데 사용됩니다.
참조 URL:
https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html
~~~

---

# Q532 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/111382-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
API Gateway REST API 를 사용하는 모든 고객에게 개별 보안 URL 을 제공하려면 다음
단계를 수행해야 합니다.
a) 등록 기관에 필요한 도메인을 등록합니다. Route 53 호스팅 영역에서 와일드카드 사용자
지정 도메인 이름을 생성하고 API 게이트웨이 엔드포인트를 가리키는 영역에 기록합니다.
이 단계를 통해 API Gateway 에서 생성한 기본 도메인 이름 대신 API 에 대한 사용자 지정
도메인 이름을 사용할 수 있습니다. 와일드카드 사용자 지정 도메인 이름은 도메인 이름
아래의 모든 하위 도메인(예: customer1.example.com 또는 customer2.example.com)을
사용하여 API 에 액세스할 수 있음을 의미합니다. 도메인 이름을 등록 대행자(예: Route 53
또는 타사 등록 대행자)에 등록하고 도메인 이름에 대해 Route 53 에 호스팅 영역을
생성해야 합니다. 또한 별칭 레코드를 사용하여 API Gateway 엔드포인트를 가리키는
호스팅 영역에 레코드를 생성해야 합니다.
d) 동일한 리전의 AWS Certificate Manager(ACM)에서 사용자 지정 도메인 이름과 일치하는
와일드카드 인증서를 요청합니다. 이 단계에서는 ACM 에서 발급한 인증서를 사용하여
HTTPS 로 API 를 보호할 수 있습니다. 와일드카드 인증서는 도메인 이름 아래의 모든 하위
도메인(예: *.example.com)과 일치할 수 있음을 의미합니다. 사용자 지정 도메인 이름과
일치하는 ACM 에서 인증서를 요청하거나 가져와 도메인 이름을 소유하고 있는지 확인해야
합니다. 또한 API와 동일한 리전에서 인증서를 요청해야 합니다.
f) API Gateway에서 REST API용 사용자 지정 도메인 이름을 생성합니다. AWS Certificate
Manager(ACM)에서 인증서를 가져옵니다. 이 단계에서는 사용자 지정 도메인 이름을 API와
연결하고 ACM 의 인증서를 사용하여 HTTPS 를 활성화할 수 있습니다. API Gateway 에서
REST API 용 사용자 지정 도메인 이름을 생성하고 ACM 에서 인증서 ARN 을 지정해야
합니다. 또한 사용자 지정 도메인 이름에서 API 단계로 경로를 매핑하는 기본 경로 매핑을
생성해야 합니다.
~~~

---

# Q533 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/111432-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
Amazon Macie 는 또한 다양한 소스의 데이터를 사용하여 애플리케이션을 쉽게 연결할 수
있게 해주는 서버리스 이벤트 버스인 Amazon EventBridge 로 결과를 보낼 수 있습니다.
Macie 결과에서 SensitiveData 이벤트 유형을 필터링하고 보안 팀에 Amazon SNS 알림을
보내는 EventBridge 규칙을 생성할 수 있습니다. Amazon SNS 는 구독자 또는 다른
애플리케이션에 메시지를 보낼 수 있는 완전 관리형 메시징 서비스입니다.
참조:
https://docs.aws.amazon.com/macie/latest/userguide/macie-findings.html#macie-findin
gseventbridge
~~~

---

# Q534 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/111434-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q535 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/111385-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q536 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/111435-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q537 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/111386-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
이 답변은 향후 애플리케이션 용량 요구 사항을 충족하기 위한 확장 요구 사항을 충족하고
세 가용 영역 모두에서 고가용성을 보장하기 때문에 정답입니다. 다중 AZ DB 클러스터
배포를 사용하여 MySQL 데이터베이스를 MySQL 용 Amazon RDS 로 마이그레이션함으로써
회사는 여러 가용 영역에서 데이터베이스의 자동 장애 조치, 백업 및 패치 적용의 이점을
누릴 수 있습니다. 고가용성 Redis 용 Amazon ElastiCache 를 사용하여 회사는 가용 영역
전체에서 장애 조치할 수 있는 빠른 인 메모리 데이터 저장소에 세션 데이터 및 캐시
읽기를 저장할 수 있습니다. 3 개의 가용 영역에 있는 Auto Scaling 그룹으로 웹 서버를
마이그레이션함으로써 회사는 수요 및 트래픽 패턴에 따라 웹 서버 용량을 자동으로 확장할
수 있습니다.
참조:
https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html
https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/AutoFailover.html
https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-sc
aling.html
~~~

---

# Q538 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/111387-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q539 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/111301-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q540 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/111439-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
Amazon Aurora 는 MySQL 및 PostgreSQL 과 호환되는 완전관리형 관계형
데이터베이스입니다. MySQL 보다 최대 5 배, PostgreSQL 보다 최대 3 배 뛰어난 성능을
제공합니다. 또한 여러 가용 영역에 걸쳐 데이터를 복제하고 데이터를 Amazon S31 에
지속적으로 백업하여 고가용성과 내구성을 제공합니다. 다중 AZ 인스턴스 배포에 배포된
Amazon RDS 를 사용하여 Amazon Aurora 데이터베이스를 생성함으로써 솔루션은 더 높은
가용성을 달성하고 애플리케이션 성능을 개선할 수 있습니다.
Amazon Aurora 는 기본 인스턴스와 동일한 기본 스토리지를 공유하는 별도의 인스턴스인
읽기 전용 복제본을 지원합니다. 읽기 전용 복제본을 사용하여 기본 인스턴스에서 읽기
전용 쿼리를 오프로드하고 성능을 향상할 수 있습니다. 읽기 전용 복제본은 보고 기능에도
사용할 수 있습니다.
보고 기능을 판독기 인스턴스로 지정함으로써 솔루션은 기본 데이터베이스 시스템에서
보고를 오프로드할 수 있습니다.
1. AWS Database Migration Service(AWS DMS)를 사용하여 여러 AWS 리전에서 Amazon
RDS DB 인스턴스 생성 보고 기능이 기본 DB 인스턴스와 별도의 DB 인스턴스를
가리키도록 합니다. 이 솔루션은 AWS 데이터베이스 서비스 사용 요구 사항을 충족하지
않습니다. AWS DMS 는 데이터베이스 서비스 자체가 아니라 사용자가 데이터베이스를
AWS 로 마이그레이션하는 데 도움을 주는 서비스이기 때문입니다. 또한 서로 다른
리전에서 여러 DB 인스턴스를 생성해야 하므로 복잡성과 비용이 증가할 수 있습니다.
2. 단일 AZ 배포에서 Amazon RDS 를 사용하여 Oracle 데이터베이스 생성 기본 DB
인스턴스와 동일한 영역에 읽기 전용 복제본을 생성합니다. 보고 기능을 읽기 전용
복제본으로 지정합니다. 단일 AZ 배포는 가용 영역 중단 시 장애 조치 보호를 제공하지
않으므로 이 솔루션은 고가용성 달성 요구 사항을 충족하지 않습니다. 또한 Oracle 을
데이터베이스 엔진으로 사용하므로 Aurora보다 더 나은 성능을 제공하지 못할 수 있습니다.
3. 다중 AZ 클러스터 배포에 배포된 Amazon RDS 를 사용하여 Oracle 데이터베이스 생성
클러스터 배포에서 리더 인스턴스를 사용하도록 보고 기능에 지시합니다. Oracle 이
Aurora 보다 더 나은 성능을 제공하지 않을 수 있으므로 이 솔루션은 애플리케이션 성능
향상 요구 사항을 충족하지 않습니다. 또한 Oracle 이 아닌 Aurora 에서만 지원되는
클러스터 배포를 사용합니다.
참조:
https://aws.amazon.com/rds/aurora/
~~~

---

# Q541 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/111440-exam-aws-certified-sol
utions-architect-associate-saa-c03/
참고
https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteHosting.html
~~~

---

# Q542 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/111441-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q543 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/111442-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q544 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/111450-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:・
이 답변은 고객에게 미치는 영향을 최소화하고 데이터 손실을 최소화하면서 API 의 새
버전을 릴리스하기 위한 요구 사항을 충족하므로 정확합니다. 카나리아 릴리스 배포는
테스트 목적으로 API 의 새 버전을 배포하고 기본 버전은 동일한 단계에서 일반 작업을
위해 프로덕션 릴리스로 배포된 상태로 유지하는 소프트웨어 개발 전략입니다. 카나리아
릴리스 배포에서 총 API 트래픽은 미리 구성된 비율로 프로덕션 릴리스와 카나리아
릴리스로 무작위로 분리됩니다. 일반적으로 카나리아 릴리스는 API 트래픽의 작은 비율을
수신하고 프로덕션 릴리스가 나머지를 차지합니다. 업데이트된 API 기능은 카나리아를 통한
API 트래픽에만 표시됩니다. 카나리아 트래픽 비율을 조정하여 테스트 범위 또는 성능을
최적화할 수 있습니다. 카나리아 트래픽을 작게 유지하고 선택을 무작위로 유지함으로써
대부분의 사용자는 새 버전의 잠재적인 버그로 인해 언제든지 악영향을 받지 않으며 단일
사용자도 항상 악영향을 받지 않습니다. 테스트 메트릭이 요구 사항을 통과한 후 canary
릴리스를 프로덕션 릴리스로 승격하고 배포에서 canary 를 비활성화할 수 있습니다. 이렇게
하면 생산 단계에서 새로운 기능을 사용할 수 있습니다.
참조:
https://docs.aws.amazon.com/apigateway/latest/developerguide/canary-release.html
~~~

---

# Q545 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/116974-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명1:
Route 53 상태 확인을 사용하여 활성-활성 및 활성-수동 장애 조치 구성을 구성할 수
있습니다. 능동-수동 장애 조치 : 기본 리소스 또는 리소스 그룹을 대부분의 시간 동안
사용할 수 있도록 하고 모든 기본 리소스를 사용할 수 없는 경우에 대비하여 보조 리소스
또는 리소스 그룹을 대기 상태로 유지하려는 경우 활성-수동 장애 조치 구성을 사용합니다.
쿼리에 응답할 때 Route 53 에는 정상적인 기본 리소스만 포함됩니다. 모든 기본 리소스가
비정상인 경우 Route 53 은 DNS 쿼리에 대한 응답으로 정상적인 보조 리소스만 포함하기
시작합니다.
https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-types.html
설명2:
이 솔루션은 기본 웹 사이트를 사용할 수 없는 경우 사용자를 백업 정적 오류 페이지로
안내하여 변경 및 인프라 오버헤드를 최소화하는 요구 사항을 충족합니다. Route 53
활성-수동 장애 조치 구성은 정상인 경우 기본 리소스로, 기본 리소스가 비정상인 경우
보조 리소스로 트래픽을 라우팅할 수 있습니다. Route 53 상태 확인은 ALB 엔드포인트의
상태를 모니터링하고 필요할 때 장애 조치를 트리거할 수 있습니다. 정적 오류 페이지는
웹사이트로 구성된 S3 버킷에서 호스팅할 수 있으며 이는 정적 콘텐츠를 제공하는
간단하고 비용 효율적인 방법입니다.
대기 시간 라우팅 정책을 사용하면 사용자에 대한 가장 낮은 네트워크 대기 시간을
기반으로 트래픽을 라우팅할 수 있지만 장애 조치 기능을 제공하지 않기 때문에 옵션 A 는
올바르지 않습니다.
ALB 및 EC2 인스턴스와 함께 활성-활성 구성을 사용하면 인프라 오버헤드와 복잡성이
증가할 수 있고 EC2 인스턴스가 항상 정상 상태임을 보장하지 않기 때문에 옵션 C 는
올바르지 않습니다.
다중값 응답 라우팅 정책을 사용하면 쿼리에 대해 여러 값을 반환할 수 있지만 장애 조치
기능을 제공하지 않기 때문에 옵션 D는 올바르지 않습니다.
참조:
https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-failover.ht
ml
https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html
https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteHosting.html
~~~

---

# Q546 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/116975-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
이를 통해 회사는 온프레미스 백업 인프라를 단순화하고 물리적 백업 테이프의 사용을
제거하여 비용을 절감할 수 있습니다. iSCSI-가상 테이프 라이브러리(VTL) 인터페이스를
사용하여 백업 애플리케이션과 연결하도록 AWS Storage Gateway 를 설정함으로써 회사는
S3 또는 Glacier 의 가상 테이프에 백업 데이터를 저장할 수 있습니다. 이를 통해 AWS
스토리지 서비스를 활용하는 동시에 온프레미스 백업 애플리케이션 및 워크플로에 대한
기존 투자를 보존합니다.
~~~

---

# Q547 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/116976-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
최소한의 운영 오버헤드로 대용량 스트리밍 데이터를 수집하고 처리하려면 Amazon Kinesis
Data Firehose가 적합한 솔루션입니다. Amazon Kinesis Data Firehose는 스트리밍 데이터를
캡처, 변환하여 Amazon S3 또는 기타 대상으로 전달할 수 있습니다. Amazon Kinesis Data
Firehose 는 데이터 처리량에 맞춰 자동으로 확장하고 모든 양의 데이터를 처리할 수
있습니다. Amazon Kinesis Data Firehose 는 프로비저닝이나 관리를 위해 서버가 필요하지
않은 완전관리형 서비스이기도 합니다.
~~~

---

# Q548 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/116977-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q549 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/116978-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
프라이빗 서브넷의 MySQL 데이터베이스가 공개적으로 노출되지 않고 인터넷에 액세스할
수 있도록 하려면 NAT 게이트웨이가 적합한 솔루션입니다. NAT 게이트웨이를 사용하면
프라이빗 서브넷의 인스턴스가 인터넷이나 다른 AWS 서비스에 연결할 수 있지만 인터넷이
해당 인스턴스와 연결을 시작하는 것은 방지됩니다. NAT 게이트웨이는 퍼블릭 서브넷에
상주하며 짧은 대기 시간으로 높은 트래픽 처리량을 처리할 수 있습니다. NAT 게이트웨이는
운영 오버헤드가 필요하지 않은 관리형 서비스이기도 합니다.
~~~

---

# Q550 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/116979-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
B 와 D 는 정답입니다. Lambda 실행 역할에 환경 변수를 해독하고 사용할 수 있는 권한이
있고 AWS KMS 키 정책에 따라 Lambda 실행 역할이 키를 사용할 수 있도록 허용하기
때문입니다. Lambda 실행 역할은 AWS KMS 와 같은 AWS 리소스에 액세스할 수 있는
권한을 Lambda 함수에 부여하는 IAM 역할입니다. AWS KMS 키 정책은 키에 대한
액세스를 제어하는 리소스 기반 정책입니다. Lambda 실행 역할에 AWS KMS 권한을
추가하고 AWS KMS 키 정책에서 Lambda 실행 역할을 허용함으로써 솔루션 아키텍트는
환경 변수를 암호화하고 해독하기 위한 올바른 권한을 구현할 수 있습니다.
~~~

---

# Q551 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/116896-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
첫 주 동안 자주 액세스하고 수년간 보관해야 하는 보고서를 저장하고 검색하려면 S3
Standard와 S3 Glacier가 적합한 솔루션입니다. S3 Standard는 자주 액세스하는 데이터에
대해 높은 내구성, 가용성 및 성능을 제공합니다. S3 Glacier 는 저렴한 비용으로 장기
데이터 보관을 위한 안전하고 내구성 있는 스토리지를 제공합니다. S3 수명 주기 규칙을
사용하면 7일 후에 보고서를 S3 Standard에서 S3 Glacier로 전환할 수 있으므로 스토리지
비용을 줄일 수 있습니다. S3 Glacier는 6시간 이내 검색도 지원합니다.
~~~

---

# Q552 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/116897-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q553 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/117206-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q554 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/117442-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q555 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/116983-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q556 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/117434-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
이를 통해 애플리케이션 EC2 인스턴스는 템플릿에 API 자격 증명을 노출하지 않고도
DynamoDB 테이블에 액세스할 수 있습니다. DynamoDB 테이블에서 읽고 쓰는 데 필요한
권한이 있는 IAM 역할을 생성하고 이를 EC2 인스턴스 프로필에 추가하면 애플리케이션
인스턴스는 AWS 에서 자동으로 교체하는 임시 보안 자격 증명을 사용할 수 있습니다. 이는
EC2 인스턴스에서 AWS 리소스에 대한 액세스 권한을 부여하는 안전한 모범 사례
방법입니다.
~~~

---

# Q557 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/117344-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q558 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/117053-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
동일한 AWS 계정 내 동일한 리전에 있는 두 개의 VPC 를 연결하려면 VPC 피어링이 가장
비용 효과적인 솔루션입니다. VPC 피어링을 사용하면 게이트웨이, VPN 연결 또는 AWS
Transit Gateway 없이도 VPC 간의 직접 네트워크 트래픽을 허용할 수 있습니다. 또한 VPC
피어링은 VPC 간 데이터 전송에 대한 추가 요금을 발생시키지 않습니다.
~~~

---

# Q559 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/117403-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
사용자 정의 태그는 AWS 리소스에 적용하여 분류하고 추적할 수 있는 키-값 쌍입니다.
사용자 정의 태그를 사용하여 비용을 할당하고 AWS 결제 콘솔에서 세부 결제 보고서를
생성할 수도 있습니다. 비용 할당을 위해 사용자 정의 태그를 사용하려면 조직의 모든 회원
계정에 대한 모든 권한을 갖는 루트 계정인 조직 마스터 계정에서 태그를 활성화해야
합니다. 활성화되면 사용자 정의 태그가 비용 할당 보고서의 열로 표시되며 제품 라인별로
비용을 필터링하고 그룹화하는 데 사용할 수 있습니다. 이 솔루션은 기존 태깅 전략을
활용하고 코드 개발이나 수동 개입이 필요하지 않으므로 최소한의 운영 오버헤드로 요구
사항을 충족합니다.
~~~

---

# Q560 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/117021-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q561 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/117022-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
이를 통해 회사는 Amazon DynamoDB 테이블에서 제품 세부 정보를 검색할 때 웹
애플리케이션의 응답 시간을 개선하고 지연 시간을 줄일 수 있습니다. DynamoDB
Accelerator(DAX) 클러스터를 설정함으로써 회사는 최대 10 배의 성능 향상을 제공하는
DynamoDB 용 완전 관리형 고가용성 인 메모리 캐시를 사용할 수 있습니다. 모든 읽기
요청을 DAX 를 통해 라우팅함으로써 회사는 DynamoDB 테이블에 대한 읽기 작업 수를
줄이고 사용자 경험을 향상시킬 수 있습니다.
~~~

---

# Q562 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/117251-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q563 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/117023-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q564 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/117024-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
이를 통해 회사는 중요한 고객 정보를 관리형 AWS 서비스에 저장하고 고객이 웹
사이트에서 구매 거래를 완료할 수 있는 기능을 제공할 수 있습니다. AWS Key Management
Service(AWS KMS) 클라이언트 측 암호화를 사용하여 회사는 데이터를 MySQL 용 Amazon
RDS 로 보내기 전에 암호화할 수 있습니다. 애플리케이션만이 암호화 키에 액세스할 수
있으므로 이를 통해 데이터베이스 관리자로부터도 민감한 고객 데이터가 보호됩니다.
~~~

---

# Q565 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/117025-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
호환성과 확장성을 갖춘 MySQL 데이터베이스를 AWS 로 마이그레이션하려면 Amazon
Aurora 가 적합한 옵션입니다. Aurora 는 MySQL 과 호환되며 Aurora Auto Scaling 을 통해
자동으로 확장할 수 있습니다. AWS Database Migration Service(AWS DMS)를 사용하면 가동
중지 시간을 최소화하면서 온프레미스에서 Aurora 로 데이터베이스를 마이그레이션할 수
있습니다.
~~~

---

# Q566 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/116902-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
이를 통해 EC2 인스턴스는 두 가용 영역에 걸쳐 공유 스토리지에 동시에 빠르게 읽고 쓸
수 있습니다. Amazon EFS 는 여러 EC2 인스턴스에서 탑재할 수 있는 확장 가능하고
탄력적이며 가용성이 높은 파일 시스템을 제공합니다. Amazon EFS 는 높은 수준의
처리량과 IOPS, 일관되게 낮은 지연 시간을 지원합니다. Amazon EFS 는 또한 높은 수준의
동시성을 지원하는 NFSv4 잠금 업그레이드 및 다운그레이드를 지원합니다.
~~~

---

# Q567 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/117026-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
AWS Lambda 에서 이벤트 기반 프로그래밍 모델을 사용하고 운영 오버헤드를 줄이려면
Amazon API Gateway 와 Amazon DynamoDB 가 적합한 솔루션입니다. Amazon API
Gateway는 센서로부터 데이터를 수신하고 AWS Lambda 함수를 호출하여 데이터를 처리할
수 있습니다. AWS Lambda 는 서버를 프로비저닝하거나 관리하지 않고도 코드를 실행하고
수신 요청에 따라 자동으로 확장할 수 있습니다. Amazon DynamoDB 는 일관된 성능으로
모든 양의 데이터를 처리할 수 있는 빠르고 유연한 NoSQL 데이터베이스에 데이터를
저장할 수 있습니다.
~~~

---

# Q568 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/117027-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
캐싱 지원을 통해 엔지니어링 도면을 저장하고 보려면 Amazon S3 및 Amazon
CloudFront 가 적합한 솔루션입니다. Amazon S3 는 높은 내구성, 가용성 및 성능으로 모든
양의 데이터를 저장할 수 있습니다. Amazon CloudFront 는 엔지니어링 도면을 사용자에게
더 가까운 엣지 로케이션에 배포하여 지연 시간을 줄이고 사용자 경험을 향상시킬 수
있습니다. Amazon CloudFront는 엔지니어링 도면을 엣지 로케이션에 캐시할 수도 있으므로
사용자가 도면이 로드될 때까지 기다리는 시간을 최소화할 수 있습니다.
~~~

---

# Q569 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/117377-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q570 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/116903-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
Auto Scaling 그룹은 유사한 특성을 공유하고 수요에 따라 자동으로 확장 또는 축소될 수
있는 EC2 인스턴스 모음입니다. Auto Scaling 그룹에는 특정 시간에 특정 크기로
확장하도록 그룹에 지시하는 구성인 예약된 작업이 있을 수 있습니다. 이러한 방식으로
회사는 매주 금요일 저녁 최대 6 개의 인스턴스로 확장하여 증가된 워크로드를 처리하고,
다른 시간에는 2 개의 인스턴스로 축소하여 비용을 절감할 수 있습니다. 이 솔루션은 수동
개입이나 사용자 지정 스크립트가 필요하지 않으므로 최소한의 운영 오버헤드로 요구
사항을 충족합니다.
~~~

---

# Q571 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/116904-exam-aws-certified-sol
utions-architect-associate-saa-c03/
A??
~~~

---

# Q572 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/117029-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
이를 통해 회사는 온프레미스 데이터베이스를 Auto Scaling 기능을 지원하고 관리
오버헤드가 가장 적은 관리형 AWS 서비스로 마이그레이션할 수 있습니다. Amazon Aurora
Serverless v2는 워크로드 수요에 따라 컴퓨팅 용량을 자동으로 확장하는 Amazon Aurora의
구성입니다. 단 몇 초 만에 수백 건에서 수십만 건의 트랜잭션을 확장할 수 있습니다.
Amazon Aurora Serverless v2는 MySQL 호환 데이터베이스와 AWS Direct Connect 연결도
지원합니다.
~~~

---

# Q573 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/116925-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
Java 11 에서 실행되는 Lambda 함수의 시작 지연 시간을 줄이기 위해 Lambda
SnapStart가 적합한 솔루션입니다. Lambda SnapStart는 Java 11 기능에 대한 더 빠른 콜드
스타트와 더 낮은 이상치 지연 시간을 지원하는 기능입니다. Lambda SnapStart 는 사전
초기화된 JVM(Java Virtual Machine)을 사용하여 기능을 실행하므로 초기화 시간과 메모리
공간이 줄어듭니다. Lambda SnapStart에는 추가 비용이 발생하지 않습니다.
~~~

---

# Q574 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/117272-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q575 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/116969-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q576 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/116906-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
엣지 최적화 API 엔드포인트는 API 요청을 가장 가까운 CloudFront POP(Point of
Presence)로 라우팅하므로 지리적으로 분산된 클라이언트에 가장 적합합니다. 이렇게 하면
대기 시간이 줄어들고 API 성능이 향상됩니다. 엣지 최적화 엔드포인트는 API Gateway
REST API의 기본 유형입니다.
지역 API 엔드포인트는 API와 동일한 지역에 있는 클라이언트를 위한 것이며 CloudFront를
사용하여 요청을 라우팅하지 않습니다. 프라이빗 API 엔드포인트는 인터페이스 VPC
엔드포인트를 사용하여 VPC 에서만 액세스할 수 있는 API 엔드포인트입니다. 지역 또는
개인 끝점은 지리적으로 분산된 사용자의 대기 시간을 줄이는 요구 사항을 충족하지
않습니다.
~~~

---

# Q577 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/117037-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q578 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/117038-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q579 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/116924-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
AWS 솔루션의 인스턴스 스케줄러는 Amazon Elastic Compute Cloud(Amazon EC2) 및
Amazon Relational Database Service(Amazon RDS) 인스턴스의 시작 및 중지를
자동화합니다. 이 솔루션은 사용하지 않는 리소스를 중지하고 필요할 때 시작하여 운영
비용을 절감하는 데 도움이 됩니다 1. 이 솔루션을 사용하면 명령줄 인터페이스(CLI) 또는
SSM 유지 관리 기간을 사용하여 맞춤형 일정과 기간을 정의할 수 있습니다. 선결제 없음,
부분 선결제, 전체 선결제 등 예약 DB 인스턴스에 대한 다양한 결제 옵션 중에서 선택할
수도 있습니다.
참고:
https://aws.amazon.com/ko/solutions/implementations/instance-scheduler-on-aws/?nc1
=h_ls
~~~

---

# Q580 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/117663-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q581 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/116968-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q582 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/118597-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q583 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/117215-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q584 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/119485-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
이를 통해 회사는 대량의 데이터를 병렬로 처리하고 노드 그룹이 동일한 기본 하드웨어를
공유하는 것을 방지하는 애플리케이션을 배포할 수 있습니다. 분산 배치 그룹에서 EC2
인스턴스를 실행함으로써 회사는 서로 다른 기본 하드웨어에서 소수의 인스턴스를 시작하여
상관 오류를 줄일 수 있습니다. 분산 배치 그룹은 각 인스턴스가 랙 수준에서 서로
격리되도록 보장합니다.
~~~

---

# Q585 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/119642-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q586 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/119645-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
이를 통해 솔루션 아키텍트는 연구 개발(R&D) 비즈니스를 위한 별도의 조직을 만들고 AWS
계정을 새 조직으로 이동할 수 있습니다. R&D AWS 계정이 이전 조직을 떠난 후 새 조직의
일부가 되도록 초대함으로써 솔루션 아키텍트는 두 조직 간에 중복이나 충돌이 없는지
확인할 수 있습니다. R&D AWS 계정은 새 조직에 가입하라는 초대를 수락하거나 거부할 수
있습니다. 일단 수락되면 새 조직에서 적용하는 모든 정책과 통제가 적용됩니다.
~~~

---

# Q587 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/119576-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q588 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/119718-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q589 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/119487-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q590 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/119719-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q591 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/119574-exam-aws-certified-sol
utions-architect-associate-saa-c03/]
~~~

---

# Q592 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/119573-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q593 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/119572-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q594 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/119570-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q595 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/119569-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q596 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/119590-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q597 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/119465-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q598 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/119563-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
비용 효율적인 방식으로 사용 사례의 요구 사항을 충족하려면 다음 단계를 수행하는 것이
좋습니다.
Amazon S3 파일 게이트웨이 모드로 온프레미스에 AWS Storage Gateway 를 배포합니다.
이를 통해 회사는 장치에서 생성된 .csv 파일을 SMB 파일 공유에 쓸 수 있으며, 이 파일은
Amazon S3 버킷에 객체로 저장됩니다. AWS Storage Gateway는 온프레미스 환경을 AWS
스토리지와 통합하는 하이브리드 클라우드 스토리지 서비스입니다. Amazon S3 파일
게이트웨이 모드는 Amazon S3 에 연결하고 거의 무제한의 클라우드 스토리지에 액세스할
수 있는 원활한 방법을 제공합니다.
Amazon S3 에 있는 데이터를 기반으로 테이블을 생성하도록 AWS Glue 크롤러를
설정합니다. 이를 통해 회사는 표준 SQL 을 사용하여 Amazon S3 버킷에 저장된 데이터를
쿼리할 수 있습니다. AWS Glue는 데이터 준비 및 분석을 단순화하는 서버리스 데이터 통합
서비스입니다. AWS Glue 크롤러는 다양한 소스의 데이터를 자동으로 검색 및 분류하고
AWS Glue 데이터 카탈로그에 메타데이터 테이블을 생성할 수 있습니다. 데이터 카탈로그는
데이터 소스에 대한 정보와 이에 액세스하는 방법을 저장하는 중앙 저장소입니다.
Amazon S3 에 있는 데이터를 쿼리하도록 Amazon Athena 를 설정합니다. 이는 회사
분석가에게 표준 SQL을 사용하여 Amazon S3에서 직접 데이터를 분석할 수 있는 서버리스
및 대화형 쿼리 서비스를 제공합니다. Amazon Athena 는 AWS Glue 데이터 카탈로그와
통합되어 있으므로 사용자는 크롤러가 정의한 데이터 원본 테이블에서 Athena 를 쉽게
가리킬 수 있습니다.
Amazon Athena 는 실행된 쿼리에 대해서만 비용을 청구하고 쿼리당 지불 가격 모델을
제공하므로 정기적인 쿼리에 비용 효율적인 옵션입니다.
다른 옵션은 비용 효율적이지 않거나 사용 사례에 적합하지 않기 때문에 올바르지 않습니다.
Amazon FSx 파일 게이트웨이 모드에서 온프레미스로 AWS Storage Gateway 를 배포하는
것은 올바르지 않습니다. 이 모드는 사용 사례에 필요하지 않은 AWS 의 완전 관리형
Windows 파일 공유에 대한 지연 시간이 짧은 액세스를 제공하기 때문입니다. Amazon
S3 에 있는 데이터를 쿼리하기 위해 EMR 파일 시스템(EMRFS)을 사용하여 Amazon EMR
클러스터를 설정하는 것은 올바르지 않습니다. 이 옵션에는 EC2 인스턴스 클러스터 설정
및 관리가 포함되어 솔루션에 복잡성과 비용이 추가되기 때문입니다. Amazon S3 에 있는
데이터를 쿼리하도록 Amazon Redshift 클러스터를 설정하는 것은 올바르지 않습니다. 이
옵션에는 솔루션에 오버헤드와 비용을 추가하는 노드 클러스터의 프로비저닝 및 관리도
포함되기 때문입니다.
~~~

---

# Q599 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/119530-exam-aws-certified-sol
utions-architect-associate-saa-c03/
A,C,D??
~~~

---

# Q600 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/121205-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~