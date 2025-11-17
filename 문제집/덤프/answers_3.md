# Q201 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/89080-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명
https://aws.amazon.com/pinpoint/product-details/sms/
양방향 메시징: 고객으로부터 SMS 메시지를 받고 채팅과 같은 대화형 환경에서 회신합니다.
Amazon Pinpoint 를 사용하면 고객이 특정 키워드가 포함된 메시지를 보낼 때 자동 응답을
생성할 수 있습니다. Amazon Lex 를 사용하여 대화형 봇을 만들 수도 있습니다. 대부분의
휴대폰 사용자는 들어오는 SMS 메시지를 받은 직후에 읽습니다. 고객에게 긴급하거나
중요한 정보를 제공해야 하는 경우 SMS 메시징이 적합한 솔루션일 수 있습니다. Amazon
Pinpoint 를 사용하여 대상 고객 그룹을 생성한 다음 캠페인 기반 메시지를 보낼 수
있습니다. Amazon Pinpoint 를 사용하여 약속 확인, 주문 업데이트, 일회용 암호와 같은
다이렉트 메시지를 보낼 수도 있습니다.

---

# Q202 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/89081-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
・S3 버킷에 저장될 때 암호화되므로 SSE(서버 측 암호화). 만약 S3 버킷으로 보내기 전에
암호화하면 CSE(클라이언트 측 암호화)임.
・Amazon S3 버킷에 저장되는 모든 객체를 암호화하는 기본 암호화 동작을 버킷에 설정할
수 있습니다. 객체는 Amazon S3 관리형 키를 사용한 서버 측 암호화(SSE-S3) 또는 AWS
Key Management Service(AWS KMS) 키를 사용한 서버 측 암호화를 사용하여
암호화됩니다.
https://docs.aws.amazon.com/ko_kr/AmazonS3/latest/userguide/default-bucket-encrypti
on.html
A(X) : 먼저 S3 버킷을 암호화한 게 아니라 데이터를 S3 버킷에 담아놓고 암호화를 했기
때문에 불필요한 배치 작업이 발생.
Amazon S3 기본 암호화를 사용하면 S3 버킷에 대한 기본 암호화 동작을 설정하여 모든 새
객체가 버킷에 저장될 때 암호화되도록 할 수 있습니다. Amazon S3 관리형 키를 사용한
서버 측 암호화(SSE-S3) 또는 AWS Key Management Service(AWS KMS)에 저장된 AWS
KMS keys 를 사용한 서버 측 암호화(SSE-KMS)로 객체를 암호화합니다. 서버 측 암호화를
사용하는 경우 Amazon S3 에서는 객체를 디스크에 저장하기 전에 암호화하고 기존
Amazon S3 객체를 암호화하기 위해 Amazon S3 배치 작업을 사용할 수 있습니다.
https://docs.aws.amazon.com/ko_kr/AmazonS3/latest/userguide/bucket-encryption.html
B(O) : AWS KMS CMK(고객 관리 키)는 원래 키 자동 교체(rotate)을 하진 않지만 이를
활성화할 수 있음.
https://docs.aws.amazon.com/ko_kr/kms/latest/developerguide/concepts.html#customer
-cmk
C(X) : 암호화 키는 매년 자동 순환되어야 한다고 했는데 수동 순환이라 오답.
D(X) : S3 버킷으로 이동하기 전에 기본 암호화 동작을 설정하므로 SSE 가 아닌
CSE(클라이언트 측 암호화)임.
설명2:
SSE-S3 - 무료이며 AWS 소유 CMK(CMK = 고객 마스터 키)를 사용합니다. 암호화 키는
AWS 에서 소유하고 관리하며 여러 계정 간에 공유됩니다. 회전은 여기 표에 표시된 대로
시간에 따라 자동으로 바뀝니다. 시간은 명시적으로 정의되지 않습니다.
SSE-KMS - 두 가지 특징이 있습니다.
AWS 관리형 CMK. 귀하의 계정에 대해서만 생성된 무료 CMK 입니다. 정책을 보고
사용량을 감사할 수만 있고 관리할 수는 없습니다. 교체는 자동입니다. 1095 일(3 년)당 한
번, 고객이 CMK 를 관리합니다. 이것은 사용자가 생성하고 관리할 수 있는 사용자 고유의
키를 사용합니다. 회전은 기본적으로 활성화되어 있지 않습니다. 그러나 활성화하면
1 년마다 자동으로 순환됩니다. 이 변형은 사용자가 가져온 키 자료를 사용할 수도
있습니다. 가져온 자료로 이러한 키를 생성하면 자동 회전이 없습니다. 수동 회전만
가능합니다.
SSE-C - 고객 제공 키. 암호화 키는 AWS 외부에서 사용자가 완전히 관리합니다. AWS 는
이를 교체하지 않습니다.
이 솔루션은 데이터를 Amazon S3 버킷으로 이동하고, 데이터가 S3 버킷에 저장될 때
데이터를 암호화하고, 최소한의 운영 오버헤드로 매년 암호화 키를 자동으로 교체하는 요구
사항을 충족합니다. AWS Key Management Service(AWS KMS)는 데이터의 암호화 키를
생성하고 관리할 수 있는 서비스입니다. 고객 관리형 키는 AWS KMS 에서 생성하고
관리하는 대칭 암호화 키입니다. 고객 관리형 키에 대해 자동 키 교체를 활성화할 수
있습니다. 즉, AWS KMS는 매년 키에 대한 새로운 암호화 자료를 생성합니다. 고객 관리형
KMS 키를 사용하도록 S3 버킷의 기본 암호화 동작을 설정할 수 있습니다. 즉, 암호화
방법을 지정하지 않고 버킷에 업로드된 모든 객체는 해당 키로 암호화됩니다.
Amazon S3 관리형 암호화 키(SSE-S3)로 서버 측 암호화를 사용하면 암호화 키를
제어하거나 관리할 수 없으므로 옵션 A 는 올바르지 않습니다. SSE-S3 는 각 객체에 대해
고유한 키를 사용하고 S3 에서 정기적으로 순환하는 마스터 키로 해당 키를 암호화합니다.
그러나 SSE-S3 키에 대한 키 교체를 활성화 또는 비활성화하거나 교체 간격을 지정할 수
없습니다.
옵션 C 는 올바르지 않습니다. 매년 KMS 키를 수동으로 교체하면 운영 오버헤드와
복잡성이 증가할 수 있고 교체 프로세스를 잊어버리거나 지연하는 경우 매년 키 교체 요구
사항을 충족하지 못할 수 있기 때문입니다.
데이터를 S3 버킷으로 이동하기 전에 고객 키 자료로 데이터를 암호화하면 운영
오버헤드와 복잡성이 증가할 수 있고 버킷의 모든 객체에 대해 일관된 암호화를 제공하지
못할 수 있으므로 옵션 D 는 올바르지 않습니다. 키 자료 없이 KMS 키를 생성하고 고객 키
자료를 KMS 키로 가져오면 고유한 임의 비트 소스를 사용하여 KMS 키를 생성할 수
있지만 자동 키 순환은 지원하지 않습니다.
참조:
https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html
https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html
https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-encryption.html

---

# Q203 

**정답: D**

https://www.examtopics.com/discussions/amazon/view/89082-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명
회의 초대 전달 시간이 길어지는 문제를 해결하기 위해 솔루션 설계자는 회의 초대를
보내는 애플리케이션에 대해 Auto Scaling 그룹을 추가하고 SQS 대기열의 깊이에 따라
확장되도록 Auto Scaling 그룹을 구성하도록 권장할 수 있습니다. 이렇게 하면 약속 요청
수가 증가함에 따라 애플리케이션이 확장되어 회의 초대의 성능 및 배달 시간이
향상됩니다.

---

# Q204 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/89083-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
A(X) : 액세스 제어하는 것까지만 나왔고 어떻게 쿼리할 것인지는 언급 안 함.
B(X) : 처음부터 S3 에 다 저장할 것이지 결국 S3 에 저장할 거면서 왜 RDS 에 저장했다가
다시 S3에 저장하는지?
C(O) : S3 버킷을 데이터레이크로 만들고 Glue 를 통해서 ETL 함으로서 S3 에 저장된
데이터를 RedShift 같은 서비스에서 사용할 수 있게끔 함. RDS 에 저장된 고객 데이터는
Glue JDBC를 통해 변환
・S3 버킷을 AWS Lake Formation 을 사용해 데이터레이크로 만들고 Glue 기능 사용해
ETL.
AWS Lake Formation 콘솔, Lake Formation API 또는 AWS 명령줄 인터페이스(AWS CLI)를
사용하여 Amazon S3 위치를 등록할 수 있습니다.
https://docs.aws.amazon.com/lake-formation/latest/dg/register-location.html
Lake Formation 은 콘솔 제어, ETL 코드 생성, 작업 모니터링, 공통 데이터 카탈로그,
서버리스 아키텍처를 포함하여 AWS Glue에서 공유 인프라를 활용합니다. AWS Glue는 아직
이러한 유형의 기능에 초점을 맞추고 있는 반면, Lake Formation 은 AWS Glue 기능을
포함하면서, 동시에 데이터 레이크를 구축하고 보안하고 관리하는 데 유용한 추가 기능을
제공합니다.
https://aws.amazon.com/ko/glue/faqs/
・AWS RDS에 저장된 데이터를 Glue에서 사용
AWS Glue는 기본적으로 Amazon Aurora, Amazon RDS for MySQL, Amazon RDS for Oracle,
Amazon RDS for PostgreSQL, Amazon RDS for SQL Server, Amazon Redshift, DynamoDB
및 Amazon S3 뿐만 아니라 Amazon EC2 에서 실행되는 Virtual Private Cloud(Amazon
VPC)에 있는 MySQL, Oracle, Microsoft SQL Server 및 PostgreSQL 데이터베이스에 저장된
데이터를 지원합니다.
https://aws.amazon.com/ko/glue/faqs/
AWS Glue 는 JDBC 연결을 통해 다음 데이터 스토어에 연결할 수 있습니다. ◎Amazon
Redshift. ◎Amazon RDS for MariaDB
https://docs.aws.amazon.com/ko_kr/glue/latest/dg/connection-properties.html#connecti
on-properties-jdbc
・데이터에 대한 세분화된 권한 관리
AWS Lake Formation 은 간단한 권한 부여/취소 메커니즘을 기반으로 하는 권한 모델을
제공합니다. Lake Formation 권한은 AWS Identity and Access Management(IAM) 권한과
결합되어 데이터 레이크에 저장된 데이터 및 해당 데이터를 설명하는 메타데이터에 대한
액세스를 제어합니다.
https://docs.aws.amazon.com/lake-formation/latest/dg/security-data-access.html
D(X) : 주기적으로 처리하라는 요구 사항이 있지 않는 이상 바로바로 처리하는 게 보통인데,
주기적으로 처리하고 있음.
설명2:
다양한 팀에서 모든 데이터를 사용할 수 있도록 하고 운영 오버헤드를 최소화하기 위해
회사는 AWS Lake Formation 을 사용하여 데이터 레이크를 생성할 수 있습니다. 이를 통해
회사는 모든 데이터를 한 곳에서 중앙 집중화하고 세분화된 액세스 제어를 사용하여
데이터에 대한 액세스를 관리할 수 있습니다. 회사의 요구 사항을 충족하기 위해 솔루션
설계자는 AWS Lake Formation을 사용하여 데이터 레이크를 만들고, Amazon RDS에 대한
AWS Glue JDBC 연결을 만들고, Lake Formation 에 S3 버킷을 등록할 수 있습니다. 그런
다음 솔루션 설계자는 Lake Formation 액세스 제어를 사용하여 데이터에 대한 액세스를
제한할 수 있습니다. 이 솔루션은 데이터에 대한 세분화된 권한을 관리하고 운영
오버헤드를 최소화하는 기능을 제공합니다.

---

# Q205 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/89085-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
프라이빗 S3 에서 웹사이트를 호스팅하면 정적 웹사이트 콘텐츠를 위한 비용 효율적이고
가용성이 높은 스토리지를 제공합니다. CloudFront OAI의 액세스를 허용하도록 버킷 정책을
구성하면 CloudFront 를 통해서만 S3 에 안전하게 액세스할 수 있습니다. 이렇게 하면 웹
사이트 콘텐츠가 S3 를 비공개로 유지하면서 CloudFront 를 통해 제공됩니다. AWS CLI 를
사용하여 웹 사이트 콘텐츠를 업로드하면 콘텐츠를 쉽고 효율적으로 관리할 수 있습니다.
A. Lightsail 가상 서버에서 웹 사이트를 호스팅하면 정적 콘텐츠 호스팅에 S3 를 직접
사용하는 것과 비교하여 추가 관리 오버헤드와 비용이 발생합니다.
B. 정적 웹 사이트 콘텐츠를 제공하기 위해 EC2 인스턴스 및 ALB 와 함께 AWS ASG 를
사용할 필요가 없습니다. 불필요한 복잡성과 비용이 추가됩니다.
D. AWS Transfer for SFTP 를 사용하면 SFTP 업로드가 가능하지만 AWS CLI 를 사용하여
콘텐츠를 S3 에 직접 업로드하는 것과 비교하여 추가 비용과 복잡성이 발생합니다. 또한
공용 S3 에서 웹 사이트 콘텐츠를 호스팅하는 것은 보안 관점에서 바람직하지 않을 수
있습니다.
참고:
https://docs.aws.amazon.com/cli/latest/reference/transfer/describe-server.html

---

# Q206 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/89086-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
https://docs.aws.amazon.com/ko_kr/AWSEC2/latest/WindowsGuide/monitor-ami-events.
html
CreateImage API 호출에 대한 Amazon EventBridge(Amazon CloudWatch Events) 규칙을
생성하고 CreateImage API 호출이 감지될 때 알림을 보내도록 대상을 Amazon Simple
Notification Service(Amazon SNS) 주제로 구성하면 운영 오버헤드가 최소인 요구 사항을
충족합니다. .
Amazon EventBridge 는 자체 애플리케이션, 통합 SaaS(Software as a Service)
애플리케이션 및 AWS 서비스의 데이터를 사용하여 애플리케이션을 쉽게 함께 연결할 수
있게 해주는 서버리스 이벤트 버스입니다. CreateImage API 호출에 대한 EventBridge
규칙을 생성하여 회사는 계정 내에서 이 작업이 호출될 때마다 경고를 설정할 수 있습니다.
경고는 SNS 주제로 보낼 수 있으며, 그런 다음 회사의 이메일 또는 기타 원하는 대상으로
알림을 보내도록 구성할 수 있습니다.
참고
https://docs.aws.amazon.com/ko_kr/AWSEC2/latest/WindowsGuide/monitor-ami-events.
html

---

# Q207 

**정답: D**

https://www.examtopics.com/discussions/amazon/view/89087-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명
솔루션 설계자는 SQS 대기열과 Lambda 를 사용하여 처리 마이크로서비스에서 API 프런트
엔드를 분리하고 시스템의 전반적인 확장성과 가용성을 개선할 수 있습니다. SQS 대기열은
버퍼 역할을 하여 API 프런트 엔드가 마이크로서비스 처리에 높은 작업 부하가 발생하거나
일시적으로 사용할 수 없는 경우에도 사용자 요청을 계속 수락할 수 있도록 합니다. 그런
다음 Lambda 함수는 SQS 대기열에서 요청을 검색하고 DynamoDB 에 기록하여 모든
사용자 요청이 저장 및 처리되도록 할 수 있습니다. 이 접근 방식을 통해 회사는 API
프런트 엔드와 독립적으로 처리 마이크로서비스를 확장할 수 있으므로 수요가 많은
기간에도 사용자가 API를 계속 사용할 수 있습니다.
즉 사용자 요청을 잃고 있음 = SQS로 해결. 정답은 D.

---

# Q208 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/89088-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
EC2 인스턴스-S3 버킷 간 통신이 인터넷에 노출되지 않음 = S3 Gateway Endpoint.
설명2:
EC2 인스턴스와 동일한 서브넷에 Amazon S3 용 인터페이스 VPC 종단점을 생성하면 EC2
인스턴스와 S3 간의 데이터 전송이 공용 인터넷을 거치지 않고 Amazon 네트워크 내에서
비공개로 발생할 수 있습니다. 이렇게 하면 EC2 인스턴스와 S3 간의 안전하고 직접적인
통신이 보장됩니다. EC2 인스턴스와 연결된 IAM 역할의 액세스만 허용하는 리소스 정책을
S3 버킷에 연결하면 권한이 부여된 인스턴스에 대한 액세스만 추가로 제한됩니다.
B. Amazon S3 용 게이트웨이 VPC 종단점을 생성하려면 공용 인터넷을 통한 라우팅이
여전히 필요하므로 이 경우에는 바람직하지 않습니다.
C. nslookup 을 실행하거나 VPC 경로 테이블에서 특정 경로를 생성하면 트래픽이 여전히
공용 인터넷 경로를 통과할 수 있으므로 원하는 수준의 보안 및 개인 정보 보호를 제공하지
않습니다.
D. 공개적으로 사용 가능한 ip-ranges.json 파일을 사용하여 S3 버킷의 서비스 API
엔드포인트의 프라이빗 IP 주소를 얻는 것은 권장되는 접근 방식이 아닙니다. IP 주소는
시간이 지남에 따라 변경될 수 있고 동일한 수준의 보안을 제공하지 않기 때문입니다. VPC
엔드포인트를 사용합니다.
참고
https://aws.amazon.com/blogs/security/how-to-restrict-amazon-s3-bucket-access-to-
a-specific-iamrole/

---

