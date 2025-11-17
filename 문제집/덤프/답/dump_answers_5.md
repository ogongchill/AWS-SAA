# Q401 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/102170-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명1:
A(O) : Amazon RDS 다중 AZ 배포에서 Amazon RDS는 자동으로 프라이머리 데이터베이스
DB 인스턴스를 생성하고 동시에 다른 AZ 의 인스턴스에 데이터를 복제합니다. 장애를
감지하면 Amazon RDS는 수동 개입 없이 자동으로 대기 인스턴스로 장애 조치합니다.
https://aws.amazon.com/ko/rds/features/multi-az/
B(X) : Auto Scaling을 단일 가용 영역에서 사용하므로 고가용성 조건 불충족.
C(X) : 단일 가용 영역에서 읽기 전용 복제본이 있는 DB 인스턴스를 사용한다고 했으므로
고가용성 조건 불충족.
D(X) : 공유 스토리지가 아니라 read replica나 다중 AZ가 더 합리적.
설명2:
여러 가용 영역의 Auto Scaling 그룹에서 Amazon EC2 인스턴스를 사용하여 애플리케이션
서버를 배포합니다. 다중 AZ 구성에서 Amazon RDS DB 인스턴스를 사용합니다. 단일 장애
지점을 피하고 사용자 요구에 맞게 애플리케이션을 확장할 수 있는 기능을 제공하면서 기존
애플리케이션의 가용성과 탄력성을 높이려면 최상의 솔루션은 Auto Scaling 그룹의
Amazon EC2 인스턴스를 사용하여 애플리케이션 서버를 여러 그룹에 배포하는 것입니다.
가용 영역 및 다중 AZ 구성에서 Amazon RDS DB 인스턴스를 사용합니다. 다중 AZ
구성에서 Amazon RDS DB 인스턴스를 사용하면 데이터베이스가 여러 가용 영역에 걸쳐
자동으로 복제되므로 데이터베이스의 가용성이 높고 단일 가용 영역의 장애를 견딜 수
있습니다. 이는 내결함성을 제공하고 단일 실패 지점을 방지합니다.
~~~

---

# Q402 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/102175-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
Kinesis 데이터 스트림의 데이터 보존 기간은 레코드가 추가된 시점부터 더 이상 액세스할
수 없는 시점까지의 기간입니다. Kinesis 데이터 스트림의 기본 보존 기간은 24 시간이며
최대 8760 시간(365 일)까지 연장할 수 있습니다. 데이터 보존 기간은 AWS Management
Console, AWS CLI 또는 Kinesis Data Streams API를 사용하여 업데이트할 수 있습니다.
시나리오의 요구 사항을 충족하려면 솔루션 설계자가 데이터 보존 기간을 수정하여 Kinesis
Data Streams 기본 설정을 업데이트해야 합니다. 솔루션 설계자는 보존 기간을 데이터를
소비하고 S3 에 쓰는 빈도보다 크거나 같은 값으로 늘려야 합니다. 이렇게 하면 회사는
애플리케이션이 Kinesis Data Streams 로 보내는 모든 데이터를 S3 가 수신하도록 할 수
있습니다.
~~~

---

# Q403 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/102178-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
Amazon S3 에 파일을 업로드하기 위해 AWS Lambda 함수에 필요한 권한을 부여하려면
솔루션 설계자는 필요한 권한이 있는 IAM 실행 역할을 생성하고 IAM 역할을 Lambda
함수에 연결해야 합니다. 이 접근 방식은 최소 권한 원칙을 따르며 Lambda 함수가 특정
작업을 수행하는 데 필요한 리소스에만 액세스할 수 있도록 합니다.
~~~

---

# Q404 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/102180-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
이 애플리케이션의 아키텍처를 개선하기 위한 최상의 솔루션은 Amazon Simple Queue
Service(Amazon SQS)를 사용하여 요청을 버퍼링하고 Lambda 함수에서 S3 버킷을
분리하는 것입니다. 이렇게 하면 문서가 손실되지 않고 Lambda 함수를 사용할 수 없는
경우 나중에 처리할 수 있습니다. 이렇게 하면 문서가 손실되지 않고 Lambda 함수를
사용할 수 없는 경우 나중에 처리할 수 있습니다. Amazon SQS 를 사용하면 아키텍처가
분리되고 Lambda 함수가 확장 가능하고 내결함성 있는 방식으로 문서를 처리할 수
있습니다.
~~~

---

# Q405 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/102181-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
https://docs.aws.amazon.com/ko_kr/autoscaling/ec2/userguide/as-scaling-target-tracki
ng.html#target-tracking-choose-metrics
대상 추적 조정 정책은 지정된 메트릭과 대상 값을 기반으로 Auto Scaling 그룹의 용량을
조정하는 일종의 동적 조정 정책입니다. 대상 추적 조정 정책은 Auto Scaling 그룹에서
자동으로 확장 또는 축소하여 실제 지표 값을 대상 값 또는 그 근처에 유지할 수 있습니다.
대상 추적 조정 정책은 근무 시간과 같이 애플리케이션에 대한 로드가 예측할 수 없이 자주
변경되는 시나리오에 적합합니다.
시나리오의 요구 사항을 충족하기 위해 솔루션 설계자는 대상 추적 조정 정책을 사용하여
인스턴스 CPU 사용률에 따라 Auto Scaling 그룹을 조정해야 합니다. 인스턴스 CPU
사용률은 애플리케이션에 대한 수요를 반영하는 일반적인 메트릭입니다. 솔루션 설계자는
애플리케이션의 이상적인 평균 CPU 사용률 수준(예: 50%)을 나타내는 목표 값을 지정해야
합니다. 그러면 Auto Scaling 그룹이 해당 수준의 CPU 사용률을 유지하기 위해 확장 또는
축소됩니다.
예약된 조정은 날짜와 시간을 기준으로 조정 작업을 수행하는 일종의 조정 정책입니다.
예약된 조정은 주말과 같이 애플리케이션의 부하가 주기적으로 예측 가능하게 변경되는
시나리오에 적합합니다.
시나리오의 요구 사항을 충족하기 위해 솔루션 설계자는 예약된 조정을 사용하여 Auto
Scaling 그룹의 최소, 최대 및 원하는 용량을 주말 동안 0으로 변경해야 합니다.
이렇게 하면 Auto Scaling 그룹은 작동이 필요하지 않은 주말에 모든 인스턴스를
종료합니다. 솔루션 설계자는 Auto Scaling 그룹이 정상 작동을 재개할 수 있도록 주의
시작 시 기본값으로 되돌려야 합니다.
~~~

---

# Q406 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/102183-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q407 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/102184-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q408 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/102185-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
장치에서 데이터를 전송하는 지연 시간을 최소화하고 다른 AWS 영역으로 신속하게
페일오버해야 하는 요구 사항을 충족하기 위해 가장 좋은 솔루션은 네트워크 로드
밸런서(NLB) 및 Amazon Elastic Container Service(Amazon ECS)와 함께 AWS Global
Accelerator를 사용하는 것입니다.
AWS Global Accelerator 는 정적 IP 주소(Anycast)를 사용하여 트래픽을 최적의 AWS
끝점으로 라우팅하여 애플리케이션의 가용성과 성능을 향상시키는 서비스입니다. Global
Accelerator 를 사용하면 트래픽을 여러 지역 및 끝점으로 유도하고 다른 AWS 지역으로
자동 페일오버를 제공할 수 있습니다.
~~~

---

# Q409 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/102186-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
이 대답은 Windows IIS 웹 서버와 호환되는 온-프레미스 파일 공유에 대한 탄력적이고
내구성 있는 대체를 제공하기 때문에 정확합니다. Amazon FSx for Windows File Server는
Windows Server에 구축된 공유 파일 스토리지를 제공하는 완전 관리형 서비스입니다. SMB
프로토콜을 지원하고 Windows 기반 애플리케이션에 대한 원활한 액세스 및 인증을
가능하게 하는 Microsoft Active Directory 와 통합됩니다. Amazon FSx for Windows File
Server는 또한 다음과 같은 이점을 제공합니다.
복원력: Amazon FSx for Windows File Server 는 고가용성 및 장애 조치 보호를 제공하는
여러 가용 영역에 배포할 수 있습니다. 또한 자동 백업 및 복원은 물론 문제를 감지하고
수정하는 자가 치유 기능도 지원합니다.
내구성: Windows File Server 용 Amazon FSx 는 가용 영역 내외에서 데이터를 복제하고
내구성이 뛰어난 스토리지 장치에 데이터를 저장합니다. 또한 유휴 및 전송 중 암호화는
물론 파일 액세스 감사 및 데이터 중복 제거를 지원합니다.
성능: Windows File Server 용 Amazon FSx 는 파일 작업을 위한 일관된 1 밀리초 미만의
지연 시간과 높은 처리량을 제공합니다. 또한 SSD 스토리지, 분산 파일 시스템(DFS)
네임스페이스 및 복제와 같은 기본 Windows 기능, 사용자 중심 성능 확장을 지원합니다.
~~~

