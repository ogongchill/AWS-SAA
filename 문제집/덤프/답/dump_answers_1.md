# Q1 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/84973-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:・
여러 글로벌 사이트의 데이터를 단일 Amazon S3 버킷에 최대한 빨리 집계하는 동시에
운영 복잡성을 최소화하려면 가장 적합한 솔루션은 옵션 A: 대상 S3 버킷에서 S3 전송
가속화를 설정하고 멀티파트 업로드를 사용하여 사이트 데이터를 대상 S3 버킷에 직접
업로드하는 것입니다.
요약하면 옵션 A 는 여러 글로벌 사이트의 데이터를 단일 Amazon S3 버킷으로 신속하게
집계하는 가장 효율적이고 운영상 간단한 솔루션을 제공합니다. S3 Transfer Acceleration 및
멀티파트 업로드를 활용하여 회사는 복잡성을 최소화하면서 빠른 데이터 수집을 달성할 수
있습니다.
~~~

---

# Q2 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/84848-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:・
S3에 쿼리하는 건 Athena.
Athena 가 사용 가능한 모든 리전에서 Amazon Athena 를 사용하여 표준 SQL 로 Amazon
S3 인벤토리를 쿼리할 수 있습니다.
https://docs.aws.amazon.com/ko_kr/AmazonS3/latest/userguide/storage-inventory-athen
a-query.html
Athena로 JSON 쿼리 가능.
Amazon Athena 를 사용하면 JSON 인코딩 값을 구문 분석하고, JSON 에서 데이터를
추출하고, 값을 검색하고, JSON 배열의 길이와 크기를 찾을 수 있습니다.
https://docs.aws.amazon.com/athena/latest/ug/querying-JSON.html
~~~

---

# Q3 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/84838-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:・
A(O) : aws:PrincipalOrgID 라는 새로운 조건 키를 권한 정책에 사용하여 조직 내의 계정에
해당하는 IAM 보안 주체(사용자 및 역할)만 리소스에 액세스할 수 있도록 합니다.
https://aws.amazon.com/ko/about-aws/whats-new/2018/05/principal-org-id/
B(X) : aws:PrincipalOrgPaths 는 다중 값 조건 키입니다. 다중 값 키에는 하나 이상의 값이
목록 형식으로 포함됩니다. 결과는 논리적 OR입니다.
https://docs.aws.amazon.com/ko_kr/IAM/latest/UserGuide/reference_policies_condition-k
eys.html
C(X) : CloudTrail 은 리소스 내역을 기록/전송하는 서비스로 지문에서 요구하는 사항에
불필요.
D(X) : 각 사용자마다 태그를 달아야 하므로 최소 운영 오버헤드라는 조건 불충족.
aws:PrincipalTag/tag-key : 문자열 연산자를 사용합니다. 이 키를 사용하여 요청한 보안
주체에 연결된 태그를 정책에서 지정한 태그와 비교합니다.
https://docs.aws.amazon.com/ko_kr/IAM/latest/UserGuide/reference_policies_condition-k
eys.html
설명2:
aws:PrincipalOrgID 전역 키는 조직의 모든 AWS 계정에 대한 모든 계정 ID 를 나열하는
대신 사용할 수 있습니다. 예를 들어 다음 Amazon S3 버킷 정책은 XXX 조직의 모든 계정
구성원이 시험 주제 버킷에 객체를 추가하도록 허용합니다.
{"Version": "2020-09-10",
"Statement": {
"Sid": "AllowPutObject",
"Effect": "Allow",
"Principal": "*",
"Action": "s3:PutObject",
"Resource": "arn:aws:s3:::examtopics/*",
"Condition": {"StringEquals":
{"aws:PrincipalOrgID":["XXX"]}}}}
https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.ht
ml
~~~

---

# Q4 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/84980-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:・
VPC-S3 간 인터넷을 통하지 않는 연결 = S3 VPC Gateway Endpoint. 정답은 A.
설명2:
VPC 종단점을 사용하면 공용 인터넷을 사용하는 대신 사설 네트워크를 사용하여 AWS
서비스에 연결할 수 있습니다.
~~~

---