# Q209 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/89089-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
https://aws.amazon.com/vi/caching/session-management/
확장성을 해결하고 개별 웹 서버에서 액세스할 수 있는 세션에 대한 공유 데이터 저장소를
제공하기 위해 웹 서버 자체에서 HTTP 세션을 추상화할 수 있습니다.
이에 대한 일반적인 솔루션은 Redis 및 Memcached 와 같은 메모리 내 키/값 저장소를
활용하는 것입니다. 메모리 내 키/값 저장소용 ElastiCache 제품에는 복제를 지원할 수
있는 Redis 용 ElastiCache 와 복제를 지원하지 않는 Memcached 용 ElastiCache 가
포함됩니다.
설명2:
A(O) : 분산 세션 관리 : 확장성을 해결하고 개별 웹 서버에서 액세스할 수 있는 세션에
대한 공유 데이터 저장소를 제공하기 위해 웹 서버 자체에서 HTTP 세션을 추상화할 수
있습니다. 이에 대한 일반적인 솔루션은 Redis 및 Memcached 와 같은 메모리 내 키/값
저장소 를 활용하는 것 입니다.
https://aws.amazon.com/ko/caching/session-management/
Redis 용 Amazon ElastiCache 는 사용자 인증 토큰, 세션 상태 등 세션 정보를 관리하는
세션 스토어로 사용하기에 매우 적합합니다. Redis 용 Amazon ElastiCache 를 세션 키에
대한 적절한 TTL과 함께 빠른 키-값 스토어로 사용하면 세션 정보를 관리할 수 있습니다.
https://aws.amazon.com/ko/elasticache/redis/?nc=sn&loc=2&dn=1#Session_Store
B(X) : EC2 인스턴스는 하루 종일 자주 확장 및 축소된다고 했는데 Session Affinity(=Sticky
Session)은 이에 맞지 않음. ""개별 노드에 세션 저장을 사용할 때의 단점은 장애가 발생할
경우 장애가 발생한 노드에 있던 세션이 손실될 가능성이 있다는 것입니다. 또한 웹 서버
수가 변경되는 경우(예: 확장 시나리오) 활성 세션이 특정 서버에 존재할 수 있으므로
트래픽이 웹 서버 전체에 불균등하게 분산될 수 있습니다.
https://aws.amazon.com/ko/caching/session-management/
C(X) : Session Manager 는 접속 서비스이지 데이터 관리 서비스가 아님. Session
Manager 는 인바운드 포트를 열거나, 배스천 호스트를 유지하거나, SSH 키를 관리할 필요
없이 안전하고 감사 가능한 노드 관리를 제공
https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html
D(X) : STS 는 임시 보안 자격 증명 서비스. ""AWS Security Token Service(AWS STS)를
사용하면 AWS 리소스에 대한 액세스를 제어할 수 있는 임시 보안 자격 증명을 생성하여
신뢰받는 사용자에게 제공할 수 있습니다.
https://docs.aws.amazon.com/ko_kr/IAM/latest/UserGuide/id_credentials_temp.html

---

# Q210 

**정답: D**

https://www.examtopics.com/discussions/amazon/view/94992-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
Auto Scaling 그룹의 인스턴스 수는 메시지를 처리하는 데 걸리는 시간과 허용 가능한 지연
시간(대기열 지연)에 따라 결정될 수 있습니다. 해결책은 유지 관리할 인스턴스당 허용
가능한 백로그인 대상 값과 함께 인스턴스 메트릭당 백로그를 사용하는 것입니다.
설명2:
A. 이 접근 방식은 CPU 사용률에만 초점을 맞추므로 주문 수집 및 이행 프로세스의 확장
요구 사항을 정확하게 반영하지 못할 수 있습니다. 분리 및 신뢰할 수 있는 메시지 처리에
대한 요구 사항은 다루지 않습니다.
B. 이 접근 방식은 경보를 통합하여 추가 Auto Scaling 그룹을 트리거하지만 SQS 대기열을
사용하여 제공되는 분리 및 안정적인 메시지 처리가 부족합니다. 비효율적인 확장 및
잠재적인 데이터 손실이 발생할 수 있습니다.
C. SQS 대기열을 사용하는 것이 올바른 방향으로 나아가는 단계이지만 대기열 알림만을
기준으로 확장하는 것은 최적의 리소스 활용을 제공하지 못할 수 있습니다. 인스턴스당
백로그를 고려하지 않으며 조정에 대한 세밀한 제어를 허용하지 않습니다.
전반적으로 주문 수집 및 이행을 위해 SQS 대기열을 사용하고, 인스턴스 계산당 백로그를
기반으로 메트릭을 생성하고, 이에 따라 Auto Scaling 그룹을 확장하는 옵션 D 는 리소스
활용을 최적화하고 보장하면서 확장 문제를 해결하는 가장 적합한 솔루션입니다. 신뢰할 수
있는 메시지 처리

---

# Q211 

**정답: D**

https://www.examtopics.com/discussions/amazon/view/95145-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
CloudTrail 은 주로 API 활동 캡처 및 로깅에 중점을 두기 때문에 A 는 가장 빠른 솔루션이
아닙니다. 리소스 변경에 대한 정보를 제공할 수 있지만 여러 서비스 및 리전에서 태그가
지정된 모든 구성 요소를 식별하는 포괄적이고 빠른 방법을 제공하지 않을 수 있습니다.
B 에는 AWS CLI 를 사용하여 각 서비스를 수동으로 쿼리하는 작업이 포함되며, 이는 특히
여러 서비스 및 리전을 처리할 때 시간이 많이 걸리고 번거로울 수 있습니다. 태그가
지정된 구성 요소를 빠르게 식별하기 위한 가장 효율적인 솔루션은 아닙니다.
C 는 태그가 지정된 구성 요소를 직접 식별하기보다는 로그 분석에 중점을 둡니다.
CloudWatch Logs Insights 는 로그에서 정보를 추출하는 데 도움이 될 수 있지만 여러
서비스 및 리전에서 태그가 지정된 모든 구성 요소의 통합 목록을 수집하는 간단하고 빠른
방법을 제공하지 않을 수 있습니다.
D는 태그를 기반으로 리소스를 관리하고 구성하도록 특별히 설계된 Resource Groups Tag
Editor 를 활용하므로 가장 빠른 솔루션입니다. 여러 서비스 및 리전에서 태그가 지정된
구성 요소에 대한 보고서를 생성하는 중앙 집중식의 효율적인 접근 방식을 제공합니다.
참고:
https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html

---

# Q212 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/95300-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
옵션 A 는 액세스 패턴이 변화하는 개체를 위해 설계되었지만 특히 액세스 패턴이
가변적이고 빠르게 변경되는 경우 데이터의 장기 저장을 위한 가장 비용 효율적인 솔루션이
아닐 수 있습니다.
옵션 B 는 장기 아카이브 저장에 최적화되어 있으며 회사에서 요구하는 즉각적인 액세스를
제공하지 않을 수 있습니다. Glacier 스토리지에서 데이터를 검색하면 일반적으로 다른
스토리지 클래스에 비해 검색 시간이 더 오래 걸립니다.
옵션 C 는 즉각적인 가용성과 데이터에 대한 빠른 액세스를 위한 적절한 선택입니다. 높은
내구성, 가용성 및 낮은 대기 시간 액세스를 제공하므로 회사의 요구 사항에 적합합니다.
그러나 장기 보관을 위한 가장 비용 효율적인 옵션은 아닙니다.
옵션 D 는 특히 자주 액세스하지 않는 데이터의 경우 S3 Standard 에 비해 비용 효율적인
스토리지 클래스입니다. 그러나 데이터에 대한 액세스 패턴이 가변적이고 빠르게 변경되기
때문에 S3 Standard-IA 는 빈번한 액세스에 대한 추가 검색 비용이 발생하므로 가장 비용
효율적인 솔루션이 아닐 수 있습니다.

---

# Q213 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/95301-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
솔루션 설계자는 AWS WAF 규칙을 구성하고 이를 ALB 와 연결하는 옵션 A 를 권장해야
합니다. 이를 통해 회사는 교차 사이트 스크립팅 또는 SQL 주입과 같은 일반적인
애플리케이션 수준 공격으로부터 ALB를 보호하는 데 필요한 애플리케이션 계층에서 트래픽
필터링을 적용할 수 있습니다. AWS WAF는 애플리케이션 가용성에 영향을 미치거나 보안을
손상시키거나 과도한 리소스를 소비할 수 있는 일반적인 웹 익스플로잇으로부터 웹
애플리케이션을 쉽게 보호할 수 있게 해주는 관리형 서비스입니다. 회사는 애플리케이션의
보안을 보장하기 위해 규칙을 쉽게 관리하고 업데이트할 수 있습니다.
설명2:
AWS WAF 규칙을 구성하고 이를 ALB 와 연결함으로써 회사는 악성 트래픽이
애플리케이션에 도달하기 전에 필터링하고 차단할 수 있습니다. AWS WAF 는 사전 구성된
규칙 세트를 제공하고 사용자 지정 규칙 생성을 허용하여 XSS 및 SQL 주입과 같은
일반적인 취약성으로부터 보호합니다.
옵션 B 는 애플리케이션 수준 공격으로부터 보호하는 데 필요한 보안 및 트래픽 필터링
기능을 제공하지 않습니다. 보안 조치를 구현하는 것보다 정적 콘텐츠를 호스팅하는 데 더
적합합니다.
옵션 C 는 XSS 또는 SQL 주입과 같은 애플리케이션 수준 공격이 아닌 DDoS 보호에
중점을 둡니다. AWS Shield Advanced 는 시나리오에 언급된 특정 요구 사항을 다루지
않습니다.
옵션 D 는 추가 인프라를 유지하고 보호하는 것과 관련되며, 이는 책임을 줄이고 최소한의
운영 직원에 의존해야 한다는 요구 사항에 위배됩니다.

---

# Q214 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/95154-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
AWS Glue는 분석을 위해 데이터를 준비하고 변환하는 프로세스를 간소화하는 완전 관리형
ETL 서비스입니다. AWS Glue 를 사용하려면 다른 옵션에 비해 최소한의 개발 노력이
필요합니다.
옵션 A는 데이터 변환을 위한 Spark 애플리케이션 작성과 관련되므로 더 많은 개발 노력이
필요합니다. 또한 EMR 클러스터로 추가 인프라 관리를 소개합니다.
옵션 C 는 데이터 변환을 위한 사용자 지정 Bash 스크립트를 작성하고 관리해야 합니다.
수동 작업이 더 많이 필요하며 데이터 변환을 위한 AWS Glue 의 내장 기능을 제공하지
않습니다.
옵션 D 는 데이터 변환을 위해 사용자 지정 Lambda 를 개발하고 관리해야 합니다.
Lambda는 변환을 처리할 수 있지만 ETL 작업을 위해 특별히 설계된 AWS Glue에 비해 더
많은 노력이 필요합니다.
따라서 옵션 B 는 AWS Glue 의 데이터 검색, 변환 및 변환된 데이터 버킷으로의 출력
기능을 활용하여 가장 쉽고 최소한의 개발 노력을 제공합니다.
참고:
https://docs.aws.amazon.com/ko_kr/prescriptive-guidance/latest/patterns/three-aws-glu
e-etl-job-types-for-converting-data-to-apache-parquet.html

---

# Q215 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/94983-exam-aws-certified-solut
ions-architect-associate-saa-c03/
해설:
700TB 나 되는 대용량을 Snowball Edge Device 를 사용하지 않고 네트워크 상으로 옮기는
것은 굉장히 많은 시간이 소요됨.
https://kindloveit.tistory.com/68
https://www.omnicalculator.com/other/data-transfer

---

# Q216 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/95040-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
S3 에서 기본 암호화 설정을 활성화하면 새로 추가된 모든 객체가 자동으로 암호화됩니다.
기존 객체를 암호화하기 위해 S3 Inventory 기능을 사용하여 암호화되지 않은 객체 목록을
생성할 수 있습니다. 그런 다음 암호화를 적용하는 동안 해당 객체를 복사하기 위해 S3
배치 작업 작업을 실행할 수 있습니다.
A. 이 솔루션에는 새 S3 를 생성하고 모든 기존 개체를 수동으로 다운로드 및 업로드하는
작업이 포함됩니다. 수백만 개의 개체를 전송하는 데 상당한 노력과 시간이 필요하므로
효율성이 떨어지는 솔루션입니다.
C. AWS KMS 로 SSE 를 활성화하는 것은 S3 에서 객체를 암호화하는 유효한 접근
방식이지만 기존 객체를 암호화해야 하는 요구 사항을 해결하지는 않습니다. 버킷에 추가된
새 객체에만 암호화를 적용합니다.
D. 기본 암호화 설정을 적용하기 위해 S3 의 각 개체를 수동으로 수정하는 것은 노동
집약적이고 오류가 발생하기 쉬운 프로세스입니다. 암호화되지 않은 각 개체를 개별적으로
선택하고 수정해야 하므로 많은 수의 개체에 비실용적입니다.
참고:
https://spin.atomicobject.com/2020/09/15/aws-s3-encrypt-existing-objects/

---

# Q217 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/95015-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
솔루션은 기본 인프라가 정상일 때 부하를 처리할 필요가 없다고 했으므로 Active/Passive
Failover를 사용하면 됨. 따라서 A,D 둘 중 하나가 답.
A(O) : Q: Amazon Aurora는 교차 리전 복제를 지원하나요? 예. 물리적 또는 논리적 복제를
사용하여 교차 리전 Aurora 복제본을 설정할 수 있습니다. Amazon RDS 콘솔에서 교차
리전 복제본을 새로운 기본 복제본으로 승격할 수 있습니다. 논리적(binlog) 복제의 경우,
승격 프로세스는 워크로드에 따라 다르지만 보통 몇 분 정도 걸립니다. 승격 프로세스를
시작하면 교차 리전 복제가 중단됩니다. https://aws.amazon.com/ko/rds/aurora/faqs/
D(X) : 굳이 AWS Backup 을 사용하지 않아도 오로라 교차 리전 복제본 (Aurora Cross
Region Replica)를 사용하면 됨. 그리고 글로벌 웹 애플리케이션을 사용한다고 했는데 이런
경우엔 데이터를 복제해 인스턴스를 다른 리전에 생성하는 것보단 복제본을 사용해서 각
지역에서 읽기 쿼리를 할 때 지연시간을 줄이는 것이 더 좋음.
참고:
https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-types.html

---

# Q218 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/95056-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
포트 443 의 모든 위치에서 웹 서버에 액세스할 수 있도록 하는 작업을 수행하는 단계
조합은 소스 0.0.0.0/0(A)에서 TCP 포트 443 을 허용하고 네트워크 ACL 을 업데이트하는
규칙으로 보안 그룹을 생성하는 것입니다. 소스 0.0.0.0/0(C)에서 인바운드 TCP 포트
443을 허용합니다.
이렇게 하면 포트 443 에 대한 트래픽이 보안 그룹 수준과 네트워크 ACL 수준 모두에서
허용되어 포트 443의 모든 위치에서 웹 서버에 액세스할 수 있습니다.

---

# Q219 

**정답: D**

https://www.examtopics.com/discussions/amazon/view/95162-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
M5 인스턴스를 메모리 집약적인 워크로드에 최적화된 R5 인스턴스로 교체하면
애플리케이션에서 메모리 용량과 성능을 높일 수 있습니다.
또한 EC2 인스턴스에 CloudWatch 에이전트를 배포하면 애플리케이션 성능에 대한 중요한
통찰력을 제공할 수 있는 사용자 지정 애플리케이션 대기 시간 메트릭을 생성할 수
있습니다.
이 솔루션은 적절한 인스턴스 유형을 활용하고 더 나은 모니터링 및 향후 용량 계획을 위해
사용자 지정 애플리케이션 메트릭을 수집하여 성능 문제를 효율적으로 해결합니다.
A. T3 인스턴스로 교체하면 인 메모리 작업에 충분한 메모리 용량을 제공하지 못할 수
있습니다.
B. ASG의 용량을 수동으로 늘리면 성능 문제가 직접적으로 해결되지 않습니다.
C. 내장된 EC2 메모리 메트릭에만 의존하면 메모리 내 작업을 최적화하는 데 충분한
세분성을 제공하지 못할 수 있습니다.
가장 효율적인 솔루션은 CloudFormation 템플릿을 수정하고, R5 인스턴스로 교체하고,
사용자 지정 메트릭을 위해 CloudWatch 에이전트를 배포하는 것입니다.

---

# Q220 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/95306-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
API Gateway + Lambda는 서버리스 아키텍처를 사용하는 최신 애플리케이션을 위한 완벽한
솔루션입니다.
설명2:
Lambda 는 요청을 비동기식으로 처리하기 위해 API Gateway 에서 트리거할 수 있는
서버리스 컴퓨팅 서비스입니다. 들어오는 요청 볼륨에 따라 자동으로 확장되며 요청을
처리하는 데 사용된 실제 컴퓨팅 시간에 대해서만 요금을 부과하여 비용 최적화를
허용합니다.
A. Glue 는 완전히 관리되는 ETL 서비스입니다. API 요청을 제공하는 대신 데이터 처리 및
변환 작업을 위해 설계되었습니다. 가변적인 요청량을 처리하고 몇 초 내에 응답을
전달하는 데 적합하지 않을 수 있습니다.
C. EKS 는 확장성과 유연성을 제공하지만 가변적인 API 요청 볼륨을 처리하기 위해
인프라를 관리하고 확장하는 데 추가적인 복잡성과 오버헤드가 발생할 수 있습니다.
D. 이전 옵션과 마찬가지로 EC2 와 함께 ECS 를 사용하려면 인프라 관리 및 확장을 위한
추가 노력이 필요하며, 이는 간헐적이고 가변적인 API 요청 볼륨을 처리하는 데 필요하지
않을 수 있습니다.

---

# Q221 

**정답: D**

https://www.examtopics.com/discussions/amazon/view/95307-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
A. EBS 는 EC2 인스턴스와 함께 사용할 블록 수준 스토리지 볼륨을 제공합니다. 내구성과
지속성을 제공하지만 로그 파일의 장기 보존을 위한 가장 비용 효율적인 솔루션은 아닙니다.
또한 이 시나리오의 요구 사항인 파일에 대한 동시 액세스를 제공하지 않습니다.
B. EFS 는 여러 EC2 인스턴스에 동시에 탑재할 수 있는 확장 가능한 파일 스토리지
서비스입니다. 파일에 대한 동시 액세스를 제공하지만 S3 에 비해 가격이 높기 때문에 장기
보존을 위한 가장 비용 효율적인 옵션이 아닐 수 있습니다.
C. 인스턴스 스토어는 EC2 인스턴스에 물리적으로 연결된 임시 스토리지 옵션입니다. 규정
준수 목적에 필요한 내구성 및 장기 보존을 제공하지 않습니다. 또한 인스턴스 스토어는
연결된 특정 EC2 인스턴스 외부에서 액세스할 수 없으므로 보고 도구를 통한 동시
액세스가 불가능합니다.
따라서 장기보존, 동시접속, 가성비 등의 요구사항을 고려할 때 S3가 가장 적합하고 가성비
좋은 스토리지 솔루션입니다.
참고:
https://docs.aws.amazon.com/efs/latest/ug/transfer-data-to-efs.html