---

# Q410 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/102187-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
EBS 볼륨에 기록되는 모든 데이터가 유휴 상태에서 암호화되도록 보장하는 요구 사항을
충족하는 솔루션은 B 입니다. EBS 볼륨을 암호화된 볼륨으로 생성하고 암호화된 EBS
볼륨을 EC2 인스턴스에 연결합니다. EBS 볼륨을 생성할 때 볼륨 암호화 여부를 지정할 수
있습니다. 볼륨을 암호화하도록 선택한 경우 볼륨에 기록된 모든 데이터는 AWS 관리형
키를 사용하여 유휴 상태에서 자동으로 암호화됩니다. 또한 AWS KMS 에 저장된 고객
관리형 키(CMK)를 사용하여 EBS 볼륨을 암호화하고 보호할 수 있습니다. 암호화된 EBS
볼륨을 생성하고 EC2 인스턴스에 연결하여 볼륨에 기록된 모든 데이터가 유휴 상태에서
암호화되도록 할 수 있습니다.
~~~

---

# Q411 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/102188-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
Amazon RDS for MySQL 은 클라우드에서 MySQL 배포를 쉽게 설정, 운영 및 확장할 수
있는 완전관리형 관계형 데이터베이스 서비스입니다. Amazon Aurora Serverless는 Amazon
Aurora(MySQL 호환 버전)에 대한 온디맨드 자동 확장 구성으로, 데이터베이스가
애플리케이션의 요구 사항에 따라 자동으로 시작, 종료 및 용량 확장 또는 축소됩니다.
간헐적이거나 예측할 수 없는 워크로드를 위한 간단하고 비용 효율적인 옵션입니다.
~~~

---

# Q412 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/102189-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
S3 퍼블릭 액세스 차단 기능을 사용하면 계정 내의 S3 버킷 및 객체에 대한 퍼블릭
액세스를 제한할 수 있습니다. 버킷 정책 설정에 관계없이 계정 수준에서 이 기능을
활성화하여 S3 버킷이 공개되지 않도록 할 수 있습니다. AWS Organizations 를 사용하여
IAM 사용자가 이 설정을 변경하지 못하도록 SCP(서비스 제어 정책)를 계정에 적용하여
모든 S3 객체가 비공개로 유지되도록 할 수 있습니다. 이는 최소한의 운영 오버헤드가
필요한 간단하고 효과적인 솔루션입니다.
~~~

---

# Q413 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/102190-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
Amazon SES 는 기업이 자체 이메일 주소와 도메인을 사용하여 이메일을 보내고 받을 수
있도록 하는 비용 효율적이고 확장 가능한 이메일 서비스입니다. Amazon SES 를 통해
이메일을 보내도록 웹 인스턴스를 구성하는 것은 복잡한 이메일 전송 문제를 해결하는 데
소요되는 시간을 줄이고 운영 오버헤드를 최소화할 수 있는 간단하고 효과적인
솔루션입니다.
~~~

---

# Q414 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/103452-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q415 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/103404-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q416 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/103423-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
AWS 에서 호스팅되는 빠르게 성장하는 전자 상거래 웹 사이트의 느린 페이지 로드 문제를
해결하기 위해 솔루션 설계자는 다음 두 가지 조치를 취할 수 있습니다.
1. Amazon CloudFront 배포 설정
2. RDS DB 인스턴스에 대한 읽기 전용 복제본 생성
Amazon Redshift 클러스터 구성은 Redshift 가 데이터 웨어하우징 서비스이고 일반적으로
대량 데이터의 분석 처리에 사용되기 때문에 이 문제와 관련이 없습니다.
S3 는 웹 애플리케이션 서버가 아니라 객체 스토리지 서비스이기 때문에 Amazon S3 에서
동적 웹 콘텐츠를 호스팅해도 성능이 반드시 향상되는 것은 아닙니다. S3 는 정적 웹
콘텐츠를 호스팅하는 데 사용할 수 있지만 S3 는 서버 측 스크립팅 또는 처리를 지원하지
않기 때문에 동적 웹 콘텐츠를 호스팅하는 데 적합하지 않을 수 있습니다.
RDS DB 인스턴스에 대해 다중 AZ 배포를 구성하면 고가용성이 향상되지만 반드시 성능이
향상되는 것은 아닙니다.
~~~

---

# Q417 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/103598-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
Compute Savings Plan 을 구매함으로써 회사는 EC2 인스턴스와 Lambda 기능을 모두
실행하는 비용을 절약할 수 있습니다. Lambda 함수는 AWS 서비스용 VPC 엔드포인트 또는
VPC 피어링 연결을 통해 EC2 인스턴스가 포함된 프라이빗 서브넷에 연결할 수 있습니다.
이렇게 하면 사설 네트워크 내에서 트래픽을 유지하면서 EC2 인스턴스에 대한 직접
네트워크 액세스를 제공하여 네트워크 대기 시간을 최소화하는 데 도움이 됩니다. Lambda
함수의 지속 시간, 메모리 사용량, 호출 수 및 전송된 데이터 양을 최적화하면 비용을
추가로 최소화하고 성능을 개선하는 데 도움이 될 수 있습니다. 또한 프라이빗 서브넷을
사용하면 보안 모범 사례인 퍼블릭 인터넷에서 EC2 인스턴스에 직접 액세스할 수 없도록
하는 데 도움이 됩니다.
~~~

---

# Q418 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/103585-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q419 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109268-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
서비스 제어 정책(SCP)은 조직에서 권한을 관리하는 데 사용할 수 있는 정책 유형입니다.
SCP 는 조직의 모든 계정에 대해 사용 가능한 최대 권한에 대한 중앙 제어를 제공하므로
계정이 조직의 액세스 제어 지침을 준수하도록 할 수 있습니다.
ec2:Encrypted 조건이 false 일 때 SCP 를 사용하여 ec2:CreateVolume 작업을 거부할 수
있습니다. 즉, 루트 OU 아래 계정의 모든 사용자 또는 역할은 암호화되지 않은 EBS
볼륨을 생성할 수 없습니다. 이 솔루션은 필요에 따라 암호화된 볼륨을 계속 생성할 수
있으므로 EBS 볼륨을 생성하는 직원에게 최소한의 영향을 미칩니다.
참조:
https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps
.html
~~~

---

# Q420 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109269-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q421 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109270-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q422 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109280-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:・
이 대답은 불규칙하고 예측할 수 없는 사용 패턴을 처리할 수 있는 독립적인 마이크로
서비스로 ML 모델을 실행하기 위한 요구 사항을 충족하기 때문에 정확합니다. API 의
요청을 Amazon SQS 대기열로 보내면 회사는 모델 실행에서 요청 처리를 분리하고 수요
급증으로 인해 요청이 손실되지 않도록 할 수 있습니다. 대기열에서 읽는 Amazon ECS
서비스로 모델을 배포함으로써 회사는 컨테이너를 활용하여 각 모델을 마이크로 서비스로
격리 및 패키징하고 시작 시 S3 에서 모델 데이터를 가져올 수 있습니다. 대기열 크기에
따라 서비스의 클러스터와 복사본 모두에 대해 Amazon ECS 에서 AWS Auto Scaling 을
활성화함으로써 회사는 클러스터의 EC2 인스턴스 수와 각 서비스의 작업 수를 성능을
요구하고 최적화합니다.
참조:
https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welc
ome.html
https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html
https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-ecs.html
~~~

---

# Q423 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109281-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q424 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109283-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q425 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109282-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
이 답변은 기존 데이터를 AWS 로 안전하게 마이그레이션하는 요구 사항을 충족하고 새로운
규정을 충족하기 때문에 정답입니다. AWS DataSync는 온프레미스 스토리지와 Amazon S3
간에 대량의 데이터를 온라인으로 쉽게 이동할 수 있게 해주는 서비스입니다. DataSync 는
전송 중인 데이터를 자동으로 암호화하고 전송 중에 데이터 무결성을 확인합니다. AWS
CloudTrail 은 계정에 대한 AWS API 호출을 기록하고 로그 파일을 Amazon S3 에 전달하는
서비스입니다. CloudTrail 은 S3 객체 수준 API 활동과 같이 AWS 계정의 리소스에서 또는
리소스 내에서 수행된 리소스 작업을 보여주는 데이터 이벤트를 기록할 수 있습니다.
CloudTrail 을 사용하여 데이터 이벤트를 기록하면 저장된 데이터의 모든 수준에서 액세스를
감사할 수 있습니다.
참조:
https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html
https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-withcl
oudtrail.html
~~~

---

# Q426 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109278-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q427 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109279-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:・
AWS Elastic Beanstalk 는 애플리케이션을 쉽고 빠르게 배포, 관리 및 확장할 수 있는
방법을 제공합니다. Java 및 Apache Tomcat을 포함한 다양한 플랫폼을 지원합니다. 솔루션
설계자는 Elastic Beanstalk를 사용하여 Java 애플리케이션을 업로드하고 Apache Tomcat을
실행하도록 환경을 구성할 수 있습니다.
~~~

