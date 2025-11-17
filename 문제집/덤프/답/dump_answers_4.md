# Q301 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/99659-exam-aws-certified-solut
ions-architect-associate-saa-c03/
~~~

---

# Q302 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/99693-exam-aws-certified-solut
ions-architect-associate-saa-c03/
~~~

---

# Q303 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/99813-exam-aws-certified-solut
ions-architect-associate-saa-c03/
참고
https://docs.aws.amazon.com/ko_kr/autoscaling/application/userguide/what-is-applicati
on-auto-scaling.html
~~~

---

# Q304 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/99949-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
이 옵션은 온프레미스와 AWS 스토리지 서비스 간에 데이터 이동을 자동화하고 가속화하는
안전한 온라인 서비스인 AWS DataSync 를 사용하기 때문에 가장 효율적입니다. 또한
DataSync 를 사용하여 정기적으로 두 리전의 NFS 파일 시스템 간에 대량의 데이터를
주고받으며 최소한의 운영 오버헤드로 데이터 전송 프로세스를 단순화하고 가속화합니다.
이 솔루션은 최소한의 운영 오버헤드로 정기적으로 두 리전의 NFS 파일 시스템 간에
대량의 데이터를 주고받는 요구 사항을 충족합니다.
옵션 B 는 대량의 데이터를 AWS 안팎으로 전송할 수 있는 물리적 디바이스인 AWS
Snowball 디바이스를 사용하기 때문에 효율성이 떨어집니다. 그러나 이것은 장치의 수동
취급 및 배송을 필요로 하기 때문에 주기적인 데이터 전송 솔루션을 제공하지 않습니다.
옵션 C 는 Amazon S33 에 저장된 파일에 대한 보안 파일 전송 프로토콜(SFTP) 액세스를
제공하는 방법인 Amazon EC2 에 SFTP 서버를 설정하기 때문에 효율성이 떨어집니다.
그러나 파일 전송을 수동으로 시작하고 모니터링해야 하므로 주기적인 데이터 전송
솔루션을 제공하지 않습니다.
옵션 D 는 데이터베이스를 AWS 로 빠르고 안전하게 마이그레이션하는 데 도움이 되는
서비스인 AWS DMS(AWS Database Migration Service)를 사용하기 때문에 효율성이
떨어집니다. 그러나 이것은 관계형 데이터베이스 및 비관계형 데이터 저장소만 지원하므로
NFS 파일 시스템용 데이터 전송 솔루션을 제공하지 않습니다.
~~~

---

# Q305 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/99809-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
Amazon FSx for Windows File Server(Amazon FSx)는 서버 메시지 블록(SMB) 프로토콜을
사용하는 Windows Server 에 구축된 완전 관리형, 고가용성 및 확장 가능한 파일 스토리지
솔루션입니다. 다른 중요한 엔터프라이즈 기능 중에서 Microsoft Active Directory 통합,
데이터 중복 제거 및 완전히 관리되는 백업을 허용합니다.
https://aws.amazon.com/blogs/storage/accessing-smb-fileshares-remotely-with-amazo
n-fsx-for-windows-file-server/
~~~

---

# Q306 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/99807-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
* 단일 AZ 내에서 인스턴스를 시작하고 클러스터 배치 그룹을 사용하면 네트워크 대기
시간이 가장 짧고 인스턴스 간 대역폭이 가장 높습니다. 이는 메모리 데이터베이스 및
처리량이 많은 애플리케이션의 성능을 최대화합니다.
* 동일한 AZ 에 있는 인스턴스와 배치 그룹 간의 통신은 무료이므로 데이터 전송 요금이
최소화됩니다. AZ 간 및 퍼블릭 IP 트래픽에는 요금이 발생할 수 있습니다.
* 클러스터 배치 그룹을 사용하면 인스턴스를 AZ 내에서 서로 가깝게 배치할 수 있으므로
필요한 높은 네트워크 처리량이 가능합니다. 파티션 그룹은 AZ 에 걸쳐 있으므로 대역폭이
줄어듭니다.
* 영역 간 Auto Scaling 은 AZ 에서 인스턴스를 시작하여 데이터 전송 요금을 증가시킬 수
있습니다. 네트워크 처리량이 줄어들어 성능에 영향을 미칠 수 있습니다.
~~~

---

# Q307 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/99611-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
AWS Storage Gateway Volume Gateway는 iSCSI 스토리지에 연결하기 위한 두 가지 구성,
즉 저장 볼륨과 캐시 볼륨을 제공합니다. 저장된 볼륨 구성은 전체 데이터 세트를
온프레미스에 저장하고 데이터를 AWS 에 비동기식으로 백업합니다. 캐싱된 볼륨 구성은
최근에 액세스한 데이터를 온프레미스에 저장하고 나머지 데이터는 Amazon S3 에
저장합니다. 회사는 최근에 액세스한 데이터만 로컬에 저장하기를 원하므로 캐시된 볼륨
구성이 가장 적절할 것입니다. 이를 통해 회사는 자주 액세스하는 데이터를 온프레미스에
보관하고 iSCSI 스토리지 확장의 필요성을 줄이면서 AWS 클라우드를 통해 모든 데이터에
대한 액세스를 계속 제공할 수 있습니다. 또한 이 구성은 자주 액세스하는 데이터에 대한
짧은 대기 시간 액세스와 자주 액세스하지 않는 데이터에 대한 비용 효율적인 오프사이트
백업을 제공합니다.
https://docs.amazonaws.cn/en_us/storagegateway/latest/vgw/StorageGatewayConcepts.
html#stora
~~~

---

# Q308 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/99936-exam-aws-certified-solut
ions-architect-associate-saa-c03/
~~~

---

# Q309 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/99803-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
S3 Storage Lens 는 객체 스토리지 사용량, 활동 추세 및 비용 최적화를 위한 권장 사항에
대한 종합적인 보기를 제공하는 완전관리형 S3 스토리지 분석 솔루션입니다. Storage
Lens 를 사용하면 모든 S3 버킷에서 객체 액세스 패턴을 분석하고 자세한 지표와 보고서를
생성할 수 있습니다.
~~~

---

# Q310 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/99697-exam-aws-certified-solut
ions-architect-associate-saa-c03/
참고:
https://docs.aws.amazon.com/ko_kr/AmazonCloudFront/latest/DeveloperGuide/PrivateCo
ntent.html
~~~

---

# Q311 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/99627-exam-aws-certified-solut
ions-architect-associate-saa-c03/
참고:
https://aws.amazon.com/getting-started/hands-on/filter-messages-published-to-topics
/
~~~

---

# Q312 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/99785-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
이러한 요구 사항을 충족하는 운영상 가장 효율적인 솔루션은 AWS Backup 을 사용하여
야간 백업을 수행하고 백업을 다른 리전에 복사하는 백업 계획을 만드는 것입니다.
애플리케이션의 EBS 볼륨을 리소스로 추가하면 애플리케이션의 EC2 인스턴스 구성 및
데이터가 백업되고 백업을 다른 리전에 복사하면 애플리케이션을 다른 AWS 리전에서
복구할 수 있습니다.
~~~

---

# Q313 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/100130-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
Amazon CloudFront 는 짧은 지연 시간과 높은 전송 속도로 데이터, 비디오, 애플리케이션
및 API 를 전 세계 고객에게 안전하게 전달하는 콘텐츠 전송 네트워크(CDN)입니다.
CloudFront 는 콘텐츠에 대한 인증된 액세스를 제공하는 서명된 URL 을 지원합니다. 이
기능을 통해 회사는 콘텐츠에 액세스할 수 있는 사람과 기간을 제어하여 수백만 명의
사용자에게 안전하고 확장 가능한 솔루션을 제공할 수 있습니다.
~~~

---

# Q314 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/99769-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
Amazon Aurora Serverless for MySQL 은 애플리케이션 수요에 따라 자동으로 확장 또는
축소되는 완전관리형 자동 확장 관계형 데이터베이스 서비스입니다. 이 서비스는 고객이
데이터베이스 인스턴스를 프로비저닝할 필요 없이 고가용성, 내구성 및 보안과 같은
Amazon Aurora 의 모든 기능을 제공합니다. Amazon Aurora Serverless for MySQL 을
사용하면 증가한 트래픽을 수용할 수 있도록 데이터베이스가 자동으로 확장되도록
설계되었기 때문에 영업 팀은 다운타임을 최소화할 수 있습니다. 또한 이 서비스를 통해
고객은 사용한 용량에 대해서만 비용을 지불할 수 있으므로 자주 사용하지 않는 액세스
패턴에 대해 비용 효율적입니다. Amazon RDS for MySQL 도 옵션이 될 수 있지만 고객이
인스턴스 유형을 선택해야 하고 데이터베이스 관리자는 증가하는 트래픽을 수용하기 위해
수동으로 인스턴스 크기를 모니터링하고 조정해야 합니다.
~~~

---

# Q315 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/99808-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
Amazon Inspector(Amazon 검사기):
* EC2 인스턴스의 활성 취약성 스캔을 수행합니다. 소프트웨어 취약성, 의도하지 않은
네트워크 접근성 및 기타 보안 문제를 찾습니다.
* 스캔을 수행하려면 EC2 인스턴스에 에이전트를 설치해야 합니다. 에이전트는 각
인스턴스에 배포되어야 합니다.
* 보안 위험 또는 취약점에 대한 발견 사항을 자세히 설명하는 예약 검사 보고서를
제공합니다. 이러한 보고서는 문제를 패치하거나 수정하는 데 사용할 수 있습니다.
* AWS 환경에서 보안 취약점 및 잘못된 구성을 사전에 감지하는 데 가장 적합합니다.
~~~

---

# Q316 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/99698-exam-aws-certified-solut
ions-architect-associate-saa-c03/
~~~

---

