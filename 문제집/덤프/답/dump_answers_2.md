# Q101 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/86019-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
프라이빗 서브넷에 있는 인스턴스가 외부 인터넷과 통신하기 위해선 NAT 게이트웨이가
필요.
A(O) : 각 가용 영역의 퍼블릭 서브넷마다 NAT 게이트웨이를 두어야 함. 프라이빗 서브넷의
인스턴스는 퍼블릭 NAT 게이트웨이를 통해 인터넷에 연결. 퍼블릭 서브넷에서 퍼블릭 NAT
게이트웨이를 생성하고 생성 시 탄력적 IP 주소를 NAT 게이트웨이와 연결해야 합니다.
여러 가용 영역에 리소스가 있고 NAT 게이트웨이 하나를 공유하는 경우, NAT 게이트웨이의
가용 영역이 다운되면 다른 가용 영역의 리소스도 인터넷에 액세스할 수 없게 됩니다. 가용
영역과 독립적인 아키텍처를 만들려면 각 가용 영역에 NAT 게이트웨이를 만들고 리소스가
동일한 가용 영역의 NAT 게이트웨이를 사용하도록 라우팅을 구성합니다.
https://docs.aws.amazon.com/ko_kr/vpc/latest/userguide/vpc-nat-gateway.html
B(X) : NAT 인스턴스는 더 이상 권장되지 않음
C(X) : 인터넷 게이트웨이는 프라이빗 서브넷과 외부 인터넷을 연결할 수 없음.
D(X) : NAT 게이트웨이가 필요한 상황임.
참고:
https://docs.aws.amazon.com/ko_kr/vpc/latest/userguide/vpc-nat-comparison.html
~~~

---

# Q102 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/85814-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
A(O)
EFS 파일 시스템과 동일한 가용 영역으로 EC2 인스턴스 시작하는건 문제 없어보입니다.
B(O) : DataSync Agent는 AWS로 전송할 떄 필요
에이전트 는 AWS DataSync 가 스토리지 시스템에서 읽거나 쓰는 데 사용하는 가상
머신(VM) 또는 Amazon EC2 인스턴스입니다 . 에이전트는 온프레미스 스토리지에서
AWS로 데이터를 복사할 때 일반적으로 사용됩니다.
https://docs.aws.amazon.com/datasync/latest/userguide/working-with-agents.html
DataSync는 DataSync 위치와 같이 사용됨
대부분의 워크로드의 경우 각 자체 관리 위치에 대해 하나의 AWS DataSync 에이전트를
사용하는 것이 좋습니다.
https://docs.aws.amazon.com/datasync/latest/userguide/multiple-agents.html
C(X) : EBS가 아니라 EFS가 NFS 지원.
D(X) : 수동으로 할 필요가 없이 DataSync같은 대안을 사용하면 됨.
E(X) : 온프레미스 SFTP 에 좀 더 적합한 건 DataSync 보다 Transfer Family 가 더
적합해보입니다.
~~~

---

# Q103 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/85781-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
이것이 북마크의 목적입니다. "AWS Glue는 작업 실행의 상태 정보를 유지하여 ETL 작업의
이전 실행 중에 이미 처리된 데이터를 추적합니다. 이 지속된 상태 정보를 작업 북마크라고
합니다. 작업 북마크는 AWS Glue 가 유지 관리하는 데 도움이 됩니다. 상태 정보를
제공하고 오래된 데이터의 재처리를 방지합니다."
https://docs.aws.amazon.com/glue/latest/dg/monitorcontinuations.html
설명2:
A(O) : AWS Glue는 작업 실행의 상태 정보를 유지하여 이전에 ETL 작업을 실행할 때 이미
처리된 데이터를 추적합니다. 이와 같은 지속 상태 정보를 작업 북마크라고 합니다.
https://docs.aws.amazon.com/ko_kr/glue/latest/dg/monitor-continuations.html
B(X) : 처리한 데이터를 어디에 쓸 줄 알고 삭제하는지...?
C(X) : ""NumberOfWorkers – 숫자(정수) : 작업이 실행될 때 할당되는 정의된 workerType의
작업자 수입니다.
https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-job.html
D(X) : 기계 변환 학습은 전혀 관계 없음.
~~~

---

# Q104 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/85342-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
A(O) : AWS Shield Advanced 보호는 네트워크 트래픽에 대한 상시 작동, 흐름 기반
모니터링과 적극적인 애플리케이션 모니터링을 통해 의심되는 DDoS 공격에 대한 거의
실시간 알림을 제공합니다. 또한 AWS Shield Advanced 는 공격을 자동으로 완화하기 위해
첨단 공격 완화 및 라우팅 기법을 적용합니다. https://aws.amazon.com/ko/shield/faqs/
B(X) : GuardDuty는 AWS 계정 보호 서비스.
Amazon GuardDuty 는 AWS 계정 및 워크로드에서 악의적 활동을 모니터링하고 상세한
보안 결과를 제공하여 가시성 및 해결을 촉진하는 위협 탐지 서비스입니다.
https://aws.amazon.com/ko/guardduty/
C(O) : CloudFront 로도 DDoS 에 대처 가능. CloudFront 는 정적 및 동적 콘텐츠 모두에
작동. 또한 Amazon CloudFront, AWS Global Accelerator 및 Amazon Route 53과 같은 엣지
로케이션에서 작동하는 AWS 서비스를 활용하여 알려진 모든 인프라 계층 공격에 대한
포괄적인 가용성 보호를 구축할 수 있습니다. 이러한 서비스는 AWS 글로벌 엣지
네트워크의 일부이며 전 세계에 분산된 엣지 로케이션에서 모든 유형의 애플리케이션
트래픽을 처리할 때 애플리케이션의 DDoS 복원력을 향상할 수 있습니다.
https://d1.awsstatic.com/whitepapers/Security/DDoS_White_Paper.pdf
일반적으로 이미지나 동영상 파일 같은 정적 콘텐츠 전송을 위해서 Amazon CloudFront 를
많이 활용하고 있지만...TTL 을 0 으로 설정하여 매번 원본 저장소에 접속하여 동적
콘텐츠를 제공하더라도, CloudFront 를 프록시로 사용함으로써 전송 성능을 향상 시킬 수
있습니다.
https://aws.amazon.com/ko/blogs/korea/how-to-improve-dynamic-contents-delievery-
using-amazon-cloudfront/
D(X) : DDoS는 수많은 좀비 PC를 동원하는데, 그런 PC들의 IP를 일일히 차단하여 막기는
비효율적.
E(X) : DDoS로 발생하는 대규모 트래픽은 Auto Scaling으로 막을 수 있는 스케일이 아님.
~~~

---

# Q105 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/85816-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
・ Lambda 의 전체 기능이 아닌 lambda 함수 호출 기능(lambda:InvokeFunction)만
사용하도록 하고, 전체 보안 주체(*)가 아닌 아마존 이벤트 서비스만 보안 주체로
설정하여야 하므로 B,D 둘 중 하나가 답.
・서버리스 워크로드를 '배포'한다고 했으므로 다른 계정에서도 쓸 수 있는 D가 유리함.
리소스 기반 정책은 해당 리소스에 액세스할 수 있는 사용자(보안 주체)를 지정합니다.
리소스 기반 정책을 사용한 교차 계정 액세스는 역할을 사용한 교차 계정 액세스에 비해 몇
가지 이점이 있습니다. 리소스 기반 정책을 통해 액세스한 리소스로 인해 보안 주체는
여전히 신뢰할 수 있는 계정에서 작업을 할 수 있고, 역할 권한을 수신하기 위해 자신의
권한을 포기할 필요가 없습니다. 즉, 보안 주체는 신뢰하는 계정의 리소스에 액세스하는
동시에 신뢰할 수 있는 계정의 리소스에 계속 액세스할 수 있습니다. 다른 계정의 공유
리소스로 정보를 복사하거나 공유 리소스의 정보를 복사하는 등의 작업에서 이는 특히
유용합니다.
https://docs.aws.amazon.com/ko_kr/IAM/latest/UserGuide/id_roles_compare-resource-p
olicies.html
https://docs.aws.amazon.com/ko_kr/eventbridge/latest/userguide/eb-use-resource-base
d.html#lambda-per
~~~

---

# Q106 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/85817-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
감사 목적으로 기록되어야 함 = AWS KMS. 따라서 C,D 둘 중 하나가 정답.
매년 키를 교체(rotate)해야하므로 운영 상 효율적인 방식은 수동이 아닌 자동 방식. 정답은
D.
설명2:
https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html
고객 관리형 키에 대해 자동 키 교체를 활성화하면 AWS KMS 는 매년 KMS 키에 대한
새로운 암호화 자료를 생성합니다. 또한 AWS KMS 는 KMS 키가 암호화한 데이터를
해독하는 데 사용할 수 있도록 KMS 키의 이전 암호화 자료를 영구적으로 저장합니다. AWS
KMS 의 키 순환은 투명하고 사용하기 쉽게 설계된 암호화 모범 사례입니다. AWS KMS 는
고객 관리형 CMK 에 대해서만 선택적 자동 키 교체를 지원합니다. 키 순환을 활성화 및
비활성화합니다. 자동 키 교체는 고객 관리형 CMK 에서 기본적으로 비활성화됩니다. 키
교체를 활성화(또는 재활성화)하면 AWS KMS 는 활성화 날짜로부터 365 일 후 그리고 이후
365일마다 CMK를 자동으로 교체합니다.
~~~

---