---

# Q428 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109285-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:・
옵션 B 는 Lambda 를 신뢰할 수 있는 서비스로 포함하는 IAM 역할을 생성할 것을
제안합니다. 즉, 이 역할은 Lambda 함수용으로 특별히 설계되었습니다. 역할에는
DynamoDB 테이블에 대한 필수 읽기 및 쓰기 액세스 권한을 부여하는 정책이 연결되어
있어야 합니다.
~~~

---

# Q429 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109286-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:・
이 답변은 그룹 구성원에 대한 IAM 정책의 영향을 반영하기 때문에 정확합니다. 정책에는
두 개의 문이 있습니다. 하나는 허용 효과가 있고 다른 하나는 거부 효과가 있습니다. Allow
문은 us-east-1 지역 내의 모든 리소스에 대해 EC2 작업을 수행할 수 있는 권한을
부여합니다. Deny 문은 Allow 문을 재정의하고 그룹 구성원이 MFA 로 로그인하지 않는 한
us-east-1 리전 내의 모든 리소스에 대해 ec2:StopInstances 및 ec2:TerminateInstances
작업을 수행할 수 있는 권한을 거부합니다. 따라서 그룹 구성원은 모든 작업을 수행할 수
있습니다. MFA 를 사용하지 않는 한 us-east-1 리전에서 인스턴스 중지 또는 종료를
제외한 EC2 작업.
~~~

---

# Q430 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109288-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:・
이러한 답변은 .csv 파일을 이미지로 변환하고 가능한 한 빨리 사용 가능하게 하며
스토리지 비용을 최소화하기 위한 요구 사항을 충족하므로 정확합니다. AWS Lambda 는
서버를 프로비저닝하거나 관리하지 않고 코드를 실행할 수 있는 서비스입니다. AWS
Lambda 를 사용하여 .csv 파일을 이미지로 변환하고 이미지를 S3 버킷에 저장하는 함수를
설계할 수 있습니다.
S3 이벤트 알림을 사용하여 .csv 파일이 S3 버킷에 업로드될 때 Lambda 함수를 호출할
수 있습니다. 이렇게 하면 이미지가 생성되어 그래픽 보고서에 가능한 한 빨리 사용할 수
있습니다. S3 수명 주기는 개체가 수명 주기 동안 비용 효율적으로 저장되도록 개체를
관리할 수 있게 해주는 기능입니다. S3 버킷의 .csv 파일 및 이미지 파일에 대한 S3 수명
주기 규칙을 생성하여 비즈니스 요구 사항에 따라 다른 스토리지 클래스로 전환하거나
만료할 수 있습니다. .csv 파일은 몇 주 전에 계획된 ML 교육 및 감사에 1 년에 두 번만
필요하므로 업로드한 지 1일 후에 S3 Standard에서 S3 Glacier로 전환할 수 있습니다. S3
Glacier는 검색 시간이 몇 분에서 몇 시간에 이르는 안전하고 내구성이 있으며 매우 저렴한
스토리지를 제공하는 데이터 아카이빙용 스토리지 클래스입니다.
이미지 파일은 1개월이 지나면 관련성이 없어지므로 30일 후에 만료될 수 있습니다.
참조:
https://docs.aws.amazon.com/lambda/latest/dg/welcome.html
https://docs.aws.amazon.com/AmazonS3/latest/userguide/NotificationHowTo.html
https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html
https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html#sc-
glacier
~~~

---

# Q431 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109274-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:・
이 답변은 거의 실시간으로 상위 10 개 점수판을 표시하고 현재 점수를 유지하면서 게임을
중지하고 복원할 수 있는 기능을 제공하는 요구 사항을 충족하므로 정확합니다. Redis 용
Amazon ElastiCache 는 인터넷 규모의 실시간 애플리케이션을 지원하기 위해 1 밀리초
미만의 지연 시간을 제공하는 초고속 인 메모리 데이터 스토어입니다. Redis 용 Amazon
ElastiCache 를 사용하여 Redis 용 ElastiCache 클러스터를 설정하여 웹 애플리케이션이
표시할 점수를 계산하고 캐시할 수 있습니다. 정렬된 세트 및 해시와 같은 Redis 데이터
구조를 사용하여 플레이어의 점수를 저장하고 순위를 매길 수 있으며 ZRANGE 및 ZADD와
같은 Redis 명령을 사용하여 점수를 효율적으로 검색 및 업데이트할 수 있습니다. 또한
스냅샷 및 추가 전용 파일(AOF)과 같은 Redis 지속성 기능을 사용하여 데이터의 특정 시점
복구를 활성화할 수 있으므로 현재 점수를 유지하면서 게임을 중지하고 복원할 수
있습니다.
참조:
https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/WhatIs.html
https://redis.io/topics/data-types
https://redis.io/topics/persistence
~~~

---

# Q432 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109291-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q433 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109384-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q434 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109294-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
이 답변은 기존 데이터를 AWS 로 안전하게 마이그레이션하는 요구 사항을 충족하고 새로운
규정을 충족하기 때문에 정답입니다. AWS DataSync는 온프레미스 스토리지와 Amazon S3
간에 대량의 데이터를 온라인으로 쉽게 이동할 수 있게 해주는 서비스입니다. DataSync 는
전송 중인 데이터를 자동으로 암호화하고 전송 중에 데이터 무결성을 확인합니다. AWS
CloudTrail 은 계정에 대한 AWS API 호출을 기록하고 로그 파일을 Amazon S3 에 전달하는
서비스입니다. CloudTrail 은 S3 객체 수준 API 활동과 같이 AWS 계정의 리소스에서 또는
리소스 내에서 수행된 리소스 작업을 보여주는 데이터 이벤트를 기록할 수 있습니다.
CloudTrail 을 사용하여 데이터 이벤트를 기록하면 저장된 데이터의 모든 수준에서 액세스를
감사할 수 있습니다.
참조:
https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html
https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-withcl
oudtrail.html
~~~

---

# Q435 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109377-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
이 대답은 가동 중지 시간을 최소화하고 비용 효율적으로 2 주 이내에 20TB MySQL
데이터베이스를 마이그레이션해야 하는 요구 사항을 충족하기 때문에 정답입니다. AWS
Snowball Edge Storage Optimized 디바이스에는 최대 80TB 의 사용 가능한 스토리지
공간이 있으며 이는 데이터베이스에 적합합니다. AWS Database Migration Service(AWS
DMS)는 소스에서 대상으로 변경 사항을 지속적으로 복제하여 다운타임을 최소화하면서
MySQL 에서 Amazon Aurora, Amazon RDS for MySQL 또는 Amazon EC2 의 MySQL 로
데이터를 마이그레이션할 수 있습니다. AWS Schema Conversion Tool(AWS SCT)은 소스
스키마와 코드를 대상 데이터베이스와 호환되는 형식으로 변환할 수 있습니다. 이러한
서비스를 함께 사용함으로써 회사는 가동 중지 시간과 비용을 최소화하면서 데이터베이스를
AWS로 마이그레이션할 수 있습니다.
Snowball Edge 디바이스를 다시 AWS 로 배송하여 마이그레이션을 완료하고
데이터베이스가 완전히 마이그레이션될 때까지 지속적인 복제를 계속할 수 있습니다.
참조:
https://docs.aws.amazon.com/snowball/latest/developer-guide/device-differences.html
https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MySQL.html
https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Source.My
SQL.htm
~~~

---

# Q436 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109277-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:・
이 대답은 인프라를 추가하지 않고 비용을 최소화하지 않고 더 큰 워크로드를 수용하는
요구 사항을 충족하기 때문에 맞습니다. 예약 DB 인스턴스는 계정에서 특정 온디맨드 DB
인스턴스 사용에 적용되는 청구 할인입니다. 예약 DB 인스턴스는 온디맨드 DB 인스턴스
요금에 비해 상당한 할인을 제공합니다. 총 워크로드에 대해 예약된 DB 인스턴스를
구입하고 선결제 없음, 부분 선결제 또는 전체 선결제의 세 가지 결제 옵션 중에서 선택할
수 있습니다. 인스턴스 유형을 더 높은 성능 클래스로 수정하여 Amazon RDS for
PostgreSQL DB 인스턴스를 더 크게 만들 수 있습니다. 이렇게 하면 DB 인스턴스의 CPU,
메모리 및 네트워크 용량을 늘리고 늘어난 워크로드를 처리할 수 있습니다.
참조:
https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithReserved
DBInstances.html
https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.
html
~~~

---

