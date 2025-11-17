# Q701 

~~~ 설명
설명:
여러 EC2 인스턴스와 여러 가용 영역에 걸쳐 25GB 이상의 파일을 저장하고 액세스하려면
Amazon Elastic File System(Amazon EFS)이 적합한 솔루션입니다. Amazon EFS 는 여러
EC2 인스턴스에 동시에 탑재할 수 있는 간단하고 확장 가능하며 탄력적인 파일 시스템을
제공합니다. Amazon EFS는 한 지역 내의 여러 가용 영역에 데이터를 저장하여 고가용성과
내구성을 지원합니다.
~~~

---

# Q702 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/85409-exam-aws-certified-solut
ions-architect-associate-saa-c03/
설명1:
전체적인 프로세스는 퍼블릭 서브넷 -> 프라이빗 서브넷(EC2 인스턴스가 있는 곳) ->
데이터베이스 전용 서브넷.
데이터베이스를 구동하는 인스턴스의 보안은 Security Group 이 담당. Security Group 은
허용 설정만 가능하고 차단 설정은 불가능하며, 기본적으로 모든 인바운드 트래픽을 차단.
따라서 허용할 곳만 등록시켜두면 나머지는 자동으로 다 차단하는 셈.
보안 그룹은 연결된 리소스에 도달하고 나갈 수 있는 트래픽을 제어합니다. 예를 들어 보안
그룹을 EC2 인스턴스와 연결하면 인스턴스에 대한 인바운드 및 아웃바운드 트래픽을
제어합니다. 허용 규칙을 지정할 수 있지만 거부 규칙은 지정할 수 없습니다. 보안 그룹을
처음 만들 때 인바운드 규칙이 없습니다. 따라서 보안 그룹에 인바운드 규칙을 추가하기
전에는 어떤 인바운드 트래픽도 허용되지 않습니다.
https://docs.aws.amazon.com/ko_kr/vpc/latest/userguide/VPC_SecurityGroups.html
설명2:
보안 그룹은 상태 저장입니다. 모든 인바운드 트래픽은 기본적으로 차단됩니다. 트래픽
인바운드를 허용하는 인바운드 규칙을 생성하면 해당 트래픽이 자동으로 다시 백아웃됩니다.
보안 그룹을 사용하여 특정 IP 주소를 차단할 수 없습니다(대신 네트워크 액세스 제어 목록
사용).
허용 규칙은 지정할 수 있지만 거부 규칙은 지정할 수 없습니다. 보안 그룹을 처음
생성하면 인바운드 규칙이 없습니다. 따라서 인바운드 규칙을 보안 그룹에 추가할 때까지
다른 호스트에서 시작하여 인스턴스로 들어오는 인바운드 트래픽은 허용되지 않습니다.
https://docs.aws.amazon.com/ko_kr/vpc/latest/userguide/vpc-security-groups.html#VPC
SecurityGroups
~~~

---

# Q703 

~~~ 설명
설명:
이러한 답변은 솔루션의 일부로 AWS Outposts 를 사용하는 데 대한 고객의 책임을
반영하기 때문에 정확합니다. AWS 공유 책임 모델에 따르면 고객은 Outposts 랙에
탄력적인 전력 및 네트워크 연결을 제공하고, 데이터 센터 환경의 물리적 보안 및 액세스
제어를 보장하며, 서버 오류 및 유지 관리를 완화하기 위해 Amazon ECS 클러스터에 추가
용량을 제공할 책임이 있습니다. 이벤트. AWS 는 가상화 하이퍼바이저, 스토리지 시스템 및
Outposts 에서 실행되는 AWS 서비스를 관리할 뿐만 아니라 Outposts 랙 내 전원 공급
장치, 서버 및 네트워킹 장비를 포함한 Outposts 인프라의 가용성 및 물리적 유지 관리를
담당합니다. 전초기지 구성 요소.
참조:
https://docs.aws.amazon.com/outposts/latest/userguide/what-is-outposts.html
https://www.contino.io/insights/the-sandwich-responsibility-model-aws-outposts/
~~~

---

# Q704 