# Q317 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/99817-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
이 솔루션은 COTS 애플리케이션이 최소한의 운영 오버헤드로 레거시 애플리케이션이
생성하는 데이터를 사용할 수 있도록 솔루션 구현 요구 사항을 충족합니다. AWS Glue 는
분석을 위해 데이터를 준비하고 로드하는 서버리스 ETL 플랫폼을 제공하는 완전 관리형
서비스입니다.
AWS Glue 는 .csv 파일을 비롯한 다양한 형식의 데이터를 처리하고 복잡한 SQL 쿼리를
지원하는 완전관리형 데이터 웨어하우스 서비스인 Amazon Redshift 에 처리된 데이터를
저장할 수 있습니다. AWS Glue 는 데이터 처리 및 로드 프로세스를 자동화할 수 있는
일정에 따라 ETL 작업을 실행할 수 있습니다.
옵션 B 는 올바르지 않습니다. Amazon EC2 인스턴스에서 실행되는 Python 스크립트를
개발하여 .csv 파일을 sql 파일로 변환하면 운영 오버헤드와 복잡성이 증가하고 COTS
애플리케이션에 일관된 데이터 처리 및 로드를 제공하지 못할 수 있기 때문입니다.
.csv 파일을 처리하고 처리된 데이터를 DynamoDB 테이블에 저장하기 위해 AWS Lambda
함수 및 Amazon DynamoDB 테이블을 생성하는 것은 Amazon Redshift 를 COTS
애플리케이션의 데이터 소스로 사용하기 위한 요구 사항을 충족하지 않기 때문에 옵션 C 는
올바르지 않습니다.
Amazon EventBridge(Amazon CloudWatch Events)를 사용하여 주간 일정에 따라 Amazon
EMR 클러스터를 시작하여 .csv 파일을 처리하고 처리된 데이터를 Amazon Redshift
테이블에 저장할 수 있으므로 옵션 D 는 올바르지 않습니다. COTS 애플리케이션에 적시에
데이터 처리 및 로드를 제공하지 않습니다.
참조:
https://aws.amazon.com/glue/
https://aws.amazon.com/redshift/
~~~

---

# Q318 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/99804-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
A) AWS CloudTrail 을 활성화하고 감사에 사용합니다. AWS CloudTrail 은 API 호출 기록을
제공하며 EC2 인스턴스 및 보안 그룹에 대한 변경 사항을 감사하는 데 사용할 수 있습니다.
솔루션 설계자는 CloudTrail 로그를 분석하여 적절한 승인 없이 누가 대규모 인스턴스를
프로비저닝했거나 보안 그룹을 수정했는지 추적할 수 있습니다.
D) AWS Config를 활성화하고 감사 및 규정 준수를 위한 규칙을 생성합니다. AWS Config는
EC2 인스턴스 및 보안 그룹과 같은 리소스에 대한 구성 변경 사항을 기록할 수 있습니다.
솔루션 설계자는 특정 인스턴스 유형을 시작하거나 권한 없이 보안 그룹 포트를 여는 것과
같은 비준수 변경 사항을 모니터링하기 위해 AWS Config 규칙을 생성할 수 있습니다. AWS
Config는 이러한 규칙 위반에 대해 경고합니다.
~~~

---

# Q319 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/99628-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
Session Manager 는 완전히 관리되는 AWS Systems Manager 기능입니다. Session
Manager를 사용하여 Amazon Elastic Compute Cloud(Amazon EC2) 인스턴스, 에지 장치,
온프레미스 서버 및 가상 머신(VM)을 관리할 수 있습니다. 대화형 원클릭 브라우저 기반 셸
또는 AWS Command Line Interface(AWS CLI)를 사용할 수 있습니다. Session Manager는
인바운드 포트를 열거나 배스천 호스트를 유지하거나 SSH 키를 관리할 필요 없이 안전하고
감사 가능한 노드 관리를 제공합니다.
또한 Session Manager 를 사용하면 관리 노드에 대한 제어된 액세스, 엄격한 보안 관행,
노드 액세스 세부 정보가 포함된 완전히 감사 가능한 로그가 필요한 기업 정책을 준수하는
동시에 최종 사용자에게 관리 노드에 대한 간단한 원클릭 교차 플랫폼 액세스를 제공할 수
있습니다.
https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html
~~~

---

# Q320 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/99752-exam-aws-certified-solut
ions-architect-associate-saa-c03/
참고
https://docs.aws.amazon.com/ko_kr/kinesisanalytics/latest/dev/what-is.html
~~~

---

# Q321 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/99685-exam-aws-certified-solut
ions-architect-associate-saa-c03/
~~~

---

# Q322 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/99753-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
이 옵션은 메시지 손실이나 다른 서비스를 사용할 필요 없이 모든 볼륨의 소프트웨어 구성
요소 간에 메시지를 전송, 저장 및 수신할 수 있는 완전 관리형 메시지 대기열 서비스인
Amazon SQS 를 사용하기 때문에 가장 효율적입니다. 또한 SQS 메시지 대기열을 사용하여
서로 다른 애플리케이션 계층에 요청을 비동기식으로 전달하여 썸네일 생성 프로세스에서
이미지 업로드 프로세스를 분리하고 확장성과 안정성을 활성화합니다. 또한 이미지가
수신되었다는 애플리케이션 메시지를 통해 사용자에게 경고하므로 섬네일 생성이 완료될
때까지 기다리는 것보다 사용자에게 더 빠른 응답 시간을 제공합니다.
옵션 A 는 서버를 프로비저닝하거나 관리하지 않고 코드를 실행하는 방법인 사용자 지정
AWS Lambda 함수를 사용하여 썸네일을 생성하고 사용자에게 경고하기 때문에 효율성이
떨어집니다.
그러나 이것은 썸네일 생성 프로세스에서 이미지 업로드 프로세스를 분리하기 위해 비동기
디스패치 메커니즘을 사용하지 않습니다. 또한 이미지 업로드 프로세스를 이벤트 소스로
사용하여 Lambda 함수를 호출하므로 한 번에 업로드된 이미지가 많은 경우 동시성 문제가
발생할 수 있습니다.
옵션 B 는 애플리케이션의 구성 요소를 일련의 단계로 배열하고 시각화하는 그래픽 콘솔을
제공하는 완전관리형 서비스인 AWS Step Functions 를 사용하기 때문에 효율성이
떨어집니다. 그러나 이것은 썸네일 생성 프로세스에서 이미지 업로드 프로세스를 분리하기
위해 비동기 디스패치 메커니즘을 사용하지 않습니다. 또한 Step Functions 를 사용하여
애플리케이션 계층 간의 오케스트레이션을 처리하고 썸네일 생성이 완료되면 사용자에게
경고하므로 추가적인 복잡성과 대기 시간이 발생할 수 있습니다.
옵션 D는 SMS 문자 메시지 또는 이메일을 통해 메시지 또는 알림을 사용자에게 직접 보낼
수 있는 완전 관리형 메시징 서비스인 Amazon SNS 를 사용하기 때문에 효율성이
떨어집니다. 그러나 이것은 썸네일 생성 프로세스에서 이미지 업로드 프로세스를 분리하기
위해 비동기 디스패치 메커니즘을 사용하지 않습니다. 또한 SNS 알림 주제 및 구독을
사용하여 이미지 업로드가 완료된 후 썸네일을 생성하고 썸네일 생성이 완료된 후 푸시
알림을 통해 사용자의 모바일 앱에 메시지를 보내므로 추가적인 복잡성과 대기 시간이
발생할 수 있습니다.
~~~

---

# Q323 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/99699-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
Amazon API Gateway를 HTTPS 엔드포인트로 배포하고 AWS Lambda를 배포하여 메시지를
처리하고 Amazon DynamoDB 테이블에 저장합니다. 이 옵션은 대량의 데이터를 쉽게
처리할 수 있는 가용성과 확장성이 뛰어난 솔루션을 제공합니다. 또한 다른 AWS 서비스와
통합되어 보안 팀의 데이터를 보다 쉽게 분석하고 시각화할 수 있습니다.
~~~

---

# Q324 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/99711-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
"회사는 최종 사용자가 온프레미스 시스템의 모든 파일 유형에 즉시 액세스할 수 있기를
원합니다."
- 캐싱된 볼륨(Cached volumes): 가장 최근 데이터에 대한 액세스 대기 시간이 짧습니다.
- 저장 볼륨(Stored volumes): 전체 데이터 세트는 온프레미스이며 S3 로 예약 백업되므로
볼륨 게이트웨이 저장 볼륨이 적절한 선택입니다.
~~~

---

# Q325 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/99754-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
Amazon Cognito 자격 증명 풀은 인증된 사용자에게 AWS 리소스에 액세스할 수 있는
권한이 제한된 임시 자격 증명 세트를 할당합니다. 각 사용자의 권한은 생성한 IAM 역할을
통해 제어됩니다.
https://docs.aws.amazon.com/cognito/latest/developerguide/role-basedaccess-control.
html
~~~

---

# Q326 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/99755-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
S3 Intelligent-Tiering 은 성능 영향, 검색 비용 또는 운영 오버헤드 없이 액세스 빈도에
따라 가장 비용 효율적인 액세스 계층으로 데이터를 자동으로 이동하는 스토리지
클래스입니다. 회사 자산과 같이 액세스 패턴을 알 수 없거나 변경하는 데이터에
이상적입니다. 30 일 후에 자산을 S3 Intelligent-Tiering 으로 이동함으로써 회사는 저장된
자산의 고가용성과 복원력을 유지하면서 스토리지 비용을 최적화할 수 있습니다.
S3 수명 주기는 개체가 수명 주기 동안 비용 효율적으로 저장되도록 개체를 관리할 수
있게 해주는 기능입니다. 수명 주기 규칙을 생성하여 Amazon S3 가 객체 그룹에 적용하는
작업을 정의할 수 있습니다. 작업 중 하나는 업로드가 중단될 때 발생할 수 있는 불완전한
멀티파트 업로드를 중단하는 것입니다. 불완전한 멀티파트 업로드를 정리하도록 S3 수명
주기 정책을 구성함으로써 회사는 스토리지 비용을 줄이고 사용하지 않는 부분에 대한 비용
지불을 피할 수 있습니다.
만료된 객체 삭제 마커는 Amazon S3 에서 자동으로 삭제되고 스토리지 비용이 발생하지
않기 때문에 옵션 C는 올바르지 않습니다. 따라서 만료된 객체 삭제 마커를 정리하도록 S3
수명 주기 정책을 구성해도 회사의 스토리지 비용에는 영향을 미치지 않습니다.
옵션 D 는 올바르지 않습니다. S3 Standard-IA 는 자주 액세스하지 않지만 필요할 때
신속하게 액세스해야 하는 데이터용 스토리지 클래스이기 때문입니다. S3 Standard 보다
저장 비용은 낮지만 검색 비용은 더 높고 최소 저장 기간 요금은 30일입니다. 따라서 30일
후에 자산을 S3 Standard-IA 로 이동해도 자산에 여전히 가끔 액세스하는 경우 회사의
스토리지 비용이 최적화되지 않을 수 있습니다.
옵션 E 는 올바르지 않습니다. S3 One Zone-IA 는 자주 액세스하지 않지만 필요할 때
신속하게 액세스해야 하는 데이터용 스토리지 클래스이기 때문입니다. S3 Standard-IA보다
스토리지 비용이 저렴하지만 하나의 가용 영역에만 데이터를 저장하고 다른 스토리지
클래스보다 복원력이 떨어집니다. 또한 검색 비용이 더 높고 최소 저장 기간 요금이
30일입니다. 따라서 30일 후에 자산을 S3 One Zone-IA로 이동하면 자산이 여전히 가끔씩
액세스되거나 고가용성이 필요한 경우 회사의 스토리지 비용이 최적화되지 않을 수
있습니다.
참조 URL:
https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html
https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html
https://docs.aws.amazon.com/AmazonS3/latest/userguide/delete-or-empty-bucket.html
#deletebucket-considerations
https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html
https://aws.amazon.com/certification/certified-solutions-architect-associate/
~~~