# Q437 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109378-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:・
이 답변은 합법적인 사용자에게 최소한의 영향을 미치는 방식으로 불법적으로 들어오는
요청을 차단하는 요구 사항을 충족하기 때문에 정확합니다. AWS WAF 는 가용성에 영향을
미치거나 보안을 손상시키거나 과도한 리소스를 소비할 수 있는 일반적인 웹
익스플로잇으로부터 웹 애플리케이션 또는 API 를 보호하는 데 도움이 되는 웹
애플리케이션 방화벽입니다. AWS WAF 는 SQL 삽입 또는 사이트 간 스크립팅과 같은
일반적인 공격 패턴을 차단하는 보안 규칙과 정의한 특정 트래픽 패턴을 필터링하는 규칙을
생성할 수 있도록 하여 트래픽이 애플리케이션에 도달하는 방식을 제어할 수 있습니다.
AWS WAF 를 ALB 와 연결하여 악의적인 요청으로부터 웹 애플리케이션을 보호할 수
있습니다. 각 발신 IP 주소에 대한 요청 속도를 추적하고 5분 이내에 특정 제한을 초과하는
IP 주소의 요청을 차단하도록 AWS WAF에서 속도 제한 규칙을 구성할 수 있습니다. 이렇게
하면 잠재적인 DDoS 공격을 완화하고 웹 사이트의 성능을 향상시킬 수 있습니다.
참조:
https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html
https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-rate-
based.html
~~~

---

# Q438 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109398-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:・
이 대답은 안전한 방식으로 감사자와 데이터베이스를 공유하는 요구 사항을 충족하기
때문에 정확합니다. AWS Key Management Service(AWS KMS)를 사용하여 데이터베이스의
암호화된 스냅샷을 생성하여 고객 관리형 키로 스냅샷을 암호화할 수 있습니다. 스냅샷의
권한을 수정하고 감사자의 AWS 계정 ID 를 지정하여 감사자와 스냅샷을 공유할 수
있습니다. 감사자의 계정에 권한을 부여하는 키 정책 설명을 추가하여 AWS KMS 암호화
키에 대한 액세스를 허용할 수도 있습니다. 이렇게 하면 감사자만 자신의 AWS 계정에서
스냅샷에 액세스하고 복원할 수 있습니다.
참조:
https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ShareSnapshot.html
https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html#key-policy-
defaultallow-root-enable-iam
~~~

---

# Q439 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109400-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q440 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109297-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:・
이러한 답변은 최신 백업에서 새 DB 인스턴스를 생성하고 Amazon Aurora 의 MySQL 호환
에디션을 사용하여 DB 인스턴스를 호스팅해야 하는 요구 사항을 충족하기 때문에
정확합니다. MySQL DB 인스턴스와 Aurora DB 클러스터가 동일한 버전의 MySQL 을 실행
중인 경우 RDS 스냅샷을 Aurora 로 직접 가져올 수 있습니다. 예를 들어 MySQL 버전 5.6
스냅샷을 Aurora MySQL 버전 5.6 으로 직접 복원할 수 있지만 MySQL 버전 5.6 스냅샷을
Aurora MySQL 버전 5.7로 직접 복원할 수는 없습니다. 이 방법은 간단하고 가장 적은 수의
단계가 필요합니다. MySQL DB 인스턴스와 Aurora DB 클러스터가 다른 버전의 MySQL 을
실행 중인 경우 데이터베이스 덤프를 Amazon S3에 업로드한 다음 Aurora로 데이터베이스
덤프를 가져올 수 있습니다. 예를 들어 MySQL 버전 5.6 데이터베이스 덤프를 Aurora
MySQL 버전 5.7 로 가져올 수 있지만 MySQL 버전 5.6 스냅샷을 Aurora MySQL 버전
5.7로 직접 복원할 수는 없습니다.
이 방법은 더 유연하며 다른 버전의 MySQL 간에 마이그레이션할 수 있습니다.
참조:
https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Migrati
ng.RDSMySQL.Import.html
https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Migrati
ng.RDSMySQL.Dump.html
~~~

---

# Q441 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109423-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:・
이 대답은 비용을 최적화하고 데이터베이스의 작업 부하를 줄이는 요구 사항을 충족하므로
정확합니다. Amazon CloudFront는 .html, .css, .js 및 이미지 파일과 같은 정적 및 동적 웹
콘텐츠를 사용자에게 빠르게 배포하는 콘텐츠 전송 네트워크(CDN) 서비스입니다.
CloudFront 는 엣지 로케이션이라고 하는 전 세계 데이터 센터 네트워크를 통해 콘텐츠를
제공합니다. CloudFront에서 제공하는 콘텐츠를 사용자가 요청하면 지연 시간(시간 지연)이
가장 짧은 엣지 로케이션으로 요청이 라우팅되므로 콘텐츠가 가능한 최상의 성능으로
제공됩니다. Amazon CloudFront 배포를 생성하여 CloudFront 에 대해 정의하는 오리진인
Amazon S3 버킷에서 정적 웹 콘텐츠를 호스팅할 수 있습니다.
이렇게 하면 정적 웹 콘텐츠에 대한 요청을 EC2 인스턴스에서 CloudFront 로 오프로드할
수 있으므로 웹 사이트의 성능과 가용성을 개선하고 EC2 인스턴스 실행 비용을 줄일 수
있습니다.
참조:
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.ht
ml
https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteHosting.html
~~~

---

# Q442 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109647-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q443 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109424-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q444 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109426-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:・
이 대답은 응용 프로그램 인프라의 안정성을 최대화하기 위한 요구 사항을 충족하기 때문에
정확합니다. DB 인스턴스를 다중 AZ로 업데이트할 수 있습니다. 즉, Amazon RDS 가 다른
가용 영역에서 동기식 대기 복제본을 자동으로 프로비저닝하고 유지합니다. 기본 DB
인스턴스는 가용 영역 전체에서 대기 복제본으로 동기식으로 복제되어 데이터 중복성을
제공하고 시스템 백업 중에 지연 시간 급증을 최소화합니다.
고가용성으로 DB 인스턴스를 실행하면 계획된 시스템 유지 관리 중에 가용성을 높일 수
있습니다. 또한 DB 인스턴스 장애 및 가용 영역 중단으로부터 데이터베이스를 보호하는 데
도움이 될 수 있습니다. 또한 DB 인스턴스에서 삭제 보호를 활성화하여 어떤 사용자도 DB
인스턴스를 삭제하지 못하도록 할 수 있습니다. 여러 가용 영역에서 EC2 인스턴스와 같은
여러 대상에 수신 애플리케이션 트래픽을 분산하는 Application Load Balancer 뒤에 EC2
인스턴스를 배치할 수 있습니다. 이렇게 하면 애플리케이션의 가용성과 내결함성이
향상됩니다.
여러 가용 영역의 EC2 Auto Scaling 그룹에서 EC2 인스턴스를 실행할 수 있으므로
애플리케이션 로드를 처리하는 데 사용할 수 있는 정확한 수의 EC2 인스턴스를 확보할 수
있습니다. 조정 정책을 사용하여 수요 변화에 따라 Auto Scaling 그룹의 인스턴스 수를
조정할 수 있습니다.
참조:
https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZSingleStan
dby.html
https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DeleteInstance.html#
USER_DeleteInstance.DeletionProtection
https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html
https://docs.aws.amazon.com/autoscaling/ec2/userguide/AutoScalingGroup.html
~~~

---

# Q445 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109403-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:・
이 답변은 중단 없이 데이터를 효율적으로 이동하고 전송 기간 동안 데이터에 계속
액세스하고 업데이트할 수 있어야 한다는 요구 사항을 충족하기 때문에 정답입니다. AWS
DataSync는 AWS로의 데이터 마이그레이션을 간소화 및 가속화하고 온프레미스 스토리지,
엣지 로케이션, 기타 클라우드 및 AWS 스토리지 간에 데이터를 빠르고 안전하게 이동할 수
있도록 지원하는 온라인 데이터 이동 및 검색 서비스입니다. 회사 데이터 센터에서 AWS
DataSync 에이전트를 생성하여 Direct Connect 연결을 통해 NAS 시스템을 AWS에 연결할
수 있습니다. 데이터 전송 작업을 생성하여 소스 위치, 대상 위치 및 데이터 전송 옵션을
지정할 수 있습니다. Amazon S3 버킷으로 전송을 시작하고 작업 진행 상황을 모니터링할
수 있습니다.
DataSync 는 전송 중인 데이터를 자동으로 암호화하고 전송 중에 데이터 무결성을
확인합니다. DataSync 는 증분 전송도 지원합니다. 즉, 마지막 전송 이후 변경된 파일만
복사됩니다. 이렇게 하면 NAS 시스템과 S3 버킷 간에 데이터가 동기화되었는지 확인할 수
있으며 전송 기간 동안 데이터에 액세스하고 데이터를 업데이트할 수 있습니다.
참조:
https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html
https://docs.aws.amazon.com/datasync/latest/userguide/how-datasync-works.html
~~~

---