~~~ 설명
설명:
EC2 인스턴스에서 실행되는 애플리케이션의 고가용성을 달성하려면 애플리케이션을 여러
가용 영역에 배포하고 로드 밸런서를 사용하여 트래픽을 분산해야 합니다. Auto Scaling
그룹을 사용하면 여러 가용 영역에서 EC2 인스턴스를 시작 및 관리하고 상태 확인을
수행할 수 있습니다. Network Load Balancer 를 사용하여 EC2 인스턴스에 대한 전송 계층
트래픽을 처리할 수 있습니다.
~~~

---

# Q705 

~~~ 설명
설명:
이를 통해 회사는 비용을 모니터링하고 비정상적인 지출이 발생할 경우 책임 있는
이해관계자에게 알릴 수 있습니다. AWS Billing and Cost Management 콘솔에서 AWS 비용
이상 탐지 모니터를 생성함으로써 회사는 비정상적인 지출을 자동으로 탐지하고 경고하는
기계 학습 서비스를 사용할 수 있습니다. 경고 임계값, 알림 기본 설정 및 근본 원인
분석을 구성함으로써 회사는 비정상적인 지출을 방지하고 그 출처를 식별할 수 있습니다.
~~~

---

# Q706 

~~~ 설명
설명:
이를 통해 회사는 가용성이 높고 비용 효율적인 방식으로 이미지를 저장하고 사용자에게
전달할 수 있습니다. Amazon S3 Standard 에 이미지를 저장함으로써 회사는 고가용성과
성능을 제공하는 내구성 있고 확장 가능하며 안전한 개체 스토리지 서비스를 사용할 수
있습니다. S3 Standard 를 사용하여 정적 웹 사이트를 통해 이미지를 직접 전달함으로써
회사는 웹 서버 실행을 방지하고 운영 오버헤드를 줄일 수 있습니다. S3 Standard 는 또한
AWS 리전 내에서 저렴한 스토리지 가격과 무료 데이터 전송을 제공합니다.
~~~

---

# Q707 

~~~ 설명
설명:
이를 통해 CloudFormation 은 공개 액세스 권한을 부여하거나 추가 리소스를 생성하지
않고도 S3 버킷의 템플릿에 액세스할 수 있습니다. 미리 서명된 URL 은 객체에 액세스할
권한이 있는 IAM 사용자 또는 역할의 액세스 키로 서명된 URL 입니다. 미리 서명된 URL 은
이를 수신하는 누구나 사용할 수 있지만 지정된 시간이 지나면 만료됩니다. 템플릿 객체에
대해 미리 서명된 URL 을 생성하고 이를 사용하도록 CloudFormation 스택을 구성함으로써
회사는 특정 사용자 요청에 따라 템플릿에 대한 CloudFormation 액세스 권한을 부여하고
보안 모범 사례를 따를 수 있습니다.
~~~

---

# Q708 

~~~ 설명
설명:
이를 통해 회사는 CloudTrail 로그를 유지하고 언제든지 쿼리할 수 있습니다. 회사는 중앙
집중식 계정의 CloudTrail 이벤트 기록을 사용하여 여러 AWS 계정의 최근 API 활동을 보고,
필터링하고, 다운로드할 수 있습니다. CloudTrail 이벤트 기록에서 Amazon Athena 테이블을
생성함으로써 회사는 표준 SQL 을 사용하여 S3 의 데이터를 쉽게 분석할 수 있는 서버리스
대화형 쿼리 서비스를 사용할 수 있습니다. Athena 에서 CloudTrail 로그를 쿼리함으로써
회사는 사용자 활동 및 리소스 변경 사항에 대한 통찰력을 얻을 수 있습니다.
~~~

---

# Q709 

~~~ 설명
설명:
이를 통해 회사는 RDS 데이터베이스의 읽기 전용 복제본을 생성하고 데이터베이스 계층의
로드를 줄일 수 있습니다. 읽기 전용 복제본을 생성하면 회사는 기본 데이터베이스
인스턴스의 읽기 트래픽을 하나 이상의 복제본으로 오프로드할 수 있습니다. 새로운 읽기
전용 복제본을 사용하도록 보고서를 구성함으로써 회사는 데이터베이스 계층의 성능과
가용성을 향상시킬 수 있습니다.
~~~

---