---

# Q222 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/95160-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
IAM 역할을 생성하고 공급업체의 IAM 역할에 대한 액세스 권한을 위임함으로써 계정 간에
신뢰 관계를 설정합니다. 이렇게 하면 공급업체의 자동화 도구가 회사 계정의 역할을 맡고
필요한 리소스에 액세스할 수 있습니다.
적절한 IAM 정책을 역할에 연결하면 해당 도구가 작업을 수행하는 데 벤더가 요구하는
정확한 권한을 정의할 수 있습니다. 이렇게 하면 공급업체가 회사 계정에 대한 직접적인
IAM 액세스 권한을 부여하지 않고도 필요한 액세스 권한을 가질 수 있습니다.
B 는 암호가 있는 IAM 사용자를 생성하려면 벤더와 자격 증명을 공유해야 하므로 보안상의
이유로 권장되지 않습니다.
공급업체의 IAM 사용자를 회사 계정의 IAM 그룹에 추가하면 공급업체 도구에 대한
액세스를 위임하는 직접적이고 통제된 방법을 제공하지 않기 때문에 C 는 올바르지
않습니다.
공급업체의 AWS 계정에 대한 새 자격 증명 공급자를 생성하면 공급업체 도구에 대한
액세스 권한을 위임하는 간단한 방법이 제공되지 않기 때문에 D는 틀렸습니다. ID 공급자는
일반적으로 외부 ID 시스템을 사용하는 연합 액세스에 사용됩니다.
참고:
https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_third-p
arty.html

---

# Q223 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/95310-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
A. IAM 역할을 EKS 포드에 연결하면 포드가 DynamoDB 에 액세스하는 데 필요한 권한을
부여할 수 있습니다. IAM 역할에는 DynamoDB 테이블에 대한 액세스를 허용하는 적절한
정책이 있어야 합니다.
D. DynamoDB용 VPC 엔드포인트를 생성하면 EKS 포드가 인터넷 연결 없이도 VPC 내에서
비공개로 DynamoDB 에 액세스할 수 있습니다. VPC 엔드포인트는 DynamoDB 에 대한
직접적이고 안전한 연결을 제공하므로 트래픽이 인터넷을 통해 흐를 필요가 없습니다.
B 는 IAM 사용자를 포드에 연결하는 것이 권장되는 접근 방식이 아니기 때문에 올바르지
않습니다. IAM 사용자는 AWS Management Console 또는 AP 를 통해 AWS 서비스에
액세스하기 위한 것입니다.
네트워크 ACL 을 통한 아웃바운드 연결 구성은 DynamoDB 에 대한 안전하고 직접적인
연결을 제공하지 않기 때문에 C는 올바르지 않습니다.
코드에 액세스 키를 포함하는 것은 권장되는 보안 방법이 아니기 때문에 E 는 올바르지
않습니다. 잠재적인 보안 취약성이 발생할 수 있습니다. AWS 서비스에 대한 액세스를
제공하기 위해 IAM 역할 또는 기타 보안 메커니즘을 사용하는 것이 좋습니다.
참고
https://docs.aws.amazon.com/ko_kr/amazondynamodb/latest/developerguide/vpc-endpo
ints-dynamodb.html
https://aws.amazon.com/ko/about-aws/whats-new/2019/09/amazon-eks-adds-support
-to-assign-iam-permissions-to-kubernetes-service-accounts/

---

# Q224 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/95311-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
C. Route 53 의 다중 응답 라우팅 정책을 사용하면 DNS 레코드에 대한 다중 값을 구성할
수 있으며 Route 53 은 다중 임의 값으로 DNS 쿼리에 응답합니다. 이를 통해 사용 가능한
EC2 인스턴스 간에 트래픽을 무작위로 분산할 수 있습니다.
E. 다른 AZ 에서 EC2 인스턴스를 시작하면 고가용성과 내결함성을 얻을 수 있습니다.
4 개의 인스턴스(각 AZ 에 2 개)를 시작하면 트래픽 로드를 처리하고 원하는 수준의
가용성을 유지하기에 충분한 리소스가 있습니다.
A. 장애 조치 라우팅은 기본 리소스 또는 위치를 사용할 수 없는 경우에만 트래픽을 백업
리소스 또는 보조 위치로 보내도록 설계되었습니다.
B. 가중 라우팅 정책을 사용하면 여러 EC2 인스턴스에 트래픽을 분산할 수 있지만 무작위
분산이 보장되지는 않습니다.
D. 여러 AZ 에서 인스턴스를 시작하는 것은 내결함성을 위해 중요하지만 세 개의
인스턴스만 있으면 트래픽이 고르게 분산되지 않습니다. 인스턴스가 3 개뿐이면 트래픽이
고르게 분산되지 않아 리소스 활용이 불균형해질 수 있습니다.
참고
https://aws.amazon.com/premiumsupport/knowledge-center/multivalue-versus-simple-p
olicies/

---

# Q225 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/94985-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
Amazon Redshift는 클라우드에서 완벽하게 관리되는 페타바이트 규모의 데이터 웨어하우스
서비스입니다. 수백 기가바이트의 데이터로 시작하여 페타바이트 이상으로 확장할 수
있습니다. 이를 통해 데이터를 사용하여 비즈니스와 고객에 대한 새로운 통찰력을 얻을 수
있습니다. 데이터 웨어하우스를 생성하는 첫 번째 단계는 Amazon Redshift 클러스터라는
노드 집합을 시작하는 것입니다. 클러스터를 프로비저닝한 후 데이터 세트를 업로드한 다음
데이터 분석 쿼리를 수행할 수 있습니다. 데이터 세트의 크기에 관계없이 Amazon
Redshift 는 오늘날 사용하는 것과 동일한 SQL 기반 도구 및 비즈니스 인텔리전스
애플리케이션을 사용하여 빠른 쿼리 성능을 제공합니다.
설명2:
B 는 데이터 수집 및 분석을 위한 완전히 관리되고 확장 가능한 솔루션을 제공합니다.
KDF 는 대량의 스트리밍 데이터를 처리하도록 자동으로 확장하여 데이터 수집 프로세스를
간소화합니다. 강력하고 완전히 관리되는 데이터 웨어하우징 솔루션인 Redshift 클러스터에
데이터를 직접 로드할 수 있습니다.
A. Kinesis 는 스트리밍 데이터를 처리할 수 있지만 분석 솔루션에 데이터를 로드하려면
추가 처리가 필요합니다.
C. S3 및 Lambda 가 데이터 저장 및 처리를 처리할 수 있지만 KDF 및 Redshift 가
제공하는 완전관리형 솔루션에 비해 수동 구성 및 관리가 더 많이 필요합니다.
D. 이 옵션은 EC2 인스턴스 및 RDS 데이터베이스 인프라를 수동으로 관리하고 확장해야
하므로 더 많은 운영 오버헤드가 필요합니다.
따라서 Redshift 클러스터에 데이터를 제공하는 KDF 가 포함된 옵션 B 는 주어진
시나리오에서 사용자 활동 데이터를 수집하고 분석하기 위한 가장 간소화되고 운영상
효율적인 솔루션을 제공합니다.

---

# Q226 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/95312-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
"RESTful 웹 서비스" => API 게이트웨이.
"EC2 인스턴스는 원시 데이터를 수신하고, 원시 데이터를 변환하고, 모든 데이터를
Amazon S3 버킷에 저장합니다."
=> (Extract - Transform - Load)가 있는 GLUE
설명2:
A. 데이터의 스키마를 자동으로 발견하고 ETL 코드를 생성하여 변환합니다.
E. API Gateway 는 RESTful 웹 서비스를 통해 원격 장치에서 원시 데이터를 수신하는 데
사용할 수 있습니다. 들어오는 요청을 처리하기 위해 확장 가능하고 관리되는 인프라를
제공합니다. 그런 다음 데이터를 확장성과 내구성이 뛰어난 실시간 데이터 스트리밍
서비스인 Amazon Kinesis 데이터 스트림으로 보낼 수 있습니다. 여기에서 데이터 스트림을
소스로 사용하고 변환된 데이터를 Amazon S3 에 전달하도록 Amazon Kinesis Data
Firehose를 구성할 수 있습니다. 이러한 서비스 조합을 통해 운영 오버헤드를 최소화하면서
원활한 데이터 수집 및 처리가 가능합니다.
B. 확장 가능한 데이터 처리 및 저장의 필요성을 직접적으로 다루지는 않습니다. DNS 관리
및 트래픽을 다른 끝점으로 라우팅하는 데 중점을 둡니다.
C. 더 많은 EC2 를 추가하면 인스턴스 관리 및 확장 측면에서 운영 오버헤드가 증가할 수
있습니다.
D. 데이터 처리에 SQS 및 EC2를 사용하면 더 복잡해지고 운영 오버헤드가 발생합니다.

---

# Q227 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/95314-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
이전 버전과 현재 버전을 삭제하도록 S3 수명 주기 정책을 구성하면 이전 버전의
CloudTrail 로그가 삭제됩니다. 이렇게 하면 3 년 이상 된 객체가 S3 버킷에서 제거되어
객체 수를 줄이고 스토리지 비용을 제어할 수 있습니다.
A. 이 옵션은 S3 의 개체 관리와 직접적인 관련이 없습니다. S3 버킷에서 객체를 삭제해야
하는 필요성을 해결하지 못할 수 있는 CloudTrail 추적 만료 구성에 중점을 둡니다.
C. Lambda를 생성하여 3년 이상 된 객체를 삭제하는 것은 기술적으로 가능하지만 이 접근
방식은 복잡성과 운영 오버헤드를 추가로 도입합니다.
D. S3 버킷에 있는 객체의 소유권을 변경해도 3년 이상 된 객체를 삭제해야 하는 필요성이
직접적으로 해결되지는 않습니다. 소유권은 개체의 삭제 동작에 영향을 주지 않습니다.
참고:
https://docs.aws.amazon.com/ko_kr/awscloudtrail/latest/userguide/best-practices-securi
ty.html

---

# Q228 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/95318-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
Amazon SQS 를 사용하면 API 가 데이터를 데이터베이스에 직접 쓰지 않고 대기열에 쓰기
때문에 데이터베이스에 대한 연결 수를 최소화하는 데 도움이 됩니다. 또한 대기열에서
데이터베이스로 데이터를 쓰기 위해 Amazon SQS 가 호출하는 AWS Lambda 함수를
사용하면 대기열이 API 와 데이터베이스 사이에서 버퍼 역할을 하므로 트래픽이 많은 기간
동안 데이터가 손실되지 않도록 하는 데 도움이 됩니다.
설명2:
SQS 를 버퍼로 활용하고 Lambda 를 사용하여 큐에서 데이터베이스로 데이터를 처리하고
기록함으로써 이 솔루션은 데이터베이스에 대한 연결 수를 최소화하면서 확장성, 분리 및
안정성을 제공합니다. 이 접근 방식은 트래픽 변동을 처리하고 트래픽이 많은 기간 동안
데이터 무결성을 보장합니다.
A. DB 인스턴스의 크기를 늘리면 더 많은 메모리를 제공할 수 있지만 높은 쓰기 트래픽을
효율적으로 처리하고 데이터베이스에 대한 연결을 최소화하는 문제는 해결되지 않습니다.
B. DB 인스턴스를 다중 AZ 인스턴스로 수정하고 모든 활성 인스턴스에 쓰면 가용성이
향상될 수 있지만 높은 쓰기 트래픽을 효율적으로 처리하고 데이터베이스에 대한 연결을
최소화하는 문제는 해결되지 않습니다.
D. SNS와 Lambda를 사용하면 디커플링과 확장성을 제공할 수 있지만 많은 쓰기 트래픽을
효율적으로 처리하고 데이터베이스에 대한 연결을 최소화하는 데 적합하지 않습니다.

---

# Q229 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/95319-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
데이터베이스를 Aurora Serverless 로 마이그레이션하면 자동 조정 및 복제 기능이
제공됩니다. Aurora Serverless는 워크로드에 따라 자동으로 용량을 조정하므로 필요에 따라
컴퓨팅 용량을 원활하게 추가하거나 제거할 수 있습니다. 또한 복제 및 확장을 수동으로
관리할 필요 없이 향상된 성능, 내구성 및 고가용성을 제공합니다.
B. 호환성 문제가 발생할 수 있고 중요한 코드 수정이 필요할 수 있는 다른 데이터베이스
엔진으로의 마이그레이션을 제안하기 때문에 올바르지 않습니다.
C. 더 큰 EC2 인스턴스에서 더 큰 MySQL 데이터베이스로 통합하면 원하는 확장성과
자동화가 제공되지 않기 때문에 올바르지 않습니다.
D. 데이터베이스 계층에 대해 EC2 Auto Scaling 그룹을 사용하려면 여전히 복제 및 조정을
수동으로 관리해야 하기 때문에 올바르지 않습니다.
참고:
https://aws.amazon.com/rds/aurora/serverless/

---

# Q230 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/95322-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
여러 가용 영역에 리소스가 있고 하나의 NAT 게이트웨이를 공유하는 경우 NAT
게이트웨이의 가용 영역이 다운되면 다른 가용 영역의 리소스가 인터넷에 액세스할 수 없게
됩니다. 가용 영역 독립적 아키텍처를 생성하려면 각 가용 영역에 NAT 게이트웨이를
생성하고 리소스가 동일한 가용 영역에서 NAT 게이트웨이를 사용하도록 라우팅을
구성합니다.
https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html#nat-gateway
-basics
설명2:
이 권장 사항은 NAT 게이트웨이를 여러 AZ 에 분산하여 고가용성과 내결함성을 보장합니다.
NAT 게이트웨이는 확장 가능하고 가용성이 높은 아웃바운드 NAT 기능을 제공하는 관리형
AWS 서비스입니다. 서로 다른 AZ 에 NAT 게이트웨이를 배포함으로써 회사는 중복성을
확보하고 단일 장애 지점을 방지할 수 있습니다. 또한 이 솔루션은 수동 개입 없이
증가하는 트래픽을 처리할 수 있는 자동 크기 조정을 제공합니다.
두 NAT 게이트웨이를 동일한 가용 영역에 배치하면 내결함성이 제공되지 않으므로 옵션
A는 올바르지 않습니다.
옵션 B 는 Network Load Balancer 와 함께 Auto Scaling 그룹을 사용하는 것이 NAT
인스턴스에 권장되는 접근 방식이 아니기 때문에 올바르지 않습니다.
옵션 D 는 스팟 인스턴스가 NAT 인스턴스와 같은 중요한 인프라 구성 요소에 적합하지
않기 때문에 올바르지 않습니다.

---

# Q231 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/95323-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
VPC 피어링 연결은 사용자가 프라이빗 IP 주소를 사용하여 트래픽을 라우팅할 수 있도록
하는 두 VPC 간의 네트워킹 연결입니다. 각 VPC의 인스턴스는 마치 동일한 네트워크 내에
있는 것처럼 서로 통신할 수 있습니다. VPC 피어링 연결은 같거나 다른 AWS 계정과
Regions1 의 VPC 간에 생성할 수 있습니다. 솔루션은 VPC A 와 VPC B 간에 VPC 피어링
연결을 구성하여 필요한 액세스를 가장 안전하게 제공할 수 있습니다.
1. VPC A 에 있는 애플리케이션 서버의 퍼블릭 IP 주소에서 오는 모든 트래픽을 허용하는
DB 인스턴스 보안 그룹을 생성합니다. 이 솔루션은 DB 인스턴스를 퍼블릭 인터넷에
노출하고 액세스 제어를 위한 단일 IP 주소.
2. DB 인스턴스를 공개적으로 액세스할 수 있도록 합니다. 퍼블릭 IP 주소를 DB
인스턴스에 할당합니다. 이 솔루션은 DB 인스턴스를 퍼블릭 인터넷에 노출하고 모든
소스에 연결할 수 있도록 허용하므로 필요한 액세스를 가장 안전하게 제공하지 않습니다.
3. 탄력적 IP 주소가 있는 EC2 인스턴스를 VPC B 로 시작합니다. 새 EC2 인스턴스를 통해
모든 요청을 프록시합니다. 이 솔루션은 대기 시간과 복잡성을 유발할 수 있는 추가 리소스
생성 및 프록시 서버 구성과 관련되므로 필요한 액세스를 가장 안전하게 제공하지
않습니다.
참조 URL: https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html
설명2:
VPC A 와 VPC B 간에 VPC 피어링 연결을 구성하면 VPC A 의 EC2 인스턴스와 VPC B 의
데이터베이스 간에 비공개 보안 통신을 설정할 수 있습니다. 공용 IP 주소가 필요하거나
데이터베이스를 인터넷에 노출해야 합니다.
옵션 A 는 덜 안전할 수 있는 응용 프로그램 서버의 공용 IP 주소에서 오는 모든 트래픽을
허용해야 하므로 최상의 솔루션이 아닙니다.
옵션 C 는 DB 인스턴스를 공개적으로 액세스 가능하게 만드는 것과 관련이 있으며, 이는
데이터베이스를 인터넷에 직접 노출함으로써 보안 위험을 초래합니다.
옵션 D 는 VPC B 에서 추가 EC2 인스턴스를 시작하고 이를 통해 모든 요청을 프록시하여
불필요한 복잡성을 추가합니다. 이는 이 시나리오에서 가장 효율적이고 안전한 접근 방식이
아닙니다.

---

# Q232 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/95324-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
CloudWatch Logs 에 VPC 흐름 로그를 게시하고 RDP 또는 SSH 액세스를 감지하는 지표
필터를 생성함으로써 운영 팀은 경보가 트리거될 때 이를 알리도록 CloudWatch 지표
경보를 구성할 수 있습니다. 이렇게 하면 환경에 대한 RDP 또는 SSH 액세스가 설정될 때
원하는 알림이 제공됩니다.
CloudWatch Application Insights 는 RDP 또는 SSH 액세스를 감지하도록 설계되지 않았기
때문에 옵션 A는 올바르지 않습니다.
옵션 B 도 올바르지 않습니다. AmazonSSMManagedInstanceCore 정책으로 IAM 인스턴스
프로필을 구성하면 RDP 또는 SSH 액세스가 발생할 때 운영 팀에 알려야 하는 요구
사항이 직접 해결되지 않기 때문입니다.
EC2 인스턴스 상태 변경 알림 이벤트를 수신하도록 EventBridge 규칙을 구성하고 SNS
주제를 대상으로 사용하면 운영 팀에 인스턴스 시작 또는 중지와 같은 인스턴스 상태 변경
사항을 알릴 수 있으므로 옵션 D 는 잘못된 것입니다. 그러나 질문에 명시된 요구 사항인
RDP 또는 SSH 액세스가 설정된 시기를 구체적으로 감지하거나 알리지는 않습니다.
참고:
https://aws.amazon.com/blogs/security/how-to-monitor-and-visualize-failed-ssh-acce
ss-attemptsto-amazon-ec2-linux-instances/