# Q5 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/84981-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:・
EBS와 EFS의 가장 큰 차이점 중 하나는 EBS는 단일 AZ안에서만 접근이 가능한 저장소인
반면, EFS 는 다중 AZ 안에서도 접근이 가능한 저장소라는 점입니다. 위 문제에서는 초기
단일 AZ 에서 운영하던 EC2 및 EBS 를 복제한뒤 AZ 를 2 중화하여 멀티 EC2 및 EBS
시스템으로 구성하였지만, 각 AZ 내에서 공유되지 않는 EBS 저장소를 별도로
운영하였기때문에 고객들에게 일관성있는 데이터를 제공할 수 없었던 것으로 보입니다.
이는 각 AZ 의 EC2 인스턴스가 동일한 저장소를 공유하도록 함으로써 해결할 수 있을 것
같습니다. 초기 EBS 에 저장되어있던 데이터들을 일관성있게 보정하여 EFS 로 일회성
마이그레이션을 수행한뒤 EC2 어플리케이션 서버 인스턴스가 EBS가 아닌 EFS에 데이터를
저장하도록 변경하는 것이 바람직해보입니다.
설명2:
Amazon EFS는 AWS 클라우드에서 파일 스토리지를 제공합니다. Amazon EFS를 사용하면
파일 시스템을 생성하고 파일 시스템을 Amazon EC2 인스턴스에 탑재한 다음 파일
시스템에서 데이터를 읽고 쓸 수 있습니다. Network File System 버전 4.0 및 4.1(NFSv4)
프로토콜을 통해 VPC 에 Amazon EFS 파일 시스템을 탑재할 수 있습니다. Amazon EFS
Mount Helper와 함께 최신 Amazon Linux, Redhat 및 Ubuntu AMI에 있는 것과 같은 현재
세대 Linux NFSv4.1 클라이언트를 사용하는 것이 좋습니다. 지침은 amazon-efs-utils 도구
사용 단원을 참조하십시오.
이 프로토콜을 지원하는 Amazon EC2 Linux Amazon 머신 이미지(AMI) 목록은 NFS 지원을
참조하십시오. 일부 AMI 의 경우 파일 시스템을 Amazon EC2 인스턴스에 탑재하려면 NFS
클라이언트를 설치해야 합니다. 지침은 NFS 클라이언트 설치를 참조하십시오.
여러 NFS 클라이언트에서 동시에 Amazon EFS 파일 시스템에 액세스할 수 있으므로 단일
연결 이상으로 확장되는 애플리케이션이 파일 시스템에 액세스할 수 있습니다. 동일한 AWS
리전 내의 여러 가용 영역에서 실행되는 Amazon EC2 인스턴스는 파일 시스템에 액세스할
수 있으므로 많은 사용자가 공통 데이터 원본에 액세스하고 공유할 수 있습니다.
https://docs.aws.amazon.com/efs/latest/ug/how-it-works.html#how-it-works-ec2
~~~

---

# Q6 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/84875-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:・
가능한 한 최소한의 네트워크 대역폭을 사용하라 했으니 아예 오프라인에서 Snowball
Edge로 올리는 게 맞음.
AWS Snowball 및 AWS Snowball Edge 는 기존 저장소에서 네트워크 대역폭이 충분하지
않을 때, 대용량 데이터 세트를 클라우드로 이전하는데 도움이 됩니다.
Snowball 장치는 80TB, Snowball Edge는 100TB까지 한번에 이동 가능합니다.
https://aws.amazon.com/ko/blogs/korea/aws-snowball-and-aws-snowball-edge-availa
ble-in-asia-pacific-seoul-region/
설명2:
Snowball 과 Snowball Edge 의 기본적인 차이점은 제공하는 용량입니다. Snowball 은 총
50TB 또는 80TB를 제공하며 그 중 42TB 또는 72TB를 사용할 수 있고 Amazon Snowball
Edge는 100TB를 제공하며 그 중 83TB를 사용할 수 있습니다.
~~~

---