# Q710 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/46383-exam-aws-certified-solut
ions-architect-associate-saa-c02/
설명1:
A(O) : arn:aws:s3:::AdminTools 는 버킷 자체를 의미. arn:aws:s3:::AdminTools/* 는 버킷
내 모든 객체를 의미
다음은 특정 Amazon S3 버킷 내에 포함된 모든 항목을 나타낸 예제입니다. 이하의 내용
참고.
https://docs.aws.amazon.com/ko_kr/IAM/latest/UserGuide/reference_policies_elements_r
esource.html
B(X) : CompanyConfidention 버킷에 권한이 없어야 하는데 s3:ListBucket 권한이 있으므로
오답.
C(X) : AdminTools 버킷에 s3:ListBucket 권한이 있어야 하는데 없으므로 오답.
s3:ListBucket 권한이 없이 읽고 쓰는 권한만 가지는 것은 무의미. 아래 링크 참고.
https://docs.aws.amazon.com/ko_kr/IAM/latest/UserGuide/reference_policies_examples_s
3_rw-bucket.html
D(X) : Allow, Deny에 모두 AdminTools/*가 등록되어있으므로 오답. Deny문은 Allow문보다
우선시 되기 때문.
정책이 Allow 설명문과 Deny 설명문을 포함한 요청에 적용된다면 Deny 설명문은 Allow
설명문에 우선합니다. 이 요청은 명시적으로 거부됩니다.
https://docs.aws.amazon.com/ko_kr/IAM/latest/UserGuide/reference_policies_evaluation-
logic.html
설명2:
https://docs.amazonaws.cn/en_us/IAM/latest/UserGuide/reference_policies_examples_s3
_rwbucket.html
ListBucket 작업에는 버킷에 대한 권한이 필요하고 다른 작업에는 버킷의 객체에 대한
권한이 필요하기 때문에 정책은 두 부분으로 구분됩니다.
버킷 수준 및 객체 수준 권한을 지정하려면 서로 다른 두 개의 ARN(Amazon 리소스
이름)을 사용해야 합니다.
첫 번째 Resource 요소는 애플리케이션이 AdminTools 버킷의 모든 객체를 나열할 수
있도록 ListBucket 작업에 대해 arn:aws:s3:::AdminTools를 지정합니다.
~~~

---

# Q711 

~~~ 설명
설명
다음과 같은 다양한 이유로 버킷에서 Transfer Acceleration을 사용할 수 있습니다.
전 세계에서 중앙 집중식 버킷에 업로드하는 고객이 있습니다.
대륙 간에 정기적으로 기가바이트에서 테라바이트의 데이터를 전송합니다.
Amazon S3에 업로드할 때 인터넷을 통해 사용 가능한 모든 대역폭을 활용할 수 없습니다.
https://docs.aws.amazon.com/AmazonS3/latest/dev/transfer-acceleration.html
"Amazon S3 Transfer Acceleration 은 더 큰 객체의 장거리 전송을 위해 Amazon S3 와의
콘텐츠 전송 속도를 50~500%까지 높일 수 있습니다.
광범위한 사용자가 있는 웹 또는 모바일 애플리케이션이 있거나 S3 버킷에서 멀리 떨어진
애플리케이션을 호스팅하는 고객은 인터넷을 통해 길고 가변적인 업로드 및 다운로드
속도를 경험할 수 있습니다."
https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html
"개선된 처리량 - 처리량을 개선하기 위해 부품을 병렬로 업로드할 수 있습니다."
여러 대륙의 도시에서 온도, 습도 및 대기압 데이터를 수집한다고 했으므로 여러 지역에서
업로드를 하는 상황. 즉 S3 Transfer Acceleration을 사용하는 A가 정답.
~~~

---

# Q712 

~~~ 설명
설명
노드 간 통신에 가장 낮은 지연 시간 = 클러스터 배치 그룹. A,B 둘 중 하나가 정답.
A(O) : Amazon EBS 다중 연결을 사용하면 단일 프로비저닝된 IOPS SSD(io1 또는 io2)
볼륨을 동일한 가용 영역에 있는 여러 인스턴스에 연결할 수 있습니다. 여러 다중 연결
지원 볼륨을 인스턴스 또는 인스턴스 집합에 연결할 수 있습니다....다중 연결을 사용하면
동시 쓰기 작업을 관리하는 클러스터링된 Linux 애플리케이션에서 더 쉽게 더 높은
애플리케이션 가용성을 얻을 수 있습니다.....다중 연결 지원 볼륨은 동일한 가용 영역에
있는 최대 16 개의 Nitro 시스템 기반 Linux 인스턴스에 연결할 수 있습니다.....다중 연결은
프로비저닝된 IOPS SSD(io1 및 io2) 볼륨에만 지원됩니다
https://docs.aws.amazon.com/ko_kr/AWSEC2/latest/UserGuide/ebs-volumes-multi.html
Provisioned IOPS SSD 볼륨의 크기는 4GiB 에서 16TiB 사이가 될 수 있고 볼륨당 100
IOPS 에서 최대 64,000 IOPS 가 프로비저닝될 수 있습니다. Nitro 시스템에 구축된
인스턴스에서만 최대 64,000 IOPS 를 달성할 수 있습니다. 다른 인스턴스 패밀리에서는
최대 32,000 IOPS 성능을 얻을 수 있습니다.
https://docs.aws.amazon.com/ko_kr/AWSEC2/latest/UserGuide/provisioned-iops.html#E
BSVolumeTypes_piops
B(X) : 공유 블록 장치 볼륨이라고 했으므로 오답. 블록 스토리지는 EBS. 그래도 IOPS
자체는 EBS보다 더 높은 편.
Amazon EFS 범용 및 최대 I/O라는 두 가지 성능 모드를 제공합니다.
◎범용 모드 : 최대 35,000 IOPS를 지원하며 작업당 지연 시간이 가장 낮습니다. EFS One
Zone 스토리지 클래스가 있는 파일 시스템은 항상 범용 성능 모드를 사용합니다. EFS
Standard 스토리지 클래스가 있는 파일 시스템의 경우 기본 범용 성능 모드 또는 최대 I/O
성능 모드를 사용할 수 있습니다.
◎최대 I/O 모드 : 500,000+ IOPS 를 지원하며 범용 모드에 비해 작업당 지연 시간이 더
깁니다. https://docs.aws.amazon.com/ko_kr/efs/latest/ug/performance.html
~~~

---

# Q713 

~~~ 설명
설명1:
A(X) : 노드 크기 조절은 아무 상관 없음.
B(X) : 데이터베이스 자체에 부하가 걸리는 것이 아니므로 읽기 부하를 분산하는
ElastiCache는 솔루션으로 적합하지 않음.
C(X) : 데이터베이스 자체에 부하가 걸리는 것이 아니므로 읽기 부하를 분산하는 복제본은
솔루션으로 적합하지 않음.
D(O) : RDS 프록시를 사용하여 예기치 않은 데이터베이스 트래픽 급증을 처리할 수
있습니다. 급증을 처리하지 않으면 연결 초과 구독 또는 빠른 속도의 새 연결 생성으로
인한 문제가 발생할 수 있습니다. RDS 프록시는 데이터베이스 연결 풀을 설정하고 이
풀에서 연결을 재사용합니다.
https://docs.aws.amazon.com/ko_kr/AmazonRDS/latest/UserGuide/rds-proxy.html
설명2:
1. 데이터베이스가 과부하의 징후를 보이지 않습니다. CPU, 메모리 및 디스크 액세스
메트릭은 모두 낮음==>A 및 C 출력입니다. 노드 인스턴스를 추가하거나 읽기 전용
복제본을 추가할 수는 없습니다.
2. "최소 운영 오버헤드"==>B 출력, b는 람다를 구성해야 하기 때문입니다.
3. ROS 프록시: 자주 사용되지 않는 연결을 공유합니다. 장애 조치를 통한 고가용성.
효율성 향상==>프록시는 장애 조치를 활용하여 시간 초과 rds 인스턴스에서 정상 rds
인스턴스로 트래픽을 리디렉션할 수 있습니다. 그래서 D가 맞습니다.
~~~

---

# Q714 

~~~ 설명
설명:
이 솔루션은 하루 중 시간에 따라 수요가 가변적이며 전체 비용을 최소화하면서 항상
사용할 수 있어야 하는 2 계층 애플리케이션의 요구 사항을 충족합니다. EC2 예약
인스턴스는 기본 사용 수준에 대해 온디맨드 인스턴스에 비해 상당한 비용 절감을 제공할
수 있으며 필요할 때 용량 예약을 보장할 수 있습니다. EC2 스팟 인스턴스는 피크 시간
동안 애플리케이션에 필요한 추가 용량에 대해 온디맨드 인스턴스에 비해 최대 90% 절감
효과를 제공할 수 있습니다. 스팟 인스턴스는 중단을 허용하고 다른 인스턴스로 교체할 수
있는 상태 비저장 애플리케이션에 적합합니다. RDS 데이터베이스를 사용하지 않을 때
중지하면 데이터베이스 계층 실행 비용을 줄일 수 있습니다.
여분의 용량이 충분하지 않거나 스팟 가격이 최대 가격을 초과하는 경우 모든 EC2 스팟
인스턴스를 사용하면 애플리케이션의 가용성에 영향을 미칠 수 있으므로 옵션 A 는
올바르지 않습니다. RDS 데이터베이스를 사용하지 않을 때 중지하면 데이터베이스 계층
실행 비용을 줄일 수 있지만 애플리케이션의 가용성에도 영향을 미칠 수 있습니다.
5 개의 EC2 인스턴스에 적용되는 EC2 Instance Savings Plans 를 구매하면 시간당 컴퓨팅
사용량이 고정되어 애플리케이션의 실제 사용 패턴과 일치하지 않을 수 있으므로 옵션 B 는
올바르지 않습니다. RDS 예약 DB 인스턴스를 구매하면 데이터베이스 계층을 절약할 수
있지만 사용하지 않을 때 데이터베이스를 중지할 수는 없습니다.
두 개의 EC2 인스턴스에 적용되는 EC2 Instance Savings Plans를 구매하면 시간당 컴퓨팅
사용량이 고정되어 애플리케이션의 실제 사용 패턴과 일치하지 않을 수 있으므로 옵션 D 는
올바르지 않습니다. 필요에 따라 최대 3개의 추가 EC2 온디맨드 인스턴스를 사용하면 스팟
인스턴스를 사용하는 것보다 더 많은 비용이 발생할 수 있습니다.
참조:
https://aws.amazon.com/ec2/pricing/reserved-instances/
https://aws.amazon.com/ec2/spot/
https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_StopInstance.html
~~~

---

# Q715 

~~~ 설명
설명:
이 옵션은 .html, .css, .js 및 이미지 파일과 같은 정적 및 동적 웹 콘텐츠를 사용자에게
빠르게 배포하는 웹 서비스인 Amazon CloudFront 를 사용하기 때문에 가장 효율적입니다.
또한 CloudFront 를 사용하여 S3 버킷에 대한 모든 요청을 처리하므로 에지 위치에서
콘텐츠를 캐싱하고 거기에서 콘텐츠를 제공하여 S3 비용을 줄입니다. 또한 CloudFront 가
지연 시간이 짧고 데이터 전송 속도가 빠른 콘텐츠를 제공하므로 인증된 외부 사용자가
밀리초 안에 문서에 액세스할 수 있습니다. 이 솔루션은 데이터 저장 비용을 계속
지불하면서 총 S3 비용을 절감해야 한다는 요구 사항을 충족합니다.
옵션 A 는 S3 버킷을 요청자 지불 버킷으로 구성하기 때문에 덜 효율적입니다. 이는 데이터
전송 및 요청 비용을 버킷 소유자에서 요청자에게 이전하는 방법입니다. 그러나 이것은
회사가 여전히 데이터 저장 및 자체 사용자의 요청에 대해 비용을 지불해야 하므로 총 S3
비용을 줄이지 않습니다.
옵션 B 는 높은 내구성과 가용성으로 자주 액세스하는 데이터를 저장하는 방법인 모든 기존
및 향후 객체에 대해 스토리지 계층을 S3 Standard 로 변경하기 때문에 효율성이
떨어집니다.
그러나 S3 Standard 는 S3 Standard-IA 보다 스토리지 비용이 높기 때문에 총 S3 비용은
줄어들지 않습니다.
옵션 C 는 CloudFront 엣지 로케이션을 통해 요청을 라우팅하여 S3 버킷 안팎으로 전송
속도를 높이는 방법인 S3 버킷에 대해 S3 Transfer Acceleration 을 활성화하기 때문에
효율성이 떨어집니다. 그러나 S3 Transfer Acceleration 에는 데이터 전송 및 요청에 대한
추가 요금이 있으므로 총 S3 비용은 줄어들지 않습니다.
~~~

---

# Q716 

~~~ 설명
설명:
서버리스 웹 애플리케이션과 호환되는 온프레미스 파일 공유에 대한 탄력적이고 내구성
있는 대체를 제공하기 때문에 이 대답은 정확합니다. Amazon S3 는 모든 양의 데이터를
저장하고 인터넷을 통해 제공할 수 있는 완전관리형 객체 스토리지 서비스입니다. 다음
기능을 지원합니다.
복원력: Amazon S3는 리전 내의 여러 가용 영역에 데이터를 저장하고 99.999999999%(11
9)의 내구성을 제공합니다. 또한 서로 다른 AWS 리전에 있는 버킷 간에 객체를 자동 및
비동기식으로 복사할 수 있는 교차 리전 복제를 지원합니다.
내구성: Amazon S3는 Amazon S3 관리형 키(SSE-S3), AWS KMS 키(SSE-KMS) 또는 고객
제공 키(SSE-C)로 서버 측 암호화를 사용하여 유휴 데이터를 암호화합니다. 또한
SSL/TLS 를 사용하여 전송 중 암호화를 지원합니다. 또한 Amazon S3 는 동일한 버킷에
객체의 여러 버전을 유지하는 버전 관리 및 객체 버전을 삭제하거나 버킷의 버전 관리
상태를 변경하기 위해 추가 인증이 필요한 MFA 삭제와 같은 데이터 보호 기능을
제공합니다.
성능: Amazon S3 는 정적 및 동적 웹 콘텐츠를 제공하기 위한 고성능 및 확장성을
제공합니다. 또한 요청을 AWS 엣지 로케이션으로 라우팅하여 데이터 전송 속도를 높이는
S3 Transfer Acceleration 및 간단한 SQL 표현식을 사용하여 객체에서 데이터의 하위
집합만 검색할 수 있는 S3 Select와 같은 기능을 지원합니다.
S3 Standard-Infrequent Access(S3 Standard-IA) 스토리지 클래스는 거의 액세스하지
않지만 필요할 때 즉시 사용할 수 있어야 하는 이미지를 저장하는 데 적합합니다. S3
Standard 와 동일한 높은 내구성, 처리량 및 짧은 대기 시간을 제공하지만 GB 당 스토리지
비용은 더 낮고 요청당 비용은 더 높습니다.
~~~

---

# Q717 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/86458-exam-aws-certified-solut
ions-architect-associate-saa-c02/
문제에서 보면 S3 2 페타바이트의 개체이고 쿼리 실행이 예상보다 오래 걸리는 상황입니다.
이를 위한 조치로는 먼저 파일을 Amazon S3 큰 단일 객체로 저장하여 AWS SDK, REST API
또는 AWS CLI를 사용하여 객체를 부분적으로 업로드합니다.
다음으로 Apache Parquet 출력 형식으로 이용할 수 있습니다. Amazon S3 Inventory 는
객체의 플랫 파일 목록과 버킷 또는 공유된 접두사에 대해 선택한 메타데이터를 제공합니다.
S3 Inventory 를 사용하여 객체 상태를 목록화, 감사 및 보고하거나 비즈니스 워크플로 및
빅 데이터 작업을 간소화하고 속도를 높일 수 있습니다.
따라서 답은 C, E로 보입니다.
https://docs.aws.amazon.com/AmazonS3/latest/userguide/upload-objects.html
https://aws.amazon.com/ko/about-aws/whats-new/2018/12/amazon-s3-announces-par
quet-output-format-for-inventory/
객체의 크기가 100MB 를 넘는 경우, 멀티파트 업로드 기능을 사용하는 방법을 고려해야
합니다. https://aws.amazon.com/ko/s3/faqs/ 따라서 A는 오답.
~~~

---

# Q718 

~~~ 설명
설명:
교차 계정 IAM 역할은 한 AWS 계정의 사용자에게 다른 AWS 계정의 리소스에 대한
액세스 권한을 부여하는 방법입니다. 교차 계정 IAM 역할에는 읽기 전용 액세스 정책이
연결되어 있어 사용자가 객체를 수정하거나 삭제하지 않고도 S3 버킷에서 객체를
다운로드할 수 있습니다. 교차 계정 IAM 역할은 또한 각 계정에서 여러 IAM 사용자 및
정책을 관리하는 운영 오버헤드를 줄입니다. 교차 계정 IAM 역할은 질문의 모든 요구
사항을 충족하지만 다른 옵션은 그렇지 않습니다.
참조:
https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-walkthroughs-mana
ging-accessexample2.html
https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.h
tml
~~~

---

# Q719 

~~~ 설명
설명1:
A(X) : DynamoDB Streams 는 수정/변경 사항을 최대 24 시간까지밖에 로그에 저장할 수
없음. 이를 변경할 수도 없음.
DynamoDB Streams 의 모든 데이터는 24 시간 동안 유지됩니다. 특정 테이블에 대한 지난
24 시간 동안의 활동을 조회하고 분석할 수 있습니다. 그러나 24 시간이 지난 데이터는
언제든 트리밍(제거)될 수 있습니다....기존 스트림을 수동으로 삭제하기 위한 메커니즘은
없습니다. 보유 제한이 만료(24 시간)될 때까지 기다려야 하며, 모든 스트림 레코드가
삭제됩니다.
https://docs.aws.amazon.com/ko_kr/amazondynamodb/latest/developerguide/Streams.ht
ml
B(X) : Redshift는 데이터베이스 서비스가 아니라 데이터 웨어하우스 서비스.
C(X) : 프로비저닝되었으므로 확장성이 떨어짐.
D(O) : Amazon Aurora MySQL 은 기본적으로 Auto Scaling 기능이 켜져있음. 복구 시간도
매우 짧음. 데이터베이스 감사 로그 또한 다운로드 가능
Aurora 는 단일 AWS 리전에서 다중 가용 영역에 걸쳐 DB 클러스터에 데이터 복사본을
저장합니다. DB 클러스터에 Aurora 복제본이 하나 이상인 경우에는 장애가 발생하더라도
Aurora 복제본이 기본 인스턴스로 승격됩니다. 이 실패 이벤트로 인해 예외적으로 실패하는
읽기 및 쓰기 작업 동안 짧은 중단이 발생합니다. 하지만, 일반적인 서비스 복구 시간은
120초 미만이지만 대부분 60초 미만에 복원됩니다.
https://docs.aws.amazon.com/ko_kr/AmazonRDS/latest/AuroraUserGuide/Concepts.Auror
aHighAvailability.html#Concepts.AuroraHighAvailability.Data
Amazon Aurora MySQL 의 고성능 고급 감사 기능을 사용하여 데이터베이스 활동을 감사할
수 있습니다. 이를 위해 여러 DB 클러스터 파라미터를 설정하여 감사 로그 수집을
활성화합니다. 콘솔을 사용하여 감사 로그를 확인하고 다운로드할 수 있습니다.
https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Auditin
g.html
~~~

---

# Q720 

~~~ 설명
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

# Q721 

~~~ 설명
설명:
Amazon RDS Proxy 는 애플리케이션의 확장성, 데이터베이스 장애에 대한 복원력, 보안을
강화하는 완전 관리형 데이터베이스 프록시입니다. RDS Proxy 는 애플리케이션과 관계형
데이터베이스 사이에 위치하여 설정된 데이터베이스 연결을 풀링하고 공유하여
데이터베이스 효율성과 애플리케이션 확장성을 개선합니다. 또한 RDS Proxy 는 일시적인
오류에 대한 연결 관리 및 쿼리 재시도를 처리하여 데이터베이스의 부하를 줄입니다.
서버리스 애플리케이션과 Amazon RDS 사이에 RDS Proxy 를 배포하면 오류가 발생하거나
연결이 끊어질 수 있는 데이터베이스 연결을 자주 열고 닫는 것을 방지할 수 있습니다. 이
솔루션은 또한 운영 비용을 절감하고 애플리케이션의 가용성을 향상시킵니다.
참조:
https://aws.amazon.com/rds/proxy/
~~~

---

# Q722 

~~~ 설명
설명:
이 옵션은 AWS 서비스와 함께 사용할 공개 및 비공개 SSL/TLS 인증서를 쉽게 프로비저닝,
관리 및 배포할 수 있는 서비스인 AWS Certificate Manager(ACM)에서 Amazon에서 발급한
공개 인증서를 요청하기 때문에 가장 효율적입니다. 내부 연결 자원. 또한 CloudFront 에서
ACM 인증서를 사용하는 데 필요한 us-east-1 리전에서 인증서를 요청합니다. 또한
ACM 은 지원되는 AWS 서비스와 함께 사용되는 인증서에 대해 비용을 청구하지 않으므로
추가 비용 없이 인증서를 배포해야 한다는 요구 사항을 충족합니다. 이 솔루션은 SSL/TLS
인증서를 사용하고 배포에 다른 도메인 이름을 사용하도록 CloudFront 배포를 구성해야
하는 요구 사항을 충족합니다.
옵션 A 는 조직 또는 Virtual Private Cloud(VPC) 내에서만 사용할 수 있는 인증서 유형인
ACM 에서 Amazon 에서 발급한 사설 인증서를 요청하기 때문에 효율성이 떨어집니다.
그러나 CloudFront 에는 공개 인증서가 필요하므로 이는 SSL/TLS 인증서를 사용하도록
CloudFront 배포를 구성해야 하는 요구 사항을 충족하지 않습니다. 또한 올바른 us-east-1
리전에서 인증서를 요청합니다.
옵션 B 는 옵션 A 와 같은 이유로 올바르지 않은 ACM 에서 Amazon 에서 발급한 사설
인증서를 요청하기 때문에 효율성이 떨어집니다. 또한 us-west-1 리전에서 인증서를
요청합니다. us-east-1 지역.
옵션 D 는 ACM 에서 Amazon 이 발행한 공용 인증서를 요청하기 때문에 효율성이
떨어집니다. 이는 올바른 것입니다.
하지만 us-west-1 리전에서 인증서를 요청합니다. 이는 CloudFront 가 us-east-1 리전의
인증서를 요구하기 때문에 올바르지 않습니다.
~~~

---

# Q723 

~~~ 설명
https://www.examtopics.com/discussions/amazon/view/35884-exam-aws-certified-solut
ions-architect-associate-saa-c02/
설명
https://docs.aws.amazon.com/ko_kr/AWSCloudFormation/latest/UserGuide/aws-resource
-ec2-placementgroup.html
"클러스터 배치 그룹은 네트워크 대기 시간이 짧고 네트워크 처리량이 높은 단일 가용 영역
내 인스턴스의 논리적 그룹입니다."
-> 긴밀하게 결합된 노드 = Cluster Deployment Group.
~~~

---

# Q724 

~~~ 설명
설명:
AWS Lambda 는 서버를 프로비저닝하거나 관리하지 않고도 코드를 실행할 수 있는
서버리스 컴퓨팅 서비스입니다. Lambda 는 들어오는 요청에 따라 자동으로 확장되지만
수요가 갑자기 증가하면 함수의 새 인스턴스를 초기화하는 데 시간이 걸릴 수 있습니다.
이로 인해 애플리케이션의 대기 시간이 길어지거나 콜드 스타트가 발생할 수 있습니다.
이를 방지하기 위해 함수가 초기화되고 언제든지 응답할 준비가 되도록 프로비저닝된
동시성을 사용할 수 있습니다. 또한 직원이 매일 애플리케이션을 사용하기 전에
프로비저닝된 동시성을 늘리고 수요가 적을 때 줄이는 예약된 조정 정책을 설정할 수도
있습니다.
참조:
https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html
~~~

---

# Q725 

~~~ 설명
설명:
Redis 솔루션용 ElastiCache 에 대해 노드 수준 및 리전 수준에서 고가용성을 제공하기
때문에 이 대답은 정확합니다. 다중 AZ Redis 복제 그룹은 각각 다른 가용 영역에 있는
기본 클러스터와 최대 5 개의 읽기 전용 복제본 클러스터로 구성됩니다. 기본 클러스터에
장애가 발생하면 읽기 전용 복제본 중 하나가 자동으로 새 기본 클러스터로 승격됩니다.
샤드가 있는 Redis 복제 그룹을 사용하면 여러 노드에 걸쳐 데이터를 분할할 수 있으므로
솔루션의 확장성과 성능이 향상됩니다. 각 샤드는 중복성과 읽기 확장성을 제공하기 위해
하나 이상의 복제본을 가질 수 있습니다.
참조:
https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/AutoFailover.html
https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Shards.html
~~~