---

# Q327 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/99795-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
EC2 에서 네트워크 방화벽으로 아웃바운드 연결을 보냅니다. 네트워크 방화벽에서
소프트웨어 패치 다운로드를 위해 특정 도메인을 허용하고 다른 모든 도메인을 거부하는
상태 저장 아웃바운드 규칙을 생성합니다.
~~~

---

# Q328 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/99704-exam-aws-certified-solut
ions-architect-associate-saa-c03/
~~~

---

# Q329 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/99796-exam-aws-certified-solut
ions-architect-associate-saa-c03/
~~~

---

# Q330 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/99702-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
Amazon RDS의 유휴 데이터를 암호화하려면 AWS Key Management Service(AWS KMS)를
사용하는 Amazon RDS 의 암호화 기능을 사용할 수 있습니다. 이 기능을 통해 Amazon
RDS는 고유한 키로 각 데이터베이스 인스턴스를 암호화합니다. 이 키는 AWS KMS에 의해
안전하게 저장됩니다. 자체 키를 관리하거나 기본 AWS 관리형 키를 사용할 수 있습니다.
DB 인스턴스에 대한 암호화를 활성화하면 Amazon RDS가 자동 백업, 읽기 전용 복제본 및
스냅샷을 비롯한 기본 스토리지를 암호화합니다.
~~~

---

# Q331 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/99603-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
AWS Snowball은 AWS 클라우드 안팎으로 대량의 데이터 이동을 가속화하는 안전한 데이터
전송 솔루션입니다. 한 번에 최대 80TB 의 데이터를 이동할 수 있고 최대 50Mbps 의
네트워크 대역폭을 제공하므로 작업에 적합합니다. 또한 안전하고 사용하기 쉬우므로 이
마이그레이션에 이상적인 솔루션입니다.
~~~

---

# Q332 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/99792-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
Windows 파일 서버는 온프레미스이며 데이터를 클라우드에 복제할 무언가가 필요합니다.
우리가 가진 유일한 옵션은 Windows 파일 서버용 AWS FSx 입니다. 또한 정보가 기밀이고
민감하기 때문에 적절한 사용자가 안전한 방식으로 정보에 액세스할 수 있도록 해야
합니다.
https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html
~~~

---

# Q333 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/99791-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
월별 일정을 기반으로 EC2 Auto Scaling 예약 조정 정책을 구성하는 것이 가장 좋은
옵션입니다. 이는 월별 배치 실행이 시작되기 전에 EC2 인스턴스의 사전 조정을 허용하기
때문입니다. 이렇게 하면 애플리케이션이 다운타임 없이 증가된 워크로드를 처리할 수
있습니다. 예약된 조정 정책은 배치 실행 몇 시간 전에 Auto Scaling 그룹의 인스턴스 수를
늘리고 배치 실행이 완료된 후 인스턴스 수를 줄이도록 구성할 수 있습니다. 이렇게 하면
필요할 때 리소스를 사용할 수 있고 필요하지 않을 때 리소스를 낭비하지 않을 수 있습니다.
월별 배치 실행 중에 증가된 워크로드를 처리하고 다운타임을 방지하는 가장 적절한
솔루션은 월별 일정을 기반으로 EC2 Auto Scaling 예약 조정 정책을 구성하는 것입니다.
https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scheduled-
scaling.html
~~~

---

# Q334 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/99703-exam-aws-certified-solut
ions-architect-associate-saa-c03/
~~~

---

# Q335 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/99686-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명
스냅샷에서 Amazon Elastic Block Store(Amazon EBS) 빠른 스냅샷 복원을 활성화하면
스냅샷에서 새 Amazon Machine Image(AMI)를 빠르게 생성할 수 있으므로 새 인스턴스를
프로비저닝할 때 초기화 지연 시간을 줄이는 데 도움이 됩니다. AMI 가 프로비저닝되면
Auto Scaling 그룹의 AMI 를 새 AMI 로 교체할 수 있습니다. 이렇게 하면 업데이트된
AMI에서 새 인스턴스가 시작되고 증가된 수요를 신속하게 충족할 수 있습니다.
~~~

---

# Q336 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/99790-exam-aws-certified-solut
ions-architect-associate-saa-c03/
~~~

---

# Q337 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/99871-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
옵션 A 는 애플리케이션 코드를 크게 변경하지 않고 복제 지연을 줄이고 진행 중인 운영
오버헤드를 최소화하는 가장 적합한 솔루션입니다. 데이터베이스를 Amazon Aurora
MySQL 로 마이그레이션하면 MySQL 용 Amazon RDS 에 비해 복제 성능과 확장성이
향상됩니다. Aurora 복제본은 더 빠른 복제를 제공하여 복제 지연을 줄이고 Aurora Auto
Scaling은 들어오는 트래픽을 처리하기에 충분한 Aurora 복제본이 있는지 확인합니다. 또한
Aurora MySQL 기본 기능은 저장 프로시저를 대체하여 데이터베이스의 부하를 줄이고
성능을 향상시킬 수 있습니다.
~~~

---

# Q338 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/99758-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
기본 DB 클러스터에서 모든 보조로의 복제는 데이터베이스 엔진이 아닌 Aurora 스토리지
계층에서 처리하므로 변경 사항 복제 지연 시간은 일반적으로 1 초 미만으로 최소화됩니다.
데이터베이스 엔진을 복제 프로세스에서 제외한다는 것은 데이터베이스 엔진이 워크로드
처리 전용임을 의미합니다. 또한 Aurora MySQL binlog(이진 로깅) 복제를 구성하거나
관리할 필요가 없음을 의미합니다.
~~~

---

# Q339 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/99705-exam-aws-certified-solut
ions-architect-associate-saa-c03/
~~~

---

# Q340 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/99708-exam-aws-certified-solut
ions-architect-associate-saa-c03/
~~~

---

# Q341 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/99710-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명:
Amazon QuickSight 및 AWS Lake Formation을 사용하여 열 수준 권한 부여를 시행합니다.
https://aws.amazon.com/ko/blogs/big-data/enforce-column-level-authorization-with-a
mazon-quicksight-and-aws-lake-formation/
~~~

---

# Q342 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/100204-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
이 옵션은 기계 학습을 사용하여 CloudWatch 의 기록 데이터를 기반으로 용량 요구 사항을
예측하는 일종의 조정 정책인 Auto Scaling 그룹에 대한 예측 조정 정책을 사용하기 때문에
가장 효율적입니다. 또한 Auto Scaling 그룹이 트래픽 변경에 앞서 용량을 조정할 수
있도록 예측을 기반으로 확장하도록 정책을 구성합니다. 또한 조정 메트릭을 CPU 사용률로
설정하고 메트릭의 대상 값을 60%로 설정합니다. 이는 각 실행에서 기록되는 기준 CPU
사용률과 일치합니다. 또한 작업이 실행되기 30 분 전에 인스턴스를 사전 실행하도록
설정하여 매주 스크립팅된 배치 작업이 시작되기 전에 충분한 용량이 프로비저닝되도록
합니다. 이 솔루션은 최소한의 운영 오버헤드로 작업이 실행되기 30 분 전에 용량을
프로비저닝해야 하는 요구 사항을 충족합니다.
옵션 A 는 변화하는 수요에 대응하여 Auto Scaling 그룹의 용량을 조정하는 일종의 조정
정책인 Auto Scaling 그룹에 대한 동적 조정 정책을 사용하기 때문에 효율성이 떨어집니다.
그러나 이것은 변화하는 트래픽에만 반응하기 때문에 작업 실행 30 분 전에 용량을
프로비저닝하는 방법을 제공하지 않습니다.
옵션 B는 생성한 일정에 따라 Auto Scaling 그룹을 조정할 수 있는 조정 정책 유형인 Auto
Scaling 그룹에 대해 예약된 조정 정책을 사용하기 때문에 효율성이 떨어집니다. 그러나
미리 정의된 지표 및 정책에 따라서만 확장되므로 예측 또는 CPU 사용률을 기반으로
확장하는 방법을 제공하지 않습니다.
옵션 D 는 Auto Scaling 그룹의 CPU 사용률 지표 값이 60%에 도달할 때 Amazon
EventBridge 이벤트를 사용하여 AWS Lambda 함수를 호출하기 때문에 효율성이
떨어집니다. 이는 이벤트를 기반으로 서버리스 함수를 트리거하는 방법입니다. 그러나
이것은 변화하는 트래픽에만 반응하기 때문에 작업 실행 30 분 전에 용량을 프로비저닝하는
방법을 제공하지 않습니다.
~~~

---

# Q343 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/100302-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
MySQL 데이터베이스를 Amazon Aurora 글로벌 데이터베이스로 마이그레이션하는 것이
최소한의 운영 오버헤드가 필요하기 때문에 최상의 솔루션입니다. Aurora 는 자동 장애
조치를 제공하는 관리형 서비스이므로 대기 인스턴스를 수동으로 구성할 필요가 없습니다.
기본 DB 클러스터는 기본 리전에서 호스팅할 수 있고 보조 DB 클러스터는 DR 리전에서
호스팅할 수 있습니다. 이 접근 방식을 통해 상당한 수동 개입 없이 데이터를 여러
리전에서 항상 사용 가능하고 최신 상태로 유지할 수 있습니다.
~~~