---

# Q233 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/95084-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
A. 루트 사용자에 대해 강력한 암호를 설정하는 것은 무단 액세스를 방지하기 위한 필수
보안 조치입니다.
B. MFA 를 활성화하면 암호 외에 모바일 앱의 코드 또는 하드웨어 토큰과 같은 추가 인증
요소를 요구하여 추가 보안 계층을 추가합니다.
C. 루트 사용자 액세스 키는 가능하면 피해야 하며 대신 권한이 제한된 IAM 사용자를
사용하는 것이 가장 좋습니다.
D. 루트 사용자는 이미 계정의 모든 리소스 및 서비스에 대한 무제한 액세스 권한을
가지고 있으므로 추가 관리 권한을 부여하면 무단 작업의 위험이 높아질 수 있습니다.
E. 대신 적절한 권한을 가진 IAM 사용자를 생성하고 해당 사용자를 일상적인 작업에
사용하는 동시에 루트 사용자를 보호하고 필요한 관리 작업에만 사용하는 것이 좋습니다.
설명2:
https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html
https://docs.aws.amazon.com/accounts/latest/reference/best-practices-root-user.html
* AWS 계정 루트 사용자에서 AWS Multi-Factor Authentication(MFA)을 활성화합니다.
자세한 내용은 IAM 사용 설명서의 AWS에서 멀티 팩터 인증(MFA) 사용을 참조하십시오.
* AWS 계정 루트 사용자 암호 또는 액세스 키를 누구와도 공유하지 마십시오.
* 강력한 암호를 사용하여 AWS Management Console에 대한 액세스를 보호하십시오. AWS
계정 루트 사용자 암호 관리에 대한 자세한 내용은 루트 사용자 암호 변경 단원을
참조하십시오.

---

# Q234 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/95325-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
이 옵션은 AWS Key Management Service(AWS KMS)를 사용하기 때문에 가장 효율적입니다.
이 서비스는 암호화 키를 쉽게 생성 및 관리하고 다양한 AWS 서비스와 실행 중인
애플리케이션에서 키 사용을 제어할 수 있게 해줍니다. AWS 에서. 또한 AWS KMS 를
사용하여 EBS 볼륨과 유휴 Aurora 데이터베이스 스토리지를 암호화하여 관리하는 암호화
키로 데이터를 암호화하여 데이터 보호를 제공합니다. 또한 AWS 서비스 및 내부 연결
리소스와 함께 사용할 공용 및 개인 SSL/TLS(Secure Sockets Layer/Transport Layer
Security) 인증서를 쉽게 프로비저닝, 관리 및 배포할 수 있는 서비스인 AWS Certificate
Manager(ACM)를 사용합니다. . 또한 ACM 인증서를 ALB 에 연결하여 전송 중인 데이터를
암호화합니다. 이는 클라이언트와 로드 밸런서 간의 연결에 SSL/TLS 암호화를 활성화하여
데이터 보호를 제공합니다. 이 솔루션은 미사용 및 전송 중인 애플리케이션의 모든
데이터를 암호화해야 한다는 요구 사항을 충족합니다.
옵션 A 는 ALB 에서 AWS KMS 인증서를 사용하여 전송 중인 데이터를 암호화하기 때문에
효율성이 떨어집니다. 이는 AWS KMS 가 인증서를 제공하지 않고 키만 제공하기 때문에
불가능합니다. 또한 AWS Certificate Manager(ACM)를 사용하여 유휴 EBS 볼륨 및 Aurora
데이터베이스 스토리지를 암호화합니다. 이는 ACM 이 암호화를 제공하지 않고 인증서만
제공하기 때문에 불가능합니다.
옵션 B 는 AWS 루트 계정을 사용하여 AWS Management Console 에 로그인하기 때문에
효율성이 떨어집니다. 이 방법은 계정의 모든 리소스에 대한 무제한 액세스 권한이
있으므로 권장되지 않습니다. 또한 회사의 암호화 인증서를 업로드하는데 ACM 은 인증서를
무료로 제공할 수 있으므로 필요하지 않습니다. 또한 계정에 대해 저장 및 전송 중인 모든
데이터에 대해 암호화를 켜는 옵션을 선택합니다. 이는 암호화 설정이 각 서비스 및
리소스에 따라 다르기 때문에 불가능합니다.
옵션 D 는 Windows 서버의 볼륨에 대한 암호화를 제공하는 Windows 기능인 BitLocker 를
사용하여 미사용 데이터를 모두 암호화하기 때문에 효율성이 떨어집니다. 그러나 이것은
Aurora 가 Linux 서버에서 실행되기 때문에 미사용 Aurora 데이터베이스 스토리지에 대한
암호화를 제공하지 않습니다. 또한 회사의 TLS 인증서 키를 AWS KMS 로 가져오는데, 이는
ACM 이 인증서를 무료로 제공할 수 있으므로 필요하지 않습니다. 또한 KMS 키를 ALB 에
연결하여 전송 중인 데이터를 암호화합니다. ALB 에는 키가 아닌 인증서가 필요하기 때문에
불가능합니다.
설명2:
AWS KMS 를 사용하여 유휴 상태의 EBS 및 Aurora 데이터베이스 스토리지를 암호화할 수
있습니다.
ACM 을 사용하여 SSL/TLS 인증서를 가져와 ALB 에 연결할 수 있습니다. 이는
클라이언트와 ALB 간에 전송 중인 데이터를 암호화합니다.
A 는 EBS 를 암호화하기 위한 올바른 서비스가 아닌 EBS 를 암호화하기 위해 ACM 을
사용하도록 제안하기 때문에 올바르지 않습니다.
B는 정답이 아닙니다. AWS 루트 계정에 의존하고 AWS Management Console에서 유휴 및
전송 중인 모든 데이터에 대한 암호화를 활성화하는 옵션을 선택하는 것은 유효한 접근
방식이 아니기 때문입니다.
BitLocker는 AWS 서비스에서 데이터를 암호화하는 데 적합한 솔루션이 아니기 때문에 D는
틀렸습니다. 주로 Windows 기반 운영 체제에서 데이터를 암호화하는 데 사용됩니다. 또한
TLS 인증서 키를 AWS KMS 로 가져와 ALB 에 연결하는 것은 전송 중인 데이터를
암호화하는 데 권장되는 접근 방식이 아닙니다.

---

# Q235 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/95326-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
AWS SCT 는 Oracle 데이터베이스의 스키마와 코드를 Aurora PostgreSQL 과 호환되도록
변환하는 데 사용됩니다. AWS DMS 는 Oracle 데이터베이스에서 Aurora PostgreSQL 로
데이터를 마이그레이션하는 데 활용됩니다. 마이그레이션 프로세스 중에 많은 수의 읽기 및
쓰기를 처리하려면 메모리 최적화 복제 인스턴스를 사용하는 것이 좋습니다.
전체 로드 및 CDC 복제 작업을 생성하면 초기 데이터 마이그레이션이 수행되고 Oracle
데이터베이스의 진행 중인 변경 사항이 지속적으로 캡처되어 Aurora PostgreSQL
데이터베이스에 적용됩니다. 테이블 매핑을 위해 모든 테이블을 선택하면 동일한 테이블에
쓰는 모든 응용 프로그램이 마이그레이션됩니다.
AWS DataSync 를 단독으로 사용하는 것은 데이터베이스 마이그레이션 및 데이터 동기화에
충분하지 않기 때문에 옵션 A 및 B는 올바르지 않습니다.
계산에 최적화된 복제 인스턴스를 사용하는 것이 많은 수의 읽기 및 쓰기를 처리하는 데
가장 적합한 선택이 아니기 때문에 옵션 D는 올바르지 않습니다.
참고
https://repost.aws/ko/knowledge-center/dms-memory-optimization

---

# Q236 

**정답: D**

https://www.examtopics.com/discussions/amazon/view/94990-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
로드 밸런싱된 다중 AZ AWS EBS 를 사용하면 애플리케이션을 크게 변경하지 않고도 두
계층 모두에 대한 확장성과 고가용성을 얻을 수 있습니다. DB 를 RDS 다중 AZ DB 로
이동하면 고가용성과 자동 장애 조치가 보장됩니다. S3 를 통해 사용자 이미지를 저장하고
제공하면 확장 가능하고 가용성이 높은 솔루션을 제공합니다.
프런트 엔드 계층에 S3 를 사용하고 애플리케이션 계층에 Lambda 를 사용하려면
애플리케이션 아키텍처를 크게 변경해야 하므로 A는 정답이 아닙니다. DB를 DynamoDB로
이동하려면 DB 관련 코드를 다시 작성해야 합니다.
이미지를 제공하기 위해 로드 밸런싱된 다중 AZ AWS EBS 환경과 읽기 전용 복제본이 있는
RDS DB 를 사용하는 것이 더 적합한 솔루션이기 때문에 B 는 틀렸습니다. 읽기 전용
복제본이 있는 RDS 는 이러한 용도로 S3 를 사용하는 것보다 이미지 제공 워크로드를 더
효율적으로 처리할 수 있습니다.
프런트 엔드 계층에 S3 를 사용하고 애플리케이션 계층에 EC2 의 ASG 를 사용하려면
애플리케이션 아키텍처를 수정해야 하므로 C 는 올바르지 않습니다. 메모리 최적화 EC2
유형의 이미지를 저장하고 제공하는 것은 S3 를 사용할 때보다 가장 효율적이고 확장
가능한 접근 방식이 아닐 수 있습니다.
설명2:
AWS Fargate 는 Amazon EC2 인스턴스의 서버 또는 클러스터를 관리할 필요 없이
컨테이너를 실행하기 위해 Amazon ECS 와 함께 사용할 수 있는 기술입니다. Fargate 를
사용하면 더 이상 컨테이너를 실행하기 위해 가상 머신의 클러스터를 프로비저닝, 구성
또는 확장할 필요가 없습니다.
https://docs.aws.amazon.com/AmazonECS/latest/userguide/what-is-fargate.html
"고가용성"의 경우: 다중 AZ 및 "애플리케이션에 대한 최소 변경 사항"의 경우: Elastic
Beanstalk 는 용량 프로비저닝, 로드 밸런싱, 자동 확장에서 애플리케이션 상태 모니터링에
이르기까지 배포를 자동으로 처리합니다.

---

# Q237 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/95144-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
VPC 피어링 연결을 사용하면 인터넷 게이트웨이, VPN 연결 또는 NAT 장치 없이 프라이빗
IP 주소를 사용하여 서로 다른 VPC 의 인스턴스 간에 안전한 통신이 가능합니다. 이를
설정하면 VPC-A 에서 실행 중인 애플리케이션이 공용 인터넷이나 단일 장애 지점을 거치지
않고 VPC-B의 EC2에 직접 액세스할 수 있습니다.
B는 VPC 게이트웨이 엔드포인트가 인터넷을 통하지 않고 VPC에서 S3 또는 DynamoDB에
액세스하는 데 사용되기 때문에 올바르지 않습니다. 서로 다른 VPC 에 있는 EC2 인스턴스
간에 연결을 설정하도록 설계되지 않았습니다.
C 는 VPC 간에 VPN 연결을 구성해야 하므로 올바르지 않습니다. 이로 인해 추가적인
복잡성과 잠재적인 단일 실패 지점이 발생합니다.
D 는 프라이빗 VIF 를 생성하고 경로를 추가하면 Direct Connect 를 사용하여 온프레미스
인프라와 VPC-B 간에 직접 연결을 설정하는 데 적용할 수 있기 때문에 올바르지 않지만
서로 다른 VPC 내의 별도 VPC 에 있는 EC2 인스턴스 간의 통신 시나리오에는 적합하지
않습니다. AWS 계정.
설명2:
AWS 는 VPC 의 기존 인프라를 사용하여 VPC 피어링 연결을 생성합니다. 게이트웨이나
VPN 연결이 아니며 별도의 물리적 하드웨어에 의존하지 않습니다. 통신 또는 대역폭 병목
현상에 대한 단일 장애 지점이 없습니다.
https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html

---

# Q238 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/94996-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
각 계정에 대한 비용 예산을 생성하고 기간을 월 단위로 지정하고 범위를 EC2 로 지정하면
EC2와 관련된 비용을 구체적으로 추적하고 모니터링할 수 있습니다. 예산에 경고 임계값을
설정하면 지정된 임계값이 초과될 때 알림이 트리거됩니다. 알림을 받도록 SNS 를
구성합니다. 회사에서 구독하면 즉시 알림을 받을 수 있습니다.
A 와 B 는 Cost Explorer 를 사용하여 임계값을 초과할 때 실시간 알림을 제공하지 않을 수
있는 보고서를 생성하기 때문에 가장 비용 효율적인 솔루션이 아닙니다. 또한 A.는 일일
보고서 사용을 제안하고 B.는 월별 보고서 사용을 제안합니다. 이는 즉각적인 알림에 대해
원하는 수준의 세분성을 제공하지 않을 수 있습니다.
D 는 Athena 및 EventBridge 와 함께 비용 및 사용 보고서를 사용하는 것과 관련됩니다. 이
솔루션은 더 많은 유연성과 데이터 분석 기능을 제공하며 더 복잡하고 Athena 를 사용하고
시간별 보고서를 생성하는 데 추가 비용이 발생할 수 있습니다.
설명2:
AWS 예산을 사용하면 AWS 계정에 대한 예산을 생성하고 사용량이 특정 임계값을 초과할
때 알림을 설정할 수 있습니다. 각 계정에 대한 예산을 생성하고 기간을 월 단위로
지정하고 범위를 EC2 인스턴스로 지정하면 각 계정의 EC2 사용량을 효과적으로 추적하고
임계값을 초과할 때 알림을 받을 수 있습니다. 이 솔루션은 Amazon Athena 또는 Amazon
EventBridge와 같은 추가 리소스가 필요하지 않기 때문에 가장 비용 효율적인 옵션입니다.

---

# Q239 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/95365-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
API Gateway REST API 를 생성하면 클라이언트가 마이크로서비스에 도달하기 위해 호출할
수 있는 HTTPS 엔드포인트를 정의할 수 있습니다. API 에서 IAM 인증을 활성화하여 API
호출에 대한 인증을 적용합니다. 이렇게 하면 인증된 요청만 마이크로서비스에 도달할 수
있습니다. 이 솔루션은 API 게이트웨이의 기본 제공 기능을 활용하여 HTTP 엔드포인트,
요청 라우팅 및 IAM 인증을 처리하므로 운영상 효율적입니다. 추가 인프라 구성 요소 없이
확장 가능하고 관리되는 솔루션을 제공합니다.
B는 Lambda URL을 생성하고 인증 유형으로 AWS IAM을 지정할 것을 제안합니다. 이것은
IAM 인증을 제공할 수 있지만 요청 유효성 검사, 속도 제한 및 API 구성의 손쉬운 관리와
같은 API Gateway의 이점이 없습니다.
C 와 D 에는 CloudFront, Lambda@Edge 및 CloudFront 함수 사용이 포함됩니다. 이러한
서비스는 유연성과 에지 위치에서 논리를 실행할 수 있는 기능을 제공하지만 추가적인
복잡성을 야기하며 지정된 요구 사항에 필요하지 않을 수 있습니다.

---

# Q240 

**정답: D**

https://www.examtopics.com/discussions/amazon/view/94998-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
데이터 웨어하우스와 동일한 AWS 리전에서 시각화 도구를 호스팅하고 동일한 리전 내에서
Direct Connect 연결을 통해 액세스하면 데이터 전송 비용이 없어지고 지연 시간이 짧은
고대역폭 연결이 보장됩니다.
A. 온프레미스에서 시각화 도구를 호스팅하고 인터넷을 통해 데이터 웨어하우스를 쿼리하면
모든 쿼리 결과에 대한 데이터 전송 비용과 잠재적 대기 시간 및 대역폭 제한이
발생합니다.
B. 데이터 웨어하우스와 동일한 AWS 리전에서 시각화 도구를 호스팅하지만 인터넷을 통해
액세스하면 여전히 각 쿼리 결과에 대한 데이터 전송 비용이 발생합니다.
C. 온프레미스에서 시각화 도구를 호스팅하고 동일한 AWS 리전 내에서 Direct Connect
연결을 통해 데이터 웨어하우스를 쿼리하면 모든 쿼리 결과에 대한 데이터 전송 비용이
발생하고 온프레미스 인프라가 필요하여 복잡성이 추가됩니다.
참고:
https://aws.amazon.com/directconnect/pricing/
https://aws.amazon.com/blogs/aws/aws-data-transfer-prices-reduced/

---

# Q241 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/95000-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
PostgreSQL 데이터베이스를 PostgreSQL DB 유지용 RDS 로 늘리고 다른 AWS 리전에
읽기 전용 복제본을 생성하면 여러 리전에서 데이터 가용성과 온라인 액세스를 충분히 할
수 있습니다. 이 솔루션은 EC2 폐쇄에서 PostgreSQL 클러스터를 관리하거나(옵션 A)
스냅샷을 사용하여 수동 복제를 설정하는 것(옵션 D)에 비해 연산된 헤드가 적입니다. 또한
Amazon RDS는 기본 복원 및 복제 설정을 처리하여 회사의 운영 문제를 줄입니다.
B 는 단일 AWS 리전 내에서 고가용성을 누릴 수 있습니다. 그러나 질문에 여러 개의 AWS
리전에서 항상 데이터를 온라인으로 사용할 수 있어야만 요구 사항을 충족할 수 없습니다.
RDS 의 다중 AZ 기능은 동일한 리전 내에서 자동으로 조치를 취하지만 데이터를 여러
리전으로 복제하지 않습니다.
설명2:
"항상 여러 AWS 리전에서 온라인으로". 현재 읽기 전용 복제본만 지역 간 지원, 다중 AZ는
지역 간 지원하지 않음(동일한 지역에서만 작동)
https://aws.amazon.com/ko/about-aws/whats-new/2018/01/amazon-rds-read-replicas-
now-support-multi-az-deployments/