# Q7 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/84721-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:・
https://aws.amazon.com/sqs/features/
들어오는 요청을 Amazon SQS 로 라우팅함으로써 회사는 처리 인스턴스에서 작업 요청을
분리할 수 있습니다. 이를 통해 대기열 크기에 따라 인스턴스 수를 확장하여 필요할 때 더
많은 리소스를 제공할 수 있습니다. 또한 대기열 크기를 기반으로 하는 Auto Scaling
그룹을 사용하면 워크로드에 따라 자동으로 인스턴스 수를 늘리거나 줄일 수 있습니다.
대기열에서 읽을 수 있도록 소프트웨어를 업데이트하면 보다 효율적인 방식으로 작업
요청을 처리할 수 있어 시스템 성능이 향상됩니다.
솔루션을 분리 = SQS.
~~~

---

# Q8 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/84679-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:・
A(X) : Scheduled Scaling은 실시간 현황에 맞춰 적용되는 탄력성이 부족.
B(O) : SQS Queue 로 갑작스레 작업이 몰려도 추후 처리하도록 보관 가능. Auto Scaling
그룹으로 여러 EC2 인스턴스의 확장/축소를 적절하게 지원.
C(X) : CloudTrail은 리소스 내역을 기록/전송하는 서비스.
D(X) : CPU사용률에 따라 EC2 Auto Scaling하려면 Target Tracking Policy를 사용하면 됨.
대상 추적 조정 정책을 사용하여 Application Load Balancer 의 RequestCountPerTarget
지표 또는 평균 CPU 사용률 같은 지표에 따라 확장하는 것이 좋습니다. 용량이 증가할 때
감소하고 용량이 감소할 때 증가하는 지표를 사용하여 비례적으로 확장하거나 대상 추적을
사용하여 인스턴스 수를 늘릴 수 있습니다.
https://docs.aws.amazon.com/ko_kr/autoscaling/ec2/userguide/as-scaling-simple-step.
html
설명2:
복원력과 확장성을 극대화하기 위한 최상의 솔루션은 Amazon SQS 대기열을 작업의
대상으로 사용하는 것입니다. 이렇게 하면 컴퓨팅 노드에서 기본 서버가 분리되어
독립적으로 확장할 수 있습니다. 이는 또한 실패 시 일자리 손실을 방지하는 데 도움이
됩니다. 컴퓨팅 노드에 대해 Amazon EC2 인스턴스의 Auto Scaling 그룹을 사용하면
워크로드에 따라 자동 조정이 가능합니다. 이 경우 Amazon SQS 대기열의 크기를 기반으로
Auto Scaling 그룹을 구성하는 것이 좋습니다. 이는 기본 서버 또는 컴퓨팅 노드의
로드보다 실제 워크로드를 더 잘 나타내는 지표입니다. 이 접근 방식은 애플리케이션이
가변 워크로드를 처리할 수 있도록 하는 동시에 필요에 따라 컴퓨팅 노드를 자동으로 확장
또는 축소하여 비용을 최소화합니다.
~~~

---

# Q9 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/84680-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:・
사용 가능한 스토리지 공간을 늘림 = Storage Gateway. 답은 B.
A(X) : AWS 에서 무슨 스토리지를 사용할 건지에 대한 언급이 없음. 또한 하이브리드
스토리지인 Storage Gateway가 더 적절한 방식임.
B(O) : 정답. 스토리지 게이트웨이는 온프레미스 스토리지와 AWS 스토리지를 합쳐 사실상
무제한의 스토리지를 향유하는 것을 목적으로 하는 서비스.
Amazon S3 File Gateway 의 사용 사례로는 (a) 최근에 액세스한 데이터에 대해 빠른 로컬
액세스를 유지하면서 온프레미스 파일 데이터를 Amazon S3 로 마이그레이션. SMB(서버
메시지 블록) 버전 2 및 3 을 사용하여 게이트웨이에 연결하는 Windows 클라이언트를
지원합니다.
https://aws.amazon.com/ko/storagegateway/faqs/?nc=sn&loc=6
C(X) : A와 같은 이유로 오답.
D(X) : SMB 사용 여부 불투명.
설명2:
Amazon S3 File Gateway 는 온프레미스 애플리케이션이 Amazon S3 클라우드 스토리지를
원활하게 사용할 수 있도록 하는 하이브리드 클라우드 스토리지 서비스입니다. Amazon
S3 에 대한 파일 인터페이스를 제공하고 SMB 및 NFS 프로토콜을 지원합니다. 또한 지정된
기간이 지나면 데이터를 S3 Standard에서 S3 Glacier Deep Archive로 자동 전환할 수 있는
S3 수명 주기 정책을 지원합니다. 이 솔루션은 짧은 대기 시간 액세스를 유지하면서
회사의 사용 가능한 저장 공간을 늘리는 요구 사항을 충족합니다.
가장 최근에 액세스한 파일에 저장하고 파일 수명 주기 관리를 제공하여 향후 스토리지
문제를 방지합니다.
~~~