---

# Q344 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/100202-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q345 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/100341-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
https://aws.amazon.com/blogs/networking-and-content-delivery/adding-http-security-h
eadersusing-lambdaedge-and-amazon-cloudfront/
Amazon CloudFront 는 웹 콘텐츠, 비디오 및 API 를 대규모로 안전하게 전송할 수 있는
글로벌 콘텐츠 전송 네트워크(CDN) 서비스입니다. 인증을 위해 Cognito와 통합하고 인증을
위해 Lambda@Edge 와 통합하므로 전 세계적으로 웹 콘텐츠를 제공하는 데 이상적인
선택입니다. Lambda@Edge 는 AWS Lambda 기능을 사용자에게 더 가까운 곳에서
전역적으로 실행할 수 있는 서비스로, 지연 시간을 줄이고 응답 시간을 단축합니다. 또한
CloudFront 의 콘텐츠를 보호하기 위해 에지에서 인증 로직을 처리할 수 있습니다. 이
시나리오에서 Lambda@Edge 는 에지에서 실행하는 짧은 대기 시간 이점을 활용하면서 웹
애플리케이션에 대한 권한 부여를 제공할 수 있습니다.
~~~

---

# Q346 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/100220-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q347 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/100221-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q348 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/100222-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
이 옵션은 테이블에서 읽기 및 쓰기를 처리하기 위한 읽기/쓰기 용량 모드인 프로비저닝
모드를 사용하기 때문에 가장 효율적입니다. 이를 통해 애플리케이션이 수행할 것으로
예상되는 읽기 및 쓰기 처리량을 지정할 수 있습니다. 또한 애플리케이션이 초당 읽거나
써야 하는 데이터의 양인 RCU(읽기 용량 단위) 및 WCU(쓰기 용량 단위)를 지정합니다.
또한 프로비저닝 모드는 예측 가능한 워크로드에 대해 온디맨드 모드보다 비용이 낮기
때문에 DynamoDB에 대한 예상 예산 이하로 유지해야 하는 요구 사항을 충족합니다.
이 솔루션은 일정하고 예측 가능한 데이터 워크로드가 있는 웨어러블 장치를 사용하는 많은
참여자로부터 데이터를 수집해야 하는 요구 사항을 충족합니다.
옵션 A 는 프로비저닝 모드와 DynamoDB Standard-Infrequent Access(DynamoDB
Standard-IA)를 사용하기 때문에 덜 효율적입니다. DynamoDB Standard-Infrequent
Access 는 밀리초의 지연 시간이 필요한 자주 액세스하지 않는 항목을 위한 스토리지
클래스입니다. 그러나 이는 일정하고 예측 가능한 데이터 워크로드가 있는 웨어러블 장치를
사용하는 많은 참여자로부터 데이터를 수집해야 하는 요구 사항을 충족하지 않습니다.
DynamoDB Standard-IA 는 액세스 빈도가 30 일에 한 번 미만인 항목에 더 적합하기
때문입니다.
옵션 C 는 수요 변화에 따라 테이블 용량을 자동으로 조정하여 사용한 만큼만 비용을
지불하는 읽기/쓰기 용량 모드인 온디맨드 모드를 사용하기 때문에 효율성이 떨어집니다.
그러나 온디맨드 모드는 예측 가능한 워크로드에 대해 프로비저닝된 모드보다 비용이 높기
때문에 DynamoDB 에 대한 예상 예산 이하로 유지해야 하는 요구 사항을 충족하지
않습니다.
옵션 D 는 온디맨드 모드를 사용하고 예약 용량이 있는 RCU 및 WCU 를 지정하기 때문에
효율성이 떨어집니다. 이는 할인된 시간당 요금과 교환하여 테이블에 대한 읽기 및 쓰기
용량을 예약하는 방법입니다. 그러나 온디맨드 모드는 예측 가능한 워크로드에 대해
프로비저닝된 모드보다 비용이 높기 때문에 DynamoDB에 대한 예상 예산 이하로 유지해야
하는 요구 사항을 충족하지 않습니다. 또한 예약된 용량이 있는 RCU 및 WCU 를 지정하는
것은 프로비저닝 모드에만 적용되므로 온디맨드 모드에서는 불가능합니다.
~~~

---

# Q349 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/100299-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
https://docs.aws.amazon.com/ko_kr/kms/latest/developerguide/key-policy-modifying-ex
ternal-accounts.html
다른 사용자 지정 AWS KMS 키를 생성할 필요가 없습니다.
https://aws.amazon.com/premiumsupport/knowledge-center/aurora-share-encrypted-sn
apshot/
원본 계정 내에서 대상 계정에 사용자 지정 AWS KMS 키에 대한 액세스 권한을
부여합니다.
1. 원본 계정에 로그인하고 DB 클러스터 스냅샷과 동일한 리전의 AWS KMS 콘솔로
이동합니다.
2. 탐색 창에서 고객 관리형 키를 선택합니다.
3. 사용자 지정 AWS KMS 키(이미 생성됨)를 선택합니다.
4. 다른 AWS 계정 섹션에서 다른 AWS 계정 추가를 선택한 다음 대상 계정의 AWS 계정
번호를 입력합니다.
그런 다음 DB 클러스터 스냅샷을 복사하고 공유합니다.
~~~

---

# Q350 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/100300-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q351 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/100371-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
이 대답은 서버리스 개념을 사용하고 운영 오버헤드를 최소화하는 이벤트 기반
아키텍처로의 전환 요구 사항을 충족하기 때문에 정확합니다. AWS Step Functions 는 상태
시스템을 사용하여 여러 AWS 서비스를 워크플로로 조정할 수 있는 서버리스 서비스입니다.
상태 머신은 워크플로 단계의 실행 논리와 순서를 정의하는 작업 및 전환으로 구성됩니다.
AWS Lambda 는 서버를 프로비저닝하거나 관리하지 않고도 코드를 실행할 수 있는
서버리스 FaaS(function-as-a-service) 플랫폼입니다. Lambda 함수는 Step Functions에서
상태 시스템의 작업으로 호출할 수 있으며 데이터 수집, 변환, 검증 및 분석과 같은 데이터
관리 워크플로의 다양한 측면을 수행할 수 있습니다. Step Functions 및 Lambda 를
사용함으로써 회사는 다음과 같은 이점을 얻을 수 있습니다.
이벤트 기반: Step Functions 는 타이머, API 호출 또는 기타 AWS 서비스 이벤트와 같은
이벤트를 기반으로 Lambda 함수를 트리거할 수 있습니다. Lambda 함수는 이벤트 기반
아키텍처를 생성하여 다른 서비스나 상태 시스템에 이벤트를 내보낼 수도 있습니다.
서버리스: Step Functions 및 Lambda는 AWS에서 완전히 관리하므로 회사에서 서버 또는
인프라를 프로비저닝하거나 관리할 필요가 없습니다. 회사는 워크플로 및 기능에서
사용하는 리소스에 대해서만 비용을 지불하고 수요에 따라 자동으로 확장 또는 축소할 수
있습니다.
운영 오버헤드: Step Functions 및 Lambda 는 모니터링, 로깅, 추적, 오류 처리, 재시도
논리 및 보안과 같은 기본 제공 기능을 제공하므로 워크플로 및 기능의 개발 및 배포를
단순화합니다. 회사는 운영 세부 사항보다는 비즈니스 논리 및 데이터 처리에 집중할 수
있습니다.
~~~

---

# Q352 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/100197-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
이 상황에 가장 적합한 솔루션은 각 리전에서 UDP 리스너 및 엔드포인트 그룹으로 AWS
Global Accelerator 를 설정하는 옵션 B 입니다. AWS Global Accelerator 는 사용자 요청을
가장 가까운 AWS 지역[1]으로 라우팅하여 인터넷 애플리케이션의 가용성과 성능을
향상시키는 네트워킹 서비스입니다. 또한 대기 시간이 짧고 패킷 손실이 적은 더 빠르고
안정적인 데이터 전송을 제공하여 UDP 응용 프로그램의 성능을 향상시킵니다. 각 리전에서
UDP 리스너와 엔드포인트 그룹을 설정함으로써 Global Accelerator는 더 빠른 응답 시간과
더 나은 사용자 경험을 위해 가장 가까운 리전으로 트래픽을 라우팅합니다.
~~~

---

# Q353 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/100225-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
RDS 지원 스토리지:
https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html
GP2 최대 IOPS:
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/general-purpose.html#gp2-per
formance
Amazon RDS는 범용 SSD(gp2 및 gp3라고도 함), 프로비저닝된 IOPS SSD(io1이라고도 함)
및 마그네틱(표준이라고도 함)의 세 가지 스토리지 유형을 제공합니다. 성능 특성과 가격이
다르기 때문에 스토리지 성능과 비용을 데이터베이스 워크로드의 요구 사항에 맞게 조정할
수 있습니다. 최대 64TiB의 스토리지로 MySQL, MariaDB, Oracle 및 PostgreSQL RDS DB
인스턴스를 생성할 수 있습니다. 최대 16TiB의 스토리지로 SQL Server RDS DB 인스턴스를
생성할 수 있습니다. 이 스토리지 용량에는 프로비저닝된 IOPS SSD 및 범용 SSD 스토리지
유형을 사용하십시오.
https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html
~~~

---

# Q354 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/100198-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
RDS Proxy 를 사용하면 예측할 수 없는 데이터베이스 트래픽 급증을 처리할 수 있습니다.
그렇지 않으면 이러한 급증으로 인해 연결 초과 구독 또는 빠른 속도로 새 연결 생성으로
인해 문제가 발생할 수 있습니다. RDS Proxy 는 데이터베이스 연결 풀을 설정하고 이
풀에서 연결을 재사용합니다. 이 접근 방식은 매번 새 데이터베이스 연결을 여는 메모리 및
CPU 오버헤드를 방지합니다. 초과 구독으로부터 데이터베이스를 보호하기 위해 생성되는
데이터베이스 연결 수를 제어할 수 있습니다.
https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy.html
~~~

---