# Q107 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/85212-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
A(X) : 기존 분석 플랫폼을 사용하려고 한다고 했으므로 분석 기능이 있는 Athena 제외.
Amazon Athena는 표준 SQL을 사용해 Amazon S3에 저장된 데이터를 간편하게 분석할 수
있는 대화식 쿼리 서비스입니다.
https://aws.amazon.com/ko/athena/faqs/
B(O) : Lambda 는 512MB 의 임시 스토리지를 가지고 있기도 하고, S3 에 데이터를 저장할
수도 있으며, 지문에서는 [이러한 데이터 포인트를 사용하려고 합니다.] 라고 언급함과
동시에 [다중 계층 옵션]이라고 했으므로 Lambda + API Gateway 조합인 B 가 정답에
가깝다고 봄.
・ 512MB 에서 10,240MB 사이에서 1MB 단위로 자체 임시 스토리지로 각 Lambda 함수를
구성할 수 있습니다. 임시 스토리지는 각 함수의 /tmp 디렉터리에서 사용할 수 있습니다.
각 함수는 추가 비용 없이 512MB의 스토리지에 액세스할 수 있습니다.
https://aws.amazon.com/ko/lambda/faqs/
・ Lambda 는 웹 애플리케이션 개발자의 요구 사항을 충족하는 포괄적인 스토리지 옵션을
제공합니다. 여기에는 Amazon S3 및 Amazon EFS 와 같은 다른 AWS 서비스가
포함됩니다 . 임시 저장소 또는 Lambda 계층과 같은 기본 저장소 옵션도 사용할 수
있습니다.
https://aws.amazon.com/ko/blogs/compute/choosing-between-aws-lambda-data-stora
ge-options-in-web-apps/
・ Lambda 계층은 Lambda 함수와 함께 사용할 수 있는 라이브러리 및 기타 종속성을
패키징하는 편리한 방법을 제공합니다.
https://docs.aws.amazon.com/ko_kr/lambda/latest/dg/configuration-layers.html
C(X) : RedShift 는 Athena 에 비해 가격보다 성능이 더 우선시 될 때 사용. 위치 정보
서비스는 Athena 대신에 RedShift를 사용해야할 정도의 서비스가 아님.
Amazon Athena와 Amazon Redshift는 모두 서버리스 서비스이지만 그 필요와 사용 사례가
서로 다릅니다. 어떤 규모에서든 높은 성능을 요하는 복잡한 BI 및 분석 워크로드를 위해
최고의 가격 대비 성능이 필요하다면 Amazon Redshift와 같은 데이터 웨어하우스가 최선의
선택입니다.""(https://aws.amazon.com/ko/redshift/faqs/)
D(X) : 기존 분석 플랫폼을 사용하려고 한다고 했으므로 분석 서비스인 Amazon Kinesis
Data Analytics는 제외.
설명2:
https://aws.amazon.com/solutions/implementations/aws-streaming-data-solution-for-a
mazonkinesis/
~~~

---

# Q108 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/85427-exam-aws-certified-solut
ions-architect-associate-saa-c03/
~~~

---

# Q109 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/85634-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
A(X) : S3에 저장한다고 했지 S3 Glacier 같은 콜드 스토리지에 저장한다고 한 적 없음.
B(X) : 일정하지 않은 시간 동안이라고 지문에서 언급했는데, 보존 기간을 설정해뒀으므로
오답.
C(X) : 일단 일이 벌어지고 나서 수습하는 방식인데다가, 변경된 객체마다 일일히
CloudTrail이 작동하므로 운영 오버헤드와 비용이 증가할 우려가 있음.
D(O) : 객체 잠금 법적 보존 작업을 사용하면 객체 버전에 법적 보전을 적용할 수 있습니다.
보관 기간 설정과 마찬가지로 법적 보존을 사용하면 객체 버전을 덮어쓰거나 삭제할 수
없습니다. 그러나 법적 보존에는 연결된 보관 기간이 없고, 제거될 때까지 유효합니다. S3
배치 작업은 매니페스트의 키를 처리하기 전에 S3 버킷에서 객체 잠금이 활성화되어
있는지 확인합니다. 객체 작업 및 버킷 수준 유효성 검사를 수행하려면 S3 배치 작업이
사용자를 대신하여 S3 객체 잠금을 호출할 수 있도록 IAM 역할의 s3:PutObjectLegalHold
및 s3:GetBucketObjectLockConfiguration가 필요합니다.
https://docs.aws.amazon.com/ko_kr/AmazonS3/latest/userguide/batch-ops-legal-hold.h
tml
설명2:
ALB를 오리진으로 사용할 수 있음
원본이 하나 이상의 Amazon EC2 인스턴스에서 호스트되는 하나 이상의 HTTP 서버(웹
서버)인 경우 Application Load Balancer 를 사용하여 인스턴스에 트래픽을 분산할 수
있습니다. Application Load Balancer 를 CloudFront 의 원본으로 사용하는 방법에 대한
자세한 내용은
https://docs.aws.amazon.com/ko_kr/AmazonS3/latest/userguide/batch-ops-legal-hold.h
tml
~~~

---

# Q110 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/86471-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
Amazon S3 는 웹 어디에서나 원하는 양의 데이터를 저장하고 검색할 수 있는 확장성과
내구성이 뛰어난 객체 스토리지 서비스입니다. 사용자는 미리 서명된 URL 을 사용하여 각
사용자의 브라우저에서 Amazon S3 으로 이미지를 직접 업로드하도록 애플리케이션을
구성할 수 있습니다. 미리 서명된 URL 은 제한된 시간 동안 객체 업로드와 같은 특정
작업을 통해 S3 버킷의 객체에 대한 액세스를 제공하는 URL 입니다. 사용자는 AWS SDK
또는 AWS CLI 를 사용하여 프로그래밍 방식으로 미리 서명된 URL 을 생성할 수 있습니다.
미리 서명된 URL 을 사용하면 사용자는 이미지를 웹 서버에 먼저 보낼 필요가 없으므로
애플리케이션 내 결합을 줄이고 웹 사이트 성능을 향상시킬 수 있습니다.
AWS Lambda 는 이벤트에 대한 응답으로 코드를 실행하고 기본 컴퓨팅 리소스를 자동으로
관리하는 서버리스 컴퓨팅 서비스입니다. 사용자는 이미지가 업로드될 때 AWS Lambda
함수를 호출하도록 S3 이벤트 알림을 구성할 수 있습니다. S3 이벤트 알림은 객체 생성이나
삭제 등 S3 버킷에서 특정 이벤트가 발생할 때 사용자가 알림을 받을 수 있도록 하는
기능입니다. 사용자는 이미지 크기를 조정하고 이를 동일하거나 다른 S3 버킷에 다시
저장하는 Lambda 함수를 호출하도록 S3 이벤트 알림을 구성할 수 있습니다. 이러한
방식으로 사용자는 이미지 크기 조정 작업을 웹 서버에서 Lambda 로 오프로드할 수
있습니다.
~~~

---

# Q111 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/85910-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
A(X) : 데이터베이스를 복제하는 것은 시간이 매우 걸리는 일임. 고가용성을 위해서라면
다중 AZ를 사용하는 것이 좋음.
B(X) : A와 마찬가지 이유로 오답.
C(X) : D가 더 좋음.
D(O) : 평소에는 Standby 브로커 인스턴스에 낮은 트래픽 기준으로 AWS 리소스를
사용하여 비용을 절감하다가 Active 브로커 인스턴스가 다운되어 Standby 브로커 인스턴스
쪽으로 트래픽이 몰려오면 Auto Scaling을 통해 대처.
일반적으로 한 번에 하나의 브로커 인스턴스만 활성 상태이고, 다른 브로커 인스턴스는
대기 상태입니다. 브로커 인스턴스 중 하나가 제대로 작동하지 않거나 유지 관리 중이면
Amazon MQ 가 비활성 인스턴스를 서비스 중지하는 데 잠깐 시간이 걸립니다. 그런 다음
정상 대기 인스턴스가 활성화되고 들어오는 통신을 수신하기 시작할 수 있습니다.
https://docs.aws.amazon.com/ko_kr/amazon-mq/latest/developer-guide/active-standby
-broker-deployment.html
설명2:
Amazon S3는 확장성이 뛰어나고 내구성이 뛰어난 객체 스토리지 서비스로, 웹 어디에서나
원하는 양의 데이터를 저장하고 검색할 수 있습니다. 사용자는 미리 서명된 URL 을
사용하여 각 사용자의 브라우저에서 Amazon S3 로 직접 이미지를 업로드하도록
애플리케이션을 구성할 수 있습니다. 미리 서명된 URL 은 제한된 시간 동안 특정 작업(예:
객체 업로드)으로 S3 버킷의 객체에 대한 액세스 권한을 부여하는 URL 입니다. 사용자는
AWS SDK 또는 AWS CLI 를 사용하여 프로그래밍 방식으로 미리 서명된 URL 을 생성할 수
있습니다. 미리 서명된 URL 을 사용하면 이미지를 웹 서버에 먼저 보낼 필요가 없으므로
사용자는 애플리케이션 내에서 결합을 줄이고 웹 사이트 성능을 향상시킬 수 있습니다.
AWS Lambda 는 이벤트에 대한 응답으로 코드를 실행하고 기본 컴퓨팅 리소스를 자동으로
관리하는 서버리스 컴퓨팅 서비스입니다. 사용자는 이미지가 업로드될 때 AWS Lambda
함수를 호출하도록 S3 이벤트 알림을 구성할 수 있습니다. S3 이벤트 알림은 객체 생성
또는 삭제와 같은 S3 버킷에서 특정 이벤트가 발생할 때 사용자가 알림을 받을 수 있도록
하는 기능입니다. 사용자는 이미지 크기를 조정하고 동일한 S3 버킷 또는 다른 S3 버킷에
다시 저장하는 Lambda 함수를 호출하도록 S3 이벤트 알림을 구성할 수 있습니다. 이러한
방식으로 사용자는 웹 서버에서 Lambda 로 이미지 크기 조정 작업을 오프로드할 수
있습니다.
~~~

---

# Q112 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/85913-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
AWS Fargate는 사용자가 Amazon EC2 인스턴스의 서버 또는 클러스터를 관리할 필요 없이
컨테이너를 실행할 수 있게 해주는 서버리스 컴퓨팅 엔진입니다. 사용자는 Amazon Elastic
Container Service(Amazon ECS)에서 AWS Fargate를 사용하여 Service Auto Scaling으로
컨테이너화된 웹 애플리케이션을 실행할 수 있습니다.
Amazon ECS 는 Docker 와 Kubernetes 를 모두 지원하는 완전관리형 컨테이너
오케스트레이션 서비스입니다. Service Auto Scaling 은 사용자가 CPU 사용률 또는 요청
수와 같은 CloudWatch 지표를 기반으로 ECS 서비스에서 원하는 작업 수를 조정할 수
있는 기능입니다. 사용자는 Amazon ECS 에서 AWS Fargate 를 사용하여 애플리케이션을
컨테이너에 패키징하고 CPU 및 메모리 요구 사항을 지정하기만 하면 되므로 최소한의
코드 변경과 최소한의 개발 노력으로 애플리케이션을 AWS로 마이그레이션할 수 있습니다.
사용자는 Application Load Balancer 를 사용하여 수신 요청을 분산할 수도 있습니다.
Application Load Balancer 는 애플리케이션 계층에서 작동하고 요청 내용에 따라 대상으로
트래픽을 라우팅하는 로드 밸런서입니다. 사용자는 ECS 작업을 Application Load
Balancer 의 대상으로 등록하고 경로 또는 호스트 헤더를 기반으로 요청을 다른 대상
그룹으로 라우팅하도록 리스너 규칙을 구성할 수 있습니다. 사용자는 Application Load
Balancer를 사용하여 웹 애플리케이션의 가용성과 성능을 개선할 수 있습니다.
컨테이너화된 웹 응용 프로그램이 핵심. Fargate + ECS 조합인 A가 정답.
~~~

---

# Q113 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/85912-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
추가 워크로드에 사용할 네트워크 대역폭이 없다는 게 핵심. 따라서 Snowball 디바이스가
필요.
A(X) : 추가 워크로드에 사용할 네트워크 대역폭이 없다고 했으므로 DataSync는 사용 불가.
B(X) : Snowcone 으로 50TB 는 어림도 없음. 그리고 Snowcone 을 사용해서 업로드하는
방법은 DataSync 를 사용하거나 AWS 로 다시 반송(?)하는 방법 뿐인데 DataSync 는 추가
워크로드에 사용할 네트워크 대역폭이 없어서 불가능하다고 A 에서 이미 설명했고, AWS 로
다시 보내는 건 시간이 너무 걸리고 번거로움.
Snowcone 디바이스를 사용하여 디바이스를 AWS 로 배송하여 오프라인으로 또는 AWS
DataSync 를 사용하여 온라인으로 데이터를 수집, 처리 및 AWS 클라우드로 이동할 수
있습니다. Snowcone 은 디바이스를 AWS 로 다시 배송하여 최대 8TB 또는 14TB 의
데이터를 AWS 클라우드로 전송할 수 있는 빠르고 저렴한 방법을 제공합니다.
https://docs.aws.amazon.com/snowball/latest/snowcone-guide/snowcone-what-is-sno
wcone.html
C(O) : Snowball Edge Storage Optimized는 수십 테라바이트(TB)~페타바이트(PB)의 고용량
데이터를 안전하고 신속하게 AWS 로 전송해야 할 때 선택할 수 있는 가장 적합한
옵션입니다. 이 옵션은 대규모 데이터 전송 및 사전 처리 사용 사례를 위해 최대 80TB 의
가용 HDD 스토리지, 40 개의 vCPU, 1TB 의 SATA SSD 스토리지 및 최대 40Gb 네트워크
연결을 제공합니다.
https://aws.amazon.com/ko/snowball/faqs/
AWS Glue를 사용하면 70개 이상의 다양한 데이터 소스를 검색하여 연결하고 중앙 집중식
데이터 카탈로그에서 데이터를 관리할 수 있습니다. 추출, 변환, 로드(ETL) 파이프라인을
시각적으로 생성, 실행, 모니터링하여 데이터 레이크에 데이터를 로드할 수 있습니다.
https://docs.aws.amazon.com/ko_kr/glue/latest/dg/what-is-glue.html
D(X) : 따로 변환 애플리케이션을 EC2 인스턴스에서 실행하므로 운영 오버헤드가 만만치
않음.
~~~

---

# Q114 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/85189-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
A(X) : DynamoDB는 데이터베이스 서비스이기 떄문에 이미지를 저장하기에는 적절치 않음.
B(X) : Amazon Kinesis Data Firehose는 저장 기능이 없고 전송 기능만 있음.
Kinesis Data Firehose 는 스트리밍 ETL 솔루션입니다. 스트리밍 데이터를 캡처하고 변환한
후 Amazon S3, Amazon Redshift, Amazon OpenSearch Service 및 Splunk로 로드하여 이미
사용하고 있는 기존 비즈니스 인텔리전스 도구 및 대시보드를 통해 거의 실시간으로 분석할
수 있습니다.
https://aws.amazon.com/ko/kinesis/data-firehose/faqs/
C(O) : 정답.
D(X) : 사용자 수가 증가하고 있으므로 프로비저닝은 적절치 않음.
설명2:
이 솔루션은 확장성, 성능 및 가용성 요구 사항을 충족합니다. AWS Lambda 는 사진을
병렬로 처리하고 수요에 따라 자동으로 확장 또는 축소할 수 있습니다.
Amazon S3 는 사진과 메타데이터를 안정적이고 내구성 있게 저장할 수 있으며 고가용성과
짧은 지연 시간을 제공합니다. DynamoDB 는 메타데이터를 효율적으로 저장하고 일관된
성능을 제공할 수 있습니다. 또한 이 솔루션은 EC2 인스턴스 및 EBS 볼륨 관리의 비용과
복잡성을 줄입니다.
DynamoDB 에 사진을 저장하는 것은 스토리지 비용을 증가시키고 처리량을 제한할 수
있으므로 A 옵션은 올바르지 않습니다.
옵션 B 는 Kinesis Data Firehose 가 사진 처리용이 아니라 S3 또는 Redshift 와 같은
대상으로 데이터 스트리밍용으로 설계되었기 때문에 올바르지 않습니다.
옵션 D 는 EC2 인스턴스 수를 늘리고 프로비저닝된 IOPS SSD 볼륨을 사용하는 것이 로드
밸런서 및 애플리케이션 코드에 따라 확장성을 보장하지 않기 때문에 올바르지 않습니다.
또한 인프라 관리 비용과 복잡성도 증가합니다.
https://www.quora.com/How-can-I-use-DynamoDB-for-storing-metadata-for-Amazon
-S3-objects
~~~

---

# Q115 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/86031-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
S3에 액세스하지만 다른 네트워크 액세스는 필요하지 않음 = S3 Gateway Endpoint.
게이트웨이 엔드포인트는 인터넷 게이트웨이나 VPC 용 NAT 디바이스 없이 Amazon S3 및
DynamoDB 에 안정적인 연결을 제공합니다. 게이트웨이 엔드포인트는 AWS PrivateLink 를
활성화하지 않습니다.
https://docs.aws.amazon.com/vpc/latest/privatelink/gateway-endpoints.html
설명2:
프라이빗 경로를 통한 파일 전송의 새로운 요구 사항을 충족하려면 EC2 인스턴스를
인터넷에 직접 액세스할 수 없는 프라이빗 서브넷으로 이동해야 합니다. 이렇게 하면 파일
전송을 위한 트래픽이 인터넷을 통해 이동하지 않습니다. EC2 인스턴스가 Amazon S3 에
액세스할 수 있도록 Amazon S3 용 VPC 엔드포인트를 생성할 수 있습니다. VPC
엔드포인트를 사용하면 인터넷을 통해 트래픽을 전송하지 않고도 VPC 내의 리소스가 다른
서비스의 리소스와 통신할 수 있습니다. VPC 엔드포인트를 프라이빗 서브넷의 라우팅
테이블에 연결하면 EC2 인스턴스가 VPC 내의 프라이빗 연결을 통해 Amazon S3 에
액세스할 수 있습니다.
~~~

---

# Q116 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/85996-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
지문은 정적 웹 사이트 호스팅에 대해서 설명하고 있음. 정적 웹사이트 호스팅에 관한 건
아래의 링크를 참조할 것.
https://aws.amazon.com/ko/getting-started/projects/build-serverless-web-app-lambda-
apigateway-s3-dynamodb-cognito/module-1/
참고로 지문에서 높은 확장성을 요구하고 있는데, 높은 확장성이란 별 거 없고 정적 웹
사이트 호스팅 환경을 구축하면 그게 높은 확장성을 갖춘 것.
정적 웹 사이트 호스팅은 비용과 유지 관리 필요성이 가장 적은 옵션이고(예: 유지
관리해야 할 서버가 없음), 높은 수준의 신뢰성과 [[[확장성]]]을 제공하기 때문입니다.
https://aws.amazon.com/ko/getting-started/hands-on/host-static-website/faq/
A(O) : 뷰어가 HTTPS 를 사용할 것을 요청하도록 CloudFront 를 구성할 수 있습니다.
이렇게 하면 CloudFront 가 뷰어와 통신할 때 연결이 암호화됩니다. 또한 CloudFront 가
오리진과 HTTPS 를 사용하도록 구성할 수 있습니다. 이렇게 하면 CloudFront 가 오리진과
통신할 때 연결이 암호화됩니다.
https://docs.aws.amazon.com/ko_kr/AmazonCloudFront/latest/DeveloperGuide/using-htt
ps.html
B(X) : AWS Web ACL은 HTTP(S) 웹 요청을 세부적으로 제어할 수 있게 해주는 것.
웹 ACL (웹 ACL) 를 사용하면 보호된 리소스가 응답하는 모든 HTTP (S) 웹 요청을
세부적으로 제어할 수 있게 해줍니다.
https://docs.aws.amazon.com/ko_kr/waf/latest/developerguide/web-acl.html
C(X) : 1년에 4번만 업데이트할 건데 그냥 Lambda 안 쓰고 수동으로 올려도 됨.
D(O) : 동적 콘텐츠가 필요하지 않다고 했으므로 정적 웹사이트 호스팅. 따라서 S3 버킷 +
CloudFront 조합. CloudFront 는 ▲위 선택지 A 번에서 이미 준비되었으므로 S3 버킷만
준비하면 됨.
E(X) : 정적 웹사이트 호스팅은 서버리스로서 EC2를 사용할 필요가 없음.
정적 웹 사이트 호스팅은 비용과 유지 관리 필요성이 가장 적은 옵션이고(예: 유지
관리해야 할 서버가 없음)
https://aws.amazon.com/ko/getting-started/hands-on/host-static-website/faq/
설명2:
A -> 클라이언트에서 HTTPS를 요구하도록 CloudFront를 구성할 수 있습니다(보안 강화).
https://docs.aws.amazon.com/ko_kr/AmazonCloudFront/latest/DeveloperGuide/using-htt
ps-viewers-to-cloudfront.html
D -> S3 에 정적 웹 사이트를 저장하면 확장성이 제공되고 운영 오버헤드가 줄어듭니다.
그런 다음 애플리케이션 LB 및 EC2 인스턴스를 구성합니다(따라서 E는 제외됨).
~~~

---

# Q117 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/85802-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
CloudWatch Logs 구독을 통해 실시간에 가깝게 Amazon OpenSearch Service 클러스터로
수신한 데이터를 스트리밍하도록 CloudWatch Logs 로그 그룹을 구성할 수 있습니다.
https://docs.aws.amazon.com/ko_kr/AmazonCloudWatch/latest/logs/CWL_OpenSearch_S
tream.html
정답은 A.
최소한의 운영헤드, 기본으로 cloudwatch log - opensearch 간 연동을 제공함
참고:
https://computingforgeeks.com/stream-logs-in-aws-from-cloudwatch-to-elasticsearch/
~~~

---

# Q118 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/86512-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명
Amazon S3는 가장 저렴하고 어디서나 액세스할 수 있습니다.
Amazon S3 (Simple Storage Service)는 확장성이 뛰어나고 비용 효율적인 스토리지
서비스입니다. 시나리오에서 언급한 900TB 의 텍스트 문서와 같은 대용량 데이터를
저장하는 데 적합합니다. S3는 높은 내구성, 가용성 및 성능을 제공합니다.
옵션 A (Amazon EBS)는 개별 EC2 인스턴스용으로 설계된 블록 스토리지이며 대용량
데이터의 경우 S3만큼 원활하고 비용 효율적으로 확장되지 않을 수 있습니다.
옵션 B (Amazon EFS)는 확장 가능한 파일 스토리지 서비스이지만 특히 예상 스토리지
크기가 900TB인 경우 S3에 비해 가장 비용 효율적인 옵션이 아닐 수 있습니다.
옵션 C( Amazon OpenSearch 서비스)는 검색 및 분석 서비스이며 텍스트 문서의 기본
스토리지 솔루션으로 적합하지 않을 수 있습니다.
요약하면 Amazon S3 는 웹 애플리케이션에 필요한 대규모 텍스트 문서 리포지토리를
저장하기 위한 높은 확장성, 비용 효율성 및 내구성을 제공하므로 권장되는 선택입니다.
~~~

---

# Q119 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/86450-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
[여러 계정]에서 SQL 주입, XSS 공격, DDoS 등을 방어하려면 AWS Firewall Manager 가
적격.
AWS Firewall Manager 는 AWS WAF 용 관리형 규칙과 통합되므로, 사전에 구성된 WAF
규칙을 애플리케이션에 손쉽게 배포할 수 있습니다. 사용자는 콘솔에서 클릭 몇 번으로
AWS Marketplace 판매자가 제공 및 업데이트하는 관리형 규칙을 선택하고 Application
Load Balancer, API Gateway 및 Amazon CloudFront 인프라에서 일관되게 해당 규칙을
배포할 수 있습니다. https://aws.amazon.com/ko/firewall-manager/
~~~

---

# Q120 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/85807-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
A(X) : 자체 관리형 DNS 솔루션을 사용하고 있다고 이미 지문에서 언급했음. 자체적으로
해결할 수 있는 걸 Route 53 을 사용해서 추가적인 지출을 할 이유가 없음. 게다가 CDN
서비스를 사용해야한다는 단서가 없는데 굳이 CDN 서비스를 끼워넣을 이유가 없음.
B(O) : AWS Global Accelerator 는 애플리케이션 상태, 사용자의 위치 및 고객이 구성하는
정책의 변경에 즉각적으로 대응하여 항상 성능에 기반한 최적의 엔드포인트로 사용자
트래픽을 라우팅합니다......온프레미스 엔드포인트를 처리하도록 각 AWS 리전에 Network
Load Balancer(NLB)를 구성할 수 있습니다. 그러면 이러한 NLB가 AWS Global Accelerator
구성에서 엔드포인트가 될 수 있습니다.
https://aws.amazon.com/ko/global-accelerator/faqs/
C(X) : 탄력적 IP 주소를 AWS Global Accelerator 에 연결하는 게 더 효과적. 앞으로
인스턴스가 늘어날 때마다 EC2 인스턴스에 탄력적 IP를 부여할 건지?
D(X) : 가능은 한데 A와 같은 이유로 out. 그리고 굳이 귀찮게 ALB로 교체할 이유가 없음.
설명2:
표준 액셀러레이터의 경우 Global Accelerator 는 AWS 글로벌 네트워크를 사용하여
사용자가 구성한 상태, 클라이언트 위치 및 정책을 기반으로 트래픽을 최적의 지역
엔드포인트로 라우팅하여 애플리케이션의 가용성을 높입니다. 표준 액셀러레이터의
엔드포인트는 Network Load Balancer, Application Load Balancer, Amazon EC2 인스턴스
또는 하나의 AWS 리전 또는 여러 리전에 위치한 탄력적 IP 주소일 수 있습니다.
https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.h
tml
~~~

---

# Q121 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/85941-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
Amazon RDS 암호화된 DB 인스턴스의 경우 모든 로그, 백업 및 스냅샷이 암호화됩니다.
Amazon RDS DB 인스턴스의 암호화는 인스턴스를 생성할 때에만 가능하며 DB 인스턴스가
생성된 후에는 불가능합니다. 다만 암호화되지 않은 스냅샷의 사본을 암호화할 수 있기
때문에 암호화되지 않은 DB 인스턴스에 실질적으로 암호화를 추가할 수 있습니다. 즉, DB
인스턴스의 스냅샷을 만든 다음 해당 스냅샷의 암호화된 사본을 만들 수 있습니다. 그런
다음 암호화된 스냅샷에서 DB 인스턴스를 복구할 수 있고, 원본 DB 인스턴스의 암호화된
사본이 생깁니다.
https://docs.aws.amazon.com/ko_kr/AmazonRDS/latest/UserGuide/Overview.Encryption.h
tml#Overview.Encryption.Limitations
설명2:
https://docs.aws.amazon.com/ko_kr/AmazonRDS/latest/UserGuide/USER_RestoreFromSn
apshot.html#USE
https://docs.aws.amazon.com/ko_kr/AWSEC2/latest/UserGuide/EBSEncryption.html
~~~

---

# Q122 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/85942-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
A(X) : MFA는 다중 인증으로, 운영 부담 감소와는 아무런 상관 없음.
B(O) : ""AWS KMS 는 암호화 작업에 사용되는 키를 쉽게 생성하고 제어할 수 있도록
지원하는 관리형 서비스입니다. https://aws.amazon.com/ko/kms/faqs/
C(X) : ACM은 SSL/TLS 인증서 관련 서비스.
AWS Certificate Manager 는 AWS 서비스 및 연결된 내부 리소스에 사용할 공인 및 사설
SSL/TLS(Secure Sockets Layer/전송 계층 보안) 인증서를 손쉽게 프로비저닝, 관리 및
배포할 수 있도록 지원하는 서비스입니다.
https://aws.amazon.com/ko/certificate-manager/faqs/
D(X) : IAM 정책은 키 관리 서비스가 아니라 권한 관련 서비스.
참고:
https://aws.amazon.com/ko/kms/faqs/#:~:text=If%20you%20are%20a%20developer%20
who%20needs
~~~

---

# Q123 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/85943-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
AWS Certificate Manager를 사용하면 인증서를 신속하게 요청하고 Elastic Load Balancer,
Amazon CloudFront 배포, API Gateway의 API와 같은 ACM 통합 AWS 리소스에 배포하고
AWS Certificate Manager가 인증서 갱신을 처리하도록 할 수 있습니다. 또한 내부 리소스에
대한 개인 인증서를 만들고 중앙에서 인증서 수명 주기를 관리할 수 있습니다.
설명2:
ACM(AWS Certificate Manager)이 필요한 상황.
AWS Certificate Manager(ACM)는 AWS 서비스 및 연결된 내부 리소스에 사용할 공인 및
사설 SSL/TLS(Secure Sockets Layer/전송 계층 보안) 인증서를 손쉽게 프로비저닝, 관리 및
배포할 수 있도록 지원하는 서비스입니다.
https://aws.amazon.com/ko/certificate-manager/
따라서 A,D 둘 중 하나가 정답.
A(X) : 기존에 이미 사용하던 SSL 인증서가 있는데 하나 새로 만들 필요는 없음.
D(O) : A와 같은 이유로 정답.
리스너는 연결 요청을 확인하는 프로세스입니다. 로드 밸런서를 생성할 때 리스너를
정의하면 언제라도 로드 밸런서에 리스너를 추가할 수 있습니다. 암호화된 연결(SSL
오프로드라고도 함)을 사용하는 HTTPS 리스너를 생성할 수 있습니다. 이 기능을 사용하면
로드 밸런서와 SSL 또는 TLS 세션을 시작하는 클라이언트 간에 트래픽 암호화가
가능합니다.
https://docs.aws.amazon.com/ko_kr/elasticloadbalancing/latest/application/create-https
-listener.html
~~~

---

# Q124 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/86038-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
EC2 스팟 인스턴스를 통해 사용자는 여분의 Amazon EC2 컴퓨팅 용량에 입찰할 수 있으며
언제든지 시작 및 중지할 수 있는 상태 비저장 및 중단 가능한 워크로드를 위한 비용
효율적인 솔루션이 될 수 있습니다.
배치 처리 작업은 상태 비저장이고 언제든지 시작 및 중지할 수 있으며 일반적으로
완료하는 데 60분 이상 걸리므로 EC2 스팟 인스턴스는 이 워크로드에 적합합니다.
설명2:
상태비저장, 시작 및 중지 가능이라는 단서를 볼 때 스팟 인스턴스가 적절함.
~~~

---

# Q125 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/85221-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
시작하기 전에: EC2 인스턴스에 사용할 두 개의 가용 영역을 결정합니다. 이러한 각 가용
영역에서 하나 이상의 퍼블릭 서브넷으로 Virtual Private Cloud(VPC)를 구성합니다.
이러한 퍼블릭 서브넷은 로드 밸런서를 구성하는 데 사용됩니다. 대신 이러한 가용 영역의
다른 서브넷에서 EC2 인스턴스를 시작할 수 있습니다.
설명2:
・EC2 인스턴스와 RDS DB 인스턴스는 퍼블릭 인터넷에 노출되지 않아야 하므로 프라이빗
서브넷에 위치해야 함.
・그러면서도 EC2 인스턴스는 인터넷에 접속해야하니 NAT 서비스가 필요. NAT
게이트웨이(기본적으로 퍼블릭 NAT 게이트웨이를 말함)는 퍼블릭 서브넷에 위치해야 함.
퍼블릭 서브넷에서 퍼블릭 NAT 게이트웨이를 생성하고 생성 시 탄력적 IP 주소를 NAT
게이트웨이와 연결해야 합니다. 트래픽을 NAT 게이트웨이에서 VPC 용 인터넷 게이트웨이로
라우팅합니다.
https://docs.aws.amazon.com/ko_kr/vpc/latest/userguide/vpc-nat-gateway.html
・가용성 = Auto Scaling, Multi AZ
A(O) : EC2 인스턴스와 RDS 인스턴스 모두 프라이빗 서브넷에 위치해야하며 고가용성을
충족시켜야 하므로 다중 AZ를 사용.
B(X) : ALB는 퍼블릭 서브넷에 위치해야 함.
프라이빗 서브넷에 있는 Amazon EC2 인스턴스를 연결하려면 백엔드 인스턴스에서
사용하는 프라이빗 서브넷과 동일한 가용 영역에 퍼블릭 서브넷을 생성합니다. 그런 다음
퍼블릭 서브넷을 로드 밸런서와 연결합니다.
https://aws.amazon.com/ko/premiumsupport/knowledge-center/public-load-balancer-pr
ivate-ec2/
C(X) : 퍼블릭 서브넷에서 EC2 인스턴스를 시작하기 때문에 오답. EC2 인스턴스는 퍼블릭
인터넷에 노출되지 않아야 하므로 프라이빗 서브넷에 있어야 함.
D(X) : 하나의 서브넷으로 두 개의 가용영역에 걸쳐 사용하는 것은 불가.
각 서브넷은 완전히 하나의 가용 영역 내에 있어야 하며 여러 영역에 걸쳐 있을 수
없습니다.
https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html#subnet-basi
cs
E(O) : 각 AZ 에 퍼블릭 서브넷은 1 개 있어야 하고(NAT 게이트웨이가 들어가야 하므로),
프라이빗 서브넷은 1개 이상 있어야 함(EC2인스턴스와 RDS가 들어갈 곳). 각 AZ에 있는
퍼블릭 서브넷에 NAT 게이트웨이가 하나씩 들어가야 각 가용영역에 있는 프라이빗
서브넷마다 인터넷에 액세스가 가능한 상태가 되므로 NAT게이트웨이는 총 2개가 됨.
따라서 2개의 AZ에 걸쳐 퍼블릭 서브넷 2, 프라이빗 서브넷 2, NAT 게이트웨이 2개가 됨."
~~~

---

# Q126 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/86731-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
A(X) : 가장 최근 2년의 데이터는 즉시 검색할 수 있어야 하므로 콜드 스토리지는 부적절.
B(O) : 정답
C(X) : 가장 최근 2 년의 데이터는 모두 가용성이 높아야 하고 즉시 검색할 수 있어야하는
데이터이므로 Intelligent-Tiering이 따로 필요하진 않음.
D(X) : One Zone-IA는 고가용성 조건 불충족.
https://aws.amazon.com/ko/about-aws/whats-new/2018/04/announcing-s3-one-zone-i
nfrequent-access-a-new-amazon-s3-storage-class/?nc1=h_ls
~~~

---

# Q127 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/85432-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명
고가용성이므로 Auto Scaling이 들어간 C,D 둘 중 하나가 정답. EFS vs EBS를 비교해보면
보통은 EFS 가 정답인 경우가 많음. 일단 EBS 는 여러 EC2 인스턴스에서 동시 접속할 수
없다는 단점이 치명적이기 때문.
Amazon Elastic File System 은 전체 파일 시스템 액세스 의미 체계를 지원하는 표준 파일
시스템 인터페이스를 제공합니다.
https://docs.aws.amazon.com/efs/latest/ug/using-fs.html
EBS 다중 연결 볼륨에서 표준 파일 시스템 작업은 지원되는 구성이 아닙니다.
https://aws.amazon.com/ko/premiumsupport/knowledge-center/ebs-access-volumes-us
ing-multi-attach/
참조
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html
~~~

---

# Q128 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/85404-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
중단을 허용할 수 있음 = 스팟 인스턴스. 컨테이너에서 애플리케이션 실행 = ECS, EKS
같은 서비스. 답은 B.
~~~

---

# Q129 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/86658-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
・컨테이너화 되어있음 = ECS(또는 EKS) + Fargate.
A(O) : Amazon Aurora 는 PostgreSQL 과 호환되고 다중 리전 및 AZ 를 기본적으로
지원하므로 인프라 및 용량 계획을 유지 관리 가능.
Amazon Aurora 는 서버리스 및 기계 학습 기반 애플리케이션의 구축을 위한 규모에 따른
성능 및 고가용성, 완전한 오픈 소스 MySQL 및 PostgreSQL 호환 버전과 광범위한 개발자
도구를 제공….Amazon Aurora 는 데이터베이스 볼륨을 10GB 세그먼트로 자동으로
분리하여 여러 디스크에 분산합니다. 데이터베이스 볼륨에서 각 10GB 청크가 3 개의 AZ 에
6가지 방법으로 복제됩니다. https://aws.amazon.com/ko/rds/aurora/faqs/
B(X) : 애플리케이션이 컨테이너화 되어있다고 했으므로 Fargate 사용이 더 적절.
C(X) : CloudFront는 CDN 서비스로 지문의 상황엔 적합치 않음.
D(X) : ElastiCache는 웹 애플리케이션과 DB간 캐시 서비스로 지문의 상황엔 적합치 않음.
E(O) : ECS + Fargate로 컨테이너화된 애플리케이션 사용 가능.
AWS Fargate Fargate 는 Amazon EC2 인스턴스의 서버나 클러스터를 관리할 필요 없이
컨테이너를 실행하기 위해 Amazon ECS에 사용할 수 있는 기술입니다.
https://docs.aws.amazon.com/ko_kr/AmazonECS/latest/userguide/what-is-fargate.html
설명2:
Amazon Aurora 는 PostgreSQL 과 호환되는 완전히 관리되고 확장 가능하며 가용성이 높은
관계형 데이터베이스 서비스입니다. 데이터베이스를 Amazon Aurora 로 마이그레이션하면
데이터베이스 인프라를 유지 관리하는 운영 오버헤드가 줄어들고 회사는 애플리케이션 구축
및 확장에 집중할 수 있습니다. AWS Fargate 는 사용자가 기본 EC2 인스턴스를 관리할
필요 없이 컨테이너를 실행할 수 있도록 하는 완전 관리형 컨테이너 오케스트레이션
서비스입니다. 솔루션 설계자는 Amazon Elastic Container Service(Amazon ECS)와 함께
AWS Fargate 를 사용하여 웹 애플리케이션의 확장성과 효율성을 개선하고 기본 인프라를
유지 관리하는 운영 오버헤드를 줄일 수 있습니다.
~~~

---

# Q130 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/86659-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명
CPU 사용률에 따라 Auto Scaling = Target Tracking Policy. 정답은 B.
https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scalin
g-targettracking.html
~~~

---

# Q131 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/85992-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명
https://aws.amazon.com/premiumsupport/knowledge-center/cloudfront-access-to-amaz
on-s3/
https://docs.aws.amazon.com/ko_kr/AmazonCloudFront/latest/DeveloperGuide/private-c
ontent-restricting-access-to-s3.html#private-content-restricting-access-to-s3-overvie
w
S3 + CloudFront 를 사용하는 상황에서 S3 에 직접 액세스하는 것을 막으려면 OAC 또는
OAI를 사용하면 됨.
Amazon S3 버킷을 오리진으로 설정하여 CloudFront 를 사용하는 경우 다음과 같은 이점을
제공하는 방식으로 CloudFront 및 Amazon S3 를 구성할 수 있습니다. ◎공개적으로
액세스할 수 없도록 Amazon S3 버킷에 대한 액세스를 제한합니다. ◎뷰어(사용자)가
지정된 CloudFront 배포를 통해서만 버킷의 콘텐츠에 액세스할 수 있도록 합니다. 즉,
뷰어가 버킷에서 직접 또는 의도하지 않은 CloudFront 배포를 통해 콘텐츠에 액세스하는
것을 방지합니다. 이렇게 하려면 인증된 요청을 Amazon S3 로 보내도록 CloudFront 를
구성하고 CloudFront 의 인증된 요청에 대한 액세스만 허용하도록 Amazon S3 를
구성합니다. CloudFront는 Amazon S3 오리진에 인증된 요청을 전송하는 두 가지 방법으로
오리진 액세스 제어(OAC)와 오리진 액세스 ID(OAI)를 제공합니다. OAC 는 다음을
지원하므로 OAC를 사용하는 것이 좋습니다.
https://docs.aws.amazon.com/ko_kr/AmazonCloudFront/latest/DeveloperGuide/private-c
ontent-restricting-access-to-s3.html
~~~

---

# Q132 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/86654-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
전 세계적으로 웹 사이트 요구 충족 = CloudFront.
빠른 응답을 위한 Cloudfront와 인프라를 최소화하기 위한 s3
~~~

---

# Q133 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/85423-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
기본 운영 체제에 대한 액세스 유지 = Amazon RDS Custom.
Amazon Relational Database Service(Amazon RDS) Custom 은 기본 OS 및 DB 환경에
액세스할 필요가 있는 레거시, 사용자 지정, 패키지 애플리케이션을 위한 관리형
데이터베이스 서비스입니다.
https://aws.amazon.com/ko/about-aws/whats-new/2021/10/amazon-rds-custom-oracle
/
참고:
https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-custom.html
https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/working-with-custom-oracl
e.html
~~~

---

# Q134 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/85993-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
A(X) : 최소한의 운영 오버헤드라고 했으므로 SSE-KMS 보다는 SSE-S3 가 AWS 에서 다
관리하기 때문에 더 적합. 또한 회사는 데이터를 S3 버킷에 저장한다고 했으므로 기존
버킷이 있는 것이고, 이는 현재 리전에서 새 S3 버킷을 생성할 필요가 없음을 의미. 그리고
지문에서 운영 오버헤드에 대한 언급은 있어도 비용에 대한 언급은 없음.
B(X) : S3에 쿼리하는 건 RDS가 아니라 Athena가 더 적합.
C(O) : KMS 필요없이 S3 측에서 암호화할 수 있음. 기존 버킷에 데이터를 로드하고 다른
리전으로 복제하는 것이기 때문에 다른 리전에서도 기존 및 신규 데이터를 모두 사용할 수
있음.
D(X) : B와 같은 이유로 오답.
~~~

---

# Q135 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/85994-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
A(X) : 대상 서비스로 제한되어야 한다는 조건 불충족. VPC 내의 특정 애플리케이션이나
서비스에 연결하려면 PrivateLInk 가 필요. 또한 연결은 회사의 VPC 에서만 시작되어야
한다는 점 불충족.
설명1:
VPC 피어링을 사용하면 VPC 를 비공개로 연결할 수 있지만 AWS PrivateLink 를 사용하면
VPC 의 애플리케이션이나 서비스를 VPC 피어링 연결에서 연결할 수 있는 엔드포인트로
구성할 수 있습니다.
(https://docs.aws.amazon.com/ko_kr/vpc/latest/userguide/vpc-peering.html)
B(X) : Virtual Private Gateway는 VPN 엔드포인트.
가상 프라이빗 게이트웨이는 단일 VPC 에 연결할 수 있는 사이트 간 VPN 연결의 Amazon
측 VPN 엔드포인트입니다.
https://docs.aws.amazon.com/ko_kr/vpn/latest/s2svpn/VPC_VPN.html
C(X) : 대상 서비스로 제한되어야 한다는 조건 불충족. 퍼블릭 서브넷의 NAT 게이트웨이는
퍼블릭 NAT 게이트웨이로서, IGW, VPC, 온프레미스 네트워크에 연결할 수 있지만 특정
서비스에만 접속하도록 할 수 있다는 건 없음.
""퍼블릭 서브넷에서 퍼블릭 NAT 게이트웨이를 생성하고 생성 시 탄력적 IP 주소를 NAT
게이트웨이와 연결해야 합니다. 트래픽을 NAT 게이트웨이에서 VPC 용 인터넷 게이트웨이로
라우팅합니다. 또는 퍼블릭 NAT 게이트웨이를 사용하여 다른 VPC 또는 온프레미스
네트워크에 연결할 수 있습니다.
https://docs.aws.amazon.com/ko_kr/vpc/latest/userguide/vpc-nat-gateway.html
D(O) : A번 참고.
~~~

---

# Q136 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/85438-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
A(O) : ongoing replication(진행중인 복제)은 CDC(변경 데이터 캡처)라고도 하며 소스
데이터 스토어에서 진행 중인 변경 사항을 복제할 때 이 프로세스를 사용.
(https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Task.CDC.html)
이는 동기화된 상태를 만들어줌. "AWS DMS 를 사용하면 일회성 마이그레이션을 수행하고
지속적인 변경 사항을 복제하여 소스와 대상을 동기화 상태로 유지할 수 있습니다.
https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html
C(O) : DMS 는 대상이 소스와 동기화된 상태를 유지하도록 지속적 복제를 지원하지만,
SCT는 그렇지 않습니다. AWS Database Migration Service(DMS)는 다양한 동종 및 이기종
데이터 복제를 지원합니다.
https://aws.amazon.com/ko/dms/faqs/?refid=bef7080f-573e-4a75-b22b-85f316173744
설명2:
AWS Database Migration Service 는 Oracle 에서 Oracle 로의 동종 마이그레이션은 물론
Oracle 또는 Microsoft SQL Server 에서 Amazon Aurora 로의 서로 다른 데이터베이스
플랫폼 간의 이기종 마이그레이션을 지원합니다. AWS Database Migration Service 를
사용하면 지원되는 소스에서 지원되는 대상으로 짧은 지연 시간으로 데이터를 지속적으로
복제할 수도 있습니다. 예를 들어 여러 소스에서 Amazon Simple Storage Service(Amazon
S3)로 복제하여 가용성과 확장성이 뛰어난 데이터 레이크 솔루션을 구축할 수 있습니다.
Amazon Redshift 로 데이터를 스트리밍하여 데이터베이스를 페타바이트 규모의 데이터
웨어하우스로 통합할 수도 있습니다. 지원되는 소스 및 대상 데이터베이스에 대해 자세히
알아보세요.
https://aws.amazon.com/dms/
~~~

---

# Q137 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/85997-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
A(X) : 향후 알림은 계정 관리자로 제한되어야 한다고 했으므로 오답.
B(O) : AWS Organizations 콘솔에서 또는 AWS CLI 또는 AWS SDK를 사용하여 프로그래밍
방식으로 조직 내 계정의 대체 연락처를 업데이트할 수 있습니다. 조직의 관리 계정을
사용하여 조직의 모든 계정에 대한 계정 설정을 보고 편집할 수 있습니다. 기본 계정
소유자는 루트 계정의 이메일에 대한 모든 이메일 통신을 계속 수신합니다.
https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact-
alternate.html
C(X) : 루트 이메일 수신자가 한 계정의 루트 사용자 이메일 주소로 전송된 알림을
놓쳤다고 했는데, 선택지 C의 방식은 기존의 방식과 동일함.
D(X) : 향후 알림은 계정 관리자로 제한되어야 한다고 했으므로 오답.
참고
https://docs.aws.amazon.com/ko_kr/organizations/latest/userguide/orgs_best-practices_
mgmt-acct.html#best-practices_mgmt-acct_email-address
~~~

---

# Q138 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/85999-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
선택지는 활성/대기 인스턴스 쌍을 사용하는 A,B 와 대기열 호스팅 방식을 사용하는 C,D 로
나눠짐.
활성/대기 방식은 활성 인스턴스가 다운되어도 대기 인스턴스가 활성 인스턴스를 대체할 수
있으므로 가용성이 높은 방식. 따라서 A,B 둘 중 하나가 답.
PostgreSQL 데이터베이스를 사용하는 A보다는 Amazon RDS for Postgre를 사용하는 B가
운영 오버헤드 절감 효과가 큼.
Amazon RDS 를 사용하면 클라우드에서 PostgreSQL 배포를 손쉽게 설정, 운영 및 확장할
수 있습니다. Amazon RDS에서는 비용 효율적이고 크기 조정 가능한 하드웨어 용량을 갖춘
확장 가능한 PostgreSQL 을 몇 분 만에 배포할 수 있습니다. Amazon RDS 에서는
PostgreSQL 소프트웨어 설치 및 업그레이드, 스토리지 관리, 고가용성 및 읽기 처리량을
위한 복제, 재해 복구용 백업 등 복잡하고 시간 소모적인 관리 작업을 관리합니다.
https://aws.amazon.com/ko/rds/postgresql/
설명2:
Amazon MQ 로 마이그레이션하면 대기열 관리의 오버헤드가 줄어듭니다. C 와 D 는
오답됩니다.
A 와 B 사이에서 결정한다는 것은 EC2 용 AutoScaling 그룹 또는 Postgress 용 RDS(모두
다중 AZ)로 이동하기로 결정하는 것을 의미합니다. RDS 옵션은 필요한 도구와
소프트웨어를 서비스로 제공하므로 운영에 미치는 영향이 적습니다. 예를 들어 읽기
복제본과 같은 추가 노드를 DB에 추가하려는 노력을 고려하십시오.
https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/activestandby-broker
-deployment.html
~~~

---

# Q139 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/85872-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
S3 복제를 사용하면 S3 버킷 간에 자동으로 복제됩니다. S3 이벤트를 CloudWatch
Events 에서 감지하여 특정 동작을 수행할 수 있습니다. Amazon S3 복제를 사용하면 S3
CRR(교차 리전 복제)을 사용하여 서로 다른 AWS 리전에서, 또는 S3 SRR(동일 리전
복제)을 사용하여 같은 AWS 리전 내의 버킷 간에 S3 객체를 자동으로 복제하도록 Amazon
S3를 구성할 수 있습니다. https://aws.amazon.com/ko/s3/features/replication/
Amazon S3 는 버킷에서 특정 이벤트가 발생할 때마다 Amazon EventBridge 에 이벤트를
보낼 수 있습니다. 이벤트 유형 : Object Created
https://docs.aws.amazon.com/ko_kr/AmazonS3/latest/userguide/EventBridge.html)
Amazon EventBridge 는 Amazon SageMaker 의 상태 변경 이벤트를 모니터링합니다.
EventBridge 를 사용하면 SageMaker 를 자동화하고 교육 작업 상태 변경 또는 끝점 상태
변경과 같은 이벤트에 자동으로 응답할 수 있습니다. 자동으로 트리거될 수 있는 작업의 몇
가지 예는 다음과 같습니다. AWS Lambda 함수 호출
https://docs.aws.amazon.com/sagemaker/latest/dg/automating-sagemaker-with-eventbr
idge.html
설명2:
이 솔루션은 파일을 자동으로 이동하고, 복사된 데이터에서 Lambda 함수를 실행하고,
최소한의 운영 오버헤드로 데이터 파일을 SageMaker Pipelines 로 보내는 요구 사항을
충족합니다. S3 복제는 파일이 도착하면 초기 S3 버킷에서 분석 S3 버킷으로 파일을
복사할 수 있습니다. 분석 S3 버킷은 객체가 생성될 때 Amazon EventBridge(Amazon
CloudWatch Events)에 이벤트 알림을 보낼 수 있습니다. EventBridge 는 Lambda 및
SageMaker 파이프라인을 ObjectCreated 규칙의 대상으로 트리거할 수 있습니다.
Lambda는 복사된 데이터에서 패턴 일치 코드를 실행할 수 있으며 SageMaker Pipelines는
데이터 파일로 파이프라인을 실행할 수 있습니다.
S3 복제가 자동으로 수행할 수 있는 경우 분석 S3 버킷에 파일을 복사하는 Lambda
함수를 생성할 필요가 없기 때문에 옵션 A 는 올바르지 않습니다. 또한 Lambda 함수를
관리하기 위해 운영 오버헤드를 추가합니다.
S3 복제가 자동으로 수행할 수 있는 경우 분석 S3 버킷에 파일을 복사하는 Lambda
함수를 생성할 필요가 없기 때문에 옵션 B 는 올바르지 않습니다. 또한 Lambda 함수를
관리하기 위해 운영 오버헤드를 추가합니다.
여러 대상과 함께 S3 이벤트 알림을 사용하면 이벤트가 너무 많은 경우 제한 또는 전달
실패가 발생할 수 있으므로 옵션 C는 올바르지 않습니다.
참조:
https://aws.amazon.com/ko/blogs/machine-learning/automate-feature-engineering-pipe
lines-with-amazon-sagemaker/
https://docs.aws.amazon.com/sagemaker/latest/dg/automating-sagemaker-with-eventbr
idge.html
https://aws.amazon.com/ko/about-aws/whats-new/2021/04/new-options-trigger-amazo
n-sagemaker-pipeline-executions/
~~~

---

# Q140 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/86083-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
・EC2 인스턴스에서 실행되는 워크로드는 언제든지 중단될 수 있습니다 = 스팟 인스턴스
・프론트엔드 활용도와 API 계층 활용도는 내년에 예측할 수 있습니다 = Savings Plans
Savings Plans 는 1 년 또는 3 년 기간의 일정 사용량 약정(시간당 USD 요금으로 측정)을
조건으로 Amazon EC2, AWS Lambda 및 AWS Fargate 사용량에 대해 저렴한 요금을
제공하는 유연한 요금 모델입니다. Savings Plans 에 가입하면 약정 사용량까지 할인된
Savings Plans 요금을 적용받습니다.
https://aws.amazon.com/ko/savingsplans/compute-pricing/
・그 중에서도 Compute Savings Plans가 정답.
Compute Savings Plans 는 최대 66%까지 비용을 절감할 수 있는 가장 유연한 요금
모델입니다. 이 플랜은 인스턴스 패밀리, 크기, AZ, 리전, OS 또는 테넌시와 관계없이 EC2
인스턴스 사용량에 적용되며, Fargate 또는 Lambda 사용량에도 적용됩니다.
https://aws.amazon.com/ko/savingsplans/compute-pricing/
정답은 A,C.
설명2:
EC2 instance Savings Plan은 72%, Compute Savings Plans는 66%를 절약합니다. 그러나
링크에 따르면 "Compute Savings Plans는 최고의 유연성을 제공하고 비용을 최대 66%까지
줄이는 데 도움이 됩니다.
이러한 요금제는 인스턴스 패밀리, 크기, AZ, 리전, OS 또는 테넌시에 관계없이 EC2
인스턴스 사용에 자동으로 적용되며 Fargate 및 Lambda 사용에도 적용됩니다." EC2
인스턴스 절약 계획은 Fargate 또는 Lambda에 적용되지 않습니다.
~~~

---

# Q141 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/85439-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
ALB를 오리진으로 사용할 수 있음
원본이 하나 이상의 Amazon EC2 인스턴스에서 호스트되는 하나 이상의 HTTP 서버(웹
서버)인 경우 Application Load Balancer 를 사용하여 인스턴스에 트래픽을 분산할 수
있습니다. Application Load Balancer 를 CloudFront 의 원본으로 사용하는 방법에 대한
자세한 내용은
https://docs.aws.amazon.com/ko_kr/AmazonCloudFront/latest/DeveloperGuide/Download
DistS3AndCustomOrigins.html#concept_elb_origin
~~~

---

# Q142 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/86667-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
TCP/UDP+엔드포인트에 입력할 수 있는 고정 IP 주소를 가져야 한다는 대목에서 Global
Accelerator임을 유추할 수 있음.
설명2:
AWS Global Accelerator 와 Amazon CloudFront 는 AWS 글로벌 네트워크와 전 세계 엣지
로케이션을 사용하는 별도의 서비스입니다. CloudFront 는 캐시 가능한 콘텐츠(예: 이미지
및 비디오)와 동적 콘텐츠(예: API 가속 및 동적 사이트 제공) 모두의 성능을 향상시킵니다.
Global Accelerator 는 하나 이상의 AWS 리전에서 실행되는 애플리케이션에 대해 에지의
패킷을 프록시하여 TCP 또는 UDP 를 통해 광범위한 애플리케이션의 성능을 개선합니다.
Global Accelerator는 게임(UDP), IoT(MQTT) 또는 VoIP와 같은 비HTTP 사용 사례와 특히
고정 IP 주소 또는 결정론적이고 빠른 지역 장애 조치가 필요한 HTTP 사용 사례에
적합합니다. 두 서비스 모두 DDoS 보호를 위해 AWS Shield와 통합됩니다.
~~~

---

# Q143 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/86473-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
ECS 는 컨테이너화된 애플리케이션을 실행하기 위해 확장성이 뛰어난 관리형 환경을
제공하여 운영 오버헤드를 줄입니다. ECS 를 대상으로 ALB 를 설정하면 확장성과 가용성을
위해 애플리케이션의 여러 인스턴스에 트래픽을 분산할 수 있습니다. 이 솔루션을 사용하면
여러 팀이 각 애플리케이션을 독립적으로 관리하여 팀 자율성과 효율적인 개발을 촉진할 수
있습니다.
A 는 이벤트 기반 및 서버리스 워크로드에 더 적합합니다. 모놀리식 애플리케이션을
마이그레이션하고 기존 코드베이스를 유지 관리하는 데 이상적인 선택이 아닐 수 있습니다.
B 는 Lambda 및 API Gateway 와 통합되므로 애플리케이션을 더 작은 애플리케이션으로
분할하고 독립적으로 관리하는 데 필요한 유연성을 제공하지 못할 수 있습니다.
C 는 인프라 관리 및 수동 확장을 포함합니다. ECS 와 같은 컨테이너 서비스를 사용할
때보다 운영 오버헤드가 높아질 수 있습니다.
~~~

---

# Q144 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/86781-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Replication.ht
ml
#Aurora.Replication.Replicas Aurora 복제본에는 두 가지 주요 목적이 있습니다.
애플리케이션에 대한 읽기 작업을 확장하기 위해 쿼리를 실행할 수 있습니다. 일반적으로
클러스터의 리더 엔드포인트에 연결하여 이를 수행합니다. 이렇게 하면 Aurora 는
클러스터에 있는 만큼 많은 Aurora 복제본에 읽기 전용 연결에 대한 로드를 분산시킬 수
있습니다. Aurora 복제본은 가용성을 높이는 데도 도움이 됩니다. 클러스터의 라이터
인스턴스를 사용할 수 없게 되면 Aurora 는 리더 인스턴스 중 하나를 자동으로 승격시켜 새
라이터로 대신합니다.
https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.html
설명2:
ReadIOPS 가 증가하고 있다고 했으므로 Aurora replica 를 통한 읽기 부하 분산 가능
"Aurora 는 클러스터에 있는 만큼의 Aurora 복제본에 읽기 전용 연결에 대한 로드를 분산할
수 있습니다.
https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Replication.ht
ml#Aurora.Replication.Replicas
~~~

---

# Q145 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/86474-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
A(X) : 두 번째 온디맨드 인스턴스를 생성하기만 하고 Auto Scaling 설정을 안 하므로
확장성이 D에 비해 떨어짐.
B(X) : Route 53 Weighted Routing은 각 리소스로 라우팅되는 트래픽 양을 조절하는 기능
가중 라우팅을 사용하면 여러 리소스를 단일 도메인 이름(example.com) 또는 하위 도메인
이름(acme.example.com)과 연결하고 각 리소스로 라우팅되는 트래픽 양을 선택할 수
있습니다.
https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-weighted.h
tml
C(X) : CloudWatch 경보는 임계값에 도달하면 자동으로 알림을 보내는 서비스.
""인스턴스 중 하나에 대한 CloudWatch 지표를 모니터링하는 CloudWatch 경보를 생성할
수 있습니다. 지표가 지정된 임계값에 도달하면 CloudWatch 에서 자동으로 알림을
보냅니다.
https://docs.aws.amazon.com/ko_kr/AWSEC2/latest/UserGuide/using-cloudwatch-create
alarm.html
D(O) : 스팟인스턴스라는 점이 걸리긴 하지만 어차피 인스턴스를 중지해서는 안 된다는
말이 나온 것도 아니고, Auto Scaling이 명시되어있으므로 정답에 가장 가까움.
설명2:
데이터베이스를 Amazon Aurora MySQL 로 마이그레이션합니다. 이렇게 하면 DB 가
자체적으로 확장됩니다. 조정할 필요 없이 자동으로 크기가 조정됩니다. 시작 템플릿을
사용하여 웹 앱의 AMI 를 생성합니다. 이렇게 하면 앱의 향후 인스턴스를 원활하게 생성할
수 있습니다. 그런 다음 Auto Scaling 그룹에 추가하면 수요에 따라 확장 및 축소되므로
비용을 절약할 수 있습니다.
스팟 집합을 사용하여 인스턴스를 시작합니다. 이것은 아마존이 적합하다고 판단하는
시점에 종료되는 비용으로 스팟 인스턴스가 크게 할인되기 때문에 질문의 "가장 비용
효율적인" 부분을 해결합니다. 이 부분에 대해서는 약간의 이견이 있기 때문이라고
생각합니다. 가장 비용 효율적이지만 아마존이 사용량이 많은 기간에 해당 스팟 인스턴스를
종료한다면 끔찍한 선택이 될 것입니다.
~~~

---

# Q146 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/86750-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
A(X) : 계속 사용량이 있고, 사용량이 적은 주말에도 꾸준히 사용량은 나오고 있는데 계속
작동 중인 걸 스팟인스턴스로 둘 이유가 없음. 스팟 인스턴스는 중지해도 되는 인스턴스에
사용되는 인스턴스 유형. 사용량이 많은 시간을 예상할 수 있는 상황에선 예약 인스턴스가
적절.
B(O) : 상태 비저장 애플리케이션이라는 단서가 있으므로 추가 용량에 대해서는 스팟
인스턴스를 사용하여 비용 절감 가능.
C(X) : 기본 사용량 수준은 예상할 수 있으므로 예약 인스턴스가 적절.
D(X) : Dedicated Instance는 온디맨드에 비해서도 비용이 많이 들어가는 인스턴스 유형임.
해당 부분에 대해서는 아래의 링크를 참고할 것.
https://aws.amazon.com/ko/ec2/pricing/on-demand/
https://aws.amazon.com/ko/ec2/pricing/dedicated-instances/
~~~

---

# Q147 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/86864-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
A(X) : Life Cycle Policy를 사용하면 되는데 굳이 AWS Backup까지 동원할 필요가 없음.
B(O) : 정답. 한 달 후에 로그를 보관하려면 S3 가 필요합니다. CloudWatch Logs 로는
그렇게 할 수 없습니다.
C(X) : CloudWatch Logs는 스토리지 서비스가 아님.
D(X) : C와 같은 이유로 오답.
~~~

---

# Q148 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/85424-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
실패한 메시지를 보관할 SQS 대기열이 필요. 정답은 D.
https://docs.aws.amazon.com/ko_kr/AWSSimpleQueueService/latest/SQSDeveloperGuide
/sqs-dead-letter-queues.html
C 같은 경우엔 재시도 전략인데, 'When tenure occurs the corresponding data is not
ingested unless company manually reruns the job' (Tenure가 발생하면 회사에서 수동으로
작업을 다시 실행하지 않는 한 해당 데이터가 수집되지 않습니다.) 라는 대목이 있므로
C는 오답. Amazon SNS가 메시지 전송을 재시도하는 방식이 전송 정책에 따라 결정됩니다.
전송 정책이 소진되면 Amazon SNS 는 전송 재시도를 중지하고 배달 못한 편지 대기열이
구독에 연결되어 있지 않는 한 메시지를 삭제합니다.
https://docs.aws.amazon.com/ko_kr/sns/latest/dg/sns-message-delivery-retries.html
참고:
https://docs.aws.amazon.com/ko_kr/sns/latest/dg/sns-dead-letter-queues.html
~~~

---

# Q149 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/86784-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명
자세한 내용은 아래 URL.
https://docs.aws.amazon.com/ko_kr/AWSSimpleQueueService/latest/SQSDeveloperGuide
/FIFO-queues.html
FIFO(First-In-First-Out) 대기열은 작업 및 이벤트 순서가 중요하거나 중복을 허용할 수
없는 경우 애플리케이션 간의 메시징을 향상하도록 설계되었습니다. FIFO 대기열을 사용할
수 있는 상황의 예는 다음과 같습니다. 사용자가 입력한 명령이 올바른 순서로 실행되도록
합니다. 올바른 순서로 가격 수정을 전송하여 올바른 제품 가격을 표시합니다. 학생이
계정을 등록하기 전에 코스에 등록하지 못하도록 합니다.
~~~

---

# Q150 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/86034-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명
자세한 내용은 아래 URL.
https://docs.aws.amazon.com/ko_kr/AWSSimpleQueueService/latest/SQSDeveloperGuide
/FIFO-queues.html
FIFO(First-In-First-Out) 대기열은 작업 및 이벤트 순서가 중요하거나 중복을 허용할 수
없는 경우 애플리케이션 간의 메시징을 향상하도록 설계되었습니다. FIFO 대기열을 사용할
수 있는 상황의 예는 다음과 같습니다. 사용자가 입력한 명령이 올바른 순서로 실행되도록
합니다. 올바른 순서로 가격 수정을 전송하여 올바른 제품 가격을 표시합니다. 학생이
계정을 등록하기 전에 코스에 등록하지 못하도록 합니다.
~~~

---

# Q151 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/86475-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
A(O) : AWS Control Tower Guardrail 을 사용해 SCP 를 통한 AWS API 액세스를 제한하여
특정 AWS 리전에서의 특정 리소스 방지 가능.
오늘부터 AWS Control Tower 를 사용하여 가드레일 이라고 하는 데이터 상주 예방 및 탐지
제어를 배포할 수 있습니다 . 이러한 가드레일은 서비스 제어 정책(SCP) 을 통해 AWS
API 에 대한 액세스를 제한하여 원치 않는 AWS 리전에서 리소스 프로비저닝을 방지합니다.
예를 들어 독일의 AWS 고객은 AWS Identity and Access Management(IAM) 및 AWS
Organizations 와 같은 글로벌 서비스를 제외하고 프랑크푸르트 이외의 지역에서 AWS
서비스에 대한 액세스를 거부할 수 있습니다. 또한 AWS Control Tower 는 Amazon Simple
Storage Service(Amazon S3) 교차 리전 복제 차단 또는 인터넷 게이트웨이 생성 차단과
같은 기본 AWS 서비스 옵션의 데이터 상주를 추가로 제어하기 위한 가드레일을
제공합니다.
https://aws.amazon.com/blogs/aws/new-for-aws-control-tower-region-deny-and-guar
drails-to-help-you-meet-data-residency-requirements/
B(X) : AWS WAF 는 Web ACL 을 통해 특정 국가나 지리적 위치, IP 의 요청을 차단할 수
있으나 리전을 차단하는 옵션은 없음.
https://aws.amazon.com/ko/premiumsupport/knowledge-center/waf-allow-block-countr
y-geolocation/)(https://aws.amazon.com/ko/premiumsupport/knowledge-center/waf-allo
w-my-ip-block-other-ip/
C(O) : AWS Organizations를 사용해 특정 리전에 대한 액세스 차단 가능.
이 SCP 는 지정된 리전 외부의 모든 작업에 대한 액세스를 거부합니다. 이 정책은 Deny
효과를 사용하여 승인된 두 리전(eu-central-1 및 eu-west-1) 중 하나를 대상으로 하지
않는 작업에 대한 모든 요청에 대한 액세스를 거부합니다.
https://docs.aws.amazon.com/ko_kr/organizations/latest/userguide/orgs_manage_policie
s_scps_examples_general.html
D(X) : NACL 0.0.0.0/0 의 아웃바운드 트래픽을 막아버리면 트래픽이 외부로 나갈 수 없어
아예 통신 자체가 안 됨. IAM 정책으로 다른 AWS 리전의 다른 리소스에 대한 액세스를
막는 것은 가능.
https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_aws_d
eny-requested-region.html
E(X) : AWS Config 는 리소스 구성 변경 사항을 감지하고 해당 구성 변경 기록 파일을
전송할 수 있는 서비스로 지문의 요구사항에는 부합하지 않음.
~~~

---

# Q152 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/86046-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
A(X) : 권한에 대한 언급이 없는데 굳이 IAM을 사용할 이유가 없음.
B(X) : ElastiCache는 웹 애플리케이션과 DB 간의 캐시 서비스.
C(X) : A와 같은 이유로 오답.
D(O) : EC2 인스턴스를 자동으로 중지 및 시작하여 Amazon Elastic Compute
Cloud(Amazon EC2) 사용량을 줄이려고 합니다. 이를 위해 AWS Lambda 및 Amazon
EventBridge를 사용하려면 어떻게 해야 하나요?
이하의 항목 참고
https://aws.amazon.com/ko/premiumsupport/knowledge-center/start-stop-lambda-even
tbridge/
설명2:
일반적인 개발 환경에서 개발 및 테스트 데이터베이스는 대부분 하루 8 시간 동안 사용되며
사용하지 않을 때는 유휴 상태입니다. 그러나 데이터베이스에는 이 유휴 시간 동안 컴퓨팅
및 스토리지 비용이 청구됩니다. 전체 비용을 줄이기 위해 Amazon RDS 에서는 인스턴스를
일시적으로 중지할 수 있습니다. 인스턴스가 중지된 동안에는 스토리지 및 백업에 대한
요금이 부과되지만 DB 인스턴스 시간에 대한 요금은 부과되지 않습니다. 중지된
인스턴스는 7 일 후에 자동으로 시작됩니다. 이 게시물은 컴퓨팅 비용을 절감하기 위해
특정 태그로 유휴 데이터베이스를 중지 및 시작하도록 Lambda 함수를 예약할 수 있는
AWS Lambda 및 Amazon EventBridge를 사용하는 솔루션을 제시합니다. 두 번째 게시물은
AWS Systems Manager 를 사용하여 유휴 Amazon RDS 데이터베이스의 중지 및 시작을
수행하는 솔루션을 제시합니다.
~~~

---

# Q153 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/86933-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
A(X) : 초기에는 사용량이 많으므로 S3 Standard가 적절.
B(X) : 90일 이상된 벨소리는 다운로드가 드물다고 했으므로 부적절.
C(X) : Amazon S3 Inventory는 Amazon S3에서 스토리지 관리를 지원하기 위해 제공하는
도구 중 하나로, 이 인벤토리를 사용하여 비즈니스, 규정 준수 및 규제 요건에 대한 객체의
복제 및 암호화 상태를 감사하고 보고할 수 있습니다. 또한 Amazon S3 동기식 List API
작업의 대안으로 Amazon S3 인벤토리를 사용하면 비즈니스 워크플로 및 빅 데이터 업무를
단순화하고 속도를 높일 수 있습니다.
https://docs.aws.amazon.com/ko_kr/AmazonS3/latest/userguide/storage-inventory.html
D(O) : 90 일 이전에는 S3 Standard 로 빈번한 액세스 처리, 90 일 이후에는 다운로드가
드물지만 가장 많이 액세스하는 일부 파일은 쉽게 사용, 즉 빠르게 액세스할 수 있어야
하므로 액세스 소요 시간이 적은 S3 Standard-IA사용이 적절.
설명2:
이 솔루션은 사용자가 가장 많이 액세스하는 파일을 쉽게 사용할 수 있도록 유지하면서
스토리지 비용을 절약해야 하는 요구 사항을 충족합니다. S3 수명 주기 정책은 사전 정의된
규칙에 따라 한 스토리지 클래스에서 다른 스토리지 클래스로 객체를 자동으로 이동할 수
있습니다. S3 Standard-IA는 자주 액세스하지 않지만 필요할 때 신속하게 액세스해야 하는
데이터를 위한 저비용 스토리지 클래스입니다. 드물게 다운로드되는 90 일 이상의 벨소리에
적합합니다.
객체의 초기 스토리지 계층에 대해 S3 Standard-IA 를 구성하면 빈번한 액세스 및 검색
요금으로 더 많은 비용이 발생할 수 있으므로 옵션 A는 올바르지 않습니다.
파일을 S3 Intelligent-Tiering으로 이동하면 90일보다 오래된 벨소리에는 필요하지 않을 수
있는 추가 모니터링 및 자동화 요금이 발생할 수 있으므로 옵션 B는 올바르지 않습니다.
옵션 C 는 올바르지 않습니다. S3 인벤토리를 사용하여 객체를 관리하고 객체를 S3
Standard-IA 로 이동하는 것은 복잡하고 시간이 많이 소요될 수 있으며 자동 비용 절감을
제공하지 않기 때문입니다.
참조:
https://aws.amazon.com/s3/storage-classes/
https://aws.amazon.com/s3/cloud-storage-cost-optimization-ebook/
~~~

---

# Q154 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/86359-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
S3 객체 수정 및 삭제 방지 = S3 Object Lock.
S3 객체 잠금을 사용하면 write once, read many(WORM) 모델을 사용하여 객체를 저장할
수 있습니다. 객체 잠금은 고정된 시간 동안 또는 무기한으로 객체의 삭제 또는 덮어쓰기를
방지하는 데 도움이 될 수 있습니다. 보관 기간은 정해진 시간 동안 객체 버전을
보호합니다. 객체 버전에 보관 기간을 설정하면 Amazon S3 는 객체 버전의 메타데이터에
타임스탬프를 저장하여 보관 기간이 만료되는 시점을 표시합니다. 보관 기간이 만료된 후
객체 버전에 법적 보존을 설정하지 않는 한 객체 버전을 덮어쓰거나 삭제할 수 있습니다.
https://docs.aws.amazon.com/ko_kr/AmazonS3/latest/userguide/object-lock-overview.ht
ml#object-lock-retention-periods
설명2:
규정 준수 모드에서는 AWS 계정의 루트 사용자를 포함하여 어떤 사용자도 보호 객체
버전을 덮어쓰거나 삭제할 수 없습니다. 객체가 규정 준수 모드에서 잠겨 있으면 보관
모드를 변경할 수 없으며 보관 기간을 단축할 수 없습니다. 규정 준수 모드는 보존 기간
동안 개체 버전을 덮어쓰거나 삭제할 수 없도록 합니다. 거버넌스 모드에서 사용자는
특별한 권한이 없는 한 개체 버전을 덮어쓰거나 삭제할 수 없으며 잠금 설정을 변경할 수
없습니다. 거버넌스 모드를 사용하면 대부분의 사용자가 개체를 삭제하지 못하도록
보호하지만 필요한 경우 일부 사용자에게 보존 설정을 변경하거나 개체를 삭제할 수 있는
권한을 계속 부여할 수 있습니다. 거버넌스 모드에서는 특수 권한이 있는 일부 사용자가
개체를 삭제할 수 있으며 이는 요구 사항에 위배됩니다.
규정 준수:
- 객체 버전은 루트 사용자를 포함한 모든 사용자가 덮어쓰거나 삭제할 수 없습니다.
- 개체 보존 모드를 변경할 수 없으며 보존 기간을 단축할 수 없습니다. 거버넌스:
- 대부분의 사용자는 개체 버전을 덮어쓰거나 삭제할 수 없으며 잠금 설정을 변경할 수
없습니다.
- 일부 사용자는 보존을 변경하거나 개체를 삭제할 수 있는 특별한 권한이 있습니다.
~~~

---

# Q155 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/86795-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
S3 버킷에 저장 + 요청이 지리적으로 어디에서 발생했는지에 관계없이 콘텐츠를 신속하게
제공 = S3 + CloudFront. 답은 C.
설명2:
CloudFront 는 로컬 캐시를 사용하여 응답을 제공하고, AWS Global Accelerator 는 요청을
프록시하고 응답을 위해 항상 애플리케이션에 연결합니다.
~~~

---

# Q156 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/85770-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
KPI 로 표시하기 위해선 Athena 가 필요하고, Athena 는 S3 에 쿼리함. 따라서 KPI 만
기억해도 A,E가 정답임을 쉽게 유추할 수 있음.
・데이터베이스에서 가져온 배치 데이터와 네트워크 센서 및 애플리케이션 API 에서 생성한
라이브 스트림 데이터를 한 곳에 모은다고 했으므로 형식이 다른 데이터를 한 곳에 모을 때
적절한 AWS LakeFormation이 필요.
・그리고 AWS Glue 는 Amazon S3 데이터 레이크의 필수 구성 요소이며 최신 데이터
분석을 위한 데이터 카탈로그 및 변환 서비스 제공
https://aws.amazon.com/ko/blogs/korea/build-a-data-lake-foundation-with-aws-glue-
and-amazon/
・AWS Glue는 Athena에서 쿼리 가능한 Parquet 파일을 쓸 수 있음.
AWS Glue 를 사용하여 Amazon S3 와 스트리밍 소스에서 Parquet 파일을 읽을 수 있을
뿐만 아니라 Amazon S3에 Parquet 파일을 쓸 수 있습니다.
https://docs.aws.amazon.com/ko_kr/glue/latest/dg/aws-glue-programming-etl-format-p
arquet-home.html
Amazon Athena에서 사용할 수 있는 Apache Parquet
https://aws.amazon.com/ko/blogs/korea/build-a-data-lake-foundation-with-aws-glue-
and-amazon/
・S3 버킷에 있는 데이터를 Athena로 쿼리 가능
Amazon Athena는 표준 SQL을 사용하여 Amazon S3(Amazon Simple Storage Service)에
있는 데이터를 직접 간편하게 분석할 수 있는 대화형 쿼리 서비스입니다.
https://docs.aws.amazon.com/ko_kr/athena/latest/ug/what-is.html
・QuickSight로 KPI 표시 가능
https://docs.aws.amazon.com/ko_kr/quicksight/latest/user/kpi.html
설명2:
Amazon Athena 는 스트리밍 데이터에 대한 일회성 쿼리를 실행하기 위한 최상의
선택입니다.
Amazon Kinesis Data Analytics 는 스트리밍 데이터를 실시간으로 분석할 수 있는 쉽고
친숙한 표준 SQL 언어를 제공하지만 일회성 쿼리가 아닌 지속적인 쿼리를 위해
설계되었습니다. 반면 Amazon Athena는 SQL을 사용하여 Amazon S3의 데이터를 쿼리할
수 있는 서버리스 대화형 쿼리 서비스입니다. 임시 쿼리에 최적화되어 있으며 스트리밍
데이터에 대한 일회성 쿼리를 실행하는 데 이상적입니다.
AWS Lake Formation은 분석 목적으로 모든 데이터를 보관하는 중앙 위치로 사용합니다.
Athena는 S3와 완벽하게 통합되며 쿼리를 만들 수 있습니다.
~~~

---

# Q157 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/87629-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
이전에는 특히 AWS 서비스 전체에서 백업을 조정할 때 수동 Aurora 클러스터 스냅샷에
대한 백업 일정을 자동화하거나 보존 정책을 적용하거나 백업 활동을 통합하기 위해 사용자
지정 스크립트를 생성해야 했습니다. AWS Backup을 사용하면 스냅샷 예약 및 스냅샷 보존
관리 기능이 있는 완전 관리형 정책 기반 백업 솔루션을 얻을 수 있습니다. 이제
PostgreSQL 호환 및 MySQL 호환 Aurora 버전 모두에 대해 AWS Backup 콘솔에서 직접
Aurora 백업을 생성, 관리 및 복원할 수 있습니다.
시작하려면 AWS Backup 콘솔에서 Amazon Aurora 클러스터를 선택하고 온디맨드 백업을
수행하거나 클러스터를 백업 계획에 할당하기만 하면 됩니다.
~~~

---

# Q158 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/87514-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명
CloudFront 를 사용하여 모든 HTTP 오리진을 사용하여 주문형 비디오(VOD) 또는 라이브
스트리밍 비디오를 제공할 수 있습니다.
클라우드에서 비디오 워크플로를 설정할 수 있는 한 가지 방법은 CloudFront를 AWS Media
Services와 함께 사용하는 것입니다.
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/on-demand-str
eamingvideo.html
~~~

---

# Q159 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/87516-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
API 사용 계획을 WAF 로 보완 가능. ""비용을 제어하거나 API 에 대한 액세스를 차단하기
위해 사용량 계획 할당량 또는 조절에 의존하지 마십시오. AWS Budget 을 사용하여 비용을
모니터링하고 AWS WAF 를 사용하여 API 요청을 관리하는 것을 고려하십시오.
https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage
-plans.html
A(O) : 애플리케이션 요청, 즉 API 요청을 함부로 하지 못하도록 하는 것이므로 A는 정답.
C(O) : 애플리케이션 계층 방어이고 봇넷 방어이므로 WAF가 있는 C는 정답
(https://aws.amazon.com/ko/waf/getting-started/)
E(X) : 공개적으로 사용가능한 서버리스 애플리케이션이라는 단서 때문에 제외됨.
~~~

---

# Q160 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/87632-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
A(X) : Amazon OpenSerach Service 는 분석 및 모니터링 서비스인데 이미 회사에서 분석
애플리케이션을 따로 사용 중이므로 데이터를 저장하는 서비스만 필요한 상황이라 필요가
없음. Amazon OpenSearch Service 는 AWS 클라우드에서 OpenSearch 클러스터를 손쉽게
배포, 운영 및 확장할 수 있도록 해주는 관리형 서비스입니다. OpenSearch 는 로그 분석,
실시간 애플리케이션 모니터링, 클릭 스트림 분석 같은 사용 사례를 위한 완전한 오픈 소스
검색 및 분석 엔진입니다.
https://docs.aws.amazon.com/ko_kr/opensearch-service/latest/developerguide/what-is.h
tml
B(X) : 아무리 빨라봤자 액세스 타임이 1분 정도 걸림.
https://docs.aws.amazon.com/AmazonS3/latest/userguide/restoring-objects-retrieval-op
tions.html
C(O) : S3 + Life Cycle Policy 조합으로 밀리초 단위 액세스와 30일간 보관 조건 충족 가능
https://aws.amazon.com/ko/s3/storage-classes/)(https://docs.aws.amazon.com/ko_kr/A
mazonS3/latest/userguide/object-lifecycle-mgmt.html
D(X) : 데이터베이스는 데이터를 수집하여 다른 서비스에 이용할 목적으로 사용하는 것이지,
특정 기간만 보관해두고자 하는 용도가 아님. 지문에서는 회사가 이미 분석 애플리케이션을
가지고 있는데다가 원하는 건 분석 애플리케이션으로 생성한 데이터를 보관할 곳을 찾는
것임. 따라서 C가 더 적합.
설명2:
이 솔루션은 분석 애플리케이션에서 생성되고 JSON 형식으로 저장되는 데이터를 백업하기
위한 재해 복구 솔루션의 요구 사항을 충족하며 필요한 경우 밀리초 내에 액세스할 수
있어야 합니다. Amazon S3 Standard 는 자주 액세스하는 데이터를 위한 내구성 있고 확장
가능한 스토리지 클래스입니다. 모든 양의 데이터를 저장할 수 있고 고가용성과 성능을
제공할 수 있습니다. 또한 데이터 검색을 위한 밀리초 액세스 시간을 지원할 수 있습니다.
Amazon OpenSearch Service(Amazon Elasticsearch Service)는 데이터를 인덱싱하고
쿼리할 수 있는 검색 및 분석 서비스이지만 JSON 형식으로 저장된 데이터에 대한 백업
솔루션이 아니기 때문에 옵션 A는 올바르지 않습니다.
옵션 B 는 Amazon S3 Glacier 가 데이터 보관 및 장기 백업을 위한 저비용 스토리지
클래스이지만 데이터 검색을 위한 밀리초 액세스 시간을 지원하지 않기 때문에 정답이
아닙니다.
PostgreSQL 용 Amazon RDS 는 구조화된 데이터를 저장하고 쿼리할 수 있는 관계형
데이터베이스 서비스이지만 JSON 형식으로 저장된 데이터에 대한 백업 솔루션이 아니기
때문에 옵션 D는 올바르지 않습니다.
참조:
https://aws.amazon.com/s3/storage-classes/
https://aws.amazon.com/s3/faqs/#Durability_and_data_protection
~~~

---

# Q161 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/87633-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
Lambda 를 사용하면 서버를 관리하고 프로비저닝할 필요가 없으므로 확장성이 보장되고
운영 오버헤드가 최소화됩니다. S3 는 JSON 문서를 위한 내구성 있고 가용성이 높은
스토리지를 제공합니다. Lambda 는 새 문서가 S3 버킷에 추가될 때마다 자동으로
트리거되어 실시간 처리가 가능합니다. 결과를 Aurora DB 클러스터에 저장하면 처리된
데이터의 고가용성과 확장성이 보장됩니다. 이 솔루션은 서버리스 아키텍처를 활용하여
인프라를 관리할 필요 없이 자동 확장 및 고가용성을 허용하므로 가장 적합한 선택입니다.
A. 이 옵션을 사용하려면 EC2 인스턴스를 수동으로 관리하고 확장해야 하므로 운영
오버헤드와 복잡성이 높아집니다.
C. 이 접근 방식에는 여전히 EC2 인스턴스의 수동 관리 및 확장이 포함되어 운영 복잡성과
오버헤드가 증가합니다.
D. 이 솔루션은 ECS 클러스터를 관리하고 확장해야 하므로 운영 오버헤드와 복잡성이
추가됩니다. SQS를 활용하면 시스템에 복잡성이 추가되어 Python 코드에서 메시지 소비 및
처리를 사용자 지정 처리해야 합니다.
설명2:
JSON 문서를 S3 버킷에 넣으면 문서가 내구성과 확장성이 뛰어난 객체 스토리지 서비스에
저장됩니다. AWS Lambda를 사용하면 회사는 Python 코드를 실행하여 기본 인프라에 대해
걱정할 필요 없이 S3 버킷에 도착하는 문서를 처리할 수 있습니다. 또한 AWS Lambda 가
들어오는 요청 비율에 따라 함수의 인스턴스 수를 자동으로 조정하므로 수평적 확장성이
가능합니다. 결과는 MySQL 및 PostgreSQL 과 호환되는 완전 관리형 고성능 데이터베이스
서비스인 Amazon Aurora DB 클러스터에 저장할 수 있습니다. 이는 처리 결과에 필요한
내구성과 확장성을 제공합니다.
https://aws.amazon.com/rds/aurora/
~~~

---

# Q162 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/87634-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명
https://aws.amazon.com/fsx/lustre/
Amazon FSx for Lustre 는 컴퓨팅 워크로드를 위한 비용 효율적이고 확장 가능한 고성능
스토리지를 제공하는 완전관리형 서비스입니다. 기계 학습, 고성능 컴퓨팅(HPC), 비디오
렌더링, 재무 시뮬레이션과 같은 많은 워크로드는 고성능 공유 스토리지를 통해 동일한
데이터 세트에 액세스하는 컴퓨팅 인스턴스에 의존합니다.
HPC = Amazon FSx for Lustre. 정답은 A.
~~~

---

# Q163 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/87509-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
AWS Fargate 는 사용자 애플리케이션을 위한 서버리스 환경으로, 사용자는 서버 구성 및
관리 대신 애플리케이션 구축에 집중할 수 있습니다. 또한 Fargate 는 리소스 관리를
자동화하여 사용자가 수요에 따라 애플리케이션을 쉽게 확장할 수 있도록 합니다.
컨테이너화된 애플리케이션 배포 = Fargate + ECS. 정답은 A.
~~~

---

# Q164 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/87523-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
메시지 처리에 실패하면 = SQS Dead Letter Queue. 정답은 C.
설명2:
발신자 및 프로세서 애플리케이션을 모두 SQS 와 통합하면 처리를 위해 발신자에서
프로세서 애플리케이션으로 메시지를 안정적으로 보낼 수 있습니다. SQS 는 최소 1 회
전달을 제공하여 메시지가 전송 중에 손실되지 않도록 합니다. 메시지 처리에 실패하면
다른 메시지 처리에 영향을 주지 않고 대기열에 보관하고 다시 시도할 수 있습니다. DLQ를
구성하면 반복적으로 처리에 실패하는 메시지를 수집할 수 있으므로 문제 해결 및 분석을
위해 실패한 메시지를 볼 수 있습니다.
A는 운영 오버헤드 및 유지 관리 요구 사항을 추가하는 Redis를 실행하는 EC2 인스턴스의
관리 및 구성과 관련되므로 최적의 선택이 아닙니다.
B 는 Amazon Kinesis 데이터 스트림을 사용하고 메시지 처리를 위해 Kinesis Client
Library 와 통합함으로써 추가적인 복잡성을 도입하므로 운영상 가장 효율적인 솔루션은
아닙니다.
SNS를 사용하는 D는 두 애플리케이션 간의 메시지 처리라는 특정 요구 사항보다 Pub/Sub
메시징 및 방송 알림에 더 적합하므로 시나리오에 가장 적합하지 않습니다.
참고:
https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-
dead-letterqueues.html
~~~

---

# Q165 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/87524-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
CloudFront로만 접속할 수 있도록 한 뒤에 WAF로 검사해야 함.
Amazon S3 버킷을 오리진으로 설정하여 CloudFront 를 사용하는 경우 다음과 같은 이점을
제공하는 방식으로 CloudFront 및 Amazon S3를 구성할 수 있습니다.
◎공개적으로 액세스할 수 없도록 Amazon S3 버킷에 대한 액세스를 제한합니다.
◎뷰어(사용자)가 지정된 CloudFront 배포를 통해서만 버킷의 콘텐츠에 액세스할 수 있도록
합니다. 즉, 뷰어가 버킷에서 직접 또는 의도하지 않은 CloudFront 배포를 통해 콘텐츠에
액세스하는 것을 방지합니다. 이렇게 하려면 인증된 요청을 Amazon S3 로 보내도록
CloudFront 를 구성하고 CloudFront 의 인증된 요청에 대한 액세스만 허용하도록 Amazon
S3 를 구성합니다. CloudFront 는 Amazon S3 오리진에 인증된 요청을 전송하는 두 가지
방법으로 오리진 액세스 제어(OAC)와 오리진 액세스 ID(OAI)를 제공합니다.
https://docs.aws.amazon.com/ko_kr/AmazonCloudFront/latest/DeveloperGuide/private-c
ontent-restricting-access-to-s3.html
AWS WAF 는 CloudFront 에 전달되는 HTTP 및 HTTPS 요청을 모니터링할 수 있게 해주고
콘텐츠에 대한 액세스를 제어할 수 있게 해주는 웹 애플리케이션 방화벽입니다.
https://docs.aws.amazon.com/ko_kr/AmazonCloudFront/latest/DeveloperGuide/distributio
n-web-awswaf.html
참조
https://docs.aws.amazon.com/ko_kr/AmazonCloudFront/latest/DeveloperGuide/private-c
ontent-restricting-access-to-s3.html
https://docs.aws.amazon.com/ko_kr/AmazonCloudFront/latest/DeveloperGuide/distributio
n-web-awswaf.html
~~~

---

# Q166 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/87522-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
정적 HTML 페이지 + 전 세계 사용자의 조회 + S3 버킷에 저장된 데이터 = S3 +
CloudFront 조합. 답은 D.
설명2:
Amazon CloudFront 는 HTML 페이지, 이미지 및 비디오와 같은 정적 및 동적 웹 콘텐츠의
전송 속도를 높이는 콘텐츠 전송 네트워크(CDN)입니다. CloudFront 를 사용하면 HTML
페이지가 가장 가까운 엣지 로케이션에서 사용자에게 제공되므로 더 빠르게 전달되고 더
나은 사용자 경험을 얻을 수 있습니다. 또한 CloudFront 는 글로벌 이벤트에 예상되는 높은
트래픽과 많은 수의 요청을 처리하여 전 세계 사용자가 HTML 페이지를 사용할 수 있고
액세스할 수 있도록 합니다.
~~~

---

# Q167 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/87510-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
A(X) : 가동 중지 시간이 없어야 한다고 했으므로 중지될 위험이 잇는 스팟 인스턴스는
적절치 않음.
B(X) : 메시지 볼륨을 예측할 수 없고 간헐적인 트래픽이 발생하는 상황에서 예측할 수
있는 트래픽이 발생하는 데에 적합한 예약 인스턴스는 맞지 않음.
C(X) : A와 같은 이유로 오답.
D(O) : 최소 사용량을 기준 용량으로 삼아 예약 인스턴스를 사용함으로서 비용을 절감하고,
추가적이고 유동적인 트래픽은 온디맨드 인스턴스로 유연하게 처리 가능.
설명2:
중단할 수 없는 단기적이고 불규칙한 워크로드가 있는 애플리케이션에는 온디맨드
인스턴스를 사용하는 것이 좋습니다.
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-on-demand-instances.ht
ml
~~~

---

# Q168 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/87512-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
권한을 유지할 수 있는 단일 지점이 핵심 키워드. 답은 D.
서비스 제어 정책(SCP)은 조직에서 권한을 관리하는 데 사용할 수 있는 조직 정책
유형입니다. SCP 는 조직의 모든 계정에 대해 사용 가능한 최대 권한을 중앙에서
제어합니다.
https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps
.html
설명2:
서비스 제어 정책(SCP)은 조직을 관리하는 데 사용할 수 있는 정책 유형 중 하나입니다.
SCP 는 조직의 모든 계정에 대해 사용 가능한 최대 권한에 대한 중앙 제어를 제공하므로
계정이 조직의 액세스 제어 지침을 준수하도록 할 수 있습니다.
https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scp.
html
~~~

---

# Q169 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/87526-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
AWS Shield Standard, AWS Shield Advanced는 애플리케이션 계층에서 DDoS 공격을 방어.
AWS Shield 는 AWS 에서 실행되는 애플리케이션을 보호하는 디도스(DDoS) 보호
서비스입니다. AWS Shield에는 두 계층 – Standard 및 Advanced가 있습니다.
https://aws.amazon.com/ko/shield/?whats-new-cards.sort-by=item.additionalFields.post
DateTime&whats-new-cards.sort-order=desc
설명2:
AWS Shield Advanced 는 Amazon EC2 인스턴스, Elastic Load Balancing 로드 밸런서,
CloudFront 배포, Route 53 호스팅 영역 및 AWS Global Accelerator 표준 가속기에 대해
확장된 DDoS 공격 보호 기능을 제공합니다.
https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html
~~~

---

# Q170 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/87528-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
AWS WAF를 사용하여 특정 국가 또는 지리적 위치로부터의 요청을 허용하거나 차단하려면
어떻게 해야 합니까?
특정 국가의 사이트 액세스를 차단하거나 특정 국가에서만 액세스하도록 허용하려면 지리적
일치 규칙 문을 사용합니다. 기원 국가를 기준으로 일부 웹 요청을 허용하려면 허용하려는
국가에 대한 지리적 일치 규칙 문을 추가합니다. 그런 다음 차단하려는 국가에 대한 두
번째 지리적 일치 규칙 문을 추가합니다.
https://aws.amazon.com/ko/premiumsupport/knowledge-center/waf-allow-block-countr
y-geolocation/
~~~

---

# Q171 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/87529-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
API 제공 + 탄력적인 = API Gateway + Lambda. 답은 B.
설명2:
Lambda 서버리스는 EC2 api 게이트웨이 솔루션보다 확장 가능하고 탄력적입니다.
~~~

---

# Q172 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/87517-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
Amazon CloudFront 를 사용하면 HTTPS 를 통해 오리진 서버에 대한 종단 간 보안 연결을
적용할 수 있습니다. 필드 레벨 암호화는 추가 보안 레이어를 추가하여 시스템 처리
전체에서 특정 데이터를 보호하고 특정 애플리케이션만 이를 볼 수 있도록 합니다.
https://docs.aws.amazon.com/ko_kr/AmazonCloudFront/latest/DeveloperGuide/field-level
-encryption.html
설명2:
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/field-levelencry
ption.html
"Amazon CloudFront 를 사용하면 HTTPS 를 사용하여 오리진 서버에 대한 엔드 투 엔드
보안 연결을 적용할 수 있습니다.
필드 수준 암호화는 특정 애플리케이션만 볼 수 있도록 시스템 처리 전반에 걸쳐 특정
데이터를 보호할 수 있는 추가 보안 계층을 추가합니다."
~~~

---

# Q173 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/87530-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
S3 + 많은 수의 비디오와 이미지 + 수백만명 액세스가 핵심. S3 + CloudFront 로 CDN
서비스 사용해야 부하를 줄일 수 있음.
설명2:
ElastiCache 는 완전 관리형 인 메모리 데이터 저장소에서 정보를 신속하게 검색하여 웹
애플리케이션의 성능을 향상시킵니다. Memcached 및 Redis 를 활용하고 애플리케이션이
디스크 기반 데이터베이스에서 데이터를 읽는 데 걸리는 시간을 상당히 단축합니다.
Amazon CloudFront 는 TCP(전송 제어 프로토콜) 프로토콜을 기반으로 하는 HTTP 및
WebSocket 프로토콜의 동적 콘텐츠를 지원합니다. 일반적인 사용 사례에는 동적 API 호출,
웹 페이지 및 웹 애플리케이션뿐만 아니라 오디오 및 이미지와 같은 애플리케이션의 정적
파일이 포함됩니다. 또한 HTTP를 통한 주문형 미디어 스트리밍을 지원합니다. AWS Global
Accelerator는 UDP(사용자 데이터그램 프로토콜)와 TCP 기반 프로토콜을 모두 지원합니다.
일반적으로 게임, IoT 및 VoIP(Voice over IP)와 같은 비HTTP 사용 사례에 사용됩니다. 고정
IP 주소 또는 빠른 지역 장애 조치가 필요한 HTTP 사용 사례에도 적합합니다.
~~~

---

# Q174 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/87533-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
다중 AZ를 사용해야 하는 상황.
A(X) : 리전 간 Auto Scaling은 불가.
지리적 이중화의 안전성과 안정성을 활용하려면 Auto Scaling 그룹을 리전 내의 여러 가용
영역에 걸쳐 확장하고 로드 밸런서를 연결하여 해당 가용 영역에 들어오는 트래픽을
분산하십시오.
https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-add-availability-zone.html
설명2:
여러 가용 영역을 사용하도록 기존 Auto Scaling 그룹을 수정하여 이 아키텍처에 대해 매우
간단하게 고가용성을 활성화할 수 있습니다. ASG 는 부하를 자동으로 분산하므로 실제로
AZ당 인스턴스를 지정할 필요가 없습니다.
참조:
https://aws.amazon.com/ec2/autoscaling/
~~~

---

# Q175 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/87533-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
연결 수가 많음 = RDS Proxy. 정답은 B.
RDS 프록시를 사용하여 예기치 않은 데이터베이스 트래픽 급증을 처리할 수 있습니다.
급증을 처리하지 않으면 연결 초과 구독 또는 빠른 속도의 새 연결 생성으로 인한 문제가
발생할 수 있습니다. RDS 프록시는 데이터베이스 연결 풀을 설정하고 이 풀에서 연결을
재사용합니다. 이 접근 방식은 매번 새 데이터베이스 연결을 여는 데서 오는 메모리 및
CPU 오버헤드 를 방지합니다. 과다 구독으로부터 데이터베이스를 보호하기 위해 생성되는
데이터베이스 연결 수를 제어할 수 있습니다.
https://docs.aws.amazon.com/ko_kr/AmazonRDS/latest/UserGuide/rds-proxy.html
설명2:
최신 서버리스 아키텍처에 구축된 애플리케이션을 포함하여 많은 애플리케이션은
데이터베이스 서버에 대해 많은 수의 열린 연결을 가질 수 있으며 빠른 속도로
데이터베이스 연결을 열고 닫을 수 있으므로 데이터베이스 메모리와 컴퓨팅 리소스가
고갈될 수 있습니다. Amazon RDS Proxy 를 사용하면 애플리케이션이 데이터베이스와
설정된 연결을 풀링하고 공유하여 데이터베이스 효율성과 애플리케이션 확장성을 개선할 수
있습니다.
https://aws.amazon.com/id/rds/proxy/
~~~

---

# Q176 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/87532-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
VPC 내에 있는 프라이빗 서브넷의 EC2 인스턴스와 DynamoDB 간 가장 안전한 AWS
네트워크 통신 = VPC Gateway Endpoint.
게이트웨이 엔드포인트는 VPC 용 인터넷 게이트웨이 또는 NAT 디바이스가 없어도 Amazon
S3 및 DynamoDB에 대한 안정적인 연결을 제공합니다.
https://docs.aws.amazon.com/ko_kr/vpc/latest/privatelink/vpce-gateway.html#vpc-endp
oints-limitations
설명2:
DynamoDB 용 VPC 엔드포인트를 사용하면 VPC 의 Amazon EC2 인스턴스가 프라이빗 IP
주소를 사용하여 퍼블릭 인터넷에 노출되지 않고 DynamoDB에 액세스할 수 있습니다. EC2
인스턴스에는 퍼블릭 IP 주소가 필요하지 않으며 VPC 에 인터넷 게이트웨이, NAT 디바이스
또는 가상 프라이빗 게이트웨이가 필요하지 않습니다. 엔드포인트 정책을 사용하여
DynamoDB 에 대한 액세스를 제어합니다. VPC 와 AWS 서비스 간의 트래픽은 Amazon
네트워크를 벗어나지 않습니다.
~~~

---

# Q177 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/87572-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
DynamoDB 와 DAX 가 결합되면 성능을 한 단계 업그레이드하여 읽기 중심의 워크로드에서
초당 수백만 개의 요청에도 마이크로초의 응답 시간을 지원합니다. DynamoDB 와
마찬가지로 DAX 는 완전관리형입니다. 따라서 하드웨어나 소프트웨어 프로비저닝, 설정 및
구성, 소프트웨어 패치, 분산 캐시 클러스터 운영 또는 확장 시 여러 인스턴스에 데이터
복제 등과 같은 관리 작업에 대해 더 이상 걱정할 필요가 없습니다. DAX 는 장애 탐지,
장애 복구, 소프트웨어 패치와 같은 일반적인 관리 작업 상당 부분을 자동화합니다. DAX 는
DynamoDB API와 호환되므로 작동하는 애플리케이션 코드를 변경할 필요가 없습니다.
참고:
https://aws.amazon.com/dynamodb/dax/
~~~

---

# Q178 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/87639-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
AWS Backup을 사용하여 EC2 및 RDS 백업을 별도의 리전에 복사하는 것은 최소한의 운영
오버헤드로 요구 사항을 충족하는 솔루션입니다. AWS Backup 은 백업 프로세스를
간소화하고 백업을 다른 리전으로 자동 복사하여 EC2 인스턴스 및 RDS 데이터베이스에
대한 별도의 백업 프로세스 관리와 관련된 수동 작업 및 운영 복잡성을 줄입니다.
B: Amazon Data Lifecycle Manager(Amazon DLM)가 RDS 백업을 별도의 리전에 직접
복사하도록 설계되지 않았기 때문에 올바르지 않습니다.
C: Amazon 머신 이미지(AMI) 및 읽기 전용 복제본을 생성하면 전용 백업 솔루션에 비해
복잡성과 운영 오버헤드가 추가되기 때문에 올바르지 않습니다.
D: Amazon EBS 스냅샷, RDS 스냅샷 및 S3 CRR(Cross-Region Replication)을 사용하려면
여러 수동 단계와 추가 구성이 수반되어 복잡성이 증가하기 때문에 올바르지 않습니다.
~~~

---

# Q179 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/87582-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
데이터베이스 사용자 이름과 암호를 AWS 시스템 관리자 파라미터 스토어에 안전하게
저장하고 EC2 인스턴스에서 실행 중인 애플리케이션이 액세스할 수 있도록 하려면
솔루션스 아키텍트는 파라미터 스토어 파라미터에 대한 읽기 액세스 권한이 있는 IAM
역할을 생성하고 파라미터를 암호화하는 데 사용되는 AWS KMS 키에 대한 암호 해독
액세스를 허용해야 합니다. 그런 다음 솔루션스 아키텍트는 이 IAM 역할을 EC2 인스턴스에
할당해야 합니다.
이 접근 방식을 사용하면 EC2 인스턴스가 파라미터 스토어의 파라미터에 액세스하고
지정된 KMS 키를 사용하여 해독하는 동시에 필요한 보안 제어를 적용하여 승인된
당사자만 파라미터에 액세스할 수 있도록 할 수 있습니다.
~~~

---

# Q180 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/87640-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
AWS Shield Advanced 는 Amazon EC2 인스턴스, Elastic Load Balancing 로드 밸런서,
CloudFront 배포, Route 53 호스팅 영역 및 AWS Global Accelerator 표준 가속기에 대해
확장된 DDoS 공격 보호 기능을 제공합니다. AWS WAF는 보호된 웹 애플리케이션 리소스로
전달되는 HTTP 및 HTTPS 요청을 모니터링할 수 있는 웹 애플리케이션 방화벽입니다.
다음 리소스 유형을 보호할 수 있습니다.
Amazon CloudFront 배포
아마존 API 게이트웨이 REST API
애플리케이션 로드 밸런서
AWS AppSync GraphQL API
Amazon Cognito 사용자 풀
https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html
설명2:
지문에서 등장한 수단은 AWS WAF, AWS Shield Standard, AWS Shield Advanced로 3개.
◈Shield Advanced = WAF + Shield Standard.
・Shield Advanced = Amazon Elastic Compute Cloud(EC2), Elastic Load Balancing(ELB),
Amazon CloudFront, AWS Global Accelerator 및 Amazon Route 53 리소스에서 실행되는
애플리케이션을 목표로 하는 공격에 대해 더 높은 수준의 보호를 구현. 정교한 대규모
DDoS 공격에 대한 추가 보호 및 완화, 실시간에 가까운 공격에 대한 가시성, 웹
애플리케이션 방화벽 [AWS WAF와의 통합]을 제공.
https://aws.amazon.com/ko/shield/?whats-new-cards.sort-by=item.additionalFields.post
DateTime&whats-new-cards.sort-order=desc
AWS Shield Advanced 구독에는 다음 기능과 옵션이 포함됩니다. 이는 AWS에서 이미 받은
DDoS 탐지 및 완화 기능을 보완합니다. ◎AWS WAF 통합. ◎보호 그룹. ◎AWS Firewall
Manager를 통한 Shield Advanced 보호의 중앙 집중식 관리.◎AWS Shield 대응 팀(SRT)
https://docs.aws.amazon.com/waf/latest/developerguide/ddos-advanced-summary-cap
abilities.html
・Shield Standard = ""네트워크 및 전송 계층 DDoS 공격으로부터 보호
https://aws.amazon.com/ko/shield/?whats-new-cards.sort-by=item.additionalFields.post
DateTime&whats-new-cards.sort-order=desc
・WAF = 일반적인 웹 공격으로부터 웹 애플리케이션이나 API 를 보호하는 데 도움이 되는
웹 애플리케이션 방화벽입니다. SQL 주입 또는 사이트 간 스크립팅과 같은 일반적인 공격
패턴을 차단하는 보안 규칙 및 사용자가 정의한 특정 트래픽 패턴을 필터링하는 규칙을
생성하도록 지원 https://aws.amazon.com/ko/waf/
AWS WAF 로 보호할 수 있는 리소스. ◎Amazon CloudFront 배포. ◎Amazon API
게이트웨이 REST API ◎애플리케이션 로드 밸런서 ◎AWS AppSync GraphQL API ◎Amazon
Cognito 사용자 풀
https://docs.aws.amazon.com/waf/latest/developerguide/how-aws-waf-works.html
A(X) : WAF 는 웹 애플리케이션 방화벽으로, 네트워크 계층이 아니라 애플리케이션 계층을
방어.
B(O) : AWS Shield Advanced 는 DDoS EC2, ELB, CloudFront, AGA, Route 53 리소스
방어하며 WAF와 통합.
C(O) : AWS WAF 는 웹 애플리케이션 및 API를 공격으로부터 보호하는 데 도움이 되는 웹
애플리케이션 방화벽입니다.
https://docs.aws.amazon.com/ko_kr/apigateway/latest/developerguide/apigateway-contr
ol-access-aws-waf.html
D(X) : GuardDuty는 AWS 계정 보호 시스템. https://aws.amazon.com/ko/guardduty/
E(X) : AWS Shield Standard는 DDoS 보호만을 제공.
~~~

---

# Q181 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/87647-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
분리와 함께 처리할 응용 프로그램에 대한 메시지를 보관할 큐를 수용하도록 아키텍처를
변경하기만 하면 됨 A(O) – SQS
설명2:
대기열의 처리량이 제한됨(일괄 처리 없이 300msg/s, 일괄 처리 시 3000msg/s, 일괄
작업당 최대 10msg, 대기열에서 메시지 복제가 허용되지 않음(정확히 한 번 전달), 메시지
순서가 보존됨(FIFO), 대기열 이름 .fifo로 끝나야 합니다.
~~~

---

# Q182 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/87641-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
데이터베이스의 고가용성이 필요한 상황이므로 Multi AZ가 필수인 상황.
A(X) : AWS로 MySQL 데이터베이스를 마이그레이션하려고 한다 했으므로 Amazon RDS for
MySQL이 맞음.
B(O) : Amazon RDS 다중 AZ 동기 복제 기술을 사용하여 대기 데이터베이스 인스턴스의
데이터를 프라이머리와 함께 최신 상태로 유지합니다. 장애를 감지하면 Amazon RDS 는
수동 개입 없이 자동으로 대기 인스턴스로 장애 조치합니다.
https://aws.amazon.com/ko/rds/features/multi-az/
C(X) : RDS read replica는 동기식이 아닌 비동기식 방식임.
기본 DB 인스턴스에 적용된 업데이트는 읽기 전용 복제본에 비동기식으로 복사됩니다.
https://docs.aws.amazon.com/ko_kr/AmazonRDS/latest/UserGuide/USER_ReadRepl.html
D(X) : 다른 AZ나 리전에 복제하는지에 대한 여부가 안 나와 있음. 그리고 굳이 Lambda를
사용해야 하는지도 의문.
설명2:
Q: Amazon RDS는 나를 대신하여 무엇을 관리합니까?
Amazon RDS 는 요청한 인프라 용량 프로비저닝에서 데이터베이스 소프트웨어 설치에
이르기까지 관계형 데이터베이스 설정과 관련된 작업을 관리합니다. 데이터베이스가
가동되고 실행되면 Amazon RDS 는 백업 수행 및 데이터베이스를 강화하는 소프트웨어
패치와 같은 일반적인 관리 작업을 자동화합니다. 선택적 다중 AZ 배포를 통해 Amazon
RDS는 자동 장애 조치를 통해 가용 영역 전체에서 동기식 데이터 복제도 관리합니다.
https://aws.amazon.com/rds/faqs/
~~~

---

# Q183 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/87570-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
질문의 핵심 문구는 읽기 및 쓰기 용량을 확장해야 한다는 것입니다. Aurora 는 읽기
전용입니다. Amazon DynamoDB에는 테이블에 대한 읽기 및 쓰기를 처리하기 위한 두 가지
읽기/쓰기 용량 모드가 있습니다. 온디맨드 프로비저닝(기본, 프리 티어 가능)
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.Rea
dWriteCapacityMode.html
DynamoDB 는 주문 데이터(키값)을 저장하는데 적합하고 온디맨드 방식으로 쓰기 및 읽기
용량을 확장합니다.
~~~

---

# Q184 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/87534-exam-aws-certified-solut
ions-architect-associate-saa-c03/
해설:
A(O) : 보안 그룹을 정의하여 VPC에 Lambda 연결 가능.
AWS 계정의 가상 사설 클라우드(VPC)에 있는 사설 서브넷에 연결하도록 Lambda 함수를
구성할 수 있습니다. Amazon Virtual Private Cloud(Amazon VPC)를 사용하여 데이터베이스,
캐시 인스턴스 또는 내부 서비스와 같은 리소스에 대한 사설 네트워크를 생성합니다.
함수가 실행되는 동안 프라이빗 리소스에 액세스하려면 함수를 VPC 에 연결합니다. 함수를
VPC 에 연결하면 Lambda 는 함수의 VPC 구성에 있는 각 서브넷의 Hyperplane ENI(탄력적
네트워크 인터페이스)에 함수를 할당합니다. Lambda 는 계정의 VPC 지원 기능에 대해
고유한 서브넷 및 보안 그룹 조합이 처음으로 정의될 때 Hyperplane ENI를 생성합니다.
https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html#vpc-managing-
eni
B(X) : ・선택지에서 말하는 VPN 연결이란 VPC-온프레미스 간 연결을 말함.
VPN 연결 이라는 용어 는 일반적인 용어이지만 이 설명서에서 VPN 연결은 VPC 와 자체
온프레미스 네트워크 간의 연결을 나타냅니다.
https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html
・먼저 Virtual Private Gateway 를 사용하여 VPC-온프레미스 간 Site to Site VPN 연결을
수립.
◎AWS Site-to-Site VPN : VPC 와 원격 네트워크 사이에 IPsec VPN 연결을 생성할 수
있습니다. AWS 측 Site-to-Site VPN 연결에서 가상 프라이빗 게이트웨이 또는 Transit
Gateway 는 자동 장애 조치를 위한 2 개의 VPN 엔드포인트(터널)를 제공합니다.
Site-to-Site VPN 원격 연결 측에서 고객 게이트웨이 디바이스를 구성합니다.
https://docs.aws.amazon.com/ko_kr/vpc/latest/userguide/vpn-connections.html
・Virtual Private Gateway + Direct Connect + VPN 조합을 사용하는 이유는 Virtual Private
Gateway + VPN 조합은 IPv4 밖에 전송이 안 되는데, Virtual Private Gateway + Direct
Connect 조합은 IPv6 를 지원하므로 3 가지를 조합하면 IPv4, IPv6 를 모두 사용할 수 있기
때문.
가상 프라이빗 게이트웨이로 라우팅 : AWS Site-to-Site VPN 연결을 사용하여 VPC 의
인스턴스를 사용자의 네트워크와 통신하도록 할 수 있습니다. 이렇게 하려면 가상 프라이빗
게이트웨이를 생성하여 VPC 에 연결합니다.그런 다음 네트워크 대상 및 가상 프라이빗
게이트웨이(vgw-xxxxxxxxxxxxxxxxx)의 대상이 있는 서브넷 라우팅 테이블에 라우팅을
추가합니다....가상 프라이빗 게이트웨이의 Site-to-Site VPN 연결은 IPv6 트래픽을
지원하지 않습니다. 그러나 가상 프라이빗 게이트웨이를 통해 AWS Direct Connect 연결로
라우팅되는 IPv6 트래픽은 지원합니다.
https://docs.aws.amazon.com/ko_kr/vpc/latest/userguide/route-table-options.html#route
-tables-vgw
・VPC과 Lambda함수 연결
AWS 계정에서 VPC(Virtual Private Cloud)의 프라이빗 서브넷에 연결하도록 Lambda 함수를
구성할 수 있습니다.
https://docs.aws.amazon.com/ko_kr/lambda/latest/dg/configuration-vpc.html
But, 여기까지는 가능하지만 정작 Lambda 함수가 VPN 을 통해 트래픽을 라우팅할 수
있는지는 불명확.
그리고 어차피 A의 내용이 충족되어야만 가능하기 때문에 정답이 아닐 가능성이 큼.
C(X) : A 의 내용이 충족되지 않으면 수립 불가. 즉, VPC 에 Lambda 가 연결이 되어야
가능하던 말던 함.
Lambda 함수는 항상 Lambda 서비스가 소유한 VPC 내에서 실행됩니다. 기본적으로
Lambda 함수는 사용자 계정의 VPC에 연결되지 않습니다.
https://docs.aws.amazon.com/ko_kr/lambda/latest/dg/foundation-networking.html
D(X) : 탄력적 IP 주소는 퍼블릭 IP 주소로, Direct Connect 가 있는 상황에서 굳이 사용할
필요가 없음. 게다가 온프레미스 데이터베이스가 있는 곳은 프라이빗 서브넷이라 퍼블릭 IP
주소로는 무리임.
참조
https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html#vpc-managing-
eni
~~~

---

# Q185 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/87648-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
A(X) : S3에 관한 권한을 물어본 거지 ECS에 대한 권한을 물어본 게 아님.
B(O) : 태스크 정의를 등록할 때 태스크 권한의 컨테이너가 사용자 대신 연결된 정책에
지정된 AWS API를 호출하도록 허용하는 IAM 역할에 태스크 역할을 제공할 수 있습니다.
https://docs.aws.amazon.com/ko_kr/AmazonECS/latest/developerguide/task_definition_p
arameters.html
C(X) : 보안 그룹 아웃바운드는 별 설정 안 해놔도 모두 허용이 기본값임. 굳이 설정할
필요가 없음.
D(X) : 액세스 권한이 있는지 확인하겠다고 다른 걸로 로그인해서 굳이 EC2 인스턴스를
다시 시작하는 것은 비효율적.
~~~

---

# Q186 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/87650-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
이 솔루션은 여러 가용 영역에 배포된 여러 Amazon EC2 Windows 인스턴스에 연결된 공유
Windows 파일 시스템을 사용해야 하는 Windows 기반 애플리케이션 마이그레이션 요구
사항을 충족합니다. Amazon FSx for Windows File Server는 Windows Server에 구축된 완전
관리형 공유 스토리지를 제공하며 광범위한 데이터 액세스, 데이터 관리 및 관리 기능을
제공합니다. SMB(서버 메시지 블록) 프로토콜을 지원하며 여러 가용 영역에서 EC2
Windows 인스턴스에 탑재할 수 있습니다.
Windows 기반 애플리케이션이 핵심 키워드. 답은 B.
옵션 A 의 볼륨 게이트웨이 모드의 AWS Storage Gateway 는 온프레미스 애플리케이션
서버에서 iSCSI 디바이스로 마운트할 수 있는 클라우드 지원 스토리지 볼륨을 제공하지만
SMB 프로토콜 또는 EC2 Windows 인스턴스를 지원하지 않기 때문에 올바르지 않습니다.
옵션 C 는 Amazon Elastic File System(Amazon EFS)이 Linux 기반 워크로드를 위한 확장
가능하고 탄력적인 NFS 파일 시스템을 제공하지만 SMB 프로토콜 또는 EC2 Windows
인스턴스를 지원하지 않기 때문에 올바르지 않습니다.
옵션 D는 Amazon Elastic Block Store(Amazon EBS)가 EC2 인스턴스와 함께 사용할 영구
블록 스토리지 볼륨을 제공하지만 SMB 프로토콜을 지원하지 않거나 동일한 볼륨에 여러
인스턴스를 연결하기 때문에 올바르지 않습니다.
참조:
https://aws.amazon.com/fsx/windows/
https://docs.aws.amazon.com/fsx/latest/WindowsGuide/using-file-shares.html
~~~

---

# Q187 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/87695-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
A(O) : 다중 AZ 모드로 고가용성 충족. 관계형 데이터베이스로 구성된 프로그램이어야
하므로 RDS 사용.
다중 AZ 배포로 실행되도록 DB 인스턴스를 생성 또는 수정하면 Amazon RDS가 다른 가용
영역에 동기식 ‘예비’ 복제본을 자동으로 프로비저닝하고 유지합니다. 특정 유형의 계획된
유지 관리를 수행하는 도중에, 또는 예기치 않은 DB 인스턴스 장애나 가용 영역 장애가
발생할 경우 Amazon RDS 가 자동으로 예비 복제본으로 장애 조치하므로 예비 복제본이
승격되자마자 데이터베이스 쓰기 및 읽기를 재개할 수 있습니다.
https://aws.amazon.com/ko/rds/faqs/
B(X) : 장애 발생 시 복구를 위한 것이면 Multi AZ 가 더 유리하므로 고가용성 면에선 Multi
AZ 가 추천됨. 읽기 복제본을 사용해 데이터베이스 쓰기 가용성을 개선하거나 내 소스 DB
인스턴스의 데이터를 장애로부터 보호할 수 있습니까? 복제를 사용해 데이터베이스 쓰기
가용성을 높이고 최근 데이터베이스 업데이트를 다양한 장애 조건으로부터 보호하려면 DB
인스턴스를 다중 AZ 배포로 실행하는 것이 좋습니다. Amazon RDS 읽기 전용 복제본과
지원되는 엔진의 기본 비동기식 복제를 사용하면 데이터베이스 쓰기가 소스 DB
인스턴스에서 발생한 후, 읽기 전용 복제본에서 발생합니다. 이 복제 ‘지연 시간’은 상당히
다를 수 있습니다. https://aws.amazon.com/ko/rds/faqs/
C(X) : EC2로 굳이 돌릴 거 없이 ECS를 사용해서 서버리스로 돌릴 수 있음
D(O) : Fargate + ECS 조합으로 컨테이너 애플리케이션을 서버리스로 돌릴 수 있음.
AWS Fargate Fargate 는 Amazon EC2 인스턴스의 서버나 클러스터를 관리할 필요 없이
컨테이너를 실행하기 위해 Amazon ECS에 사용할 수 있는 기술입니다.
https://docs.aws.amazon.com/ko_kr/AmazonECS/latest/developerguide/AWS_Fargate.ht
ml
E(X) : C와 같은 이유로 오답.
설명2:
https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html
1. 관계형 데이터베이스: RDS
2. 컨테이너 기반 애플리케이션: ECS
"Amazon ECS 를 사용하면 간단한 API 호출을 사용하여 컨테이너 기반 애플리케이션을
시작 및 중지할 수 있습니다. 또한 중앙 집중식 서비스에서 클러스터 상태를 검색하고 많은
익숙한 Amazon EC2 기능에 액세스할 수 있습니다."
3. 약간의 수동 개입: Fargate AWS Fargate 에서 관리하는 서버리스 인프라에서 작업과
서비스를 실행할 수 있습니다. 또는 인프라를 더 잘 제어하기 위해 관리하는 Amazon EC2
인스턴스의 클러스터에서 작업과 서비스를 실행할 수 있습니다.
~~~

---

# Q188 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/87566-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
이 솔루션은 수동 관리 또는 운영 오버헤드 없이 고가용성 SFTP 솔루션을 제공합니다.
AWS Transfer Family 를 사용하면 인증, 권한 부여 및 스토리지 백엔드로 S3 와의 통합을
통해 SFTP 서버를 쉽게 설정할 수 있습니다.
옵션 B 는 SFTP 액세스가 아닌 NFS 또는 SMB 프로토콜을 통한 S3 스토리지에 대한 파일
기반 액세스에 주로 사용되는 Amazon S3 파일 게이트웨이 사용을 제안하므로 최선의
선택이 아닙니다.
옵션 C 는 파일 업로드를 위한 EC2 인스턴스, VPN 설정 및 cron 작업 스크립트의 수동
관리가 필요하여 운영 오버헤드와 잠재적인 복잡성을 유발하므로 최선의 선택이 아닙니다.
옵션 D 는 파일 업로드를 위한 EC2 인스턴스, Network Load Balancer 및 cron 작업
스크립트의 수동 관리도 필요하므로 최선의 선택이 아닙니다. 옵션 A 에서 AWS Transfer
Family 가 제공하는 더 단순하고 완벽하게 관리되는 솔루션에 비해 더 복잡하고 추가 구성
요소가 필요합니다.
~~~

---

# Q189 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/87535-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
B. 규정 준수 모드에서 S3 객체 잠금을 사용하면 객체에 엄격한 보존 정책을 적용하여
수정이나 삭제를 방지합니다.
D. AWS KMS 고객 관리형 키와 함께 서버 측 암호화를 사용하면 문서가 고객 제어형 키로
암호화됩니다. 키 순환을 활성화하면 정의된 순환 간격으로 새 암호화 키가 자동으로
생성되어 보안이 강화됩니다.
옵션 A: 거버넌스 모드의 S3 객체 잠금은 문서에 필요한 불변성을 제공하지 않으므로
잠재적인 수정 또는 삭제가 허용됩니다.
옵션 C: SSE-S3 만으로는 서버 측 암호화가 명시적으로 지정된 암호화 키 순환 요구
사항을 충족하지 않습니다.
옵션 E: AWS KMS 고객 관리 키(옵션 D)를 사용할 수 있는 경우 고객 제공(가져온)
키(SSE-C)를 사용한 서버 측 암호화는 필요하지 않으며, 이는 보다 통합되고 관리 가능한
솔루션을 제공합니다.
~~~

---

# Q190 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/87536-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
Elastic Beanstalk 를 사용하면 애플리케이션을 실행하는 인프라에 대해 자세히 알지 못해도
AWS 클라우드에서 애플리케이션을 신속하게 배포하고 관리할 수 있습니다.
Elastic Beanstalk 는 Go, Java, .NET, Node.js, PHP, Python 및 Ruby 에서 개발된
애플리케이션을 지원합니다....애플리케이션을 생성 및 배포한 후에는 지표, 이벤트, 환경
상태 등의 애플리케이션 정보를 Elastic Beanstalk 콘솔, API 또는 통합된 AWS CLI 를
비롯한 명령줄 인터페이스를 통해 확인할 수 있습니다.
https://docs.aws.amazon.com/ko_kr/elasticbeanstalk/latest/dg/Welcome.html
설명2:
빈번한 기능 테스트 -
- 개발, 테스트 및 프로덕션 사용 사례를 위해 여러 Elastic Beanstalk 환경을 쉽게 생성할
수 있습니다.
- 간단한 URL 스와핑 기술을 사용하여 A/B 테스트 및 기능 반복을 위한 환경 간에
트래픽을 라우팅할 수 있습니다. 복잡한 라우팅 규칙이나 인프라 변경이 필요하지
않습니다.
~~~

---

# Q191 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/89077-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
A. 보고 쿼리를 읽기 전용 복제본으로 이동하면 주문 처리에 사용되는 기본 DB 인스턴스가
장기 실행 보고 쿼리의 영향을 받지 않습니다. 이렇게 하면 주문 처리 중 시간 초과를
제거하는 동시에 직원이 애플리케이션 성능에 영향을 주지 않고 쿼리를 수행할 수
있습니다.
B. 이것은 일정 수준의 부하 분산을 제공할 수 있지만 주문 처리 중 쿼리 보고로 인해
발생하는 시간 초과 문제를 구체적으로 다루지는 않습니다.
C. DynamoDB 는 확장성과 성능상의 이점을 제공하지만 애플리케이션의 데이터 모델 및
쿼리 접근 방식을 크게 변경해야 할 수 있습니다.
D. 이 접근 방식은 주문 처리에 미치는 영향을 완화하는 데 도움이 될 수 있지만 직원이
쿼리를 수행하는 것을 막지 않고 시간 초과를 제거해야 하는 요구 사항을 해결하지는
못합니다.
~~~

---

# Q192 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/89133-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
A(X) : AWS 클라우드에 문서를 업로드할 거라고 했으니 적절치 않음. MySQL 이 아니라
Amazon RDS for MySQL이 됐던지 했어야 함.
B(O) : S3는 자료를 저장하는데 많이 사용되고, Athena는 S3에 쿼리하는 대화형 서비스임.
Amazon Athena는 표준 SQL을 사용하여 Amazon S3(Amazon Simple Storage Service)에
있는 데이터를 직접 간편하게 분석할 수 있는 대화형 쿼리 서비스입니다.
https://docs.aws.amazon.com/ko_kr/athena/latest/ug/what-is.html
C(?) : 프로그램을 AWS에서 돌려야한다는 말이 없어서 불명확.
D(X) : Amazon Rekognition은 이미지나 비디오 분석 서비스인데, 문서라면 텍스트 위주라서
탈락. 그리고 Transcribe Medical 은 음성->텍스트 변환이지 텍스트->의료 정보 추출이
아님.
Amazon Transcribe Medical 은 사용자가 의료 관련 음성 데이터를 텍스트로 변환하는
기능을 사용자의 음성 지원 애플리케이션에 쉽게 추가할 수 있도록 하는 자동 음성
인식(ASR) 서비스입니다.
https://aws.amazon.com/ko/transcribe/medical/
E(O) : Lambda 로 Scalabilty 확보 가능. Amazon Textract 는 이미지 등에서 텍스트를
추출하는 OCR 서비스로 문서화에 적합. Amazon Comprehend Medical은 미리 학습된 기계
학습을 사용하여 처방전, 처치, 진단과 같은 의료 텍스트에서 의료 데이터를 파악하고
추출하는 서비스로 병원에서 사용하기 적합.
확장성 : Lambda 는 코드를 실행하는 인프라를 관리하고 수신 요청에 대한 응답으로 자동
확장됩니다.
https://docs.aws.amazon.com/ko_kr/lambda/latest/dg/gettingstarted-features.html#getti
ngstarted-features-scaling
Amazon Textract 는 스캔한 문서에서 텍스트, 필기 및 데이터를 자동으로 추출하는 기계
학습(ML) 서비스입니다. 단순한 광학 문자 인식(OCR) 이상으로 양식 및 표의 데이터를
식별하고 이해하며 추출합니다.
https://aws.amazon.com/ko/textract/
Amazon Comprehend Medical 은 HIPAA 적격 자연어 처리(NLP) 서비스로, 미리 학습된
기계 학습을 사용하여 처방전, 처치, 진단과 같은 의료 텍스트에서 의료 데이터를 파악하고
추출합니다.
https://aws.amazon.com/ko/comprehend/medical/
설명2:
이 솔루션은 애플리케이션이 데이터에 대해 SQL 쿼리를 실행할 수 있도록 문서를 분석하고
의료 정보를 추출하고 문서를 저장하는 대량의 과거 서면 기록 컬렉션을 위한 디지털 사본
생성 요구 사항을 충족합니다. 문서 정보를 Amazon S3 버킷에 쓰면 스캔한 파일을 위한
확장 가능하고 내구성 있는 스토리지를 제공할 수 있습니다. Amazon Athena 를 사용하여
데이터를 쿼리하면 S3 에 저장된 데이터에 대한 서버리스 및 대화형 SQL 분석을 제공할 수
있습니다. 새 문서가 업로드될 때 실행되는 AWS Lambda 함수를 생성하면 스캔한 파일의
이벤트 기반 및 서버리스 처리를 제공할 수 있습니다. Amazon Textract를 사용하여 문서를
원시 텍스트로 변환하면 정확한 광학 문자 인식(OCR)을 제공하고 인공 지능(AI)을
사용하여 문서에서 테이블 및 양식과 같은 구조화된 데이터를 추출할 수 있습니다. Amazon
Comprehend Medical 을 사용하여 텍스트에서 관련 의료 정보를 감지하고 추출하면 의료
텍스트에서 건강 데이터를 이해하고 추출하도록 사전 훈련된 기계 학습을 사용하는 자연어
처리(NLP) 서비스를 제공할 수 있습니다.
실행되는 Amazon EC2 인스턴스에 문서 정보를 쓰기 때문에 옵션 A가 올바르지 않습니다.
MySQL 데이터베이스는 인프라 오버헤드와 복잡성을 증가시킬 수 있으며 대량의 데이터를
처리하지 못할 수 있습니다.
스캔한 파일을 처리하고 의료 정보를 추출하는 사용자 지정 애플리케이션을 실행하기 위해
Amazon EC2 인스턴스의 Auto Scaling 그룹을 생성하면 인프라 오버헤드와 복잡성이
증가할 수 있고 기존 AI 및 NLP 서비스를 활용하지 못할 수 있으므로 옵션 C 는 올바르지
않습니다. Textract 및 Comprehend Medical과 같은
Amazon Rekognition을 사용하여 문서를 원시 텍스트로 변환하면 이미지 및 비디오 분석을
제공할 수 있지만 OCR 또는 문서에서 구조화된 데이터 추출을 지원하지 않기 때문에 옵션
D 는 올바르지 않습니다. Amazon Transcribe Medical 을 사용하여 텍스트에서 관련 의료
정보를 감지하고 추출하면 의료 대화를 위한 음성-텍스트 변환 서비스를 제공할 수 있지만
텍스트 분석이나 의료 텍스트에서 건강 데이터 추출은 지원하지 않습니다.
참조:
https://aws.amazon.com/s3/
https://aws.amazon.com/athena/
https://aws.amazon.com/lambda/
https://aws.amazon.com/texttract/
https://aws.amazon.com/comprehend/medical/
~~~

---

# Q193 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/89134-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
이 솔루션은 여러 Amazon RDS 데이터베이스가 있는 백엔드로 구성된 배치
애플리케이션의 고가용성을 보장하면서 데이터베이스 읽기 수를 줄이는 요구 사항을
충족합니다.
Amazon RDS 읽기 전용 복제본은 읽기 전용 트래픽을 처리할 수 있는 기본 데이터베이스
인스턴스의 복사본입니다. 기본 데이터베이스 인스턴스에 대해 하나 이상의 읽기 전용
복제본을 만들고 특수 엔드포인트를 사용하여 연결할 수 있습니다. 읽기 전용 복제본은
기본 데이터베이스 인스턴스에서 읽기 쿼리를 오프로드하여 애플리케이션의 성능과
가용성을 향상시킬 수 있습니다.
Redis 용 Amazon ElastiCache 를 사용하면 자주 액세스하는 데이터를 캐시할 수 있는 빠른
인 메모리 데이터 스토어를 제공할 수 있지만 Amazon RDS 데이터베이스에서 복제를
지원하지 않기 때문에 옵션 B는 올바르지 않습니다.
Amazon Route 53 DNS 캐싱을 사용하면 DNS 쿼리의 성능과 가용성을 개선할 수 있지만
데이터베이스 읽기 수는 줄어들지 않기 때문에 옵션 C는 올바르지 않습니다.
Memcached용 Amazon ElastiCache를 사용하면 자주 액세스하는 데이터를 캐시할 수 있는
빠른 메모리 데이터 스토어를 제공할 수 있지만 Amazon RDS 데이터베이스에서 복제를
지원하지 않기 때문에 옵션 D는 올바르지 않습니다.
설명2:
Amazon RDS 데이터베이스에 읽기 전용 복제본을 추가하면 읽기 워크로드를 복제본으로
오프로드하여 데이터베이스 읽기 수를 줄이고 성능을 향상할 수 있습니다. 읽기 전용
복제본은 고가용성을 제공하고 읽기 트래픽을 독립적으로 처리하여 로드를 분산하고 기본
데이터베이스의 부담을 줄일 수 있습니다.
B. Redis용 Amazon ElastiCache는 주로 캐싱에 사용되는 인 메모리 데이터 스토어로, 읽기
성능을 향상시킬 수 있지만 데이터베이스 읽기 수를 직접적으로 줄이지는 않습니다.
C. Amazon Route 53 DNS 캐싱은 DNS 응답을 캐시하는 서비스로, 전체 네트워크 성능을
향상시킬 수 있지만 데이터베이스 읽기 감소를 구체적으로 다루지는 않습니다.
D. Memcached 용 Amazon ElastiCache 는 Redis 와 유사한 또 다른 캐싱 서비스이지만
데이터베이스 읽기 감소 문제를 직접적으로 해결하지는 않습니다.
참조:
https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html
~~~

---

# Q194 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/89136-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
서로 다른 가용 영역에서 두 개의 EC2 인스턴스를 시작하고 데이터베이스 복제가 있는
클러스터로 구성하면 데이터베이스에서 고가용성과 자동 장애 조치를 달성할 수 있습니다.
한 인스턴스 또는 가용 영역을 사용할 수 없게 되더라도 다른 인스턴스는 중단 없이
애플리케이션을 계속 제공할 수 있습니다.
B. 단일 EC2 인스턴스를 시작하고 백업 및 프로비저닝 자동화를 위해 AMI 를 사용하면
자동 장애 조치 또는 고가용성이 제공되지 않습니다.
C. 다른 AWS 리전에서 EC2 인스턴스를 시작하고 데이터베이스 복제를 설정하는 것은
재해 복구 기능을 제공할 수 있지만 단일 리전 내에서 자동 장애 조치를 제공하지 않는
다중 리전 설정입니다.
D. EC2 자동 복구를 사용하면 하드웨어 문제로 인해 인스턴스가 실패하는 경우 인스턴스를
복구할 수 있지만 여러 인스턴스 또는 가용 영역에서 자동 장애 조치 또는 고가용성을
제공하지는 않습니다.
~~~

---

# Q195 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/89138-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
SQS 는 Dead Letter Queue 등 다양한 옵션으로 메시지 처리가 실패했을 경우 해당
메시지를 보관했다가 다시 처리할 수 있게끔 하는 기능을 제공하고 있음.
설명2:
시스템 중단 시 자동으로 주문을 처리할 수 있는 탄력적인 솔루션을 보유해야 한다는
회사의 요구 사항을 충족하려면 솔루션 설계자가 내결함성 아키텍처를 구현해야 합니다.
주어진 시나리오에 따라 가능한 솔루션은 EC2 인스턴스를 Auto Scaling 그룹으로 이동하고
메시지를 Amazon Simple Queue Service(Amazon SQS) 대기열로 보내도록 주문 시스템을
구성하는 것입니다. 그런 다음 EC2 인스턴스는 대기열의 메시지를 사용할 수 있습니다.
~~~

---

# Q196 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/89140-exam-aws-certified-solut
ions-architect-associate-saa-c03/
해설1:
30 일 동안의 데이터만 필요하다고 했으니 30 일이 지나면 자동 삭제되도록 하는 기능이
필요.
A(X) : 30일마다 재배포하는 것은 번거로움.
B(X) : 스크립트를 사용하는 것은 스크립트를 짜야하므로 번거로움.
C(X) : Lambda 함수를 매번 쓰는 것은 비용 효율성 면에서 좋지 않고 Lambda 코드 짜는
것도 번거로움.
D(O) : TTL 속성을 사용하면 별다른 코딩이나 노력 없이 설정만 해두면 자동으로
삭제되므로 간편함.
Amazon DynamoDB TTL(Time to Live)을 사용하면 항목별 타임스탬프를 정의하여 항목이 더
이상 필요하지 않은 시기를 결정할 수 있습니다. 지정된 타임스탬프의 날짜 및 시간 직후
DynamoDB는 쓰기 처리량을 소모하지 않고 테이블에서 항목을 삭제합니다.
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TTL.html
설명2:
Amazon DynamoDB TTL(Time to Live)을 사용하면 항목별 타임스탬프를 정의하여 항목이 더
이상 필요하지 않은 시기를 결정할 수 있습니다. 지정된 타임스탬프의 날짜 및 시간 직후
DynamoDB 는 쓰기 처리량을 소비하지 않고 테이블에서 항목을 삭제합니다. TTL 은
워크로드 요구 사항에 따라 최신 상태로 유지되는 항목만 유지하여 저장된 데이터 볼륨을
줄이는 수단으로 추가 비용 없이 제공됩니다. TTL 은 특정 시간이 지나면 관련성을 잃는
항목을 저장할 때 유용합니다.
다음은 TTL 사용 사례의 예입니다.
애플리케이션에서 1 년 동안 활동이 없으면 사용자 또는 센서 데이터를 제거합니다. 만료된
항목을 Amazon DynamoDB Streams 및 AWS Lambda를 통해 Amazon S3 데이터 레이크에
보관합니다. 계약 또는 규제 의무에 따라 일정 기간 동안 민감한 데이터를 보관합니다.
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TTL.html
~~~

---

# Q197 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/89068-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
A(X) : 리팩터링은 코드 변경을 수반하므로 개발 변경 사항 최소화 조건 불충족.
B(O) : AWS Elastic Beanstalk.NET용 에서 Amazon Web Services를 사용하는 ASP.NET 웹
애플리케이션을 보다 쉽게 배포, 관리 및 조정할 수 있습니다.
https://docs.aws.amazon.com/ko_kr/elasticbeanstalk/latest/dg/create_deploy_NET.html
C(X) : 재플랫폼화는 개발 변경 사항 최소화 조건 불충족.
D(X) : Oracle 데이터베이스는 관계형 데이터베이스이고, DynamoDB 는 비관계형
데이터베이스로 유형이 다름. 개발 변경 최소화 조건 불충족.
E(O) : 다중 AZ 배포로 고가용성 조건 충족. DMS 서비스로 데이터베이스 마이그레이션
가능. RDS for Oracle로 개발 변경 최소화 가능.
설명2:
애플리케이션을 AWS 로 이동하는 동안 개발 변경을 최소화하고 높은 수준의 가용성을
보장하기 위해 회사는 다중 AZ 배포에서 .NET 플랫폼을 사용하여 AWS Elastic
Beanstalk 에서 애플리케이션을 다시 호스팅할 수 있습니다. 이렇게 하면 애플리케이션
코드를 변경할 필요 없이 고가용성 환경에서 애플리케이션을 실행할 수 있습니다.
또한 회사는 AWS Database Migration Service(AWS DMS)를 사용하여 다중 AZ 배포에서
Oracle 데이터베이스를 Amazon RDS 의 Oracle 로 마이그레이션할 수 있습니다. 이를 통해
회사는 여전히 높은 수준의 가용성을 달성하면서 기존 데이터베이스 플랫폼을 유지할 수
있습니다.
~~~

---

# Q198 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/89078-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
Kubernetes 클러스터 = EKS
MongoDB 호환 = DocumentDB
설명2:
Amazon DocumentDB(MongoDB 와 호환)는 빠르고 안정적이며 완벽하게 관리되는
데이터베이스 서비스입니다.
Amazon DocumentDB를 사용하면 클라우드에서 MongoDB 호환 데이터베이스를 쉽게 설정,
운영 및 확장할 수 있습니다. Amazon DocumentDB 를 사용하면 동일한 애플리케이션
코드를 실행하고 MongoDB 에서 사용하는 것과 동일한 드라이버 및 도구를 사용할 수
있습니다.
https://docs.aws.amazon.com/documentdb/latest/developerguide/what-is.html
~~~

---

# Q199 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/89141-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
A(X) : Amazon Rekognition 은 이미지/비디오 분석 서비스. 콜센터라고 했으므로 오디오를
다른 걸로 변환시켜주는 서비스가 필요하므로 오답.
Amazon Rekognition 은 애플리케이션에 강력한 시각 분석 기능을 쉽게 추가할 수 있게 해
주는 서비스입니다. Rekognition Image를 통해 수백만 개의 이미지를 검색, 확인 및 구성할
수 있는 강력한 애플리케이션을 쉽게 구축할 수 있습니다. Rekognition Video 를 통해
저장된 동영상 또는 실시간 스트림 동영상에서 동작 기반 컨텍스트를 추출하고 이를 분석할
수 있습니다. https://aws.amazon.com/ko/rekognition/faqs/
B(O) : Amazon Transcribe로 다중 Speaker 인식 가능. 7년 동안 저장해야한다고 했으므로
S3 같은 스토리지 서비스가 필요한데, 해당 선택지에서는 S3 가 언급은 되지 않았으나
S3에 쿼리하는 Athena가 있으므로 S3를 사용하고 있다고 추측할 수 있음.
Amazon Transcribe 는 고객이 손쉽게 음성을 텍스트로 변환할 수 있게 해주는 AWS
서비스입니다. https://aws.amazon.com/ko/transcribe/faqs/
C(X) : Amazon Translate는 기계 번역 서비스.
Amazon Translate 는 합리적인 가격으로 고품질의 사용자 지정 가능한 언어 번역을 빠르게
제공하는 신경망 기계 번역 서비스입니다. https://aws.amazon.com/ko/translate/
D(X) : A와 동일한 이유로 오답.
설명2:
Amazon Transcribe는 이제 스트리밍 트랜스크립션을 위한 화자 레이블 지정을 지원합니다.
Amazon Transcribe 는 음성을 텍스트로 쉽게 변환할 수 있는 자동 음성 인식(ASR)
서비스입니다.
라이브 오디오 전사에서 각 오디오 스트림에는 여러 명의 화자가 포함될 수 있습니다. 이제
화자에게 레이블을 지정하는 기능을 편리하게 켤 수 있으므로 출력 기록에서 누가 무엇을
말하는지 식별하는 데 도움이 됩니다.
https://aws.amazon.com/ko/about-aws/whats-new/2020/08/amazon-transcribe-support
s-speaker-labeling-streaming-transcription/
~~~

---

# Q200 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/89142-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
Amazon Cognito 콘솔, CLI/SDK 또는 API 를 사용하여 사용자 풀을 만들거나 다른 AWS
계정이 소유한 풀을 사용합니다.
설명2:
https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-integrate-w
ithcognito.html
REST API 에 대한 액세스를 제어하고 개발 노력을 줄이기 위해 회사는 API Gateway 에서
Amazon Cognito 사용자 풀 권한 부여자를 사용할 수 있습니다. 이를 통해 Amazon
Cognito 는 각 요청을 검증하고 인증된 사용자만 API 에 액세스할 수 있도록 합니다. 이
솔루션은 회사가 추가 인프라나 코드를 개발하고 유지 관리할 필요가 없으므로 운영
오버헤드가 가장 적습니다.
~~~