---

# Q10 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/84681-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:・
주문이 접수된 순서대로 처리되도록 하기 위한 최상의 솔루션은 Amazon SQS
FIFO(선입선출) 대기열을 사용하는 것입니다. 이 유형의 대기열은 메시지를 보내고 받는
정확한 순서를 유지합니다. 이 경우 애플리케이션은 새 주문에 대한 정보를 Amazon API
Gateway REST API 로 보낼 수 있습니다. 그런 다음 API Gateway 통합을 사용하여 처리를
위해 메시지를 Amazon SQS FIFO 대기열로 보낼 수 있습니다. 그런 다음 AWS Lambda
함수를 호출하여 각 주문에 필요한 처리를 수행하도록 대기열을 구성할 수 있습니다.
이렇게 하면 주문이 접수된 정확한 순서대로 처리됩니다.
즉. 주문한 순서대로 = FIFO
~~~

---

# Q11 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/84682-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:・
A(O) : Secrets Manager는 자격증명을 저장해두고 관리할 수 있는 서비스.
AWS Secrets Manager는 애플리케이션, 서비스 및 IT 리소스에 대한 액세스를 보호하는 데
도움이 되는 보안 정보 관리 서비스입니다. 이 서비스를 사용하면 수명 주기 동안
데이터베이스 자격 증명, API 키 및 기타 보안 정보를 손쉽게 교체, 관리 및 검색할 수
있습니다. https://aws.amazon.com/ko/secrets-manager/faqs/
Secrets Manager에서 보안 암호에 대한 자동 교체를 설정할 수 있습니다.
https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html
B(X) : Systems Manager Parameter Store 는 구성 데이터 같은 걸 코드와 분리하여 원치
않는 노출을 막는 것.
Q:AWS Systems Manager parameter store 란 무엇입니까? AWS Systems Manager 는
데이터베이스 문자열과 같은 평문 데이터든 암호와 같은 비밀이든 관계없이 구성 데이터를
관리할 수 있는 중앙 스토어를 제공합니다. 따라서 비밀과 구성 데이터를 코드와 분리할 수
있습니다. https://aws.amazon.com/ko/systems-manager/faq/
C(X) : KMS키는 S3 버킷에 저장하는 것이 아니라 Secrets Manager 등을 이용해 관리.
D(X) : C와 비슷한 이유로 오답."
~~~

---

# Q12 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/85010-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
A(O) : 배포를 만들 때 CloudFront 가 파일에 대한 요청을 보내는 원본을 지정합니다.
CloudFront에서 여러 원본을 사용할 수 있습니다. 예를 들어 Amazon S3 버킷, MediaStore
컨테이너, MediaPackage 채널, Application Load Balancer 또는 AWS Lambda 함수 URL을
사용할 수 있습니다.
https://docs.aws.amazon.com/ko_kr/AmazonCloudFront/latest/DeveloperGuide/Download
DistS3AndCustomOrigins.html
Amazon Route 53을 구성하여 CloudFront 배포로 트래픽을 라우팅합니다. 이하 항목 참고
https://docs.aws.amazon.com/ko_kr/Route53/latest/DeveloperGuide/routing-to-cloudfro
nt-distribution.html
B(X) : 지문의 상황은 애플리케이션 계층에서 벌어지는 일이므로 TCP/UDP 를 사용하는
AWS Global Accelerator는 부적절.
C(X) : B와 같은 이유로 오답.
D(X) : B와 같은 이유로 오답.
설명2:
정적 콘텐츠는 S3의 클라우드 프런트 엣지 위치와 ALB 뒤의 동적 콘텐츠 EC2에서 캐싱할
수 있습니다. 그 성능은 하나의 엔드포인트가 ALB 이고 다른 클라우드 프런트인 Global
Accelerator에 의해 개선될 수 있습니다.
따라서 사용자 지정 도메인 이름 끝점과 관련하여 웹 응용 프로그램은 웹 응용 프로그램에
대한 사용자 지정 도메인 지점에 대한 R53 별칭 레코드입니다.
https://aws.amazon.com/blogs/networking-and-content-delivery/improving-availability-a
ndperformance-for-app
~~~