# Q354 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/100227-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
Amazon EC2 에서 AWS Batch 를 사용합니다. AWS Batch 는 Amazon EC2 인스턴스에서
배치 작업을 쉽게 실행하는 데 사용할 수 있는 완전 관리형 배치 처리 서비스입니다.
워크로드에 맞게 인스턴스 수를 확장할 수 있으므로 최소한의 운영 오버헤드로 원하는 시간
내에 배치 작업을 완료할 수 있습니다.
Amazon API Gateway에서 AWS Lambda 사용 - AWS Lambda
https://docs.aws.amazon.com/lambda/latest/dg/services-apigateway.html
AWS Lambda FAQ
https://aws.amazon.com/lambda/faqs/
~~~

---

# Q356 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/100229-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
30 일 후에 데이터 객체를 S3 Standard-Infrequent Access(S3 Standard-IA)로 이동하면
스토리지 비용을 최소화하면서 고가용성 및 복원력으로 데이터에 즉시 액세스할 수 있어야
한다는 요구 사항을 충족합니다. S3 Standard-IA 는 자주 액세스하지 않는 데이터를 위해
설계되었으며 S3 Standard 보다 낮은 스토리지 비용을 제공하는 동시에 S3 Standard 와
동일한 짧은 지연 시간, 높은 처리량 및 높은 내구성을 제공합니다.
~~~

---

# Q357 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/100230-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
A: Elasticache 는 Amazon 당 순위표에 이상적임에도 불구하고 에지 위치에서 캐싱하지
않기 때문입니다.
D: FSx가 대기 시간이 짧은 요구 사항에 대해 더 높은 성능을 제공하기 때문입니다.
https://www.techtarget.com/searchaws/tip/Amazon-FSx-vs-EFS-Compare-the-AWS-fil
e-services
FSx 는 솔리드 스테이트 드라이브 스토리지 볼륨을 사용하여 고성능 및 1 밀리초 미만의
대기 시간을 위해 구축되었습니다. 이 설계를 통해 사용자는 스토리지 용량과 대기 시간을
독립적으로 선택할 수 있습니다. 따라서 테라바이트 이하의 파일 시스템도 256Mbps
이상의 처리량을 가질 수 있으며 최대 64TB 의 볼륨을 지원할 수 있습니다. Amazon S3 는
이미지, 동영상, 문서 등과 같은 정적 파일을 저장할 수 있는 객체 스토리지 서비스입니다.
Amazon EFS 는 파일을 계층 구조로 저장할 수 있는 파일 스토리지 서비스이며 NFS
프로토콜을 지원합니다.
Amazon FSx for Windows File Server 는 파일을 계층 구조로 저장할 수 있고 SMB
프로토콜을 지원하는 파일 스토리지 서비스입니다. Amazon EBS 는 데이터를 고정 크기
블록에 저장하고 EC2 인스턴스에 연결할 수 있는 블록 스토리지 서비스입니다.
이러한 정의에 따라 요구 사항을 충족하기 위해 취해야 하는 단계 조합은 다음과 같습니다.
1. 정적 파일을 Amazon S3 에 저장합니다. Amazon CloudFront 를 사용하여 엣지에서
객체를 캐싱합니다.
2. Windows File Server 용 Amazon FSx 에 서버 측 코드를 저장합니다. 파일을 공유할 각
EC2 인스턴스에 FSx for Windows File Server 볼륨을 탑재합니다.
~~~

---

# Q358 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/100231-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
Lambda@Edge 는 CloudFront 엣지 위치에서 Lambda 함수를 실행할 수 있게 해주는
서비스입니다. CloudFront 를 통과하는 요청 및 응답을 수정하는 데 사용할 수 있습니다.
CloudFront 오리진 요청 정책은 CloudFront 가 오리진으로 보내는 요청에 포함된 값(URL
쿼리 문자열, HTTP 헤더 및 쿠키)을 제어하는 정책입니다. 오리진에서 추가 정보를
수집하거나 오리진 응답을 사용자 정의하는 데 사용할 수 있습니다. CloudFront 응답 헤더
정책은 CloudFront 가 최종 사용자에게 보내는 응답에서 제거하거나 추가하는 HTTP 헤더를
지정하는 정책입니다. 응답에 보안 또는 사용자 지정 헤더를 추가하는 데 사용할 수
있습니다.
이러한 정의에 따라 최소한의 운영 오버헤드로 요구 사항을 충족하는 솔루션은 다음과
같습니다.
외부 이미지 관리 라이브러리와 함께 Lambda@Edge 함수를 사용합니다. Lambda@Edge
함수를 이미지를 제공하는 CloudFront 동작과 연결합니다.
이 솔루션을 사용하면 애플리케이션이 Lambda@Edge 함수를 사용하여 이미지 크기를
동적으로 조정하고 요청의 User-Agent HTTP 헤더를 기반으로 클라이언트에 적절한 형식을
제공할 수 있습니다. Lambda@Edge 기능은 엣지 위치에서 실행되어 오리진의 대기 시간과
부하를 줄입니다. 애플리케이션 코드는 이미지 조작 작업을 수행할 수 있는 외부 이미지
관리 라이브러리만 포함하면 됩니다.
~~~

---

# Q359 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/100232-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
이를 통해 규정 준수 팀은 서버 측 암호화에 사용되는 KMS 키를 관리할 수 있으므로
암호화 키에 필요한 제어 기능을 제공합니다. 또한 버킷 정책에서 "aws:SecureTransport"
조건을 사용하면 S3 버킷에 대한 모든 연결이 전송 중에 암호화됩니다.
~~~

---

# Q360 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/100238-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
인터페이스 엔드포인트를 사용하면 BuyStock RESTful 웹 서비스와 CheckFunds RESTful 웹
서비스가 코드를 변경하지 않고도 VPC 를 통해 통신할 수 있습니다. 인터페이스
엔드포인트는 고객의 VPC 에 탄력적 네트워크 인터페이스(ENI)를 생성한 다음 API 에서
ENI 로 트래픽을 라우팅하도록 라우팅 테이블을 구성합니다. 이렇게 하면 코드를 변경하지
않고도 두 API가 VPC를 통해 통신할 수 있습니다.
~~~

---

# Q361 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/102119-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q362 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/102121-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
1) SQS FIFO 대기열은 메시지가 전송된 정확한 순서대로 수신되도록 보장합니다. 지불
ID를 메시지 그룹으로 사용하면 지불 ID에 대한 모든 메시지가 순차적으로 수신됩니다.
2) Kinesis 데이터 스트림은 파티션 키별로 순서를 지정할 수도 있습니다. 지불 ID를 파티션
키로 사용하면 각 지불 ID에 대한 메시지의 엄격한 순서가 보장됩니다.
~~~

---

# Q363 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/102124-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q364 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/102125-exam-aws-certified-sol
utions-architect-associate-saa-c03/
참고:
https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html
https://docs.aws.amazon.com/ko_kr/AWSSimpleQueueService/latest/SQSDeveloperGuide
/sqs-server-side-encryption.html
~~~

---

# Q365 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/102127-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
https://aws.amazon.com/rds/features/backup/
자동 백업은 요구 사항을 충족합니다. Amazon RDS 를 사용하면 DB 인스턴스의 백업을
자동으로 생성할 수 있습니다. 자동 백업을 사용하면 DB 인스턴스에 대한 PITR(특정 시점
복구)을 보존 기간(최대 35일) 내의 특정 초 단위로 낮출 수 있습니다. 보존 기간을 30일로
설정하면 최근 30 일 이내 변경 전 최대 5 분 전의 상태로 데이터베이스를 복원할 수
있습니다.
~~~

---

# Q366 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/102128-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
이 옵션은 API 사용 계획 및 API 키를 사용하기 때문에 가장 효율적입니다. API에 액세스할
수 있는 사람과 API 에 액세스할 수 있는 양과 속도를 제어할 수 있는 Amazon API
Gateway 의 기능입니다. 또한 API 사용 계획 및 API 키를 구현하여 구독하지 않은
사용자의 액세스를 제한하므로 API 에 대한 다양한 액세스 계층을 생성하고 그에 따라
사용자에게 요금을 청구할 수 있습니다. 이 솔루션은 구독이 있는 사용자만 프리미엄
콘텐츠에 액세스할 수 있도록 애플리케이션 업데이트 요구 사항을 충족합니다.
옵션 A 는 Amazon API Gateway 의 기능인 API Gateway API 에서 API 캐싱 및 제한을
사용하기 때문에 효율성이 떨어집니다.
API 의 성능과 가용성을 개선하고 트래픽 급증으로부터 백엔드 시스템을 보호할 수
있습니다. 그러나 이는 가입하지 않은 사용자의 액세스를 제한하는 방법을 제공하지
않습니다.
옵션 B 는 가용성에 영향을 미치거나 보안을 손상시키거나 과도한 리소스를 소비할 수 있는
일반적인 웹 악용으로부터 웹 애플리케이션 또는 API 를 보호하는 웹 애플리케이션 방화벽
서비스인 API Gateway API에서 AWS WAF를 사용하기 때문에 효율성이 떨어집니다. 그러나
이는 가입하지 않은 사용자의 액세스를 제한하는 방법을 제공하지 않습니다.
옵션 C 는 테이블 내의 특정 항목 또는 속성에 대한 액세스를 제어할 수 있는 권한인
DynamoDB 테이블의 프리미엄 콘텐츠에 대한 세분화된 IAM 권한을 사용하기 때문에
효율성이 떨어집니다. 그러나 이는 API 수준에서 구독하지 않은 사용자의 액세스를
제한하는 방법을 제공하지 않습니다.
~~~

---

# Q367 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/102131-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
https://aws.amazon.com/ko/step-functions/#:~:text=AWS%20Step%20Functions%20is%
20a
AWS Step Functions 의 일반적인 사용 사례는 사람의 개입이 필요한 작업입니다(예: 승인
프로세스). Step Functions 를 사용하면 분산 애플리케이션의 구성 요소를 상태 머신이라고
하는 시각적 워크플로의 일련의 단계로 쉽게 조정할 수 있습니다. 안정적이고 확장 가능한
방식으로 애플리케이션의 단계를 실행하기 위해 상태 시스템을 신속하게 구축하고 실행할
수 있습니다.
~~~

---