# Q446 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109404-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q447 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109405-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q448 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109499-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:・
이 답변은 관리 VPC 와 데이터 센터 간의 VPN 연결에 중복성을 제공하기 때문에
정답입니다. 하나의 고객 게이트웨이 디바이스 또는 하나의 VPN 터널을 사용할 수 없게
되더라도 트래픽은 여전히 두 번째 고객 게이트웨이 디바이스와 두 번째 VPN 터널을 통해
흐를 수 있습니다. 이렇게 하면 VPN 연결의 단일 실패 지점이 완화됩니다.
참조:
https://docs.aws.amazon.com/vpn/latest/s2svpn/vpn-redundant-connection.html
https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/VPC/vpn-tunnelr
edundancy.html
~~~

---

# Q449 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109432-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q450 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109406-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q451 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109408-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q452 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109521-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q453 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109410-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
AWS Backup 은 컴퓨팅, 스토리지 및 데이터베이스 전반에서 AWS 서비스의 데이터 보호를
중앙 집중화하고 자동화할 수 있는 완전 관리형 서비스입니다. AWS Backup Vault Lock 은
백업 볼트에 대한 보안 및 제어를 강화하는 데 도움이 되는 백업 볼트의 선택적 기능입니다.
규정 준수 모드에서 잠금이 활성화되고 유예 시간이 끝나면 고객, 계정/데이터 소유자 또는
AWS 가 볼트 구성을 변경하거나 삭제할 수 없습니다. 이렇게 하면 보존 기간이 만료되고
규정 요구 사항을 충족할 때까지 백업을 사용할 수 있습니다.
참조:
https://docs.aws.amazon.com/aws-backup/latest/devguide/vaultlock.html
~~~

---

# Q454 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109433-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
Workload Discovery on AWS(이전에는 AWS Perspective 라고 함)는 AWS 클라우드
워크로드를 시각화하는 도구입니다. 계정과 리전 전체에서 AWS 리소스의 인벤토리를
유지하고 이들 간의 관계를 매핑하고 웹 UI 에 표시합니다. 또한 AWS 비용 및 사용 보고서
쿼리, 리소스 검색, 아키텍처 다이어그램 저장 및 내보내기 등을 수행할 수 있습니다.
솔루션은 AWS 에서 Workload Discovery 를 사용하여 최소한의 운영 노력으로 모든
계정에서 다양한 워크로드의 관계 세부 정보를 구축하고 매핑할 수 있습니다.
1. AWS Systems Manager Inventory 를 사용하여 상세 보기 보고서에서 지도 보기를
생성합니다. AWS Systems Manager Inventory 는 관리형 인스턴스에서 메타데이터를
수집하여 중앙 Amazon S3 버킷에 저장하는 기능이므로 이 솔루션은 모든 계정에서 다양한
워크로드의 관계 세부 정보를 구축하고 매핑해야 하는 요구 사항을 충족하지 않습니다.
워크로드의 맵 보기 또는 아키텍처 다이어그램을 제공하지 않습니다.
2. AWS Step Functions를 사용하여 워크로드 세부 정보를 수집합니다. 워크로드의 아키텍처
다이어그램을 수동으로 구축합니다. 이 솔루션은 워크로드 세부 정보 수집을
오케스트레이션하고 아키텍처 다이어그램을 수동으로 구축하기 위해 상태 시스템을 생성 및
관리해야 하므로 최소한의 운영 노력 요구 사항을 충족하지 않습니다.
3. AWS X-Ray 를 사용하여 워크로드 세부 정보 보기 관계가 있는 아키텍처 다이어그램을
구축합니다. 이 솔루션은 워크로드 세부 정보를 수집하고 아키텍처 다이어그램을 수동으로
구축하기 위해 X-Ray SDK 로 애플리케이션을 구성해야 하므로 최소한의 운영 노력 요구
사항을 충족하지 않습니다.
참조:
https://aws.amazon.com/solutions/implementations/workload-discovery-on-aws/
~~~

---

# Q455 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109522-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q456 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109523-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q457 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109524-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q458 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109435-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q459 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109440-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q460 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109525-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
Amazon AppFlow 는 사용자가 SaaS 애플리케이션과 AWS 서비스 간에 안전하게 데이터를
전송할 수 있도록 하는 완전관리형 통합 서비스입니다. Salesforce를 소스로, Amazon S3를
대상으로 지원합니다. 또한 AWS KMS CMK 를 사용하여 유휴 데이터 암호화 및
SSL/TLS1 을 사용하여 전송 중인 데이터 암호화를 지원합니다. Amazon AppFlow 를
사용하면 솔루션이 최소한의 개발 노력으로 요구 사항을 충족할 수 있습니다.
1. 데이터를 Salesforce 에서 Amazon S3 로 안전하게 전송하는 AWS Lambda 함수를
생성합니다. 이 솔루션은 Salesforce 및 Amazon S3 API 와 상호 작용하고 인증, 암호화,
오류 처리 및 모니터링을 처리하기 위한 사용자 지정 코드 작성을 포함하므로 최소한의
개발 노력 요구 사항을 충족하지 않습니다.
2. AWS Step Functions 워크플로 생성 Salesforce 에서 Amazon S3 로 데이터를 안전하게
전송하는 작업을 정의합니다. 이 솔루션은 데이터 전송 작업을 오케스트레이션하기 위한
상태 시스템 정의를 생성하고 실제 데이터 전송을 수행하기 위해 Lambda 함수 또는 기타
서비스를 호출하기 때문에 최소한의 개발 노력 요구 사항을 충족하지 않습니다.
3. Salesforce 용 사용자 지정 커넥터를 생성하여 Salesforce 에서 Amazon S3 로 데이터를
안전하게 전송합니다. 이 솔루션은 Amazon AppFlow 사용자 지정 커넥터 SDK 를 사용하여
Salesforce 용 사용자 지정 커넥터를 구축하고 배포하므로 추가 구성 및 관리가 필요하므로
최소한의 개발 노력 요구 사항을 충족하지 않습니다.
참조: https://aws.amazon.com/appflow/
~~~

---

# Q461 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109446-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
AWS Global Accelerator 는 글로벌 사용자를 위해 애플리케이션의 성능과 가용성을
향상시키는 네트워킹 서비스입니다. AWS 글로벌 네트워크를 사용하여 사용자 트래픽을
성능 및 상태에 따라 최적의 엔드포인트로 라우팅합니다. 또한 애플리케이션에 대한 고정
진입점 역할을 하고 TCP 및 UDP 프로토콜을 모두 지원하는 고정 IP 주소를 제공합니다.
솔루션은 AWS Global Accelerator 를 사용하여 모든 사용자에게 가능한 최저 지연 시간을
보장할 수 있습니다.
1. AWS Global Accelerator 를 사용하여 가속기를 생성합니다. Global Accelerator 통합을
사용하고 TCP 및 UDP 포트에서 수신 대기하는 가속기 엔드포인트 뒤에 Application Load
Balancer(ALB)를 생성합니다. Auto Scaling 그룹을 업데이트하여 ALB 에 인스턴스를
등록합니다. ALB는 UDP 프로토콜을 지원하지 않으므로 이 솔루션은 작동하지 않습니다.
2. Amazon CloudFront 콘텐츠 전송 네트워크(CDN) 엔드포인트를 생성합니다. 엔드포인트
뒤에 NLB(Network Load Balancer)를 생성하고 TCP 및 UDP 포트에서 수신 대기합니다.
Auto Scaling 그룹을 업데이트하여 NLB 에 인스턴스를 등록합니다. NLB 를 오리진으로
사용하도록 CloudFront 를 업데이트합니다. CloudFront 는 UDP 프로토콜을 지원하지
않으므로 이 솔루션은 작동하지 않습니다.
3. Amazon CloudFront 콘텐츠 전송 네트워크(CDN) 엔드포인트를 생성합니다. 엔드포인트
뒤에 Application Load Balancer(ALB)를 생성하고 TCP 및 UDP 포트에서 수신 대기합니다.
Auto Scaling 그룹을 업데이트하여 ALB 에 인스턴스를 등록합니다. ALB 를 오리진으로
사용하도록 CloudFront 를 업데이트합니다. CloudFront 및 ALB 는 UDP 프로토콜을
지원하지 않으므로 이 솔루션은 작동하지 않습니다.
참조: https://aws.amazon.com/global-accelerator/
~~~

---

# Q462 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109653-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
Amazon SQS는 마이크로서비스, 분산 시스템 및 서버리스 애플리케이션을 분리하고 확장할
수 있는 완전관리형 메시지 대기열 서비스입니다. 애플리케이션은 SQS 대기열에 주문을
기록함으로써 주문 손실 없이 트래픽 급증을 처리할 수 있습니다. Auto Scaling 그룹의 EC2
인스턴스는 SQS 대기열에서 읽고 꾸준한 속도로 데이터베이스로 주문을 처리할 수
있습니다. Application Load Balancer 는 EC2 인스턴스에 부하를 분산하고 상태 확인을
제공할 수 있습니다. 이 솔루션은 질문의 모든 요구 사항을 충족하지만 다른 옵션은 그렇지
않습니다.
참조:
https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html
https://aws.amazon.com/architecture/serverless/
https://aws.amazon.com/sqs/
~~~