---

# Q13 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/84728-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:・
다중 리전 애플리케이션에 필수 리전의 복제된 암호에 대한 액세스 권한을 부여하고
Secrets Manager 를 사용하여 복제본이 기본 암호와 동기화된 상태를 유지할 수 있습니다.
Secrets Manager 를 사용하면 데이터베이스 자격 증명, API 키 및 기타 비밀을 포함한
비밀을 저장, 검색, 관리 및 교체할 수 있습니다.
https://aws.amazon.com/ko/blogs/security/how-to-replicate-secrets-aws-secrets-mana
ger-multiple-regions/
~~~

---

# Q14 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/85019-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:・
A(X) : 단일 노드에서 고가용성 불만족. RedShift 는 MySQL 과 같은 관계형 데이터베이스
서비스가 아니라 데이터 웨어하우스 서비스.
B(X) : 단일 AZ이기 때문에 고가용성 불만족.
C(O) : Aurora는 자동으로 3개의 AZ에 6개의 복제본을 생성. 이러한 복제본은 읽기 부하
분산 효과가 있음.
D(X) : 스팟 인스턴스를 사용할 때는 언제든 중지될 위험에 대비해야 함이 기본임. 즉,
중지될 수 있는 위험이 높은 인스턴스라는 이야기. 그리고 다중 AZ 를 사용하지 않으므로
고가용성을 만족하지 못했음.
설명2:
Aurora 는 RDS 에서 MySQL 보다 5 배 향상된 성능을 제공하며 쓰기보다 더 많은 읽기
요청을 처리합니다. 고가용성 유지 = 다중 AZ 배포.
~~~

---

# Q15 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/84731-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:・
AWS Network Firewall은 필요에 따라 검사와 필터링을 모두 지원합니다.
설명2:
A(X) : GuardDuty는 계정 보호 서비스.
Amazon GuardDuty 는 AWS 계정 및 워크로드에서 악의적 활동을 모니터링하고 상세한
보안 결과를 제공하여 가시성 및 해결을 촉진하는 위협 탐지 서비스입니다.
https://aws.amazon.com/ko/guardduty/
B(X) : 트래픽 미러링은 네트워크 트래픽 복사 서비스.
트래픽 미러링은 유형의 탄력적 네트워크 인터페이스에서 네트워크 트래픽을 복사하는 데
사용할 수 있는 Amazon VPC 기능입니다.
https://docs.aws.amazon.com/vpc/latest/mirroring/what-is-traffic-mirroring.html
C(O) : AWS Network Firewall 을 사용하면 VPC 경계에서 네트워크 트래픽을 필터링할 수
있습니다.
https://docs.aws.amazon.com/ko_kr/vpc/latest/userguide/network-firewall.html
D(X) : Firewall Manager는 중앙에서 방화벽 규칙 관리하는 서비스.
AWS Firewall Manager 는 AWS Organization 의 여러 계정과 애플리케이션에서 방화벽
규칙을 중앙에서 구성 및 관리할 수 있는 보안 관리 서비스입니다. AWS Firewall Manager를
사용하면 조직의 여러 계정 및 리소스에 대한 AWS WAF 규칙, AWS Shield Advanced 보호,
Amazon Virtual Private Cloud(VPC) 보안 그룹 및 AWS Network Firewall 및 Amazon Route
53 Resolver DNS Firewall 규칙을 중앙에서 구성할 수 있습니다.
https://aws.amazon.com/ko/firewall-manager/faqs/
~~~

---