---

# Q242 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/95001-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
다중 응답 라우팅 정책을 사용하여 여러 리소스에 DNS 응답을 배포할 수 있습니다.
예를 들어 라우팅 레코드를 Route 53 상태 확인과 연결하려는 경우 다중값 응답 라우팅을
사용합니다. 예를 들어 DNS 쿼리에 대해 여러 값을 반환하고 트래픽을 여러 IP 주소로
라우팅해야 하는 경우 다중 값 응답 라우팅을 사용합니다.
https://aws.amazon.com/premiumsupport/knowledge-center/multivalue-versus-simple-p
olicies/
설명2:
다중값 라우팅 정책은 Route 53이 동일한 리소스에 대한 여러 정상 IP 주소로 DNS 쿼리에
응답하도록 허용합니다. 이는 여러 인스턴스가 동일한 용도로 사용되며 부하 분산 또는
장애 조치가 가능한 시나리오에서 특히 유용합니다. 다중 값 라우팅 정책을 사용하면
Route 53 은 여러 IP 주소를 무작위 순서로 반환하여 모든 정상 인스턴스에 트래픽을
분산합니다.
옵션 A(단순 라우팅 정책)는 DNS 쿼리에 대한 응답으로 단일 IP 주소만 반환하며 여러
주소 반환을 지원하지 않습니다.
옵션 B(대기 시간 라우팅 정책)는 리소스에 대한 최저 대기 시간을 기반으로 트래픽을
라우팅하는 데 사용되며 모든 정상 IP 주소를 반환해야 하는 요구 사항을 충족하지
않습니다.
옵션 D(Geolocation 라우팅 정책)는 사용자의 지리적 위치를 기반으로 트래픽을
라우팅하는 데 사용되며 정상 IP 주소를 모두 반환해야 하는 요구 사항을 충족하지
않습니다.
따라서 다중 값 라우팅 정책은 DNS 쿼리에 대한 응답으로 모든 정상 EC2 인스턴스의 IP
주소를 반환하는 데 가장 적합한 옵션입니다.

---

# Q243 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/95002-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
AWS Storage Gateway는 온프레미스 소프트웨어 어플라이언스와 클라우드 기반 스토리지를
연결하여 조직의 온프레미스 IT 환경과 AWS 스토리지 인프라 간의 원활하고 안전한
통합을 제공하는 서비스입니다. 각 진료소 구내에 파일 게이트웨이를 가상 머신으로
배포함으로써 의료 연구실은 각 진료소에 대한 읽기 전용 권한을 유지하면서 S3 버킷에
저장된 데이터에 대한 짧은 대기 시간 액세스를 제공할 수 있습니다. 이 솔루션을 통해
클리닉은 데이터 전송이나 마이그레이션 없이 온프레미스 파일 기반 애플리케이션에서 직접
데이터 파일에 액세스할 수 있습니다.
설명2:
A. 클리닉에서 파일 인터페이스를 통해 S3 버킷에 저장된 데이터 파일에 액세스할 수
있습니다. 파일 게이트웨이는 자주 액세스하는 데이터를 로컬로 캐시하여 대기 시간을
줄이고 데이터에 대한 빠른 액세스를 제공합니다.
B. AWS DataSync 를 사용하여 Amazon S3 버킷에서 각 클리닉의 온프레미스
애플리케이션으로 데이터 파일을 전송하는 작업이 포함됩니다. 이렇게 하면 데이터
마이그레이션이 가능하지만 실시간 액세스를 제공하지 않을 수 있으며 추가 대기 시간이
발생할 수 있습니다.
C. 파일 수준의 접근보다는 데이터에 대한 블록 수준의 접근에 적합하다. 파일 기반
애플리케이션을 위한 가장 효율적인 솔루션이 아닐 수도 있습니다.
D. 확장 가능한 파일 스토리지 서비스인 Amazon EFS 를 사용하여 데이터에 대한 파일
수준 액세스를 제공합니다. 그러나 파일 게이트웨이 솔루션을 사용할 때보다 복잡성과 대기
시간이 추가로 발생할 수 있습니다.

---

# Q244 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/95336-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
이 접근 방식은 웹 사이트 플랫폼에 고가용성과 확장성을 모두 제공합니다. 데이터베이스를
다른 가용 영역에 있는 읽기 전용 복제본이 있는 Amazon Aurora 로 이동하면
데이터베이스에 대한 장애 조치 옵션이 제공됩니다. 두 가용 영역에서 Application Load
Balancer 및 Auto Scaling 그룹을 사용하면 증가하는 사용자 수요를 충족하기 위해 웹
사이트를 자동으로 확장할 수 있습니다. 또한 원래 EC2 인스턴스에서 AMI 를 생성하면
장애 발생 시 인스턴스를 쉽게 복제할 수 있습니다.
설명2:
옵션 A 는 고가용성 또는 확장성을 위한 솔루션을 제공하지 않습니다. 동일한 AZ 에서 다른
EC2 인스턴스를 수동으로 시작하면 해당 AZ 에 장애가 발생하면 다운타임이 발생하므로
고가용성이 보장되지 않을 수 있습니다.
옵션 B 는 데이터베이스 성능을 개선하고 내결함성 수준을 제공하지만 웹 사이트 플랫폼의
확장성 측면을 다루지는 않습니다.
옵션 C 는 고가용성과 내결함성을 모두 제공합니다. AMI 를 생성하면 AZ 간에 EC2
인스턴스를 쉽게 복제할 수 있습니다. 두 AZ 에서 ALB 를 구성하고 ASG 를 연결하면 여러
인스턴스에 걸쳐 확장성과 부하 분산이 보장됩니다.
옵션 D 는 회사에서 요구하는 고가용성 및 확장성을 제공하지 않습니다. S3 에 예약된
백업은 데이터 보호를 다루지만 웹사이트 가용성이나 확장성에 기여하지는 않습니다.

---

# Q245 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/95337-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명
대상으로 하나의 EC2 인스턴스만 포함하도록 개발 환경에서 대상 그룹을 구성하면 해당
환경에 할당된 리소스를 효과적으로 줄일 수 있습니다. 이렇게 하면 더 적은 수의 EC2
인스턴스 및 관련 리소스를 활용하여 비용을 최소화할 수 있습니다.
옵션 B 는 개발 환경의 비용 효율성을 직접 다루지 않습니다. 비용 최적화보다는 로드
밸런싱 전략에 중점을 둡니다.
옵션 C 는 현재 인스턴스 크기가 과도하게 프로비저닝되거나 애플리케이션 요구 사항에
불필요하지 않는 한 가장 비용 효율적인 솔루션이 아닐 수 있습니다.
옵션 D 는 비용 절감에 도움이 될 수 있지만 특히 부하가 증가하는 기간 동안 트래픽을
처리하고 효율적으로 확장하는 환경의 기능에 영향을 미칠 수 있습니다.
전반적으로 옵션 A 는 기능 설정을 유지하면서 개발 환경에 할당된 리소스를
최소화함으로써 비용 효율적인 접근 방식을 제공합니다.

---

# Q246 

**정답: D**

https://www.examtopics.com/discussions/amazon/view/95003-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
A. 다른 유형의 로드 밸런서를 사용하고 NAT 게이트웨이를 구성할 것을 제안하지만 EC2
인스턴스에 도달하는 인터넷 트래픽 문제는 다루지 않습니다.
B.는 EC2 인스턴스를 퍼블릭 인터넷에 노출할 것을 제안합니다. 이는 보안 위험을 초래할
수 있으며 인스턴스에 도달하는 인바운드 인터넷 트래픽 문제를 해결하지 않습니다.
C.는 아웃바운드 인터넷 액세스를 갖도록 EC2 인스턴스를 구성할 것을 제안하지만
인스턴스에 도달하는 인바운드 인터넷 트래픽 문제를 해결하지는 않습니다.
D.가 정답입니다. 퍼블릭 서브넷을 생성하고 이를 ALB 와 연결하면 인바운드 인터넷
트래픽이 ALB 에 도달할 수 있습니다. 프라이빗 서브넷에 대한 경로를 포함하도록 퍼블릭
서브넷의 라우팅 테이블이 업데이트되어 트래픽이 프라이빗 서브넷의 EC2 인스턴스에
도달할 수 있습니다. 이 설정을 사용하면 인터넷 트래픽이 ALB 를 통해 EC2 인스턴스에
도달하도록 허용하면서 애플리케이션에 대한 보안 액세스가 가능합니다.
참고:
https://repost.aws/ko/knowledge-center/public-load-balancer-private-ec2

---

# Q247 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/95004-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
A. 읽기 복제본 설정에 필요한 RDS 기본 노드에서 이진 로그 복제 기능을 활성화합니다.
B. 장애 조치 시나리오 중에 DB 인스턴스가 기본 역할로 승격되는 순서를 결정합니다.
느린 읽기 문제를 해결하기 위해 읽기 전용 복제본을 추가하는 것과 직접적인 관련이
없습니다.
C. 원본 DB 인스턴스에서 진행 중인 모든 트랜잭션이 변경 사항을 구현하기 전에
완료되도록 합니다. 읽기 전용 복제본으로 전환하는 동안 데이터 무결성과 일관성을
유지하는 데 도움이 됩니다.
D.는 DynamoDB 전용 기능입니다. DynamoDB 에서 다중 리전 복제 및 고가용성을
허용하지만 이 시나리오에는 적용할 수 없습니다.
E. 원본 DB 인스턴스에 대해 정기적인 백업이 수행되는지 확인합니다. 이는 읽기 전용
복제본을 추가하는 동안 또는 이후에 문제가 발생할 경우 특정 시점 복원을 허용하므로
데이터 보호 및 복구 목적에 중요합니다.
설명2:
"오래 실행되는 활성 트랜잭션은 읽기 전용 복제본 생성 프로세스를 느리게 할 수 있습니다.
읽기 전용 복제본을 생성하기 전에 장기 실행 트랜잭션이 완료될 때까지 기다리는 것이
좋습니다. 동일한 원본 DB 인스턴스에서 여러 읽기 전용 복제본을 병렬로 생성하는 경우 ,
Amazon RDS는 첫 번째 생성 작업 시작 시 하나의 스냅샷만 찍습니다. 읽기 전용 복제본을
생성할 때 고려해야 할 몇 가지 사항이 있습니다. 먼저 백업 보존 기간을 0 이외의 값.
이 요구 사항은 다른 읽기 전용 복제본의 원본 DB 인스턴스인 읽기 전용 복제본에도
적용됩니다."
https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html

---

# Q248 

**정답: D**

https://www.examtopics.com/discussions/amazon/view/95329-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
A. 인스턴스 사본을 생성하고 모든 인스턴스를 ALB 뒤에 배치하는 것은 높은 CPU 사용률
문제를 해결하거나 사용자 부하에 따라 확장성을 제공하지 않습니다.
B. S3 용 S3 VPC 엔드포인트를 생성하고 엔드포인트를 참조하도록 소프트웨어를
업데이트하면 네트워크 성능이 향상되지만 높은 CPU 사용률 문제를 해결하거나 사용자
부하에 따라 확장성을 제공하지 않습니다.
C. EC2 인스턴스를 중지하고 인스턴스 유형을 더 강력한 CPU 와 더 많은 메모리를 가진
인스턴스 유형으로 수정하면 성능이 향상될 수 있지만 사용자 부하에 따른 확장성은
해결되지 않습니다.
D. 들어오는 요청을 SQS 로 라우팅하고, 대기열 크기에 따라 EC2 ASG 를 구성하고,
대기열에서 읽을 수 있도록 소프트웨어를 업데이트하면 시스템 성능이 향상되고 사용자
로드에 따라 확장성이 제공됩니다.
따라서 옵션 D 는 높은 CPU 사용률을 해결하고 시스템 성능을 개선하며 사용자 부하에
따라 확장성을 활성화하므로 올바른 선택입니다.

---

# Q249 

**정답: D**

https://www.examtopics.com/discussions/amazon/view/95006-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
A. Storage Gateway 사용과 관련이 있지만 SMB 클라이언트에 대한 지원을 구체적으로
언급하지는 않습니다. SMB 클라이언트를 사용하여 데이터에 액세스해야 하는 요구 사항을
충족하지 못할 수 있습니다.
B. S3 에 데이터를 보관하는 데 주로 사용되는 테이프 게이트웨이 구성과 함께 Storage
Gateway 를 사용하는 것과 관련됩니다. SMB 클라이언트가 데이터에 액세스할 수 있도록
기본 지원을 제공하지 않습니다.
C. EC2 Windows 인스턴스에서 Windows 파일 공유를 수동으로 설정하고 구성하는 작업이
포함됩니다. SMB 클라이언트가 데이터에 액세스할 수 있지만 수동 설정 및 유지 관리가
필요하므로 완전히 관리되는 솔루션은 아닙니다.
D. SMB 클라이언트를 지원하는 완전히 관리되는 Windows 파일 시스템인 FSx for Windows
파일 서버 파일 시스템 생성이 포함됩니다. 기본 SMB 를 지원하는 사용하기 쉬운 공유
스토리지 솔루션을 제공합니다.
SMB 클라이언트를 사용하고 완전히 관리되는 솔루션이 필요한 요구 사항을 기반으로 옵션
D가 가장 적합한 선택입니다.
설명2:
https://aws.amazon.com/fsx/lustre/
Amazon FSx는 Windows 파일 시스템 기능과 업계 표준 서버를 기본적으로 지원합니다.
네트워크를 통해 파일 저장소에 액세스하기 위한 메시지 블록(SMB) 프로토콜.
https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html
온프레미스-AWS 간 스토리지 서비스 중 SMB 지원하는 건 Storage Gateway File
Gateway나 Amazon FSx for Windows라고 보면 됨.

---

# Q250 

**정답: D**

https://www.examtopics.com/discussions/amazon/view/95007-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
A. CloudWatch 를 VPC 흐름 로그의 대상으로 사용할 것을 제안합니다. 그러나 90 일 동안
로그 보존을 관리한 다음 간헐적으로 액세스하는 메커니즘을 제공하지 않습니다.
B. Kinesis를 VPC 흐름 로그의 대상으로 사용할 것을 제안합니다. 90일 동안 로그를 보관할
수 있지만 로그에 대한 간헐적 액세스 요구 사항은 다루지 않습니다.
C. CloudTrail 을 VPC 흐름 로그의 대상으로 사용할 것을 제안합니다. 그러나 CloudTrail 은
네트워크 트래픽 로그 캡처가 아니라 API 활동을 감사 및 모니터링하도록 설계되었습니다.
VPC 흐름 로그 캡처 요구 사항을 충족하지 않습니다.
D. S3 를 VPC 흐름 로그의 대상으로 사용하고 S3 수명 주기 정책을 활용하여 90 일 후에
로그를 비용 효율적인 스토리지 클래스로 전환할 것을 제안합니다. 90 일 동안 로그를
유지해야 하는 요구 사항을 충족하고 스토리지 비용을 최적화하면서 간헐적인 액세스에
대한 유연성을 제공합니다.
설명2:
여기에는 VPC 흐름 로그가 S3 로 직접 이동할 수 있음을 지정하는 표가 있습니다.
CloudTrail을 거쳐 S3로 이동할 필요가 없습니다. CW를 통해서도 아닙니다.
https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resourcep
olicy.html#AWS-logs-i

---

# Q251 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/95023-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
A. 사설 서브넷에 직접 인터넷 액세스를 제공합니다. 이는 아웃바운드 인터넷 액세스를
제한하는 것이 목표이므로 이 경우에는 바람직하지 않습니다.
B. 프라이빗 서브넷의 EC2 가 프록시 역할을 하는 NAT 게이트웨이를 통해 인터넷에
액세스할 수 있습니다. 프라이빗 서브넷의 보안을 유지하면서 통제된 아웃바운드 인터넷
액세스를 제공합니다.
C. NAT 게이트웨이를 사용하는 것과 유사하지만 NAT 인스턴스를 사용하는 것과 관련이
있습니다. NAT 인스턴스는 NAT 게이트웨이에 비해 더 많은 수동 구성 및 관리가
필요하므로 덜 선호되는 옵션입니다.
D. 필요하지 않은 인터넷 게이트웨이와 NAT 인스턴스의 사용을 결합합니다. 불필요한
복잡성이 발생하고 추가 관리가 필요한 NAT 인스턴스가 추가됩니다.
전반적으로 옵션 B 는 퍼블릭 서브넷에 배치된 NAT 게이트웨이를 활용하여 프라이빗
서브넷의 EC2 인스턴스에 대해 제어된 아웃바운드 인터넷 액세스를 활성화하므로 가장
적합한 솔루션입니다.
NAT 게이트웨이는 AWS 및 일반적으로 NAT 인스턴스보다 선호됩니다.
설명2:
이 접근 방식을 사용하면 EC2 인스턴스가 여전히 프라이빗 서브넷에 있는 동안 인터넷에
액세스하고 월별 보안 업데이트를 다운로드할 수 있습니다. NAT 게이트웨이를 만들어
퍼블릭 서브넷에 배치하면 프라이빗 서브넷의 인스턴스가 NAT 게이트웨이를 통해 인터넷에
액세스할 수 있습니다. 그런 다음 NAT 게이트웨이를 기본 경로로 사용하도록 프라이빗
서브넷 경로 테이블을 구성합니다. 이렇게 하면 모든 아웃바운드 트래픽이 NAT
게이트웨이를 통해 전달되어 EC2 인스턴스가 프라이빗 서브넷의 보안을 유지하면서
인터넷에 액세스할 수 있습니다.

---