---

# Q463 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109501-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q464 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109449-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
기존 단일 AZ DB 인스턴스를 다중 AZ 배포로 변환하려면 AWS Management Console에서
DB 인스턴스에 해당하는 "수정" 옵션을 사용하십시오.
참고:
https://aws.amazon.com/rds/features/multi-az/
~~~

---

# Q465 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109655-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q466 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109450-exam-aws-certified-sol
utions-architect-associate-saa-c03/
참고:
https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-add-availability-zone.html
~~~

---

# Q467 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109485-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q468 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109451-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q469 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109452-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
S3 Intelligent-Tiering은 액세스 빈도에 따라 가장 비용 효율적인 액세스 계층으로 데이터를
이동하여 스토리지 비용을 자동으로 줄이는 스토리지 클래스입니다. 여기에는 빈번한
액세스와 드문 액세스의 두 가지 액세스 계층이 있습니다. 데이터는 기본적으로 빈번한
액세스 계층에 저장되며 연속 30 일 동안 액세스가 없으면 빈번하지 않은 액세스 계층으로
이동됩니다. 데이터에 다시 액세스하면 자주 액세스하는 tier1 로 다시 이동됩니다. S3 수명
주기 규칙을 사용하여 개체를 S3 Standard 에서 S3 Intelligent-Tiering 으로 전환함으로써
솔루션은 액세스 패턴을 알 수 없거나 변경하는 데이터에 대한 S3 비용을 줄일 수
있습니다.
1. S3 복제를 사용하여 자주 액세스하지 않는 객체를 S3 Standard-Infrequent Access(S3
Standard-IA)로 전환합니다. 이 솔루션은 액세스 패턴을 알 수 없거나 변경하는 데이터에
대한 S3 비용 절감 요구 사항을 충족하지 않습니다. S3 복제는 중복성 또는 규정 준수를
위해 버킷 또는 리전 간에 개체를 복사하는 기능이기 때문입니다. 액세스 빈도에 따라
개체를 다른 스토리지 클래스로 자동으로 이동하지 않습니다.
2. S3 수명 주기 규칙을 사용하여 객체를 S3 Standard에서 Standard-Infrequent Access(S3
Standard-IA)로 전환합니다. 이 솔루션은 액세스 패턴을 알 수 없거나 변경하는 데이터에
대한 S3 비용 절감 요구 사항을 충족하지 않습니다. S3 Standard-IA 는 S3 Standard 보다
낮은 스토리지 비용을 제공하지만 데이터 액세스에 대한 검색 요금을 부과하는 스토리지
클래스이기 때문입니다. 액세스 패턴이 변화하는 데이터가 아니라 수명이 길고 자주
액세스하지 않는 데이터에 적합합니다.
3. S3 Inventory를 사용하여 S3 Standard에서 S3 Intelligent-Tiering으로 액세스하지 않은
객체를 식별하고 전환합니다. 이 솔루션은 액세스 패턴을 알 수 없거나 변경하는 데이터에
대한 S3 비용 절감 요구 사항을 충족하지 않습니다. S3 Inventory 는 버킷의 객체 및 해당
메타데이터에 대한 보고서를 매일 또는 매주 제공하는 기능이기 때문입니다. 액세스 빈도에
따라 개체를 다른 스토리지 클래스로 자동으로 이동하지 않습니다.
참조 URL: https://aws.amazon.com/s3/storage-classes/intelligent-tiering/
S3 지능형 계층화
액세스 패턴을 예측할 수 없거나 변경될 때 S3 비용을 줄이기 위한 최상의 솔루션입니다.
S3 Intelligent-Tiering 은 성능에 미치는 영향이나 검색 비용 없이 액세스 빈도를 기준으로
두 액세스 계층(빈번함 및 비빈번함) 간에 객체를 자동으로 이동합니다. S3
Intelligent-Tiering 에는 거의 액세스하지 않는 개체에 대한 선택적 아카이브 계층도
있습니다. S3 수명 주기 규칙을 사용하여 객체를 S3 Standard 에서 S3
Intelligent-Tiering으로 전환할 수 있습니다.
참조 URL:
1 https://aws.amazon.com/s3/storage-classes/intelligent-tiering/
2 https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-intelligent-tiering.html
3
https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering-overview.ht
ml
~~~

---

# Q470 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109334-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
외부 전용 인터넷 게이트웨이는 VPC 의 인스턴스에서 인터넷으로 IPv6 을 통한 아웃바운드
통신을 허용하고 인터넷이 인스턴스와의 IPv6 연결을 시작하지 못하도록 하는 VPC 구성
요소입니다. 이것은 회사의 보안 정책 및 요구 사항을 충족합니다. 외부 전용 인터넷
게이트웨이를 사용하려면 IPv6 인터넷 트래픽(::/0)을 외부 전용 인터넷 게이트웨이로
라우팅하는 경로를 서브넷의 라우팅 테이블에 추가해야 합니다.
참조 URL:
1 https://docs.aws.amazon.com/vpc/latest/userguide/egress-only-internet-gateway.html
2 https://dev.to/aws-builders/what-is-an-egress-only-internet-gateways-in-aws-7gp
3 https://docs.aws.amazon.com/vpc/latest/userguide/route-table-options.html
~~~

---

# Q471 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109453-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
Amazon S3 용 게이트웨이 VPC 엔드포인트는 인터넷 게이트웨이나 NAT 디바이스가
필요하지 않은 VPC 와 Amazon S3 간의 프라이빗 연결을 가능하게 합니다. 이렇게 하면
비용이 최소화되고 트래픽이 인터넷을 통과하는 것을 방지할 수 있습니다. 게이트웨이 VPC
엔드포인트는 트래픽을 비공개로 Amazon S31 로 라우팅하기 위해 접두사 목록을 VPC
라우팅 테이블의 라우팅 대상으로 사용합니다. 엔드포인트를 VPC 의 모든 라우팅 테이블과
연결하면 모든 서브넷이 엔드포인트를 통해 Amazon S3에 액세스할 수 있습니다.
옵션 A 는 S3 Intelligent-Tiering 이 변화하는 액세스 패턴을 기반으로 두 액세스 계층 간에
객체를 자동으로 이동하여 스토리지 비용을 최적화하는 스토리지 클래스이기 때문에
올바르지 않습니다. VPC와 Amazon S3 간의 네트워크 트래픽에는 영향을 미치지 않습니다.
옵션 B 는 올바르지 않습니다. S3 Transfer Acceleration 은 클라이언트와 S3 버킷 간에
장거리에서 파일을 빠르고 쉽고 안전하게 전송할 수 있는 기능이기 때문입니다. 트래픽이
인터넷을 통과하는 것을 막지는 않습니다.
옵션 D 는 Amazon S3 용 인터페이스 VPC 엔드포인트는 각 서브넷에 프라이빗 IP 주소가
있는 탄력적 네트워크 인터페이스(ENI)가 필요한 AWS PrivateLink 에 의해 구동되기 때문에
올바르지 않습니다. 이것은 솔루션에 복잡성과 비용을 추가합니다. 또한 인터페이스 VPC
엔드포인트는 Amazon S3에 대한 교차 리전 액세스를 지원하지 않습니다.
참조 URL:
https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html
https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html#sc-
dynamicdata-access
https://docs.aws.amazon.com/AmazonS3/latest/userguide/transfer-acceleration.html
https://aws.amazon.com/blogs/architecture/choosing-your-vpc-endpoint-strategy-for-a
mazon-s3/
~~~

---

# Q472 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109454-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
https://aws.amazon.com/premiumsupport/knowledge-center/dynamodb-high-latency/
Amazon DynamoDB Accelerator(DAX)는 DynamoDB를 위한 완전 관리형 인 메모리 캐시로,
DynamoDB 테이블의 성능을 최대 10 배까지 향상시키고 모든 규모에서 마이크로초 수준의
응답 시간을 제공합니다. DynamoDB API 작업과 호환되며 use1 에 대한 최소한의 코드
변경이 필요합니다. 새 메시지 테이블에 대해 DAX 를 구성함으로써 솔루션은 최소한의
애플리케이션 변경으로 새 메시지를 읽는 대기 시간을 줄일 수 있습니다.
1. 증가된 읽기 로드를 처리하기 위해 DynamoDB 읽기 replicas 를 추가합니다. 읽기 전용
복제본의 읽기 엔드포인트를 가리키도록 애플리케이션을 업데이트합니다. DynamoDB 는
읽기 전용 복제본을 기능으로 지원하지 않으므로 이 솔루션은 작동하지 않습니다. 읽기
전용 복제본은 DynamoDB가 아닌 Amazon RDS에서 사용할 수 있습니다.
2. DynamoDB 의 새 메시지 테이블에 대한 읽기 용량 단위 수를 두 배로 늘립니다. 기존
DynamoDB 엔드포인트를 계속 사용합니다. 읽기 용량 단위를 늘리면 성능이나 지연
시간이 아니라 DynamoDB 의 처리량만 증가하므로 이 솔루션은 가능한 한 적은 지연
시간으로 새 메시지를 읽어야 한다는 요구 사항을 충족하지 않습니다.
3. Redis용 Amazon ElastiCache 캐시를 애플리케이션 스택에 추가합니다. DynamoDB 대신
Redis 캐시 엔드포인트를 가리키도록 애플리케이션을 업데이트합니다. Redis 용
ElastiCache 를 추가하려면 먼저 캐시 쿼리, DynamoDB 에 쓴 후 캐시 업데이트, 필요할 때
캐시 무효화와 같은 캐싱 로직을 구현하기 위해 상당한 코드 변경이 필요하므로 이
솔루션은 최소한의 애플리케이션 변경 요구 사항을 충족하지 않습니다.
참조: https://aws.amazon.com/dynamodb/dax/
~~~