# Q16 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/84732-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:・
시각화 = QuickSight. A,B 둘 중 하나가 정답. 대시보드를 그룹과 사용자와 공유해야하므로
정답은 B.
기본적으로 Amazon QuickSight 의 대시보드는 누구와도 공유되지 않으며 소유자만
액세스할 수 있습니다. 그러나 대시보드를 게시한 후에는 QuickSight 계정의 다른 사용자
또는 그룹과 공유할 수 있습니다.
https://docs.aws.amazon.com/quicksight/latest/user/sharing-a-dashboard.html
설명2:
Amazon QuickSight 는 PostgreSQL 용 Amazon S3 및 Amazon RDS 를 비롯한 다양한
데이터 소스에서 대화형 대시보드 및 보고서를 생성할 수 있는 데이터 시각화 서비스입니다.
모든 데이터 소스를 연결하고 QuickSight 에서 새 데이터 세트를 만든 다음 대시보드를
게시하여 데이터를 시각화할 수 있습니다. 또한 적절한 사용자 및 그룹과 대시보드를
공유하고 IAM 역할 및 권한을 사용하여 액세스 수준을 제어할 수 있습니다.
~~~

---

# Q17 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/85032-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:・
https://aws.amazon.com/premiumsupport/knowledge-center/ec2-instance-access-s3-b
ucket/
설명2:
EC2 인스턴스가 S3 버킷에 액세스할 수 있는 권한이 있어야 하므로 IAM 역할을 부여해야
함.
EC2 인스턴스에서 S3 버킷에 연결하려면 다음을 실행해야 합니다.
1. Amazon S3에 대한 액세스 권한을 부여하는 AWS Identity and Access Management(IAM)
프로파일 역할을 생성합니다.
2. 인스턴스에 IAM 인스턴스 프로파일을 연결합니다.
3. S3 버킷에 대한 권한을 확인합니다.
https://aws.amazon.com/ko/premiumsupport/knowledge-center/ec2-instance-access-s
3-bucket/
~~~

---

# Q18 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/85033-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:・
A,E 조합으로 S3 버킷->EventBridge->SNS Topic->SQS->Lambda 프로세스도 가능하긴
한데, A,B 조합으로 S3->SQS->Lambda가 훨씬 운영 및 비용 효율적.
・S3 Events -> SQS Queue
Amazon S3 은 다음과 같은 대상으로 이벤트 알림 메시지를 보낼 수 있습니다....◎Amazon
Simple Queue Service(Amazon SQS) 대기열
https://docs.aws.amazon.com/ko_kr/AmazonS3/latest/userguide/NotificationHowTo.html
・SQS Queue -> Lambda
Lambda 함수를 사용하여 Amazon Simple Queue Service(Amazon SQS) 대기열의 메시지를
처리할 수 있습니다.
https://docs.aws.amazon.com/ko_kr/lambda/latest/dg/with-sqs.html
설명2:
Amazon Simple Queue Service(SQS) 대기열을 생성하고 이미지가 S3 버킷에 업로드될 때
SQS 대기열에 알림을 보내도록 S3 버킷을 구성하면 Lambda 함수가 상태 비저장 및
내구성 방식으로 트리거됩니다.
SQS 대기열을 호출 소스로 사용하도록 Lambda 함수를 구성하고 성공적으로 처리된 후
대기열에서 메시지를 삭제하면 Lambda 함수가 상태 비저장 및 내구성 방식으로 이미지를
처리합니다.
Amazon SQS는 마이크로서비스, 분산 시스템 및 서버리스 애플리케이션을 분리하고 확장할
수 있는 완전관리형 메시지 대기열 서비스입니다. SQS 는 메시지 지향 미들웨어 관리 및
운영과 관련된 복잡성과 오버헤드를 제거하고 개발자가 차별화 작업에 집중할 수 있도록
합니다. 새 이미지가 S3 버킷에 업로드되면 SQS 는 Lambda 함수를 트리거하여 이미지를
처리하고 압축합니다. 이미지가 처리되면 SQS 메시지가 삭제되어 Lambda 함수가 상태
비저장 및 내구성이 보장됩니다.
~~~

---