# Q252 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/95024-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
EFS 는 여러 EC2 에서 동시에 액세스할 수 있는 확장 가능하고 완벽하게 관리되는 파일
스토리지 서비스를 제공합니다. 리전 내의 여러 AZ 에 데이터를 저장하여 기본 제공
중복성을 제공합니다. EFS 를 사용하면 여러 애플리케이션 서버에서 클라이언트 사례
파일에 동시에 액세스할 수 있으므로 시간이 지남에 따라 파일 수가 증가함에 따라
고가용성과 확장성이 보장됩니다.
옵션 B 인 EBS 는 일반적으로 개별 EC2 에 연결하는 데 사용되는 블록 수준 스토리지
서비스이며 여러 인스턴스에 대한 동시 액세스를 제공하지 않으므로 이 시나리오에
적합하지 않습니다.
옵션 C, S3 Glacier Deep Archive는 장기 아카이브 스토리지 서비스이며 활성 파일 액세스
및 여러 애플리케이션 서버의 동시 액세스에 적합하지 않을 수 있습니다.
옵션 D, AWS Backup 은 중앙 집중식 백업 관리 서비스이며 필요한 동시 파일 액세스 및
중복 기능을 제공하지 않습니다.
따라서 가장 적합한 솔루션은 Amazon EFS(옵션 A)입니다.
설명2:
Amazon EFS 는 여러 EC2 인스턴스에서 동시에 액세스할 수 있는 간단하고 확장 가능한
완전 관리형 파일 시스템을 제공하며 내장된 중복성을 제공합니다. 동일한 파일에
액세스하기 위해 여러 EC2 인스턴스에 최적화되어 있으며 가용성, 내구성 및 보안성이
우수하도록 설계되었습니다. 데이터를 페타바이트까지 확장할 수 있고 수천 개의 동시
연결을 처리할 수 있으며 대량의 데이터를 저장하고 액세스하기 위한 비용 효율적인
솔루션입니다.

---

# Q253 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/95008-exam-aws-certified-solut
ions-architect-associate-saa-c03/

---

# Q254 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/95009-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
A. 특정 인스턴스를 기반으로 트래픽을 제한하므로 애플리케이션 계층 간에 최소 권한
원칙을 적용하는 데 가장 적합한 솔루션이 아닐 수 있습니다.
B. 규칙에서 보안 그룹 ID 를 사용하면 필요한 통신만 허용하고 최소 권한 원칙을 준수하여
애플리케이션 계층 간의 트래픽을 정밀하게 제어할 수 있습니다.
C. 전체 VPC CIDR 블록을 기반으로 광범위한 규칙을 적용하여 특정 애플리케이션 계층
간의 보안 통신에 필요한 수준의 세분성을 제공하지 못할 수 있습니다.
D. 서브넷 CIDR 블록을 기반으로 트래픽을 제한하므로 애플리케이션 계층 간의 적절한
보안을 보장하기에 충분하지 않을 수 있습니다.
요약하면 보안 그룹 ID(옵션 B)를 사용하면 최소 권한 원칙에 따라 애플리케이션 계층 간의
트래픽을 정밀하게 제어할 수 있으므로 권장되는 접근 방식입니다.
참고
https://docs.aws.amazon.com/ko_kr/AWSEC2/latest/UserGuide/security-group-rules.html

---

# Q255 

**정답: D**

https://www.examtopics.com/discussions/amazon/view/95026-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
A. 다중 주문 생성 방지에 적합한 솔루션이 아닙니다. 이 접근 방식은 순차적이고 안정적인
주문 처리를 보장하지 않습니다.
B. 다중 주문 생성을 방지하기 위한 적절한 해결책이 아닙니다. CloudTrail 은 주로 API
활동을 기록하고 감사하는 데 사용되며 기록된 요청을 기반으로 Lambda 를 호출하면
올바른 주문 처리가 보장되지 않습니다.
C.는 적절한 솔루션이 아닙니다. SNS 는 게시-구독 메시징 서비스이며 이를 폴링하면
처리가 지연되고 잠재적인 주문 중복이 발생할 수 있습니다.
D.가 정답입니다. SQS FIFO 를 사용하면 주문이 순차적이고 안정적인 방식으로 처리되어
동일한 거래에 대해 여러 주문이 생성되는 것을 방지할 수 있습니다.
설명2:
VPC 내에 있는 프라이빗 서브넷의 EC2 인스턴스와 DynamoDB 간 가장 안전한 AWS
네트워크 통신 = VPC Gateway Endpoint.
게이트웨이 엔드포인트는 VPC 용 인터넷 게이트웨이 또는 NAT 디바이스가 없어도 Amazon
S3 및 DynamoDB에 대한 안정적인 연결을 제공합니다.
https://docs.aws.amazon.com/ko_kr/vpc/latest/privatelink/vpce-gateway.html#vpc-endp
oints-limitations
설명3:
DynamoDB 용 VPC 엔드포인트를 사용하면 VPC 의 Amazon EC2 인스턴스가 프라이빗 IP
주소를 사용하여 퍼블릭 인터넷에 노출되지 않고 DynamoDB에 액세스할 수 있습니다. EC2
인스턴스에는 퍼블릭 IP 주소가 필요하지 않으며 VPC 에 인터넷 게이트웨이, NAT 디바이스
또는 가상 프라이빗 게이트웨이가 필요하지 않습니다. 엔드포인트 정책을 사용하여
DynamoDB 에 대한 액세스를 제어합니다. VPC 와 AWS 서비스 간의 트래픽은 Amazon
네트워크를 벗어나지 않습니다.

---

# Q256 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/95460-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
B. S3 버킷에 여러 버전의 객체를 저장할 수 있습니다. 이렇게 하면 문서를 실수로
덮어쓰거나 삭제하더라도 모든 버전의 문서를 사용할 수 있습니다.
D. 버킷의 객체를 우발적으로 삭제하지 않도록 추가 보호 계층을 추가합니다. MFA 삭제가
활성화된 상태에서 사용자는 버킷에서 객체를 성공적으로 삭제하려면 추가 인증 요소를
제공해야 합니다. 이를 통해 우발적 삭제 또는 무단 삭제를 방지하고 중요한 문서에 대한
추가 보안 수준을 제공합니다.
A. 사용자가 문서를 수정하거나 업로드하는 것을 제한합니다. 사용자가 문서를 다운로드,
수정 및 업로드할 수 있도록 허용하는 요구 사항을 충족하지 않습니다.
C. 버킷에 대한 액세스 권한을 제어할 수 있지만 우발적인 삭제를 방지하거나 문서의 모든
버전의 가용성을 보장하는 요구 사항을 구체적으로 다루지는 않습니다.
E. 암호화는 버전 관리 및 삭제 방지보다는 데이터 보호에 중점을 둡니다.

---

# Q257 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/95027-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
B. EC2 Auto Scaling 상태 데이터를 수집하고 S3 로 보내는 데 불필요한 복잡성과
오버헤드가 발생합니다. 이 특정 요구 사항에 가장 효율적인 서버리스 솔루션은 아닙니다.
C. 실시간으로 트리거되지 않기 때문에 데이터 업데이트가 지연될 수 있습니다. 또한 직접
데이터 스트림을 사용하는 것과 비교할 때 불필요한 오버헤드와 복잡성이 추가됩니다.
D. 추가 종속성 및 관리 오버헤드를 도입합니다. 또한 피해야 할 요구 사항인 EC2
인스턴스 시작 속도에 영향을 미칠 수 있습니다.
전반적으로 옵션 A 는 CloudWatch 지표 스트림과 Kinesis Data Firehose 를 활용하여 EC2
인스턴스 시작 속도에 영향을 주지 않고 S3 에서 EC2 Auto Scaling 상태 데이터를
효율적으로 캡처하고 저장함으로써 간소화된 서버리스 솔루션을 제공합니다.
설명2:
지표 스트림을 사용하여 CloudWatch 지표를 거의 실시간으로 제공하고 낮은 지연
시간으로 선택한 대상으로 지속적으로 스트리밍할 수 있습니다. 사용 사례 중 하나는
데이터 레이크입니다. 지표 스트림을 생성하고 CloudWatch 지표를 Amazon S3 와 같은
데이터 레이크에 전달하는 Amazon Kinesis Data Firehose 전달 스트림으로 보냅니다.
https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Metric
-Streams.html

---

# Q258 

**정답: D**

https://www.examtopics.com/discussions/amazon/view/95028-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
A. 상당한 운영 오버헤드가 발생합니다. 이 접근 방식에는 Lambda 관리, 동시성 처리, 큰
파일 크기에 대한 적절한 오류 처리 보장이 필요하며 이는 어려울 수 있습니다.
B. 불필요한 복잡성과 운영 오버헤드를 추가합니다. Spark 작업 관리, 확장성 처리 및 각
파일 업로드에 대한 Lambda 호출 조정은 번거로울 수 있습니다.
C. 추가 복잡성을 도입하고 가장 효율적인 솔루션이 아닐 수 있습니다. 여기에는 Glue
리소스 관리, Lambda 예약, 새 파일이 업로드되지 않은 경우에도 데이터 쿼리가
포함됩니다.
옵션 D 는 AWS Glue 의 ETL 기능을 활용하여 규모에 맞게 데이터 변환 작업을 정의하고
실행할 수 있습니다. 각 S3 PUT 이벤트에 대해 Lambda 함수를 사용하여 ETL 작업을
호출하면 수동 개입 없이 파일이 Parquet 형식으로 효율적으로 변환되도록 할 수 있습니다.
이 접근 방식은 운영 오버헤드를 최소화하고 간소화되고 확장 가능한 솔루션을 제공합니다.
참고:
https://docs.aws.amazon.com/ko_kr/prescriptive-guidance/latest/patterns/three-aws-glu
e-etl-job-types-for-converting-data-to-apache-parquet.html

---

# Q259 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/95030-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
A. 중앙 집중식 백업 관리 서비스인 AWS Backup 을 사용하여 RDS 백업을 유지할 것을
제안합니다. 백업 볼트가 생성되고 일일 일정과 2 년의 백업 보존 기간으로 백업 계획이
정의됩니다. RDS DB 인스턴스가 이 백업 계획에 할당됩니다.
B. 일관되고 복원 가능한 백업에 대한 요구 사항을 다루지 않습니다. 스냅샷은 시점
백업이며 원하는 수준의 일관성을 제공하지 못할 수 있습니다.
C. 데이터베이스에 필요한 백업 및 복원 기능을 제공하도록 설계되지 않았습니다. 백업의
일관성을 보장하거나 쉬운 복원 메커니즘을 제공하지 않습니다.
D. 일일 백업 및 일관된 백업 보존에 대한 요구 사항을 다루지 않습니다. 백업 및
복원보다는 복제 및 변경 데이터 캡처에 더 중점을 둡니다.
설명2:
AWS Backup 은 사용자가 AWS 서비스 전체에서 데이터 백업을 중앙 집중화하고 자동화할
수 있는 완전 관리형 서비스입니다. 백업 빈도 및 보존 기간을 지정하는 백업 계획을
생성하고 관리할 수 있습니다. 또한 백업 데이터를 저장하는 컨테이너인 백업 볼트에 백업
리소스를 할당할 수도 있습니다 1. 솔루션은 AWS Backup 을 사용하여 RDS 백업이
일관되고 복원 가능하며 최소 2년 동안 유지되도록 할 수 있습니다.
1. 일일 스냅샷을 위해 RDS DB 인스턴스의 백업 기간을 구성합니다. 각 RDS DB
인스턴스에 2 년의 스냅샷 보존 정책을 할당합니다. Amazon DLM(Amazon Data Lifecycle
Manager)을 사용하여 스냅샷 삭제를 예약합니다. Amazon DLM 은 RDS 스냅샷과 호환되지
않고 스냅샷 삭제를 예약하는 데 사용할 수 없기 때문에 이 솔루션은 백업의 일관성과 복원
가능성을 보장해야 하는 요구 사항을 충족하지 않습니다.
2. 만료 기간이 2 년인 Amazon CloudWatch Logs 에 자동으로 백업되도록 데이터베이스
트랜잭션 로그를 구성합니다. 이 솔루션은 데이터베이스를 특정 시점으로 복원하는 데
데이터베이스 트랜잭션 로그가 충분하지 않기 때문에 백업이 일관되고 복원 가능한지
확인해야 하는 요구 사항을 충족하지 않습니다. 데이터베이스의 전체 상태가 아니라
데이터베이스에 대한 변경 사항만 캡처합니다.
3. AWS Database Migration Service(AWS DMS) 복제 작업을 구성합니다. 복제 인스턴스를
배포하고 변경 데이터 캡처(CDC) 작업을 구성하여 데이터베이스 변경 사항을 대상으로
Amazon S3 에 스트리밍합니다. 2 년 후 스냅샷을 삭제하도록 S3 수명 주기 정책을
구성합니다. AWS DMS 는 사용자가 데이터베이스를 백업하는 것이 아니라 AWS 로
데이터베이스를 마이그레이션하는 데 도움이 되는 서비스이므로 이 솔루션은 백업의
일관성과 복원 가능성을 보장해야 하는 요구 사항을 충족하지 않습니다. 또한 복제
인스턴스 및 CDC 작업과 같은 추가 리소스 및 구성이 필요합니다.
참조 URL:
https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html

---

# Q260 

**정답: D**

https://www.examtopics.com/discussions/amazon/view/95343-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
D. 파일 시스템이 인증 및 액세스 제어를 위해 기존 AD 인프라를 활용할 수 있습니다.
이 시나리오에서는 AD 그룹을 IAM 그룹에 매핑하는 것이 적용되지 않기 때문에 옵션 A 가
올바르지 않습니다. IAM 은 주로 AWS 리소스에 대한 액세스를 관리하는 데 사용되지만
요구 사항은 액세스 제어를 위해 온프레미스 AD와 통합하는 것입니다.
Restrict 태그 키와 규정 준수 태그 값이 있는 태그를 할당하면 액세스 제어를 위해
온프레미스 AD 와의 필수 통합이 제공되지 않기 때문에 옵션 B 는 올바르지 않습니다.
태그는 리소스를 구성하고 분류하는 데 사용되며 인증 또는 액세스 제어 메커니즘을
제공하지 않습니다.
FSx for Windows File Server 에 직접 연결된 IAM 서비스 연결 역할 생성이 온프레미스
AD 와 통합되지 않기 때문에 옵션 C 는 올바르지 않습니다. IAM 역할은 권한 관리를 위해
AWS 내에서 사용되며 외부 AD 시스템과의 필수 통합을 제공하지 않습니다.
설명2:
FSx for Windows File Server 파일 시스템을 온프레미스 Active Directory 에 결합하면
회사에서 기존 Active Directory 그룹을 사용하여 AWS 로 이동한 후 파일 공유, 폴더 및
파일에 대한 액세스를 제한할 수 있습니다. 이 옵션을 사용하면 회사는 기존 액세스 제어
및 관리 구조를 계속 사용하여 AWS로 보다 원활하게 전환할 수 있습니다.

---

# Q261 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/95011-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
A. 고객이 위치 및 장치 유형에 따라 적절한 버전의 콘텐츠를 받을 수 있습니다.
C. Lambda@Edge 를 생성하면 들어오는 요청의 User-Agent 헤더를 검사하고 사용 중인
장치 유형을 확인할 수 있습니다. 이 정보를 기반으로 응답을 사용자 지정하고 적절한
버전의 콘텐츠를 사용자에게 보낼 수 있습니다.
B. 장치 유형에 따라 다른 콘텐츠 버전을 제공해야 하는 요구 사항을 다루지 않습니다.
D. & E.는 장치별 콘텐츠 요구 사항을 다루지 않습니다.
따라서 옵션 A 와 C 는 고객이 웹 사이트에 액세스하는 데 사용하는 장치에 따라 다양한
버전의 콘텐츠를 제공해야 하는 요구 사항을 충족하기 위한 올바른 작업 조합입니다.
설명
C 의 경우: 향상된 사용자 경험 Lambda@Edge 는 성능 저하 없이 콘텐츠를 개인화할 수
있도록 하여 전 세계 웹 사이트 및 웹 애플리케이션에 대한 사용자 경험을 개선하는 데
도움을 줄 수 있습니다. 실시간 이미지 변환 사용자 특성에 따라 즉시 이미지를 변환하여
사용자 경험을 사용자 정의할 수 있습니다. 예를 들어 뷰어의 장치 유형(모바일, 데스크톱
또는 태블릿)에 따라 이미지 크기를 조정할 수 있습니다. 또한 CloudFront Edge 위치에서
변환된 이미지를 캐싱하여 이미지를 제공할 때 성능을 더욱 향상시킬 수 있습니다.
https://aws.amazon.com/lambda/edge/

---

# Q262 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/95463-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
VPC 간에 피어링 연결을 생성하는 것은 연결을 설정하는 비용 효율적인 방법입니다. 두
VPC 에서 피어링 연결을 위한 라우팅 테이블 항목을 추가하면 두 VPC 간에 트래픽이 흐를
수 있습니다. ElastiCache 클러스터의 보안 그룹에서 인바운드 규칙을 구성하면
애플리케이션 보안 그룹의 인바운드 연결이 허용되어 앱 VPC 의 EC2 인스턴스에서
ElastiCache 클러스터에 액세스할 수 있습니다.
옵션 B 는 이 시나리오에 불필요한 복잡성과 비용을 추가하는 Transit VPC 생성을
제안합니다.
옵션 C 는 인바운드 연결을 제어하는 데 ElastiCache 클러스터의 보안 그룹을 사용해야
하므로 필요하지 않은 피어링 연결의 보안 그룹에 대한 인바운드 규칙 구성을 제안합니다.
옵션 D 는 Transit VPC 의 보안 그룹에 대한 인바운드 규칙 구성을 제안하며, 이는 이
경우에 필요하지 않으며 불필요한 복잡성을 추가합니다.
따라서 옵션 A 는 애플리케이션의 EC2 인스턴스에 ElastiCache 클러스터에 대한 액세스
권한을 제공하는 가장 비용 효율적인 솔루션입니다.
설명2:
두 VPC 간에 피어링 연결을 생성하고 ElastiCache 클러스터의 보안 그룹에 대한 인바운드
규칙을 구성하여 애플리케이션의 보안 그룹에서 인바운드 연결을 허용하는 것이 가장 비용
효율적인 솔루션입니다. 피어링 연결은 무료이며 보안 그룹 규칙을 구성하는 비용만
발생합니다. Transit VPC 솔루션에는 추가 비용이 발생하는 추가 VPC 및 관련 리소스가
필요합니다.
https://aws.amazon.com/certification/policies/before-testing/

---