---

# Q473 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109455-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q474 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109659-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q475 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109456-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q476 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109458-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
IAM 정책은 IAM 자격 증명(예: 사용자, 그룹 또는 역할)에 대한 권한을 정의하는
문서입니다. IAM 정책을 사용하여 부서에 따라 기존 사용자 및 그룹에 권한을 부여할 수
있습니다. 최소 권한 권한을 부여하는 IAM 정책을 생성할 수 있습니다. 즉, 사용자가
작업을 수행하는 데 필요한 최소한의 권한만 부여한다는 의미입니다. 그런 다음 정책을
IAM 그룹에 연결하면 해당 그룹의 모든 사용자에게 정책이 적용됩니다. 이 솔루션은 운영
비용을 줄이고 권한 구성 및 관리를 단순화합니다.
참조:
https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html
~~~

---

# Q477 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109459-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q478 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109725-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q479 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109461-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
AWS CloudFormation 은 Auto Scaling 그룹, 로드 밸런서, 데이터베이스 등 원하는 모든
리소스를 설명하는 템플릿을 사용하여 AWS 리소스를 모델링하고 설정할 수 있도록
도와주는 서비스입니다. AWS CloudFormation 을 사용하여 여러 환경과 리전에서
자동화되고 일관된 방식으로 인프라를 배포할 수 있습니다. 또한 AWS CloudFormation 을
사용하여 인프라를 단일 단위로 업데이트하거나 삭제할 수 있습니다.
참조 URL:
1 https://aws.amazon.com/cloudformation/
2 https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html
3
https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-whatis-concep
ts.html
~~~

---

# Q480 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109663-exam-aws-certified-sol
utions-architect-associate-saa-c03/
참고:
https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints.html
~~~

---

# Q481 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109462-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q482 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109490-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
AWS DataSync 는 인터넷 또는 AWS Direct Connect 를 통해 온프레미스 스토리지와 AWS
스토리지 서비스 간에 대량의 데이터를 온라인으로 쉽게 이동할 수 있게 해주는 데이터
전송 서비스입니다. DataSync 는 TLS 암호화를 사용하여 전송 중인 데이터를 자동으로
암호화하고 체크섬을 사용하여 전송하는 동안 데이터 무결성을 확인합니다. DataSync 는
오픈 소스 도구보다 최대 10 배 빠르게 데이터를 전송할 수 있으며 전송 예약, 모니터링 및
재개와 같은 작업을 단순화하고 자동화하여 운영 오버헤드를 줄입니다.
참조:
https://aws.amazon.com/datasync/
~~~

---

# Q483 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109463-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q484 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109467-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
AWS Organizations 는 사용자가 여러 AWS 계정을 중앙에서 관리하고 제어할 수 있도록
도와주는 서비스입니다. 이를 통해 사용자는 비즈니스 요구 사항 또는 기타 기준에 따라
계정을 그룹화하는 조직 단위(OU)를 만들 수 있습니다. 또한 사용자는 서비스 제어
정책(SCP)을 정의하고 OU 또는 계정에 연결하여 계정에서 수행할 수 있는 작업을 제한할
수 있습니다. 모든 기능을 켠 상태에서 AWS Organizations 에 새 조직을 생성하면 이
솔루션은 서로 다른 비즈니스 단위의 새 AWS 계정을 통합하고 관리할 수 있습니다. AWS
IAM Identity Center(이전에는 AWS Single Sign-On 이라고 함)는 모든 AWS 계정 및
클라우드 애플리케이션에 대한 Single Sign-On 액세스를 제공하는 서비스입니다. AWS
Directory Service를 통해 Microsoft Active Directory와 연결하여 해당 디렉터리의 사용자가
기존 Active Directory 사용자 이름과 암호를 사용하여 맞춤형 AWS 액세스 포털에 로그인할
수 있도록 합니다. AWS 액세스 포털에서 사용자는 권한이 있는 모든 AWS 계정 및
클라우드 애플리케이션에 액세스할 수 있습니다 2. 조직에 IAM Identity Center 를 설정하고
회사의 회사 디렉터리 서비스와 통합함으로써 솔루션은 중앙 집중식 회사 디렉터리
서비스를 사용하여 이러한 AWS 계정에 대한 액세스를 인증할 수 있습니다.
1. Amazon Cognito 자격 증명 풀을 설정합니다. Amazon Cognito 인증을 수락하도록 AWS
IAM Identity Center(AWS Single Sign-On)를 구성합니다. 이 솔루션은 중앙 집중식 기업
디렉터리 서비스를 사용하여 이러한 AWS 계정에 대한 액세스 인증 요구 사항을 충족하지
않습니다. Amazon Cognito 는 웹 및 모바일 애플리케이션에 대한 사용자 가입, 로그인 및
액세스 제어를 제공하는 서비스이기 때문입니다. 기업 디렉토리 서비스.
2. 서비스 제어 정책(SCP)을 구성하여 AWS 계정을 관리합니다. AWS IAM Identity
Center(AWS Single Sign-On)를 AWS Directory Service에 추가합니다. SCP는 계정 자체를
관리하는 것이 아니라 조직의 계정이 수행할 수 있는 작업을 제한하는 데 사용되기 때문에
이 솔루션은 작동하지 않습니다 1. 또한 IAM Identity Center 는 AWS Directory Service 를
통해 Microsoft Active Directory와 연결하는 별도의 서비스이므로 AWS Directory Service에
추가할 수 없습니다.
3. AWS Organizations 에서 새 조직을 생성합니다. AWS Directory Service 를 직접
사용하도록 조직의 인증 메커니즘을 구성합니다. AWS Organizations 에는 AWS Directory
Service 를 직접 사용할 수 있는 인증 메커니즘이 없기 때문에 이 솔루션은 작동하지
않습니다. AWS Organizations는 IAM Identity Center를 사용하여 조직의 계정에 대한 Single
Sign-On 액세스를 제공합니다.
참조:
https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.htm
l
~~~

---

# Q485 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109470-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q486 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109664-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
Amazon S3는 업계 최고의 확장성, 데이터 가용성, 보안 및 성능을 제공하는 객체 스토리지
서비스입니다. Amazon S3 를 사용하여 HTML 파일, 이미지, 비디오 등과 같은 웹 사이트용
정적 콘텐츠를 호스팅할 수 있습니다. Amazon Elastic Container Service(Amazon ECS)는
AWS 에서 컨테이너화된 애플리케이션을 실행하고 확장할 수 있는 완전 관리형 컨테이너
오케스트레이션 서비스입니다. .
AWS Fargate 는 Amazon ECS 및 Amazon EKS 모두에서 작동하는 컨테이너용 서버리스
컴퓨팅 엔진입니다. Fargate 를 사용하면 서버를 프로비저닝하고 관리할 필요가 없으므로
애플리케이션 구축에 쉽게 집중할 수 있습니다. 컨테이너화된 애플리케이션 논리 계층의
컴퓨팅 성능을 위해 AWS Fargate 와 함께 Amazon ECS 를 사용할 수 있습니다. Amazon
RDS 는 클라우드에서 관계형 데이터베이스를 쉽게 설정, 운영 및 확장할 수 있게 해주는
관리형 관계형 데이터베이스 서비스입니다. 애플리케이션의 데이터베이스 계층에 대해
관리형 Amazon RDS 클러스터를 사용할 수 있습니다. 이 솔루션은 배포를 단순화하고
3계층 애플리케이션의 운영 비용을 줄여줍니다.
참조:
https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteHosting.html
https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html
https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html
~~~

---