# Q19 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/84727-exam-aws-certified-solut
ions-architect-associate-saa-c03/
해설:・
Gateway Load Balancer 를 사용하면 방화벽, 침입 탐지 및 방지 시스템, 심층 패킷 검사
시스템과 같은 가상 어플라이언스를 배포, 확장 및 관리할 수 있습니다. Gateway Load
Balancer 는 Gateway Load Balancer 엔드포인트를 사용하여 VPC 경계 전체에서 트래픽을
안전하게 교환합니다.
https://docs.aws.amazon.com/ko_kr/elasticloadbalancing/latest/gateway/introduction.htm
l
오늘 AWS Gateway Load Balancer(GWLB)가 정식 출시되었다는 소식을 알려드리고자
합니다. 이를 통해 타사 가상 어플라이언스의 가용성을 쉽고 비용 효율적으로 배포, 확장
및 관리 할 수있는 서비스 방화벽 , 침입 감지 및 방지 시스템과 클라우드의 심층 패킷
검사 시스템. AWS 파트너 네트워크 및 AWS Marketplace 파트너는 규모, 가용성 및 서비스
제공이라는 복잡한 문제를 해결하지 않고도 AWS 고객에게 가상 어플라이언스를 서비스로
제공 할 수도 있습니다.
https://aws.amazon.com/ko/blogs/korea/introducing-aws-gateway-load-balancer-easy-
deployment-scalability-and-high-availability-for-partner-appliances/
~~~

---

# Q20 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/85226-exam-aws-certified-solut
ions-architect-associate-saa-c03/
해설:・
A(X) : 인스턴스 스토어 볼륨은 휘발성이라 꺼지면 데이터 날라감.
B(X) : EBS 다중 연결을 사용하게 되면 복제된 데이터를 수정할 때 프로덕션 환경에 영향을
주게 됨. 이는 지문에서 요구한 사항과 위배됨.
C(X) : 스냅샷으로 새로운 볼륨을 만드는 것이지 만들어진 볼륨에 스냅샷을 복원하는 게
아님.
D(O) : 정답.
~~~

---

# Q21 

~~~ 설명
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
~~~

---

# Q22 

~~~ 설명
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
~~~

---

# Q23 

~~~ 설명
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
~~~

---

# Q24 

~~~ 설명
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
~~~

---

# Q25 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/85197-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:・
대기열(SQS)로 병목 현상을 방지할 수 있습니다.
대량의 데이터 처리 + 확장성 개선 = SQS queue + Lambda 조합.
~~~

---

# Q26 

~~~ 설명
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
~~~

---

# Q27 

~~~ 설명
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
~~~

---

# Q28 

~~~ 설명
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
~~~

---

# Q29 

~~~ 설명
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
~~~

---

# Q30 

~~~ 설명
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
~~~

---

# Q31 

~~~ 설명
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
~~~

---

# Q32 

~~~ 설명
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
~~~

---

# Q33 

~~~ 설명
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
~~~

---

# Q34 

~~~ 설명
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
~~~

---

# Q35 

~~~ 설명
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
~~~

---

# Q36 

~~~ 설명
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
~~~

---

# Q37 

~~~ 설명
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
~~~

---

# Q38 

~~~ 설명
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
~~~

---

# Q39 

~~~ 설명
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
~~~

---

# Q40 

~~~ 설명
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
~~~

---

# Q41 

~~~ 설명
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
~~~

---

# Q42 

~~~ 설명
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
~~~

---

# Q43 

~~~ 설명
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
~~~

---

# Q44 

~~~ 설명
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
~~~

---

# Q45 

~~~ 설명
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
~~~

---

# Q46 

~~~ 설명
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
~~~

---

# Q47 

~~~ 설명
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
~~~

---

# Q48 

~~~ 설명
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
~~~

---

# Q49 

~~~ 설명
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
~~~

---

# Q50 

~~~ 설명
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
~~~

---

# Q51 

~~~ 설명
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
~~~

---

# Q52 

~~~ 설명
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
~~~

---

# Q53 

~~~ 설명
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
~~~

---

# Q54 

~~~ 설명
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
~~~

---

# Q55 

~~~ 설명
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
~~~

---

# Q56 

~~~ 설명
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
~~~

---