# Q263 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/95012-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
옵션 B 와 E 는 Kubernetes 컨트롤 플레인과 작업자 노드를 EC2 인스턴스에 배포할 것을
제안합니다. 이렇게 하려면 노력을 최소화해야 한다는 요구 사항과 달리 인프라를 관리하고
지속적인 유지 관리 오버헤드를 추가해야 합니다.
옵션 C 는 ECS 에 대해 Amazon EC2 시작 유형을 사용할 것을 제안합니다. 이 유형은
여전히 EC2 인스턴스 관리가 필요하고 Fargate 를 사용하는 것만큼 비용 효율적이고 확장
가능하지 않습니다.
따라서 Amazon ECS 클러스터와 ECS 서비스를 Fargate 시작 유형(옵션 A 및 D)으로
배포하는 조합은 추가 인프라를 관리하지 않고 유지 관리 및 확장 노력을 최소화하는 데
가장 적합합니다.
설명2:
AWS Fargate 는 Amazon EC2 인스턴스의 서버 또는 클러스터를 관리할 필요 없이
컨테이너를 실행하기 위해 Amazon ECS 와 함께 사용할 수 있는 기술입니다. Fargate 를
사용하면 더 이상 컨테이너를 실행하기 위해 가상 머신의 클러스터를 프로비저닝, 구성
또는 확장할 필요가 없습니다.
https://docs.aws.amazon.com/AmazonECS/latest/userguide/what-is-fargate.html

---

# Q264 

**정답: D**

https://www.examtopics.com/discussions/amazon/view/95345-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
설계자는 ALB 를 생성하고 상태 확인을 구성하여 정상 인스턴스만 트래픽을 수신하도록
합니다. ALB 는 구성된 상태 확인 설정을 기반으로 EC2 인스턴스의 상태를 주기적으로
확인합니다.
Route 53 에서 ALB 로 트래픽을 라우팅하면 DNS 쿼리가 개별 인스턴스 대신 ALB 의 IP
주소를 반환합니다. 이를 통해 ALB 는 정상 인스턴스에만 트래픽을 분산하여 비정상
인스턴스로 인한 시간 초과를 방지할 수 있습니다.
A & B: 상태 확인을 각 레코드와 연결하면 비정상 인스턴스를 식별하는 데 도움이 될 수
있지만 자동 로드 밸런싱 및 정상 인스턴스에 대한 트래픽 배포를 제공하지 않습니다.
C: CloudFront 는 성능과 가용성을 향상시킬 수 있지만 기본적으로 CDN 이며 로드 밸런싱
및 정상 인스턴스에 대한 트래픽 분산 문제를 직접적으로 해결하지 못할 수 있습니다.
따라서 옵션 D 는 상태 확인이 포함된 ALB 를 구현하고 Route 53 을 통해 트래픽을
라우팅하여 시간 초과 오류를 극복하는 데 가장 적합한 솔루션입니다.
설명2:
ALB(Application Load Balancer)를 사용하면 들어오는 트래픽을 여러 백엔드 인스턴스에
분산하고 비정상 인스턴스에서 트래픽을 제거하면서 정상 인스턴스로 트래픽을 자동으로
라우팅할 수 있습니다. EC2 인스턴스 앞에 ALB를 사용하고 Route 53에서 ALB로 트래픽을
라우팅함으로써 로드 밸런서는 인스턴스에 대한 상태 확인을 수행하고 정상 인스턴스로만
트래픽을 라우팅할 수 있으므로 비정상 인스턴스로 인한 시간 초과 오류를 줄이거나
제거하는 데 도움이 됩니다.

---

# Q265 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/95013-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
A. EC2 인스턴스를 퍼블릭 인터넷에 직접 노출하므로 보안이 손상될 수 있습니다.
B. 효율적인 부하 분산과 고가용성을 위해 필요한 퍼블릭 서브넷의 부하 분산 장치가
부족합니다.
D. 로드 밸런싱 및 HTTPS 콘텐츠 전송을 제공하며 EC2 인스턴스를 공용 인터넷에 직접
노출하므로 보안 위험이 발생할 수 있습니다.
C. 퍼블릭 ALB 를 오리진으로 하는 CloudFront 를 사용하여 고가용성, 프라이빗 서브넷을
통한 보안 액세스 및 최적화된 HTTPS 콘텐츠 전송을 제공합니다.
설명2:
이 솔루션은 웹, 애플리케이션 및 데이터베이스 계층이 있는 고가용성 애플리케이션에 대한
요구 사항을 충족할 뿐만 아니라 에지 기반 콘텐츠 전달을 제공합니다. 또한 웹 서버에
대한 직접 액세스를 제한하는 프라이빗 서브넷에 ALB 를 두어 보안을 최대화하는 동시에
퍼블릭 ALB 를 통해 인터넷을 통해 트래픽을 제공할 수 있습니다. 이렇게 하면 웹 서버가
공용 인터넷에 노출되지 않으므로 공격 표면이 줄어들고 애플리케이션에 안전하게 액세스할
수 있습니다.

---

# Q266 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/95014-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
B. CloudFront 는 캐싱 및 콘텐츠 전송에 도움이 될 수 있지만 애플리케이션의 상태를
모니터링하거나 상태 확인을 기반으로 트래픽 리디렉션을 수행하는 메커니즘을 제공하지
않습니다.
C. 이 구성은 정적 콘텐츠 전달에 적합하지만 응용 프로그램의 상태 모니터링 및 트래픽
리디렉션 요구 사항을 다루지 않습니다.
D. 이렇게 하면 성능이 향상될 수 있지만 애플리케이션의 상태를 모니터링하거나 상태
확인을 기반으로 트래픽을 리디렉션하지 않습니다.
따라서 옵션 A는 AWS Global Accelerator를 활용하여 애플리케이션 상태를 모니터링하고,
트래픽을 정상 엔드포인트로 라우팅하고, 지연 시간 문제를 해결하면서 사용자 경험을
최적화하므로 가장 적합한 솔루션입니다.
설명2:
AWS Global Accelerator 는 상태 확인을 기반으로 최적의 정상 엔드포인트로 트래픽을
전달하고 클라이언트의 지리적 위치를 기반으로 가장 가까운 정상 엔드포인트로 트래픽을
라우팅할 수도 있습니다. 액셀러레이터를 구성하고 이를 각 리전의 지역 엔드포인트에
연결하고 ALB 를 엔드포인트로 추가함으로써 솔루션은 트래픽을 정상 엔드포인트로
리디렉션하여 대기 시간을 줄이고 애플리케이션이 최적으로 실행되도록 함으로써 사용자
경험을 개선합니다. 이 솔루션은 트래픽이 가장 가까운 정상 엔드포인트로 전달되도록 하고
전반적인 사용자 경험을 개선하는 데 도움이 됩니다.

---

# Q267 

**정답: D**

https://www.examtopics.com/discussions/amazon/view/95347-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
A. 데이터를 분석 애플리케이션으로 보내려면 Lambda 를 호출해야 합니다. 이로 인해
추가적인 운영 오버헤드와 복잡성이 발생합니다.
B. EMR 은 빅 데이터 처리를 위한 강력한 도구이지만 Kinesis Data Analytics 에 비해 더
많은 운영 관리 및 구성이 필요합니다.
C. Kinesis Data Analytics 가 보다 간소화되고 자동화된 방식으로 분석을 수행할 때 데이터
분석에 EMR을 포함하여 불필요한 복잡성을 도입합니다.
따라서 옵션 D 는 데이터 수집에 Kinesis Data Firehose 를 활용하고 S3 에 데이터를
저장하며 거의 실시간 분석을 위해 Kinesis Data Analytics를 활용하여 데이터 사용 분석 및
암호화를 위한 운영 오버헤드가 낮은 솔루션을 제공하므로 가장 적합한 솔루션입니다. .
설명2:
이 솔루션은 거의 실시간으로 데이터 수집, 데이터 변환, 암호화 및 데이터 저장을
자동으로 처리할 수 있는 완전관리형 서비스인 Amazon Kinesis Data Firehose 를
사용하므로 최소한의 운영 오버헤드로 요구 사항을 충족합니다. Kinesis Data Firehose 는
추가 처리를 위해 Amazon S3 에 Apache Parquet 형식으로 데이터를 자동으로 저장할 수
있습니다.
또한 Amazon Kinesis Data Analytics 애플리케이션을 생성하여 인프라를 관리하거나
Lambda 함수를 호출할 필요 없이 거의 실시간으로 데이터를 분석할 수 있습니다. 이렇게
하면 최소한의 운영 오버헤드로 많은 양의 데이터를 처리할 수 있습니다.

---

# Q268 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/95016-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
A. ElastiCache 는 자주 액세스하는 데이터를 캐싱하여 읽기 성능을 향상시킬 수 있지만
애플리케이션 아키텍처를 변경해야 합니다. 또한 특히 애플리케이션의 데이터베이스 사용에
복잡한 쿼리 또는 빈번한 데이터 업데이트가 포함되는 경우 RDS Proxy 와 동일한 수준의
읽기 성능 향상을 제공하지 못할 수 있습니다.
C. Lambda 는 확장성 및 운영 오버헤드 감소와 같은 이점을 제공할 수 있지만
데이터베이스 읽기 성능 문제를 직접 해결하지 못할 수 있습니다. Lambda 로
마이그레이션하려면 애플리케이션의 아키텍처 및 코드베이스를 크게 변경해야 합니다.
D. DynamoDB 는 확장 가능한 고성능 NoSQL 데이터베이스이지만 MySQL 과 같은 관계형
데이터베이스에서 DynamoDB 로 마이그레이션하려면 애플리케이션의 데이터 모델과 쿼리
패턴을 크게 변경해야 합니다.
따라서 옵션 B 는 RDS Proxy 를 활용하여 데이터베이스 연결을 최적화하고 읽기 성능을
개선하고 애플리케이션 아키텍처의 변경을 최소화하며 데이터베이스 읽기 성능 문제를
해결하기 위한 확장 가능하고 효율적인 솔루션을 제공하므로 가장 적합한 솔루션입니다.

---

# Q269 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/95032-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
A. DynamoDB 는 확장 가능한 NoSQL 데이터베이스이지만 애플리케이션의 데이터 모델 및
쿼리 패턴을 변경해야 합니다.
B. ElastiCache 는 쿼리 성능을 향상시킬 수 있는 인메모리 데이터 저장소이지만 주로
복잡한 쿼리를 실행하기보다는 캐싱에 사용됩니다.
D. Redshift 는 강력한 데이터 웨어하우징 솔루션이지만 데이터를 마이그레이션하고 쿼리를
Redshift 의 열 기반 아키텍처에 적용하려면 애플리케이션 및 쿼리 논리를 크게 변경해야
합니다.
따라서 옵션 C 는 RDS 의 읽기 전용 복제본을 활용하여 기본 데이터베이스에서 읽기 전용
쿼리 트래픽을 오프로드하므로 비즈니스 분석가가 웹 애플리케이션의 성능에 영향을 주지
않고 쿼리를 실행할 수 있으므로 가장 적합한 권장 사항입니다. 기존 웹 애플리케이션에
대한 최소한의 변경으로 확장 가능하고 효율적인 솔루션을 제공합니다.
설명2:
기본 RDS 데이터베이스의 읽기 복제본을 생성하면 기본 데이터베이스에서 읽기 전용 SQL
쿼리를 오프로드하여 웹 애플리케이션의 성능을 향상시키는 데 도움이 됩니다. 읽기
복제본은 읽기 전용 트래픽을 처리하는 데 사용할 수 있는 기본 데이터베이스의 정확한
복사본으로, 기본 데이터베이스의 부하를 줄이고 웹 애플리케이션의 성능을 향상시킵니다.
이 솔루션은 기존 웹 애플리케이션에 대한 최소한의 변경으로 구현할 수 있습니다.
분석가는 코드를 수정하지 않고 읽기 복제본에서 쿼리를 계속 실행할 수 있습니다.

---

# Q270 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/95031-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
클라이언트 측 암호화는 데이터를 Amazon S3 에 업로드하기 전에 데이터를 암호화하는
방법입니다. 이를 통해 사용자는 암호화 프로세스, 암호화 키 및 관련 도구를 관리할 수
있습니다. 클라이언트 측 암호화를 사용하면 Amazon S3 가 암호화 키나 암호화되지 않은
데이터에 액세스할 수 없기 때문에 솔루션은 유휴 및 전송 중에 데이터를 암호화할 수
있습니다.

---

# Q271 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/95018-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
예약된 조정을 구성하여 솔루션 설계자는 배치 작업이 시작될 때 특정 시간(IAM)에 원하는
컴퓨팅 수준으로 자동으로 확장한 다음 작업이 완료되면 자동으로 축소하도록 Auto Scaling
그룹을 설정할 수 있습니다. 이렇게 하면 원하는 EC2 용량에 빠르게 도달할 수 있고 비용
절감에도 도움이 됩니다.

---

# Q272 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/99865-exam-aws-certified-solut
ions-architect-associate-saa-c03/

---

# Q273 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/99505-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
・웜 스탠바이는 감소된 수준의 트래픽을 즉시 처리할 수 있습니다. 그런 다음 이 기존
배포를 확장해야 하므로 파일럿 라이트보다 RTO 시간이 더 짧습니다. 파일럿 라이트를
사용하려면 먼저 인프라를 배포한 다음 워크로드가 요청을 처리할 수 있기 전에 리소스를
확장해야 하기 때문입니다.
https://aws.amazon.com/ko/blogs/architecture/disaster-recovery-dr-architecture-on-aw
s-part-iii-pilot-light-and-warm-standby/
A(X) : 파일럿 라이트를 사용하기 때문에 오답.
B(O) : Amazon Aurora 글로벌 데이터베이스는 여러 리전에 걸쳐 자동으로 복제를 진행
Amazon Aurora Global Database 는 단일 Amazon Aurora 데이터베이스를 여러 AWS
리전으로 확장할 수 있는 기능입니다. 데이터베이스 성능에 전혀 영향을 주지 않고
데이터를 복제하고, 각 리전에서 보통 1 초 미만의 짧은 대기 시간으로 빠른 로컬 읽기를
지원하며, 리전 규모의 가동 중단 발생 시 재해 복구를 제공합니다.""
https://aws.amazon.com/ko/rds/aurora/faqs/
C(X) : 파일럿 라이트를 사용하기 때문에 오답.
D(X) : RDS Multi AZ는 동일 리전 내로 한정됨.
Amazon RDS 다중 AZ 배포는 단일 AWS 리전 내의 데이터베이스 인스턴스에 대한 향상된
가용성을 제공합니다.
https://aws.amazon.com/ko/about-aws/whats-new/2018/01/amazon-rds-read-replicas-
now-support-multi-az-deployments/

---

# Q274 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/99459-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
이를 통해 회사는 RTO(복구 시간 목표)가 4 시간 미만이고 정상 운영 중에 AWS 리소스를
최대한 적게 사용하는 애플리케이션에 대한 재해 복구(DR) 솔루션을 구현할 수 있습니다.
Amazon 머신 이미지(AMI)를 생성하여 EC2 인스턴스를 백업하고 AMI 를 보조 AWS 리전에
복사함으로써 회사는 애플리케이션의 특정 시점 스냅샷을 생성하고 이를 다른 지리적
위치에 저장할 수 있습니다. AWS CloudFormation 을 사용하여 보조 지역의 인프라 배포를
자동화함으로써 회사는 재해 발생 시 템플릿에서 리소스 스택을 신속하게 시작할 수
있습니다. 이는 EC2 인스턴스용 DR 솔루션을 구현하는 비용 효율적이고 운영 효율적인
방법입니다.

---

# Q275 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/99584-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
이 옵션은 아침에 용량을 더 빠르게 확장하여 성능을 개선하지만 작업 외 시간에도 여전히
용량을 축소할 수 있습니다. 다음과 같이 이를 달성합니다.
* 대상 추적 작업은 CPU 사용률 대상에 따라 확장됩니다. 아침에 더 낮은 CPU 임계값에서
트리거함으로써 Auto Scaling 그룹은 트래픽이 증가함에 따라 더 빨리 확장을 시작하여
사용률이 너무 높아져 성능에 영향을 미치기 전에 인스턴스를 시작합니다.
* 휴지 기간을 줄이면 Auto Scaling 이 보다 적극적으로 확장하여 목표에 도달할 때까지 더
많은 인스턴스를 더 빠르게 시작할 수 있습니다. 이렇게 하면 용량 증가 속도가
빨라집니다.
* 그러나 고정된 최소/최대 용량을 설정하는 예약된 작업과 달리 대상 추적을 사용하면
수요에 따라 근무 외 시간에도 그룹을 축소할 수 있습니다. 이는 비용을 최소화하는 데
도움이 됩니다.

---

# Q276 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/99739-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
Auto Scaling Storage RDS 는 스토리지 문제를 완화하고 Oracle Pl/Sql 을 Aurora 로
마이그레이션하는 것은 번거롭습니다. 또한 Aurora 에는 기본적으로 자동 스토리지 확장
기능이 있습니다.
https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIOPS.StorageTypes.
html#USER_PIOPS.Autoscaling

---

# Q277 

**정답: D**

https://www.examtopics.com/discussions/amazon/view/99509-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
* 비디오 콘텐츠의 대규모, 내구성 및 저렴한 스토리지를 위한 Amazon S3. S3 스토리지
비용은 EFS보다 훨씬 저렴합니다.
* Amazon EBS 는 처리 중에 일시적으로만 가능합니다. 비디오를 처리해야 할 때만 EBS
볼륨을 마운트하고 그 후에 마운트를 해제함으로써 컨텐츠가 고가의 EBS 스토리지에
소요되는 시간을 최소화합니다.
* EBS 볼륨은 활성 처리에 필요한 워크로드에 맞게 크기를 조정하여 비용을 낮출 수
있습니다. 볼륨은 전체 비디오 라이브러리를 장기간 저장할 필요가 없습니다.

---

# Q278 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/99940-exam-aws-certified-solut
ions-architect-associate-saa-c03/
참고:
https://docs.aws.amazon.com/ko_kr/prescriptive-guidance/latest/dynamodb-hierarchical
-data-model/introduction.html

---

# Q279 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/99793-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
이 솔루션은 다음과 같은 요구 사항을 충족합니다.
* AWS Backup 은 백업 계획에 정의된 일정(매월 1 일)에 따라 DynamoDB 테이블의 전체
백업을 자동으로 수행합니다.
* 수명 주기 정책은 6 개월 후에 백업을 콜드 스토리지로 전환하여 해당 요구 사항을
충족할 수 있습니다.
* 백업 계획에서 7년 보존 기간을 설정하면 필요에 따라 각 백업이 7년 동안 보존됩니다.
* AWS Backup 은 백업 작업 및 수명 주기 정책을 관리하므로 사용자 지정 스크립팅 또는
관리가 필요하지 않습니다.