# Q487 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109665-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q488 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109509-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:・
서비스 제어 정책(SCP): SCP 는 AWS Organizations 의 필수적인 부분이며 이를 통해 AWS
Organization 내 조직 단위(OU)에 대한 세분화된 권한을 설정할 수 있습니다. SCP 는 루트
사용자를 포함하여 멤버 계정에 부여할 수 있는 최대 권한에 대한 중앙 제어를 제공합니다.
청구 정보에 대한 액세스 거부: SCP 를 만들어 루트 OU 에 연결하면 조직 내 모든 계정의
청구 정보에 대한 액세스를 명시적으로 거부할 수 있습니다. SCP 는 청구 관련 서비스를
포함하여 다양한 AWS 서비스 및 작업에 대한 액세스를 제한하는 데 사용할 수 있습니다.
세분화된 제어: SCP 를 사용하면 조직 단위 수준에서 특정 권한 및 제한을 정의할 수
있습니다. 루트 OU 에서 청구 정보에 대한 액세스를 거부하면 루트 사용자를 포함한 어떤
멤버 계정도 청구 정보에 액세스할 수 없습니다.
~~~

---

# Q489 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109637-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q490 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109577-exam-aws-certified-sol
utions-architect-associate-saa-c03/
참고:
https://aws.amazon.com/ko/blogs/database/dynamodb-streams-use-cases-and-design
-patterns/
https://repost.aws/ko/knowledge-center/back-up-dynamodb-s3
~~~

---

# Q491 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109513-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q492 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109638-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
동적 조정은 수요 또는 부하에 따라 Auto Scaling 그룹의 EC2 인스턴스 수를 자동으로
조정하는 일종의 자동 조정입니다. 지정된 지표가 임계값을 초과하면 CloudWatch 경보를
사용하여 조정 작업을 트리거합니다. 필요에 따라 확장(인스턴스 추가) 또는 축소(인스턴스
제거)할 수 있습니다 1. 솔루션은 동적 확장을 사용하여 갑작스러운 트래픽 증가 중에 가장
비용 효율적으로 애플리케이션 성능을 유지할 수 있습니다.
1. 수동 조정을 사용하여 Auto Scaling 그룹의 크기를 변경합니다. 수동 확장은 사용자가
CLI 또는 콘솔을 통해 인스턴스 수를 수동으로 늘리거나 줄여야 하므로 이 솔루션은
트래픽이 갑자기 증가하는 동안 애플리케이션 성능을 유지해야 하는 요구 사항을 충족하지
않습니다. 수요나 부하의 변화에 자동으로 반응하지 않습니다.
2. 예측 조정을 사용하여 Auto Scaling 그룹의 크기를 변경합니다. 이 솔루션은 예측
확장이 기계 학습 및 인공 지능 도구를 사용하여 트래픽 부하를 평가하고 더 많거나 적은
리소스가 필요할 때를 예상하므로 대부분의 비용 효율성 요구 사항을 충족하지 않습니다.
주어진 시간에 실제 수요 또는 로드와 일치하지 않을 수 있는 예측을 기반으로 예약된 조정
작업을 수행합니다. 예측 조정은 예측 가능한 트래픽 패턴이 있거나 트래픽 부하의 알려진
변경 사항이 있는 시나리오에 더 적합합니다.
3. 일정 조정을 사용하여 Auto Scaling 그룹의 크기를 변경합니다. 일정 조정은 사용자가
예약한 특정 시간에 조정 작업을 수행하므로 이 솔루션은 트래픽이 갑자기 증가하는 동안
애플리케이션 성능을 유지해야 하는 요구 사항을 충족하지 않습니다. 수요나 부하의 변화에
자동으로 반응하지 않습니다. 일정 조정은 하루 중 특정 시간에 예측 가능한 트래픽 감소
또는 급증이 있는 시나리오에 더 적합합니다.
참조:
https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scale-based-ondemand.ht
ml
~~~

---

# Q493 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109639-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:・
이러한 답변은 모든 언어로 된 고객 서비스 통화 녹음에서 서면 감정 분석 보고서를
작성하고 이를 영어로 번역하는 요구 사항을 충족하므로 정확합니다. Amazon Transcribe는
고급 기계 학습 기술을 사용하여 오디오 파일의 음성을 인식하고 텍스트로 변환하는
서비스입니다. Amazon Transcribe 를 사용하여 모든 언어의 오디오 녹음을 텍스트로
변환하고 소스 오디오의 언어 코드를 지정할 수 있습니다. Amazon Translate 는 빠르고
고품질의 저렴한 언어 번역을 제공하는 신경망 기계 번역 서비스입니다. Amazon
Translate 를 사용하여 모든 언어의 텍스트를 영어로 번역하고 소스 및 대상 언어 코드를
지정할 수 있습니다. Amazon Comprehend 는 기계 학습을 사용하여 텍스트에서 통찰력과
관계를 찾는 자연어 처리(NLP) 서비스입니다. Amazon Comprehend 를 사용하여 텍스트가
긍정적인지, 부정적인지, 중립적인지 또는 혼합되어 있는지 판단하는 감정 분석 보고서를
생성할 수 있습니다.
참조:
https://docs.aws.amazon.com/transcribe/latest/dg/what-is-transcribe.html
https://docs.aws.amazon.com/translate/latest/dg/what-is.html
https://docs.aws.amazon.com/comprehend/latest/dg/how-sentiment.html
~~~

---

# Q494 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109727-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q495 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109666-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
Amazon Macie는 기계 학습 및 패턴 일치를 사용하여 AWS에서 중요한 데이터를 검색하고
보호하는 완전 관리형 데이터 보안 및 데이터 개인 정보 보호 서비스입니다. Macie 는
다양한 유형의 PII 또는 금융 정보(예: 여권 번호 및 신용 카드 번호)에 대해 관리형
식별자를 사용하는 데이터 검색 작업을 실행할 수 있습니다. Macie 는 또한 데이터의
잠재적인 문제나 위험을 경고하는 결과를 생성할 수 있습니다.
참조:
https://docs.aws.amazon.com/macie/latest/userguide/macie-identifiers.html
~~~

---

# Q496 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109552-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:・
https://aws.amazon.com/storagegateway/file/
파일 게이트웨이는 애플리케이션 데이터 파일과 백업 이미지를 Amazon S3 클라우드
스토리지에 내구성 있는 개체로 저장하기 위해 클라우드에 원활하게 연결할 수 있는 방법을
제공합니다. 파일 게이트웨이는 로컬 캐싱을 통해 Amazon S3 의 데이터에 대한 SMB 또는
NFS 기반 액세스를 제공합니다. 온프레미스 애플리케이션과 S3 객체 스토리지에 대한 파일
프로토콜 액세스가 필요한 Amazon EC2 기반 애플리케이션에 사용할 수 있습니다.
https://aws.amazon.com/storagegateway/volume/
볼륨 게이트웨이는 온프레미스 애플리케이션에 클라우드 지원 iSCSI 블록 스토리지 볼륨을
제공합니다.
볼륨 게이트웨이는 사용자를 대신하여 Amazon S3 에 온프레미스 데이터를 저장하고
관리하며 캐시 모드 또는 저장 모드에서 작동합니다. 캐싱된 볼륨 게이트웨이 모드에서
기본 데이터는 Amazon S3 에 저장되는 반면 자주 액세스하는 데이터는 짧은 지연 시간
액세스를 위해 캐시에 로컬로 유지됩니다.
~~~

---

# Q497 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109667-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
이를 통해 회사는 VPC 의 Amazon EC2 인스턴스에서 Amazon S3 에 액세스하기 위한
데이터 출력 비용을 줄일 수 있습니다. 회사는 VPC 게이트웨이 엔드포인트를
프로비저닝함으로써 VPC 와 S3 간의 프라이빗 연결을 활성화할 수 있습니다. 게이트웨이
엔드포인트를 모든 S3 트래픽의 경로로 사용하도록 프라이빗 서브넷의 라우팅 테이블을
구성함으로써 회사는 데이터 처리 및 데이터 전송 비용을 청구하는 NAT 게이트웨이 사용을
피할 수 있습니다.
~~~

---

# Q498 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109668-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q499 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109515-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명
회사는 더 저렴한 연결(200M)을 설정해야 하지만 호스트 연결로 더 많은 유연성을 위해 1,
10 또는 100Gbps 의 포트 속도만 주문할 수 있기 때문에 B 는 올바르지 않습니다.
50Mbps에서 10Gbps 사이의 포트 속도를 주문할 수 있습니다.
https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-dir
ectconnect.html
~~~

---

# Q500 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/109689-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:・
A 이 옵션에는 온프레미스 파일 서버에 DataSync 에이전트를 배포하고 DataSync 를
사용하여 데이터를 FSx for Windows File Server 로 직접 전송하는 작업이 포함됩니다.
DataSync는 마이그레이션 프로세스 중에 파일 권한이 보존되도록 합니다.
D 이 옵션에는 휴대용 데이터 전송 장치인 AWS Snowcone 장치 사용이 포함됩니다.
Snowcone 디바이스를 온프레미스 네트워크에 연결하고 디바이스에서 DataSync
에이전트를 시작하고 DataSync 작업을 예약하여 데이터를 FSx for Windows File Server 로
전송합니다.
DataSync는 파일 권한을 유지하면서 마이그레이션 프로세스를 처리합니다.
~~~