# Q57 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/85452-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:・
Amazon Rekognition 을 사용하여 부적절하거나 원치 않거나 불쾌감을 주는 콘텐츠를
감지할 수 있습니다.
https://docs.aws.amazon.com/rekognition/latest/dg/moderation.html
참조
https://docs.aws.amazon.com/rekognition/latest/dg/moderation.html?pg=ln&sec=ft
https://docs.aws.amazon.com/rekognition/latest/dg/a2i-rekognition.html
~~~

---

# Q58 

~~~ 설명
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
~~~

---

# Q59 

~~~ 설명
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
~~~

---

# Q60 

~~~ 설명
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
~~~

---

# Q61 

~~~ 설명
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
~~~

---

# Q62 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/85524-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:・
외부 인증기관에서 발급한 SSL/TLS 인증서가 이미 있고 이를 사용해야하므로 ACM 쪽에서
SSL/TLS 인증서를 발급하는 A,B는 모두 오답.
C(X) : 인증서가 있는데 또 발급받을 필요가 없음.
https://www.amazonaws.cn/en/certificate-manager/faqs/#Managed_renewal_and_deploy
ment
~~~

---

# Q63 

~~~ 설명
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
~~~

---

# Q64 

~~~ 설명
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
~~~

---

# Q65 

~~~ 설명
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
~~~

---

# Q66 

~~~ 설명
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
~~~

---

# Q67 

~~~ 설명
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
~~~

---

# Q68 

~~~ 설명
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
~~~

---

# Q69 

~~~ 설명
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
~~~

---

# Q70 

~~~ 설명
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
~~~

---

# Q71 

~~~ 설명
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
~~~

---

# Q72 

~~~ 설명
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
~~~

---

# Q73 

~~~ 설명
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
~~~

---

# Q74 

~~~ 설명
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
~~~

---

# Q75 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/86120-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:・
AWS Lambda, Amazon API Gateway, AWS Amplify, Amazon DynamoDB 및 Amazon
Cognito를 사용하여 서버리스 웹 애플리케이션을 구축하십시오. 이 예에서는 AWS Lambda,
Amazon API Gateway, AWS Amplify, Amazon DynamoDB 및 Amazon Cognito를 사용하여
서버리스 웹 애플리케이션 구축 질문과 유사한 설정을 보여줍니다.
RESTful API = API Gateway 사용.
트랜잭션 삭제되는 문제 = SQS.
~~~

---

# Q76 

~~~ 설명
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
~~~

---

# Q77 

~~~ 설명
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
~~~

---

# Q78 

~~~ 설명
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
~~~

---

# Q79 

~~~ 설명
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
~~~

---

# Q80 

~~~ 설명
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
~~~

---

# Q81 

~~~ 설명
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
~~~

---

# Q82 

~~~ 설명
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
~~~

---

# Q83 

~~~ 설명
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
~~~

---

# Q84 

~~~ 설명
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
~~~

---

# Q85 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/85751-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:・
수정하거나 삭제할 수 없음 = S3 Object Lock.
S3 객체 잠금을 사용하면 write-once-read-many(WORM) 모델을 사용하여 객체를 저장할
수 있습니다. 객체 잠금은 고정된 시간 동안 또는 무기한으로 객체의 삭제 또는 덮어쓰기를
방지하는 데 도움이 될 수 있습니다.
https://docs.aws.amazon.com/ko_kr/AmazonS3/latest/userguide/object-lock.html
~~~

---

# Q86 

~~~ 설명
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
~~~

---

# Q87 

~~~ 설명
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
~~~

---

# Q88 

~~~ 설명
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
~~~

---

# Q89 

~~~ 설명
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
~~~

---

# Q90 

~~~ 설명
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
~~~

---

# Q91 

~~~ 설명
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
~~~

---

# Q92 

~~~ 설명
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
~~~

---

# Q93 

~~~ 설명
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
~~~

---

# Q94 

~~~ 설명
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
~~~

---

# Q95 

~~~ 설명
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
~~~

---

# Q96 

~~~ 설명
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
~~~

---

# Q97 

~~~ 설명
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
~~~

---

# Q98 

~~~ 설명
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
~~~

---

# Q99 

~~~ 설명
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
~~~

---

# Q100 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/85186-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:・
고가용성 저장소 = S3. B,C 둘 중 하나가 답.
Lambda보다 KMS가 암호화 및 해독에 적합. 정답은 C.
~~~