# Q368 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/102132-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
이 옵션은 IAM 사용자 암호에 대한 복잡성 요구 사항 및 필수 교체 기간을 지정하는
방법인 전체 AWS 계정에 대한 전체 암호 정책을 설정하기 때문에 가장 효율적입니다. 또한
암호 정책은 계정의 모든 IAM 사용자에게 적용되므로 모든 새 사용자에 대한 암호 정책
설정 요구 사항을 충족합니다. 이 솔루션은 IAM 사용자 암호에 대한 특정 복잡성 요구
사항 및 필수 교체 기간 설정 요구 사항을 충족합니다.
옵션 B 는 AWS 계정의 각 IAM 사용자에 대해 암호 정책을 설정하기 때문에 효율성이
떨어집니다. 암호 정책은 계정 수준에서만 설정할 수 있으므로 불가능합니다.
옵션 C 는 타사 공급업체 소프트웨어를 사용하여 암호 요구 사항을 설정하기 때문에
효율성이 떨어집니다. IAM 은 암호 정책을 설정하는 기본 제공 방법을 제공하므로 필요하지
않습니다.
옵션 D 는 Amazon CloudWatch 규칙을 Create_newuser 이벤트에 연결하여 적절한 요구
사항으로 암호를 설정하기 때문에 효율성이 떨어집니다. 이는 CloudWatch 규칙이 IAM
사용자 암호를 수정할 수 없기 때문에 불가능합니다.
~~~

---

# Q369 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/102133-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
AWS Batch 는 사용자가 AWS 에서 배치 작업을 실행할 수 있게 해주는 완전관리형
서비스입니다. 다른 언어로 작성된 다양한 유형의 작업을 처리하고 EC2 인스턴스에서
실행할 수 있습니다. 또한 Amazon EventBridge(Amazon CloudWatch Events)와 통합되어
시간 또는 이벤트 트리거를 기반으로 작업을 예약합니다. 이 솔루션은 성능, 확장성 및
낮은 운영 오버헤드 요구 사항을 충족합니다.
1. EC2 인스턴스를 컨테이너로 변환합니다. AWS App Runner를 사용하여 작업을 작업으로
실행할 온디맨드 컨테이너를 생성합니다. 이 솔루션은 EC2 인스턴스를 컨테이너로
변환하고 웹 애플리케이션을 자동으로 빌드 및 배포하고 트래픽 부하를 분산하는 서비스인
AWS App Runner 를 사용하므로 낮은 운영 오버헤드 요구 사항을 충족하지 않습니다. 배치
작업을 실행하는 데는 필요하지 않습니다.
2. 작업을 AWS Lambda 함수에 복사합니다. Amazon EventBridge(Amazon CloudWatch
Events)를 사용하여 Lambda 함수를 예약합니다. AWS Lambda 에는 실행 시간이 15 분,
메모리 할당이 10GB 로 제한되어 있으므로 이 솔루션은 성능 요구 사항을 충족하지
않습니다. 이러한 제한은 1시간 작업을 실행하는 데 충분하지 않을 수 있습니다.
3. 작업을 실행하는 EC2 인스턴스의 Amazon 머신 이미지(AMI)를 생성합니다. AMI로 Auto
Scaling 그룹을 생성하여 인스턴스의 여러 복사본을 실행합니다. 이 솔루션은 구성 및
관리가 필요한 추가 리소스인 AMI 및 Auto Scaling 그룹을 생성하고 유지 관리하므로 낮은
운영 오버헤드 요구 사항을 충족하지 않습니다.
참조 URL:
https://docs.aws.amazon.com/ko_kr/whitepapers/latest/aws-overview/compute-services.
html
설명:
NAT 게이트웨이는 프라이빗 서브넷의 인스턴스가 인터넷이나 다른 AWS 서비스에 연결할
수 있게 해주지만 인터넷이 해당 인스턴스와의 연결을 시작하지 못하도록 하는 네트워크
주소 변환(NAT) 장치 유형입니다. NAT 게이트웨이는 최소한의 운영 유지 관리가 필요하고
최대 45Gbps 의 버스트 트래픽을 처리할 수 있는 관리형 서비스입니다. NAT 게이트웨이는
시나리오의 3 계층 웹 애플리케이션과 같이 프라이빗 서브넷의 EC2 인스턴스가 인터넷을
통해 라이선스 서버와 통신해야 하는 시나리오에 적합합니다.
시나리오의 요구 사항을 충족하려면 솔루션 설계자가 퍼블릭 서브넷에서 NAT 게이트웨이를
프로비저닝해야 합니다. 솔루션 설계자는 또한 NAT 게이트웨이를 가리키는 기본 경로로 각
프라이빗 서브넷의 경로 테이블을 수정해야 합니다. 이렇게 하면 프라이빗 서브넷에서
실행되는 EC2 인스턴스가 NAT 게이트웨이를 통해 인터넷을 통해 라이선스 서버에
액세스할 수 있습니다.
~~~

---

# Q370 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/102134-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q371 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/102135-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q372 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/102136-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
Amazon S3 는 수백만 개의 이미지 1 를 저장할 수 있는 확장성과 내구성이 뛰어나고 비용
효율적인 객체 스토리지 서비스입니다. Amazon DynamoDB 는 키-값 및 문서 데이터에
대해 높은 처리량과 짧은 지연 시간을 처리할 수 있는 완전관리형 NoSQL
데이터베이스입니다. S3 를 사용하여 이미지를 저장하고 DynamoDB 를 사용하여 지리적
코드와 이미지 S3 URL 을 저장함으로써 솔루션은 자연 재해 중에 고가용성과 확장성을
달성할 수 있습니다. 또한 캐싱, 자동 확장, 글로벌 테이블과 같은 DynamoDB 의 기능을
활용하여 성능을 개선하고 비용을 절감할 수 있습니다.
1. 데이터베이스 테이블에 이미지와 지리적 코드를 저장합니다. Amazon RDS 다중 AZ DB
인스턴스에서 실행되는 Oracle 을 사용합니다. Oracle 은 이미지와 같은 대량의 비정형
데이터를 효율적으로 처리하지 못할 수 있는 관계형 데이터베이스이므로 이 솔루션은
확장성 및 비용 효율성 요구 사항을 충족하지 않습니다. 또한 S3 및 DynamoDB 보다
라이선스 및 운영 비용이 더 많이 듭니다.
2. Amazon DynamoDB 테이블에 이미지와 지리적 코드를 저장합니다. 로드가 많은 시간
동안 DynamoDB Accelerator(DAX)를 구성합니다. 이 솔루션은 DynamoDB 에 이미지를
저장하면 S312 에 저장하는 것보다 더 많은 스토리지 공간을 사용하고 더 많은 비용이
발생하므로 비용 효율성 요구 사항을 충족하지 않습니다. 또한 높은 부하를 처리하기 위해
DAX 클러스터의 추가 구성 및 관리가 필요합니다.
3. Amazon S3 버킷에 이미지를 저장합니다. 지리적 코드와 이미지 S3 URL을 데이터베이스
테이블에 저장합니다. Amazon RDS 다중 AZ DB 인스턴스에서 실행되는 Oracle 을
사용합니다. Oracle 은 지리적 코드와 같은 키-값 데이터에 대한 높은 처리량과 낮은 대기
시간을 효율적으로 처리하지 못할 수 있는 관계형 데이터베이스이므로 이 솔루션은 확장성
및 비용 효율성 요구 사항을 충족하지 않습니다. 또한 DynamoDB2 보다 라이선스 및 운영
비용이 더 많이 듭니다.
참조 URL: https://dynobase.dev/dynamodb-vs-s3/
~~~

---

# Q373 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/102137-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q374 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/102138-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
A(X) : VPC-온프레미스 간 통신은 이루어지나 VPC 간 통신은 이루어지지 않고 있음.
B(X) : A와 같은 이유로 오답.
C(X) : A와 같은 이유로 오답.
D(O) : Transit Gateway 는 동일한 리전 내에 있는 여러 VPC 들을 연결하는 전송
'허브'이므로 Transit Gateway를 거쳐 VPC끼리 통신이 가능
AWS Transit Gateway는 동일한 리전의 VPC를 상호 연결하여 Amazon VPC 라우팅 구성을
한 곳에 통합하는 네트워크 전송 허브입니다.
https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-dir
ect-connect-aws-transit-gateway.html
~~~

---

# Q375 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/102139-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
AWS Step Functions 는 시각적 워크플로를 사용하여 분산 애플리케이션 및 마이크로
서비스의 구성 요소를 조정하여 애플리케이션을 쉽게 구축할 수 있게 해주는 완전 관리형
서비스입니다.
Step Functions 를 사용하면 여러 AWS Lambda 함수를 반응형 서버리스 애플리케이션에
결합하고 Amazon EC2 인스턴스, 컨테이너 또는 온프레미스 서버에서 실행되는 데이터 및
서비스를 오케스트레이션할 수 있습니다. Step Functions 는 또한 워크플로의 일부로 수동
승인을 허용합니다. 이 솔루션은 최소한의 운영 오버헤드로 모든 요구 사항을 충족합니다.
https://aws.amazon.com/ko/step-functions/#:~:text=AWS%20Step%20Functions%20is%
20a
~~~

---