---

# Q280 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/99508-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
https://docs.aws.amazon.com/quicksight/latest/user/welcome.html
Athena를 사용하여 S3 버킷의 CloudFront 로그를 쿼리하고 QuickSight를 사용하여 결과를
시각화하는 것이 비용 효율적이고 확장 가능하며 인프라 설정이 필요하지 않기 때문에
최상의 솔루션입니다. 또한 전담 개발자 팀 없이 회사에서 고급 분석을 수행하고 대화형
시각화를 구축할 수 있는 강력한 솔루션을 제공합니다.

---

# Q281 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/99511-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
이 옵션은 다른 가용 영역에 있는 대기 인스턴스에 데이터를 자동으로 복제하여 RDS
데이터베이스 인스턴스에 향상된 가용성과 내구성을 제공하는 DB 인스턴스용 다중 AZ
배포를 사용하기 때문에 가장 효율적입니다. 또한 대기 인스턴스가 동기식 물리적 복제를
사용하여 기본 인스턴스와 동기화 상태를 유지하므로 모든 프로덕션 데이터베이스에 대해
1 초 미만의 복구 지점 목표(RPO)를 제공합니다. 이 솔루션은 모든 프로덕션
데이터베이스에 대해 1초 미만의 RPO 요구 사항을 충족합니다.
옵션 B 는 로드 또는 일정에 따라 DB 인스턴스의 컴퓨팅 용량을 자동으로 조정하는 방법인
하나의 가용 영역에서 DB 인스턴스에 대해 Auto Scaling 을 사용하기 때문에 효율성이
떨어집니다.
그러나 이것은 데이터를 다른 가용 영역에 복제하지 않기 때문에 모든 프로덕션
데이터베이스에 대해 1초 미만의 RPO를 제공하지 않습니다.
옵션 C 는 읽기 트래픽을 제공하고 조정을 지원할 수 있는 기본 데이터베이스의 읽기 전용
복사본인 별도의 가용 영역에서 읽기 전용 복제본을 사용하기 때문에 효율성이 떨어집니다.
그러나 읽기 전용 복제본은 비동기식 복제를 사용하고 기본 데이터베이스보다 지연될 수
있으므로 모든 프로덕션 데이터베이스에 대해 1초 미만의 RPO를 제공하지 않습니다.
옵션 D 는 원본 데이터에 대한 변경 사항을 캡처하고 대상 데이터에 적용하는 작업인 AWS
DMS(AWS Database Migration Service) 변경 데이터 캡처(CDC) 작업을 사용하기 때문에
효율성이 떨어집니다. 그러나 AWS DMS 는 비동기식 복제를 사용하고 소스
데이터베이스보다 지연될 수 있으므로 모든 프로덕션 데이터베이스에 대해 1 초 미만의
RPO를 제공하지 않습니다.

---

# Q282 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/99660-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
ALB 에서 EC2 인스턴스로의 인바운드 트래픽을 제한하려면 EC2 인스턴스의 보안 그룹은
ALB 의 보안 그룹에서 들어오는 트래픽만 허용해야 합니다. 이렇게 하면 EC2 인스턴스는
ALB 에서만 요청을 받을 수 있으며 프라이빗 서브넷 내부 또는 외부의 다른 소스에서는
요청을 받을 수 없습니다.

---

# Q283 

**정답: D**

https://www.examtopics.com/discussions/amazon/view/99512-exam-aws-certified-solut
ions-architect-associate-saa-c03/

---

# Q284 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/99513-exam-aws-certified-solut
ions-architect-associate-saa-c03/

---

# Q285 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/99680-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
이 옵션은 시간 경과에 따른 AWS 비용 및 사용량을 시각화, 이해 및 관리할 수 있는
도구인 Cost Explorer를 사용하기 때문에 가장 효율적입니다. 비용 탐색기에서 사용자 이름
태그를 필터로 사용하여 사용자별로 AWS 청구 항목을 나열하는 보고서를 생성할 수
있습니다. 그런 다음 보고서를 CSV 파일로 다운로드하여 예산 계획에 사용할 수 있습니다.
옵션 A 는 표준 SQL 을 사용하여 Amazon S3 의 데이터를 분석할 수 있는 서버리스 대화형
쿼리 서비스인 Amazon Athena를 사용하기 때문에 효율성이 떨어집니다. S3에서 AWS 비용
및 사용 보고서 데이터를 가리키는 Athena 테이블을 설정한 다음 쿼리를 실행하여
보고서를 생성해야 합니다. 이렇게 하면 추가 비용과 복잡성이 발생합니다.
옵션 C 는 AWS 비용 및 사용량에 대한 높은 수준의 요약을 제공하는 결제 대시보드를
사용하기 때문에 효율성이 떨어집니다. 청구 대시보드에서 청구 세부 정보에 액세스하고
청구서를 통해 다운로드할 수 있지만 사용자별로 청구 항목이 나열되지 않습니다. 추가
단계가 필요한 사용자 이름별로 비용을 그룹화하려면 태그를 사용해야 합니다.
옵션 D 는 서비스 사용량, 서비스 비용 및 인스턴스 예약을 계획할 수 있는 도구인 AWS
예산을 사용하기 때문에 효율성이 떨어집니다. Amazon Simple Email Service(Amazon
SES)로 알리도록 AWS 예산에서 비용 예산을 수정할 수 있지만 이렇게 하면 사용자별로
AWS 청구 항목 보고서가 생성되지 않습니다. 이는 실제 또는 예상 비용이 예산 금액을
초과하거나 초과할 것으로 예상되는 경우에만 알려줍니다.

---

# Q286 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/99669-exam-aws-certified-solut
ions-architect-associate-saa-c03/

---

# Q287 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/99670-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
이 솔루션을 통해 회사는 Amazon FSx for Windows File Server 를 사용하여 계층 간에
Windows 기반 파일 공유를 제공하면서 Amazon EC2 인스턴스에서 세 계층을 모두
호스팅할 수 있습니다. 이를 통해 회사는 기본 백업 및 데이터 품질 서비스와 같은 SQL
Server의 특정 기능을 사용하면서 계층 간에 처리를 위해 파일을 공유할 수 있습니다.

---

# Q288 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/99671-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
Amazon Elastic File System(Amazon EFS) 파일 시스템을 생성합니다. 모든 웹 서버에 EFS
파일 시스템을 마운트합니다. 애플리케이션을 변경하지 않고 Linux 기반 웹 서버용 공유
파일 스토어를 제공해야 한다는 요구 사항을 충족하려면 Amazon EFS 파일 시스템을
사용하는 것이 가장 좋은 솔루션입니다.
Amazon EFS는 여러 Linux 기반 인스턴스에서 파일에 대한 공유 액세스를 제공하는 관리형
NFS 파일 시스템 서비스이므로 이 사용 사례에 적합합니다. Amazon S3 는 파일 시스템이
아닌 객체 스토리지 서비스이고 S3 버킷을 파일 시스템으로 탑재하려면 추가 도구 또는
라이브러리가 필요하기 때문에 이 시나리오에 적합하지 않습니다. Amazon CloudFront 는
콘텐츠 전송 성능을 개선하는 데 사용할 수 있지만 이 요구 사항에는 필요하지 않습니다.
또한 Amazon EBS 볼륨은 한 번에 하나의 인스턴스에만 탑재할 수 있으므로 여러
인스턴스에서 파일을 공유하는 데 적합하지 않습니다.

---

# Q289 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/99756-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
이 옵션은 최소 권한 원칙을 따르고 코드의 자격 증명을 노출하지 않고 Lambda 함수에
필요한 권한만 부여하기 때문에 가장 안전합니다. IAM 역할은 Lambda 함수의 실행 역할로
구성할 수 있으며 IAM 정책은 S3 버킷 ARN 및 s3:GetObject 작업을 지정할 수 있습니다.
옵션 A 는 Lambda 함수보다 더 많은 S3 버킷에 대한 액세스 권한이 있는 보안 주체에게
읽기 액세스 권한을 부여하기 때문에 덜 안전합니다.
옵션 C는 손상되거나 노출될 수 있는 자격 증명을 코드에 내장하기 때문에 덜 안전합니다.
옵션 D 는 계정의 모든 S3 버킷에 대한 읽기 액세스 권한을 부여하기 때문에 덜
안전합니다. 이는 Lambda 함수에 필요한 것보다 많을 수 있습니다.

---

# Q290 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/100006-exam-aws-certified-sol
utions-architect-associate-saa-c03/
참고
https://docs.aws.amazon.com/ko_kr/autoscaling/ec2/userguide/ec2-auto-scaling-mixed
-instances-groups.html

---

# Q291 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/99831-exam-aws-certified-solut
ions-architect-associate-saa-c03/

---

# Q292 

**정답: A**

https://www.examtopics.com/discussions/amazon/view/99834-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
여러 소스에서 실시간 스트리밍 데이터를 수집, 변환 및 쿼리하려면 Amazon Kinesis 와
Amazon MSK 가 적합한 솔루션입니다. Amazon Kinesis Data Streams 는 다양한 소스의
데이터를 스트리밍하고 다른 AWS 서비스와 통합할 수 있습니다. Amazon Kinesis Data
Analytics 는 SQL 또는 Apache Flink 를 사용하여 데이터를 변환할 수 있습니다. Amazon
Kinesis Data Firehose는 Amazon S3 또는 다른 대상에 데이터를 쓸 수 있습니다. Amazon
Athena는 표준 SQL을 사용하여 Amazon S3에서 변환된 데이터를 쿼리할 수 있습니다.
Amazon MSK 는 데이터 스트리밍을 위한 인기 있는 오픈 소스 플랫폼인 Apache Kafka 를
사용하여 데이터를 스트리밍할 수 있습니다. AWS Glue 는 Apache Spark 또는 Python
스크립트를 사용하여 데이터를 변환하고 Amazon S3 또는 기타 대상에 데이터를 쓸 수
있습니다. Amazon Athena 는 표준 SQL 을 사용하여 Amazon S3 에서 변환된 데이터를
쿼리할 수도 있습니다.

---

# Q293 

**정답: D**

https://www.examtopics.com/discussions/amazon/view/99692-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
이 옵션은 온프레미스 소프트웨어 어플라이언스와 클라우드 기반 스토리지를 연결하여
온프레미스 IT 환경과 AWS 스토리지 인프라 간의 데이터 보안 기능과의 원활한 통합을
제공하는 서비스인 AWS Storage Gateway 를 사용하기 때문에 가장 효율적입니다. . 또한
기본 데이터를 로컬에 저장하고 데이터의 특정 시점 스냅샷을 Amazon S3 에 비동기식으로
백업하는 볼륨 게이트웨이 유형인 저장된 볼륨 게이트웨이를 사용합니다. 또한
온프레미스에서 Storage Gateway 소프트웨어 애플리케이션을 실행하고 게이트웨이
스토리지 볼륨을 온프레미스 스토리지에 매핑하므로 기존 스토리지 하드웨어 및 네트워크
인프라를 사용할 수 있습니다. 또한 게이트웨이 스토리지 볼륨을 탑재하여 데이터에 대한
로컬 액세스를 제공하므로 온프레미스에서 지연 시간이 짧은 액세스를 위해 데이터를
사용할 수 있으며 동시에 AWS 에 백업할 수 있습니다. 이 솔루션은 AWS 에 백업되는 동안
모든 데이터에 대한 로컬 액세스를 유지하고 AWS 에 백업된 데이터가 자동으로 안전하게
전송되도록 하는 요구 사항을 충족합니다.
옵션 A는 대량의 데이터를 AWS 안팎으로 전송할 수 있는 물리적 장치인 AWS Snowball을
사용하기 때문에 효율성이 떨어집니다. 그러나 이것은 장치의 수동 취급 및 배송을 필요로
하기 때문에 주기적인 백업 솔루션을 제공하지 않습니다. 또한 데이터에 대한 로컬
액세스를 제공하기 위해 Snowball S3 엔드포인트를 탑재하도록 온프레미스 시스템을
구성하므로 추가적인 복잡성과 지연 시간이 발생할 수 있습니다.
옵션 B 는 일부 AWS 기능을 위한 온보드 스토리지 및 컴퓨팅 기능이 있는 물리적
디바이스인 AWS Snowball Edge 를 사용하기 때문에 효율성이 떨어집니다. 그러나 이것은
장치의 수동 취급 및 배송을 필요로 하기 때문에 주기적인 백업 솔루션을 제공하지
않습니다. 또한 Snowball Edge 파일 인터페이스를 사용하여 온프레미스 시스템에 데이터에
대한 로컬 액세스를 제공하므로 추가적인 복잡성과 지연 시간이 발생할 수 있습니다.
옵션 C는 AWS Storage Gateway를 사용하고 기본 데이터를 Amazon S3에 저장하고 자주
액세스하는 데이터 하위 집합의 복사본을 로컬에 보관하는 일종의 볼륨 게이트웨이인
캐시된 볼륨 게이트웨이를 구성하기 때문에 효율성이 떨어집니다. 그러나 일부 데이터 하위
집합만 로컬로 캐시되기 때문에 모든 데이터에 대한 로컬 액세스를 제공하지는 않습니다.
또한 로컬로 캐시할 데이터의 비율을 구성하므로 저장된 볼륨 게이트웨이를 사용하는
것보다 더 높은 비용과 복잡성이 발생할 수 있습니다.

---

# Q294 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/99954-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
이 옵션은 인터넷 게이트웨이나 VPC 용 NAT 장치 없이 Amazon S3 에 대한 안정적인
연결을 제공하는 Amazon S3 용 게이트웨이 VPC 엔드포인트를 사용하기 때문에 가장
효율적입니다. 게이트웨이 VPC 엔드포인트는 서비스의 접두사 목록을 사용하여 VPC 에서
Amazon S3 로 트래픽을 라우팅하고 AWS 네트워크를 벗어나지 않습니다. 이것은 인터넷을
통과하지 않는다는 요구 사항을 충족합니다.
옵션 A 는 VPC 내의 리소스에 대한 사용자 지정 도메인 이름을 생성할 수 있는 DNS
서비스인 Amazon Route 53을 사용하여 프라이빗 호스팅 영역을 사용하기 때문에 효율성이
떨어집니다. 그러나 이것은 인터넷 게이트웨이나 NAT 장치 없이는 Amazon S3 에 대한
연결을 제공하지 않습니다.
옵션 C 는 NAT 게이트웨이를 사용하여 S3 버킷에 액세스하기 때문에 효율성이 떨어집니다.
S3 버킷은 개인 서브넷의 인스턴스가 인터넷 또는 다른 AWS 서비스에 연결할 수 있도록
지원하지만 인터넷이 이러한 인스턴스와의 연결을 시작하지 못하도록 하는 고가용성 관리형
NAT(Network Address Translation) 서비스입니다. 그러나 이것은 인터넷을 통과하지 않는
요구 사항을 충족하지 못합니다.그러나 이것은 인터넷을 통과하지 않는다는 요구 사항을
충족하지 않습니다.
옵션 D는 온프레미스 네트워크와 VPC 간의 안전하고 암호화된 네트워크 연결인 S3 버킷과
VPC 간에 AWS Site-to-Site VPN 연결을 사용하기 때문에 효율성이 떨어집니다. 그러나
이것은 인터넷을 통과하지 않는다는 요구 사항을 충족하지 않습니다.

---

# Q295 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/99956-exam-aws-certified-solut
ions-architect-associate-saa-c03/

---

# Q296 

**정답: D**

https://www.examtopics.com/discussions/amazon/view/99651-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
허용되는 블록 크기는 /28 넷마스크와 /16 넷마스크 사이입니다. CIDR 블록은 VPC 와
연결된 기존 CIDR 블록과 겹치지 않아야 합니다.
https://docs.aws.amazon.com/vpc/latest/userguide/configure-your-vpc.html

---

# Q297 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/99652-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
* Auto Scaling 그룹은 수요 변화에 맞춰 EC2 인스턴스를 자동으로 확장합니다. 이는
필요한 만큼의 인스턴스만 실행하여 비용을 최적화합니다.
* 대상 추적 조정 정책은 ASGAverageCPUUtilization 지표를 모니터링하고 평균 CPU 를 약
50% 대상 값으로 유지하도록 조정합니다. 이렇게 하면 CPU 가 급증하는 동안 리소스가
충분해집니다.
* ALB 와 대상 그룹은 재사용되므로 애플리케이션 아키텍처가 변경되지 않습니다. Auto
Scaling 그룹은 기존 로드 밸런서 설정에 연결됩니다.
* 최소 2 개에서 최대 6 개의 인스턴스는 수요에 따라 필요에 따라 3 개에서 6 개 사이의
인스턴스를 확장할 수 있는 기능을 제공합니다.
* 단 3 개의 인스턴스(원하는 용량)로 시작하고 필요에 따라 확장하여 비용을 최적화합니다.
CPU 사용량이 떨어지면 원하는 용량에 맞게 인스턴스가 종료됩니다.

---

# Q298 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/99653-exam-aws-certified-solut
ions-architect-associate-saa-c03/
참고:
https://aws.amazon.com/ko/vpc/faqs/#:~:text=Can%20a%20subnet%20span%20Availabil
ity

---

# Q299 

**정답: B**

https://www.examtopics.com/discussions/amazon/view/99676-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
원시 데이터를 저장할 Amazon S3 버킷 생성 영구 SSD 스토리지를 사용하는 Amazon FSx
for Lustre 파일 시스템 생성 Amazon S3 에서 데이터를 가져오고 내보내는 옵션 선택 EC2
인스턴스에 파일 시스템을 탑재합니다. Amazon FSx for Lustre 는 밀리초 미만의 지연
시간과 최대 6GBps의 처리량을 위해 SSD 스토리지를 사용하고 Amazon S3에서 데이터를
가져오고 내보낼 수 있습니다. 또한 영구 SSD 스토리지를 선택하는 옵션은 데이터가
디스크에 저장되고 파일 시스템이 중지되어도 손실되지 않도록 합니다.

---

# Q300 

**정답: C**

https://www.examtopics.com/discussions/amazon/view/99948-exam-aws-certified-solut
ions-architect-associate-saa-c03/
참고:
https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMySQL.
html