# Q376 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/102140-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
최신 서버리스 아키텍처에 구축된 애플리케이션을 포함하여 많은 애플리케이션은
데이터베이스 서버에 대해 많은 수의 열린 연결을 가질 수 있으며 빠른 속도로
데이터베이스 연결을 열고 닫을 수 있으므로 데이터베이스 메모리와 컴퓨팅 리소스가
고갈될 수 있습니다. Amazon RDS Proxy 를 사용하면 애플리케이션이 데이터베이스와
설정된 연결을 풀링하고 공유하여 데이터베이스 효율성과 애플리케이션 확장성을 개선할 수
있습니다.
(https://aws.amazon.com/pt/rds/proxy/)
~~~

---

# Q377 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/102142-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
Amazon EC2 Auto Scaling 은 Auto Scaling 그룹에 수명 주기 후크를 추가하는 기능을
제공합니다. 이러한 후크를 사용하면 Auto Scaling 인스턴스 수명 주기의 이벤트를
인식하는 솔루션을 생성한 다음 해당 수명 주기 이벤트가 발생할 때 인스턴스에서 사용자
지정 작업을 수행할 수 있습니다.
(https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks.html)
~~~

---

# Q378 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/102143-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
Network Load Balancer 는 연결 수준(계층 4)에서 작동하고 TCP 및 UDP 트래픽 모두의
부하를 분산할 수 있는 일종의 부하 분산 장치입니다. Network Load Balancer 는 실시간
멀티플레이어 게임과 같이 고성능과 짧은 대기 시간이 필요한 시나리오에 적합합니다.
Network Load Balancer 는 가용 영역당 단일 고정 IP 주소를 사용하면서 갑작스럽고
변동성이 큰 트래픽 패턴을 처리할 수도 있습니다.
시나리오의 요구 사항을 충족하려면 솔루션 설계자는 Auto Scaling 그룹의 EC2 인스턴스
간 트래픽 분산을 위해 Network Load Balancer 를 사용해야 합니다. Network Load
Balancer 는 클라이언트에서 적절한 포트의 서버로 UDP 트래픽을 라우팅할 수 있습니다.
Network Load Balancer 는 클라이언트와 서버 간의 보안 통신을 위해 TLS 오프로딩도
지원할 수 있습니다.
Amazon DynamoDB 는 일관된 성능과 짧은 지연 시간으로 모든 양의 데이터를 저장하고
검색할 수 있는 완전 관리형 NoSQL 데이터베이스 서비스입니다. Amazon DynamoDB
온디맨드는 용량 계획이 필요 없고 테이블에서 수행되는 읽기 및 쓰기 요청에 대해서만
요금을 부과하는 유연한 결제 옵션입니다 3. Amazon DynamoDB 온디맨드는 게임
애플리케이션과 같이 애플리케이션 트래픽을 예측할 수 없거나 산발적인 시나리오에
이상적입니다.
시나리오의 요구 사항을 충족하려면 솔루션 설계자는 데이터 스토리지에 Amazon
DynamoDB 온디맨드를 사용해야 합니다. Amazon DynamoDB 온디맨드는 개발자의 개입
없이 게이머 점수 및 기타 비관계형 데이터를 저장할 수 있습니다. Amazon DynamoDB
온디맨드는 자동으로 확장하여 성능이나 가용성에 영향을 주지 않고 모든 수준의 요청
트래픽을 처리할 수 있습니다.
~~~

---

# Q379 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/102144-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
요청을 처리하는 Lambda 함수에 대해 프로비저닝된 동시성을 구성합니다. 프로비저닝된
동시성을 사용하면 Lambda 함수에서 사용할 수 있는 컴퓨팅 리소스의 양을 설정할 수
있으므로 한 번에 더 많은 요청을 처리하고 지연 시간을 줄일 수 있습니다. 쿼리 결과를
Amazon S3 에 캐싱하면 대기 시간을 줄이는 데 도움이 되지만 프로비저닝된 동시성을
설정하는 것만큼 효과적이지는 않습니다. 데이터베이스 크기를 늘려도 지연 시간을 줄이는
데 도움이 되지 않습니다. 이는 Lambda 함수가 설정할 수 있는 연결 수를 늘리지 않고
프런트엔드 애플리케이션과 데이터베이스 사이에 직접 연결을 설정하면 API 를 우회하기
때문입니다. 최고의 솔루션 중 하나입니다.
https://docs.aws.amazon.com/lambda/latest/dg/services-apigateway.html
Using AWS Lambda with Amazon API Gateway - AWS Lambda
https://docs.aws.amazon.com/lambda/latest/dg/services-apigateway.html
https://aws.amazon.com/lambda/faqs/
AWS Lambda FAQs
https://aws.amazon.com/lambda/faqs/
~~~

---

# Q380 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/102145-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
비용 및 인프라 유지 관리를 최소화하면서 일정에 따라 EC2 인스턴스 및 DB 인스턴스를
자동으로 시작 및 중지하는 가장 효율적인 솔루션은 AWS Lambda 함수를 생성하고 일정에
따라 함수를 호출하도록 Amazon EventBridge를 구성하는 것입니다.
옵션 A, 탄력적 크기 조정을 사용하여 EC2 인스턴스를 확장하고 업무 시간 외에 DB
인스턴스를 0 으로 확장하는 것은 DB 인스턴스를 0 으로 확장할 수 없기 때문에 실행
불가능합니다.
파트너 솔루션에 대한 AWS Marketplace 를 탐색하는 옵션 B 가 옵션일 수 있지만 가장
효율적인 솔루션이 아닐 수 있으며 잠재적으로 추가 비용이 추가될 수 있습니다.
다른 EC2 인스턴스를 시작하고 일정에 따라 기존 EC2 인스턴스 및 DB 인스턴스를 시작
및 중지하는 셸 스크립트를 실행하도록 crontab 일정을 구성하는 옵션 C 는 불필요한
인프라 및 유지 관리를 추가합니다.
~~~

---

# Q381 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/102147-exam-aws-certified-sol
utions-architect-associate-saa-c03/
~~~

---

# Q382 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/102149-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명1:
전송 중인 데이터의 보안을 개선하는 가장 좋은 옵션은 TLS 수신기를 구성하고 NLB 에
서버 인증서를 배포하는 것입니다. 이렇게 하면 데이터가 네트워크를 통해 이동할 때
암호화되고 안전해집니다. 또한 AWS Shield Advanced를 구성하고 NLB에서 AWS WAF를
활성화하여 악의적인 공격으로부터 네트워크를 추가로 보호할 수도 있습니다. 또는 로드
밸런서를 Application Load Balancer(ALB)로 변경하고 ALB에서 AWS WAF를 활성화할 수도
있습니다.
마지막으로 AWS Key Management Service(AWS KMS)를 사용하여 EC2 인스턴스에서
Amazon Elastic Block Store(Amazon EBS) 볼륨을 암호화할 수도 있습니다.
TLS 수신기에 대한 SSL 인증서를 지정해야 합니다. 로드 밸런서는 인증서를 사용하여
연결을 종료하고 대상으로 라우팅하기 전에 클라이언트의 요청을 해독합니다.
https://docs.aws.amazon.com/elasticloadbalancing/latest/network/create-listener.html
설명2:
A: 전송 중인 데이터를 어떻게 보호합니까?
모범 사례:
보안 키 및 인증서 관리 구현: 암호화 키 및 인증서를 안전하게 저장하고 엄격한 액세스
제어를 적용하면서 적절한 시간 간격으로 교체합니다. 예를 들어 AWS Certificate
Manager(ACM)와 같은 인증서 관리 서비스를 사용합니다.
전송 중 암호화 적용: 조직, 법률 및 규정 준수 요구 사항을 충족하는 데 도움이 되는
적절한 표준 및 권장 사항에 따라 정의된 암호화 요구 사항을 적용합니다.
의도하지 않은 데이터 액세스 탐지 자동화: GuardDuty 와 같은 도구를 사용하여 데이터
분류 수준에 따라 정의된 경계 외부로 데이터를 이동하려는 시도를 자동으로 탐지합니다.
예를 들어 DNS 프로토콜을 사용하여 알 수 없거나 신뢰할 수 없는 네트워크에 데이터를
복사하는 트로이 목마를 탐지합니다. .
네트워크 통신 인증: TLS(전송 계층 보안) 또는 IPsec 과 같은 인증을 지원하는 프로토콜을
사용하여 통신 ID를 확인합니다.
https://wa.aws.amazon.com/wat.question.SEC_9.en.html
~~~

---

# Q383 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/102150-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
https://aws.amazon.com/ec2/dedicated-hosts/
Amazon EC2 전용 호스트를 사용하면 Amazon EC2 에서 Microsoft 및 Oracle 과 같은
공급업체의 적격 소프트웨어 라이선스를 사용할 수 있으므로 자체 라이선스 사용의
유연성과 비용 효율성을 얻으면서도 AWS의 탄력성, 단순성 및 탄력성을 얻을 수 있습니다.
~~~

---

# Q384 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/102152-exam-aws-certified-sol
utions-architect-associate-saa-c03/
참고:
https://aws.amazon.com/efs/features/infrequent-access/
~~~

---

# Q385 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/102153-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
이 답변은 Windows IIS 웹 서버와 호환되는 온-프레미스 파일 공유에 대한 탄력적이고
내구성 있는 대체를 제공하기 때문에 정확합니다. Amazon FSx for Windows File Server는
Windows Server 에 구축된 공유 파일 스토리지를 제공하는 완전관리형 서비스입니다. SMB
프로토콜을 지원하고 Windows 기반 애플리케이션에 대한 원활한 액세스 및 인증을
가능하게 하는 Microsoft Active Directory 와 통합됩니다. Amazon FSx for Windows File
Server는 또한 다음과 같은 이점을 제공합니다.
복원력: Amazon FSx for Windows File Server 는 고가용성 및 장애 조치 보호를 제공하는
여러 가용 영역에 배포할 수 있습니다. 또한 자동 백업 및 복원은 물론 문제를 감지하고
수정하는 자가 치유 기능을 지원합니다.
내구성: Windows File Server 용 Amazon FSx 는 가용 영역 내외에서 데이터를 복제하고
내구성이 뛰어난 스토리지 장치에 데이터를 저장합니다. 또한 유휴 및 전송 중 암호화는
물론 파일 액세스 감사 및 데이터 중복 제거를 지원합니다.
성능: Windows File Server 용 Amazon FSx 는 파일 작업을 위한 일관된 1 밀리초 미만의
지연 시간과 높은 처리량을 제공합니다. 또한 SSD 스토리지, 분산 파일 시스템(DFS)
네임스페이스 및 복제와 같은 기본 Windows 기능, 사용자 중심 성능 확장을 지원합니다.
AWS KMS CMK를 사용하여 파일 공유의 이미지를 암호화하도록 Amazon FSx 파일 공유를
구성함으로써 회사는 무단 액세스로부터 이미지를 보호하고 회사 정책을 준수할 수
있습니다. 이미지에 대한 NTFS 권한 집합을 사용하여 회사는 이미지를 수정하거나 삭제할
수 있는 사람을 제한하여 실수로 이미지를 삭제하는 것을 방지할 수 있습니다.
~~~

---

# Q386 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/102154-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
가장 좋은 솔루션은 Amazon ElastiCache 를 구현하여 대용량 데이터 세트를 캐시하는
것입니다. 이렇게 하면 자주 액세스하는 데이터를 메모리에 저장하여 검색 시간을 단축할
수 있습니다. 이는 데이터베이스에 대한 빈번한 호출을 완화하고 대기 시간을 줄이며
백엔드 계층의 전반적인 성능을 향상시키는 데 도움이 될 수 있습니다.
~~~

---

# Q387 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/102155-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
배포 엔지니어가 CloudFormation 을 사용하여 필요한 작업을 전부 해결할 수 있으므로
관련 작업만 허용해주면 최소 권한의 원칙이 충족됨.
A(X) : 루트 사용자 자격 증명으로 최소 권한의 원칙에 어긋나서 제외.
B(X) : PowerUsers 는 PowerUser 사용자 그룹의 멤버는 사용자 관리 작업(예: IAM 및
Organizations)을 제공하는 일부 서비스를 제외한 모든 서비스에 대해 전체 권한을 갖
으므로 최소 권한의 원칙에 어긋나서 제외
https://docs.aws.amazon.com/ko_kr/IAM/latest/UserGuide/getting-started_create-delega
ted-user.html
C(X) : 관리/액세스 권한을 굳이 줄 필요없음. CloudFormation 관련 권한만 부여하면 됨.
D(O) : CloudFormation 작업만 허용하도록 하여 최소 권한 부여 조건 충족.
E(O) : D와 마찬가지 이유로 정답.
참고:
https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html
https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html
~~~

---

# Q388 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/102156-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
이 대답은 웹 계층이 보안 그룹을 소스로 사용하여 데이터베이스 계층에 액세스할 수
있도록 허용하기 때문에 정확합니다. 이는 VPC 연결에 권장되는 모범 사례입니다. 보안
그룹은 상태 저장이며 동일한 VPC 에 있는 다른 보안 그룹을 참조할 수 있으므로 방화벽
규칙의 구성 및 유지 관리가 간소화됩니다. 데이터베이스 계층의 보안 그룹에 인바운드
규칙을 추가하면 웹 계층의 EC2 인스턴스가 IP 주소나 서브넷에 관계없이 포트 3306 에서
RDS 인스턴스에 연결할 수 있습니다.
~~~

---

# Q389 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/102157-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
읽기 전용 복제본 사용 사례 - 일반 로드를 수행하는 프로덕션 데이터베이스가 있고 일부
분석을 실행하기 위해 보고 애플리케이션을 실행하려고 합니다. * 읽기 전용 복제본을
생성하여 그곳에서 새 워크로드를 실행합니다. * 프로덕션 애플리케이션은 영향을 받지
않습니다. SELECT(=읽기) 종류의 문에만 사용됨(INSERT, UPDATE, DELETE 아님)
~~~

---

# Q390 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/102213-exam-aws-certified-sol
utions-architect-associate-saa-c03/
참고:
https://aws.amazon.com/caching/session-management/
~~~

---

# Q391 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/102212-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
애플리케이션에는 인스턴스에 대한 로컬 데이터가 없으므로 AMI 만으로는 최신 AMI
백업에서 인스턴스를 복원하여 RPO 를 충족할 수 있습니다. 데이터베이스에 대한 자동화된
RDS 백업과 결합하면 이 환경에 대한 완벽한 백업 솔루션을 제공합니다. EBS 스냅샷과
관련된 다른 옵션은 인스턴스의 상태 비저장 특성을 고려할 때 불필요합니다. AMI 는 앱
계층에 필요한 모든 백업을 제공합니다. 이는 최소한의 지속적인 관리가 필요한 기본 자동
AWS 백업 기능을 사용합니다. - AMI 자동 백업은 상태 비저장 앱 계층에 대한 특정 시점
복구를 제공합니다. - RDS 자동 백업은 데이터베이스에 대한 특정 시점 복구를 제공합니다.
~~~

---

# Q392 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/102160-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명1:
A(O) : S3에 넣으면 Lambda를 통해 자동으로 처리가 되도록 하는 거라 OK. S3는 저렴함.
B(X) : dynamodb는 이미지 저장용으론…
C(X) : 저렴한 S3가 있는데 굳이... 인스턴스 비용도 나감.
D(x) : C와 마찬가지.
설명2:
웹 서버에 대한 인바운드 액세스를 HTTPS 트래픽에 사용되는 포트 443 으로만 제한하고
애플리케이션이 공개되어 글로벌 고객이 액세스할 수 있으므로 모든 IP 주소(0.0.0.0/0)에서
액세스를 허용합니다.
DB 인스턴스에 대한 인바운드 액세스를 MySQL 트래픽에 사용되는 포트 3306 으로만
제한하고 웹 서버의 보안 그룹에서만 액세스를 허용하여 두 계층 간의 보안 연결을
생성하고 데이터베이스에 대한 무단 액세스를 방지합니다.
아웃바운드 액세스를 두 계층에 필요한 최소 수준으로 제한합니다. 이는 질문에 지정되지
않았지만 인바운드 규칙과 유사하다고 가정할 수 있습니다.
~~~

---

# Q393 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/102322-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
민감한 데이터 수정은 텍스트 스크립트와 오디오 파일의 개인 식별 가능 정보(PII)를
대체합니다. 수정된 내용은 원본 텍스트를 [PII]로 대체하고 수정된 오디오 파일은 음성
개인 정보를 침묵으로 대체합니다. 이 매개 변수는 고객 정보를 보호하는 데 유용합니다.
https://docs.aws.amazon.com/transcribe/latest/dg/call-analytics-insights.html#callanalyt
ics-insights-redaction
~~~

---

# Q394 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/102161-exam-aws-certified-sol
utions-architect-associate-saa-c03/
B??
~~~

---

# Q395 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/102162-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
가장 좋은 방법은 AWS CloudTrail 을 사용하여 원하는 정보를 찾는 것입니다. AWS
CloudTrail 은 AWS 계정 활동의 거버넌스, 규정 준수, 운영 감사 및 위험 감사를 지원하는
서비스입니다. CloudTrail 은 IAM 사용자, EC2 인스턴스, AWS 관리 콘솔 및 기타 AWS
서비스에 의한 변경 사항을 포함하여 AWS 계정의 리소스에 대한 모든 변경 사항을
기록하는 데 사용할 수 있습니다. 솔루션 설계자는 CloudTrail 을 사용하여 보안 그룹
규칙의 구성을 변경한 IAM 사용자를 식별할 수 있습니다.
~~~

---

# Q396 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/102164-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
AWS Shield는 AWS에서 실행되는 애플리케이션에 대한 DDoS(Distributed Denial of Service)
공격으로부터 보호하는 관리형 서비스입니다. AWS Shield Standard는 추가 비용 없이 모든
AWS 고객에게 자동으로 활성화됩니다. AWS Shield Advanced는 선택적 유료 서비스입니다.
AWS Shield Advanced 는 Amazon Elastic Compute Cloud(EC2), Elastic Load
Balancing(ELB), Amazon CloudFront, AWS Global Accelerator 및 Route 53에서 실행되는
애플리케이션에 대해 더 정교하고 더 큰 공격에 대한 추가 보호 기능을 제공합니다.
https://docs.aws.amazon.com/waf/latest/developerguide/ddos-event-mitigation-logic-g
ax.html
~~~

---

# Q397 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/102165-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
최소한의 운영 오버헤드로 요구 사항을 충족하는 솔루션은 속도 기반 규칙을 사용하여 리전
AWS WAF 웹 ACL 을 생성하고 웹 ACL 을 API 게이트웨이 단계와 연결하는 것입니다. 이
솔루션은 들어오는 요청을 모니터링하고 사전 정의된 속도를 초과하는 IP 주소의 요청을
차단하여 HTTP 플러드 공격으로부터 애플리케이션을 보호합니다. API Gateway 지역 API
엔드포인트 앞에 Lambda@Edge 가 있는 Amazon CloudFront 배포도 좋은 솔루션이지만
이전 솔루션보다 더 많은 운영 오버헤드가 필요합니다. Amazon CloudWatch 지표를
사용하여 개수 지표를 모니터링하고 미리 정의된 속도에 도달했을 때 보안 팀에 알리는
것은 HTTP 플러드 공격으로부터 보호할 수 있는 솔루션이 아닙니다. 최대 TTL이 24시간인
API Gateway 지역 API 엔드포인트 앞에 Amazon CloudFront 배포를 생성하는 것은 HTTP
플러드 공격으로부터 보호할 수 있는 솔루션이 아닙니다.
~~~

---

# Q398 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/102166-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
가장 좋은 방법은 AWS Snow Family 콘솔을 사용하여 여러 AWS Snowball Edge Storage
Optimized 디바이스를 주문하고 디바이스를 사용하여 데이터를 Amazon S3 로 전송하는
것입니다. Snowball Edge 는 많은 양의 데이터를 안전하고 빠르게 전송할 수 있는
페타바이트 규모의 데이터 전송 디바이스입니다.
Snowball Edge 를 사용하면 장거리에서 대량의 데이터를 전송하는 가장 비용 효율적인
솔루션이 될 수 있으며 2 주 이내에 600TB 의 데이터를 전송해야 하는 요구 사항을 충족할
수 있습니다.
~~~

---

# Q399 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/102167-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
AWS WAF의 속도 기반 규칙을 사용하면 보안 팀이 속도 기반 규칙을 트리거하는 임계값을
구성할 수 있습니다. 이를 통해 AWS WAF 는 지정된 기간 동안 요청 속도를 추적한 다음
임계값이 초과되면 자동으로 차단할 수 있습니다. 이는 최소한의 운영 오버헤드로 HTTP
플러드 공격을 방지하는 기능을 제공합니다.
참조:
https://docs.aws.amazon.com/waf/latest/developerguide/web-acl.html
~~~

---

# Q400 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/102169-exam-aws-certified-sol
utions-architect-associate-saa-c03/
설명:
최소한의 운영 오버헤드로 이러한 요구 사항을 충족하는 최상의 솔루션은 테이블에서
Amazon DynamoDB 스트림을 활성화하고 트리거를 사용하여 팀이 구독할 수 있는 단일
Amazon Simple Notification Service(Amazon SNS) 주제에 쓰는 것입니다. 이 솔루션에는
최소한의 구성 및 인프라 설정이 필요하며 Amazon DynamoDB Streams 는 DynamoDB
테이블에 대한 변경 사항을 캡처하는 지연 시간이 짧은 방법을 제공합니다. 트리거는
자동으로 변경 사항을 캡처하고 이를 내부 팀에 알리는 SNS 주제에 게시합니다.
~~~