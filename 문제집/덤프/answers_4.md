

# Q301
**정답: C**

**문제 분석:**
- 30TB 데이터를 5일 이내에 마이그레이션해야 하며, 대역폭 제어가 필요한 상황
- 1Gbps 네트워크지만 다른 부서와 공유하므로 대역폭 조절이 핵심 요구사항
- AWS DataSync는 네트워크 대역폭 제한(bandwidth throttling) 기능을 제공하여 다른 부서에 영향을 최소화하면서 데이터를 전송할 수 있음

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | AWS 스노우콘 | ❌ AWS Snowcone(A)은 오프라인 디바이스로 5일 배송/반송 시간을 고려하면 부적합 |
| B | Amazon FSx 파일 게이트웨이 | ❌ FSx 파일 게이트웨이(B)는 하이브리드 액세스용이지 마이그레이션 도구가 아님 |
| ✅ C | AWS 데이터싱크 | ✅ 정답 |
| D | AWS Transfer Family | ❌ AWS Transfer Family(D)는 SFTP/FTPS용으로 대량 마이그레이션에 부적합 |

---

# Q302
**정답: A, C**

**문제 분석:**
- 대용량 원시 비디오를 모바일에서 스트리밍할 때 버퍼링 문제 발생
- 운영 오버헤드 최소화하면서 성능과 확장성 극대화 필요

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| ✅ A | 콘텐츠 전송 및 캐싱을 위해 Amazon CloudFront를 배포합니다. | ✅ Amazon CloudFront(A): 전 세계 엣지 로케이션에서 콘텐츠 캐싱 및 전송, 사용자와 가까운 위치에서 콘텐츠 제공으로 버퍼링 감소 |
| B | AWS DataSync 를 사용하여 다른 S3 버킷의 AW'S 지역 전체에 비디오 파일을 복제합니다. | ❌ DataSync(B)는 데이터 복제용이지 스트리밍 최적화가 아님 |
| ✅ C | Amazon Elastic Transcoder 를 사용하여 비디오 파일을 보다 적절한 형식으로 변환합니다. | ✅ Amazon Elastic Transcoder(C): 원시 비디오를 모바일에 적합한 형식(HLS, DASH 등)으로 자동 변환, 관리형 서비스로 운영 오버헤드 최소화 |
| D | 콘텐츠 전송 및 캐싱을 위해 로컬 영역에 Amazon EC2 인스턴스의 Auto Sealing 그룹을 배포합... | ❌ Amazon Elastic Transcoder(C): 원시 비디오를 모바일에 적합한 형식(HLS, DASH 등)으로 자동 변환, 관리형 서비스로 운영 오버헤드 최소화 |
| E | Amazon EC2 인스턴스의 Auto Scaling 그룹을 배포하여 비디오 파일을 보다 적절한 형식으로 변... | ❌ EC2 기반 솔루션(D, E)은 운영 오버헤드가 높음 |

---

# Q303
**정답: D**

**문제 분석:**
- ECS Fargate에서 실행되는 애플리케이션의 CPU/메모리 기반 Auto Scaling 필요
- Target tracking은 지정된 메트릭(CPU, 메모리)을 목표값으로 유지하며 자동으로 스케일 조정
- CloudWatch 경보와 자동 통합되어 설정이 간단함

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | Amazon EC2 Auto Scaling 을 사용하여 이전 트래픽 패턴을 기반으로 특정 기간에 조정합니다. | ❌ ECS Fargate에서 실행되는 애플리케이션의 CPU/메모리 기반 Auto Scaling 필요 |
| B | AWS Lambda 함수를 사용하여 Amazon CloudWatch 경보를 트리거하는 메트릭 위반을 기반으로... | ❌ Lambda를 통한 수동 스케일링(B)은 복잡하고 비효율적 |
| C | 간단한 조정 정책과 함께 Amazon EC2 Auto Scaling 을 사용하여 ECS 메트릭 위반이 Ama... | ❌ EC2 Auto Scaling(A, C)은 ECS Fargate 작업에 직접 적용 불가 |
| ✅ D | 대상 추적 정책과 함께 AWS Application Auto Scaling 을 사용하여 ECS 메트릭 위반이... | ✅ AWS Application Auto Scaling with target tracking policy(D)가 ECS 서비스에 최적화된 솔루션 |

---

# Q304
**정답: A**

**문제 분석:**
- 두 리전의 NFS 파일 시스템 간 대량 데이터 정기 전송
- 최소 운영 오버헤드 요구
- AWS DataSync는 NFS 간 데이터 동기화를 자동화하는 관리형 서비스

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| ✅ A | AWS DataSync를 사용하십시오. | ✅ AWS DataSync는 NFS 간 데이터 동기화를 자동화하는 관리형 서비스 |
| B | AWS Snowball 디바이스를 사용합니다. | ❌ Snowball(B)은 오프라인 전송으로 정기적 사용에 부적합 |
| C | Amazon EC2에서 SFTP 서버를 설정합니다. | ❌ SFTP 서버(C)는 수동 관리 필요로 운영 오버헤드 증가 |
| D | AWS 데이터베이스 마이그레이션 서비스(AWS DMS)를 사용합니다. | ❌ DMS(D)는 데이터베이스 마이그레이션 전용 |

---

# Q305
**정답: C**

**문제 분석:**
- SMB 클라이언트 액세스가 가능한 완전 관리형 공유 스토리지 필요
- Amazon FSx for Windows File Server는 완전 관리형 Windows 파일 시스템
- 네이티브 SMB 프로토콜 지원으로 Windows 애플리케이션과 완벽 호환

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | 탑재 가능한 파일 시스템으로 데이터를 공유하는 AWS DataSync 작업을 생성합니다. 파일 시스템을 애플... | ❌ DataSync(A)는 데이터 전송 서비스이지 파일 시스템이 아님 |
| B | Amazon EC2 Windows 인스턴스를 생성합니다. 인스턴스에 Windows 파일 공유 역할을 설치하고... | ❌ EC2 기반 파일 서버(B)는 관리형이 아님 |
| ✅ C | Windows 파일 서버 파일 시스템용 Amazon FSx 를 생성합니다. 원본 서버에 파일 시스템을 연결합... | ✅ EC2 기반 파일 서버(B)는 관리형이 아님 |
| D | Amazon S3 버킷을 생성합니다. 애플리케이션에 IAM 역할을 할당하여 S3 버킷에 대한 액세스 권한을 ... | ❌ S3(D)는 SMB 프로토콜을 직접 지원하지 않음 |

---

# Q306
**정답: A**

**문제 분석:**
- 고성능 네트워크 처리량과 낮은 지연 시간이 필요한 인메모리 데이터베이스
- 데이터 전송 비용 최소화 필요
- 클러스터 배치 그룹은 단일 AZ 내에서 인스턴스를 물리적으로 가깝게 배치하여 최저 지연시간과 최고 네트워크 성능 제공

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| ✅ A | 동일한 AWS 리전 내의 동일한 가용 영역에서 모든 EC2 인스턴스를 시작합니다. EC2 인스턴스를 시작할 ... | ✅ 동일 AZ의 Cluster placement group(A)이 최적 솔루션 |
| B | 동일한 AWS 지역 내의 다른 가용 영역에서 모든 EC2 인스턴스를 시작합니다. EC2 인스턴스를 시작할 때... | ❌ Partition placement group(B)은 장애 격리용으로 네트워크 성능 최적화 안됨 |
| C | Auto Scaling 그룹을 배포하여 네트워크 활용 목표에 따라 다른 가용 영역에서 EC2 인스턴스를 시작... | ❌ 동일 AZ의 Cluster placement group(A)이 최적 솔루션 |
| D | 서로 다른 가용 영역에서 EC2 인스턴스를 시작하기 위해 단계 조정 정책으로 Auto Scaling 그룹을 ... | ❌ 다중 AZ 배포(C, D)는 AZ 간 데이터 전송 비용 발생 |

---

# Q307
**정답: D**

**문제 분석:**
- iSCSI 스토리지 확장 최소화, 최근 액세스 데이터만 로컬 저장 필요
- 자주 액세스하는 데이터만 로컬 캐시에 저장하고 전체 데이터는 S3에 저장
- iSCSI 프로토콜 지원으로 기존 애플리케이션 호환

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | Amazon S3 파일 게이트웨이 | ❌ S3 File Gateway(A)는 NFS/SMB용 |
| B | AWS Storage Gateway 테이프 게이트웨이 | ❌ Tape Gateway(B)는 백업/아카이빙용 |
| C | AWS Storage Gateway 볼륨 게이트웨이 저장 볼륨 | ❌ Stored Volumes(C)는 전체 데이터를 로컬에 저장하여 요구사항 불일치 |
| ✅ D | AWS Storage Gateway 볼륨 게이트웨이 캐시 볼륨 | ✅ Volume Gateway - Cached Volumes(D)가 요구사항에 정확히 일치 |

---

# Q308
**정답: B, C**

**문제 분석:**
- 90일 이상 실행되는 고성능 RDS Oracle 온디맨드 인스턴스의 비용 절감
- 통합 결제 계정에서 Trusted Advisor 확인 필요
- 90일 이상 실행되는 온디맨드 인스턴스는 RI로 전환하면 최대 75% 비용 절감 가능

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | RDS 인스턴스가 실행 중인 계정의 Trusted Advisor 권장 사항을 사용합니다. | ❌ 개별 계정(A)은 비효율적 |
| ✅ B | 통합 결제 계정의 Trusted Advisor 권장 사항을 사용하여 모든 RDS 인스턴스 확인을 동시에 확인... | ✅ 통합 결제 계정(B)에서 모든 멤버 계정의 RDS 인스턴스를 한 번에 확인 가능 |
| ✅ C | Amazon RDS 예약 인스턴스 최적화에 대한 Trusted Advisor 검사를 검토합니다. | ✅ Amazon RDS 예약 인스턴스 최적화 검사(C)를 통해 RI 구매 권장사항 확인 |
| D | Amazon RDS 유휴 DB 인스턴스에 대한 Trusted Advisor 검사를 검토합니다. | ❌ 유휴 DB 인스턴스(D)는 사용하지 않는 인스턴스 확인용으로 비용 절감과 다름 |
| E | Amazon Redshift 예약 노드 최적화에 대한 Trusted Advisor 검사를 검토합니다. | ❌ Redshift(E)는 관련 없음 |

---

# Q309
**정답: A**

**문제 분석:**
- 액세스하지 않는 S3 버킷 식별, 최소 운영 오버헤드 요구
- 버킷별 액세스 패턴, 활동 지표, 비용 최적화 기회를 대시보드로 제공
- 고급 메트릭으로 액세스 빈도, 마지막 액세스 시간 등 상세 분석 가능

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| ✅ A | 고급 활동 메트릭에 대한 S3 Storage Lens 대시보드를 사용하여 버킷 액세스 패턴을 분석합니다. | ✅ S3 Storage Lens with advanced activity metrics(A)가 최적 솔루션 |
| B | AWS Management Console 에서 S3 대시보드를 사용하여 버킷 액세스 패턴을 분석합니다. | ❌ S3 대시보드(B)는 기본 메트릭만 제공 |
| C | 버킷에 대한 Amazon CloudWatch BucketSizeBytes 지표를 켭니다. Amazon Ath... | ❌ BucketSizeBytes(C)는 용량만 측정하며 액세스 패턴 미제공 |
| D | S3 객체 모니터링을 위해 AWS CloudTrail 을 켭니다. Amazon CloudWatch Logs ... | ❌ CloudTrail(D)은 설정과 분석이 복잡하여 운영 오버헤드 증가 |

---

# Q310
**정답: B**

**문제 분석:**
- 대용량 파일 다운로드의 데이터 전송 비용 절감 및 성능 유지
- 고객이 북미/유럽에 분산, S3 서명 URL 사용 중
- CloudFront는 전 세계 엣지 로케이션에서 콘텐츠 캐싱하여 S3 아웃바운드 전송 비용 절감

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | 기존 S3 버킷에서 S3 Transfer Acceleration 을 구성합니다. 고객 요청을 S3 Trans... | ❌ S3 Transfer Acceleration(A)은 업로드 최적화용 |
| ✅ B | 기존 S3 버킷을 원본으로 사용하여 Amazon CloudFront 배포를 배포합니다. 고객 요청을 Clou... | ✅ CloudFront with CloudFront signed URLs(B)가 최적 솔루션 |
| C | 버킷 사이에 S3 교차 리전 복제가 있는 eu-central-1 리전에서 두 번째 S3 버킷을 설정합니다. ... | ❌ S3 CRR(C)은 여러 리전에 데이터 복제로 스토리지 비용 증가 |
| D | 데이터세트를 최종 사용자에게 스트리밍할 수 있도록 웹 애플리케이션을 수정합니다. 기존 S3 버킷에서 데이터를... | ❌ 웹 애플리케이션을 통한 스트리밍(D)은 EC2 비용 증가 및 확장성 문제 |

---

# Q311
**정답: C**

**문제 분석:**
- 견적 유형별 분리, 24시간 내 응답, 메시지 손실 방지, 운영 효율성 극대화
- SNS 메시지 필터링으로 견적 유형에 따라 적절한 SQS 대기열로 자동 라우팅
- SQS는 메시지 내구성 보장(손실 방지)

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | 견적 유형에 따라 여러 Amazon Kinesis 데이터 스트림을 생성합니다. 적절한 데이터 스트림으로 메시... | ❌ Kinesis(A)는 실시간 스트리밍용으로 과도한 설계 |
| B | 각 견적 유형에 대해 AWS Lambda 함수 및 Amazon Simple Notification Servi... | ❌ Lambda + SNS(B)는 큐 없이 메시지 손실 위험 |
| ✅ C | 단일 Amazon Simple Notification Service(Amazon SNS) 주제를 생성합니다.... | ✅ SNS topic with SQS queue subscription and message filtering(C)가 최적 솔루션 |
| D | 데이터 스트림을 Amazon OpenSearch Service 클러스터로 전달하기 위해 견적 유형을 기반으로... | ❌ Kinesis Firehose + OpenSearch(D)는 복잡하고 비용 증가 |

---

# Q312
**정답: B**

**문제 분석:**
- EC2 인스턴스 구성 및 여러 EBS 볼륨의 야간 백업, 다른 리전 복구 가능
- 운영 효율성 극대화 필요
- EC2 인스턴스를 리소스로 추가하면 연결된 모든 EBS 볼륨과 인스턴스 구성 자동 백업

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | 애플리케이션 EBS 볼륨의 야간 스냅샷을 예약하고 스냅샷을 다른 리전에 복사하는 AWS Lambda 함수를 ... | ❌ AWS Backup with EC2 instances as resources(B)가 최적 솔루션 |
| ✅ B | 야간 백업을 수행하기 위해 AWS Backup 을 사용하여 백업 계획을 생성합니다. 백업을 다른 리전에 복사... | ✅ AWS Backup with EC2 instances as resources(B)가 최적 솔루션 |
| C | 야간 백업을 수행하기 위해 AWS Backup 을 사용하여 백업 계획을 만듭니다. 백업을 다른 리전에 복사합... | ❌ EBS 볼륨만 백업(C)은 인스턴스 구성 누락 |
| D | 애플리케이션 EBS 볼륨의 야간 스냅샷을 예약하고 스냅샷을 다른 가용 영역에 복사하는 AWS Lambda 함... | ❌ Lambda 스크립트(A, D)는 수동 관리 필요 |

---

# Q313
**정답: C**

**문제 분석:**
- 수백만 사용자에게 모바일 콘텐츠 안전하게 제공
- 승인된 사용자만 액세스 가능
- CloudFront는 전 세계 엣지 로케이션으로 대규모 사용자에게 빠른 콘텐츠 전송

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | 퍼블릭 Amazon S3 버킷에 콘텐츠를 게시합니다. AWS Key Management Service(AWS... | ❌ 퍼블릭 S3 + KMS(A)는 액세스 제어 불가 |
| B | 모바일 앱과 AWS 환경 간에 IPsec VPN을 설정하여 콘텐츠를 스트리밍합니다. | ❌ IPsec VPN(B)은 모바일 앱에 부적합하고 확장성 제한 |
| ✅ C | Amazon CloudFront를 사용합니다. 스트리밍 콘텐츠에 서명된 URL을 제공합니다. | ✅ CloudFront with signed URLs(C)가 최적 솔루션 |
| D | 모바일 앱과 AWS 환경 간에 AWS Client VPN을 설정하여 콘텐츠를 스트리밍합니다. | ❌ Client VPN(D)도 모바일 대규모 사용자에 부적합 |

---

# Q314
**정답: B**

**문제 분석:**
- 드물게 액세스하는 MySQL 데이터베이스의 AWS 마이그레이션
- 가동 중지 최소화, 향후 사용자 증가 대비, 특정 인스턴스 유형 선택 불가
- 자동 스케일링으로 사용자 증가에 자동 대응

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | 아마존 오로라 MySQL | ❌ Aurora MySQL(A)은 인스턴스 크기 선택 필요 |
| ✅ B | MySQL용 Amazon Aurora 서버리스 | ✅ Amazon Aurora Serverless for MySQL(B)이 최적 솔루션 |
| C | 아마존 레드시프트 스펙트럼 | ❌ Redshift Spectrum(C)은 데이터 웨어하우스용 |
| D | MySQL용 Amazon RDS | ❌ RDS MySQL(D)은 인스턴스 크기 선택 및 수동 스케일링 필요 |

---

# Q315
**정답: D**

**문제 분석:**
- EC2 인스턴스의 맞춤형 애플리케이션 취약점 능동 스캔 및 상세 보고서 필요
- EC2 인스턴스의 소프트웨어 취약점 및 네트워크 노출 자동 스캔
- Inspector 에이전트로 깊이 있는 보안 평가

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | AWS Shield 를 배포하여 EC2 인스턴스의 취약점을 스캔합니다. 결과를 AWS CloudTrail에 ... | ❌ Shield(A)는 DDoS 방어 서비스 |
| B | Amazon Macie 및 AWS Lambda 함수를 배포하여 EC2 인스턴스의 취약점을 스캔합니다. 결과를... | ❌ Macie(B)는 S3 데이터 보안 서비스 |
| C | Amazon GuardDuty 를 켭니다. GuardDuty 에이전트를 EC2 인스턴스에 배포합니다. 결과를... | ❌ GuardDuty(C)는 위협 탐지 서비스로 취약점 스캔 기능 없음 |
| ✅ D | Amazon Inspector를 켭니다. Amazon Inspector 에이전트를 EC2 인스턴스에 배포합니... | ✅ Amazon Inspector(D)가 정확한 솔루션 |

---

# Q316
**정답: C**

**문제 분석:**
- SQS 대기열 메시지 처리를 위한 EC2 기반 스크립트의 비용 절감
- 증가하는 메시지 처리 능력 유지
- Lambda는 SQS 대기열과 네이티브 통합

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | 메시지를 더 빠르게 처리하려면 EC2 인스턴스의 크기를 늘리십시오. | ❌ EC2 크기 증가(A)는 비용 증가 |
| B | 인스턴스가 충분히 활용되지 않을 때 Amazon EventBridge를 사용하여 EC2 인스턴스를 끕니다. | ❌ EventBridge로 인스턴스 끄기(B)는 메시지 처리 능력 감소 |
| ✅ C | EC2 인스턴스의 스크립트를 적절한 런타임이 있는 AWS Lambda 함수로 마이그레이션합니다. | ✅ Lambda function with appropriate runtime(C)이 최적 솔루션 |
| D | AWS Systems Manager Run Command를 사용하여 요청 시 스크립트를 실행합니다. | ❌ Systems Manager Run Command(D)는 온디맨드 실행으로 지속적 처리에 부적합 |

---

# Q317
**정답: A**

**문제 분석:**
- 레거시 CSV 출력을 COTS 애플리케이션(Redshift/S3 쿼리)이 사용할 수 있도록 변환
- 최소 운영 오버헤드 요구
- Glue는 완전 관리형 ETL 서비스로 CSV를 Redshift 호환 형식으로 변환

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| ✅ A | 일정에 따라 실행되는 AWS Glue 추출, 변환 및 로드(ETL) 작업을 생성합니다. .csv 파일을 처리... | ✅ AWS Glue ETL job on schedule(A)가 최적 솔루션 |
| B | Amazon EC2 인스턴스에서 실행되는 Python 스크립트를 개발하여 .csv 파일을 .sql 파일로 변... | ❌ Python 스크립트 + cron(B)은 EC2 관리 필요 |
| C | AWS Lambda 함수와 Amazon DynamoDB 테이블을 생성합니다. S3 이벤트를 사용하여 Lamb... | ❌ Lambda + DynamoDB(C)는 Redshift/S3 쿼리 요구사항 불일치 |
| D | Amazon EventBridge 를 사용하여 매주 일정에 따라 Amazon EMR 클러스터를 시작합니다. ... | ❌ EMR(D)은 과도한 설계이며 Glue보다 운영 오버헤드 높음 |

---

# Q318
**정답: A, D**

**문제 분석:**
- EC2 인스턴스 프로비저닝 및 보안 그룹 변경에 대한 추적과 감사 필요
- 변경 제어 프로세스 우회 방지
- 두 서비스를 함께 사용하면 완전한 감사 및 규정 준수 모니터링 가능

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| ✅ A | AWS CloudTrail을 활성화하고 감사에 사용하십시오. | ✅ AWS CloudTrail(A): 모든 API 호출 기록으로 누가, 언제, 무엇을 변경했는지 감사 |
| B | Amazon EC2 인스턴스에 대한 데이터 수명 주기 정책을 사용합니다. | ❌ 데이터 수명 주기 정책(B)은 관련 없음 |
| C | AWS Trusted Advisor를 활성화하고 보안 대시보드를 참조합니다. | ❌ Trusted Advisor(C)는 권장사항 제공이지 변경 추적 아님 |
| ✅ D | AWS Config를 활성화하고 감사 및 규정 준수를 위한 규칙을 생성합니다. | ✅ AWS Config(D): 리소스 구성 변경 추적, 규정 준수 규칙으로 부적절한 변경 탐지 및 경고 |
| E | AWS CloudFormation 템플릿을 사용하여 이전 리소스 구성을 복원합니다. | ❌ CloudFormation(E)은 복원 도구이지 추적 도구 아님 |

---

# Q319
**정답: A**

**문제 분석:**
- 공유 SSH 키 제거, 보안 액세스 제공, 최소 관리 오버헤드
- SSH 키 없이 브라우저 기반 또는 CLI로 인스턴스 액세스
- IAM 정책으로 세분화된 액세스 제어

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| ✅ A | AWS Systems Manager Session Manager를 사용하여 EC2 인스턴스에 연결합니다. | ✅ AWS Systems Manager Session Manager(A)가 최적 솔루션 |
| B | AWS Security Token Service(AWS STS)를 사용하여 온디맨드 방식으로 일회성 SSH ... | ❌ STS 일회용 키(B)는 표준 기능 아님 |
| C | 배스천 인스턴스 집합에 대한 공유 SSH 액세스를 허용합니다. 배스천 인스턴스에서 SSH 액세스만 허용하도록... | ❌ Bastion 인스턴스(C)는 여전히 키 관리 필요 |
| D | Amazon Cognito 사용자 지정 권한 부여자를 사용하여 사용자를 인증합니다. AWS Lambda 함수... | ❌ Cognito + Lambda(D)는 과도하게 복잡함 |

---

# Q320
**정답: A**

**문제 분석:**
- JSON 데이터 수집(최대 1MB/s), 거의 실시간 쿼리, 데이터 손실 최소화
- Kinesis Data Streams는 실시간 데이터 수집 및 내구성 보장(데이터 손실 방지)
- 여러 파티션으로 자동 확장

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| ✅ A | Amazon Kinesis Data Streams에 데이터를 게시하고 Kinesis Data Analytic... | ✅ Kinesis Data Streams + Kinesis Data Analytics(A)가 최적 솔루션 |
| B | Amazon Redshift 를 대상으로 사용하여 Amazon Kinesis Data Firehose 에 데... | ❌ Firehose + Redshift(B)는 실시간 쿼리에 지연 발생 |
| C | 수집된 데이터를 EC2 인스턴스 스토어에 저장합니다. Amazon S3 를 대상으로 Amazon Kinesi... | ❌ 인스턴스 스토어(C)는 재부팅 시 데이터 손실 |
| D | 수집된 데이터를 Amazon Elastic Block Store(Amazon EBS) 볼륨에 저장합니다. R... | ❌ EBS + ElastiCache(D)는 JSON 쿼리에 부적합 |

---

# Q321
**정답: D**

**문제 분석:**
- S3 버킷에 업로드되는 모든 객체의 암호화 강제
- PutObject 요청에 서버 측 암호화 헤더가 없으면 거부
- SSE-S3, SSE-KMS, SSE-C 중 선택 가능

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | PutObject 에 s3:x-amz-acl 헤더 세트가 없는 경우 거부하도록 버킷 정책을 업데이트합니다. | ❌ s3:x-amz-acl(A, B)은 액세스 제어 리스트 관련 |
| B | PutObject 에 프라이빗으로 설정된 s3:x-amz-acl 헤더가 없는 경우 거부하도록 버킷 정책을 업... | ❌ s3:x-amz-acl(A, B)은 액세스 제어 리스트 관련 |
| C | PutObject 에 true 로 설정된 aws:SecureTransport 헤더가 없는 경우 거부하도록 버... | ❌ aws:SecureTransport(C)는 HTTPS 전송 암호화이지 저장 암호화 아님 |
| ✅ D | PutObject 에 x-amz-server-side-encryption 헤더 세트가 없는 경우 거부하도록 ... | ✅ x-amz-server-side-encryption header(D)를 요구하는 버킷 정책이 정답 |

---

# Q322
**정답: C**

**문제 분석:**
- 이미지 업로드 후 60초 소요 썸네일 생성을 비동기로 처리, 빠른 업로드 확인 필요
- 프런트엔드가 이미지 업로드 완료 즉시 사용자에게 확인 응답
- 썸네일 생성 메시지를 SQS에 전송하여 비동기 처리

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | 사용자 지정 AWS Lambda 함수를 작성하여 썸네일을 생성하고 사용자에게 알립니다. 이미지 업로드 프로세... | ❌ Lambda(A)는 동기적 처리로 지연 발생 |
| B | AWS Step Functions 워크플로를 생성합니다. 애플리케이션 계층 간의 오케스트레이션을 처리하고 썸... | ❌ Step Functions(B)는 완료 알림이 워크플로 끝에서만 가능 |
| ✅ C | Amazon Simple Queue Service(Amazon SQS) 메시지 대기열을 생성합니다. 이미지가... | ✅ SQS message queue(C)가 최적 솔루션 |
| D | Amazon Simple Notification Service(Amazon SNS) 알림 주제 및 구독을 생... | ❌ SNS(D)는 썸네일 생성 완료 후 알림으로 요구사항 불일치 |

---

# Q323
**정답: B**

**문제 분석:**
- 배지 리더 HTTPS 메시지 처리, 고가용성, 보안 팀 분석용 결과 제공
- API Gateway는 고가용성 HTTPS 엔드포인트 제공, 자동 스케일링
- Lambda는 서버리스로 메시지 처리, 인프라 관리 불필요

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | Amazon EC2 인스턴스를 시작하여 HTTPS 엔드포인트 역할을 하고 메시지를 처리합니다. 결과를 Ama... | ❌ 단일 EC2(A)는 단일 장애점 |
| ✅ B | Amazon API Gateway 에서 HTTPS 엔드포인트를 생성합니다. AWS Lambda 함수를 호출하... | ✅ API Gateway + Lambda + DynamoDB(B)가 최적 솔루션 |
| C | Amazon Route 53을 사용하여 들어오는 센서 메시지를 AWS Lambda 함수로 보냅니다. 메시지를... | ❌ Route 53(C)는 DNS 서비스로 메시지 전달 불가 |
| D | Amazon S3 용 게이트웨이 VPC 엔드포인트를 생성합니다. 센서 데이터가 VPC 엔드포인트를 통해 S3... | ❌ S3 + Site-to-Site VPN(D)은 실시간 처리에 부적합 |

---

# Q324
**정답: D**

**문제 분석:**
- 수백 TB iSCSI 온프레미스 스토리지의 DR, 지연 없는 즉시 액세스, 최소 인프라 변경
- 전체 데이터를 로컬에 저장하여 지연 없는 즉시 액세스
- 비동기로 S3에 스냅샷 백업

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | 온프레미스에서 호스팅되는 가상 머신(VM)으로 Amazon S3 파일 게이트웨이를 프로비저닝합니다. 로컬 캐... | ❌ S3 File Gateway(A)는 NFS/SMB용이며 로컬 캐시 10TB는 수백 TB에 부족 |
| B | AWS Storage Gateway 테이프 게이트웨이를 프로비저닝합니다. 데이터 백업 솔루션을 사용하여 모든... | ❌ Tape Gateway(B)는 백업/복원이 느림 |
| C | AWS Storage Gateway 볼륨 게이트웨이 캐시 볼륨을 프로비저닝합니다. 로컬 캐시를 10TB 로 ... | ❌ Cached Volumes(C)는 로컬 캐시 10TB로 전체 데이터 즉시 액세스 불가 |
| ✅ D | 기존 파일 스토리지 볼륨과 동일한 양의 디스크 공간으로 AWS Storage Gateway 볼륨 게이트웨이 ... | ✅ Volume Gateway - Stored Volumes(D)가 최적 솔루션 |

---

# Q325
**정답: A**

**문제 분석:**
- Cognito JWT로 S3 보호 리소스 액세스 시 권한 오류
- Identity pool은 Cognito 인증 토큰을 AWS 자격 증명으로 교환
- IAM 역할로 S3 버킷 액세스 권한 부여

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| ✅ A | Amazon Cognito 자격 증명 풀을 업데이트하여 보호된 콘텐츠에 액세스하기 위한 적절한 IAM 역할을... | ✅ Cognito identity pool with IAM role(A)이 정답 |
| B | 애플리케이션이 보호된 콘텐츠에 액세스할 수 있도록 S3 ACL을 업데이트합니다. | ❌ S3 ACL(B)은 Cognito와 통합 안됨 |
| C | 애플리케이션을 Amazon S3 에 재배포하여 S3 버킷의 최종적으로 일관된 읽기가 보호된 콘텐츠에 액세스하... | ❌ 최종 일관성(C)은 문제 원인 아님 |
| D | 자격 증명 풀 내에서 사용자 지정 속성 매핑을 사용하고 사용자에게 보호된 콘텐츠에 액세스할 수 있는 적절한 ... | ❌ 사용자 지정 속성(D)은 AWS 리소스 액세스 권한 제공 불가 |

---

# Q326
**정답: A, B**

**문제 분석:**
- S3 Standard 버킷의 멀티파트 업로드, 30일 후 액세스 감소, 고가용성 유지, 비용 최적화

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| ✅ A | 30일 후에 자산을 S3 Intelligent-Tiering으로 이동합니다. | ✅ S3 Intelligent-Tiering 전환(A): 30일 후 액세스 패턴이 일관되지 않으므로 Intelligent-Tiering이 자동으로 적절한 계층 선택 |
| ✅ B | 불완전한 멀티파트 업로드를 정리하도록 S3 수명 주기 정책을 구성합니다. | ✅ 불완전한 멀티파트 업로드 정리(B): 완료되지 않은 멀티파트 업로드는 스토리지 비용 발생, 수명 주기 정책으로 자동 정리 |
| C | 만료된 개체 삭제 마커를 정리하도록 S3 수명 주기 정책을 구성합니다. | ❌ 만료된 삭제 마커(C)는 버전 관리 버킷에만 해당 |
| D | 30일 후에 자산을 S3 Standard-Infrequent Access(S3 Standard-IA)로 이동... | ❌ S3 Standard-IA(D)는 액세스 패턴이 일관되지 않아 Intelligent-Tiering보다 비효율적 |
| E | 30일 후 자산을 S3 One Zone-Infrequent Access(S3 One Zone-IA)로 이동합... | ❌ S3 One Zone-IA(E)는 단일 AZ로 고가용성 요구사항 불일치 |

---

# Q327
**정답: A**

**문제 분석:**
- 프라이빗 서브넷 EC2의 아웃바운드 인터넷 액세스를 승인된 URL만 허용
- 도메인 목록 규칙 그룹으로 특정 URL만 허용
- 프라이빗 서브넷 라우팅 테이블을 Network Firewall로 업데이트

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| ✅ A | 아웃바운드 트래픽을 AWS 네트워크 방화벽 방화벽으로 라우팅하도록 프라이빗 서브넷의 라우팅 테이블을 업데이트... | ✅ AWS Network Firewall with domain list rule group(A)이 최적 솔루션 |
| B | AWS WAF 웹 ACL 을 설정합니다. 소스 및 대상 IP 주소 범위 집합을 기반으로 트래픽 요청을 필터링... | ❌ AWS WAF(B)는 인바운드 웹 애플리케이션 보호용 |
| C | 엄격한 인바운드 보안 그룹 규칙을 구현합니다. URL 을 지정하여 인터넷에서 승인된 소프트웨어 리포지토리에 ... | ❌ 보안 그룹(C)은 URL 지정 불가, IP/포트만 가능 |
| D | EC2 인스턴스 앞에 Application Load Balancer(ALB)를 구성합니다. 모든 아웃바운드 ... | ❌ ALB(D)는 아웃바운드 트래픽 제어 불가 |

---

# Q328
**정답: D**

**문제 분석:**
- S3 호스팅 웹사이트, ALB 뒤 EC2 API, 비동기 백엔드 워커, 판매 급증 대비
- CloudFront로 정적 콘텐츠 캐싱하여 S3/EC2 부하 감소
- SQS 큐로 판매 요청을 버퍼링하여 백엔드 워커가 비동기 처리

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | 동적 콘텐츠에 대한 Amazon CloudFront 배포를 추가합니다. 트래픽 증가를 처리하기 위해 EC2 ... | ❌ S3 호스팅 웹사이트, ALB 뒤 EC2 API, 비동기 백엔드 워커, 판매 급증 대비 |
| B | 정적 콘텐츠에 대한 Amazon CloudFront 배포를 추가합니다. Auto Scaling 그룹에 EC2... | ❌ 네트워크 트래픽 기반 Auto Scaling(B)은 급증에 반응 지연 |
| C | 동적 콘텐츠에 대한 Amazon CloudFront 배포를 추가합니다. ALB 앞에 Amazon Elasti... | ❌ 동적 콘텐츠 CloudFront(A, C)는 API 요청 캐싱에 부적합 ElastiCache(C)는 비동기 처리 제공 안함 |
| ✅ D | 정적 콘텐츠에 대한 Amazon CloudFront 배포를 추가합니다. Amazon Simple Queue ... | ✅ CloudFront for static content + SQS queue(D)가 최적 솔루션 |

---

# Q329
**정답: D**

**문제 분석:**
- 대규모 EC2의 정기 보안 스캔, 정기 패치, 패치 상태 보고
- Inspector: EC2 소프트웨어 취약점 자동 스캔, 지속적 평가
- Patch Manager: 정기 일정으로 자동 패치, 패치 준수 보고서 제공

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | EC2 인스턴스에서 소프트웨어 취약성을 스캔하도록 Amazon Macie 를 설정합니다. 각 EC2 인스턴스... | ❌ Macie(A)는 S3 데이터 보안 서비스 |
| B | 계정에서 Amazon GuardDuty 를 켭니다. 소프트웨어 취약성에 대해 EC2 인스턴스를 스캔하도록 G... | ❌ GuardDuty(B)는 위협 탐지이지 취약점 스캔/패치 아님 |
| C | 소프트웨어 취약성에 대해 EC2 인스턴스를 스캔하도록 Amazon Detective를 설정합니다. 정기적인 ... | ❌ Detective(C)는 보안 조사 서비스 |
| ✅ D | 계정에서 Amazon Inspector 를 켭니다. 소프트웨어 취약성에 대해 EC2 인스턴스를 스캔하도록 A... | ✅ Amazon Inspector + Systems Manager Patch Manager(D)가 최적 솔루션 |

---

# Q330
**정답: A**

**문제 분석:**
- RDS DB 인스턴스의 미사용 데이터 암호화
- RDS 생성 시 KMS 고객 관리형 키로 암호화 활성화
- 스토리지, 백업, 스냅샷, 읽기 복제본 모두 자동 암호화

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| ✅ A | AWS Key Management Service(AWS KMS)에서 키를 생성합니다. DB 인스턴스에 대한 ... | ✅ AWS KMS key + enable encryption(A)이 정답 |
| B | 암호화 키를 생성합니다. AWS Secrets Manager에 키를 저장합니다. 키를 사용하여 DB 인스턴스... | ❌ Secrets Manager(B)는 자격 증명 관리용이지 데이터 암호화 아님 |
| C | AWS Certificate Manager(ACM)에서 인증서를 생성합니다. 인증서를 사용하여 DB 인스턴스... | ❌ ACM/IAM 인증서(C, D)는 전송 중 암호화(SSL/TLS)용 |
| D | AWS Identity and Access Management(IAM)에서 인증서를 생성합니다. 인증서를 사... | ❌ ACM/IAM 인증서(C, D)는 전송 중 암호화(SSL/TLS)용 |

---

# Q331
**정답: A**

**문제 분석:**
- 20TB 데이터를 30일 내 전송, 15Mbps의 70% 사용 제한
- 15Mbps × 0.7 × 30일 = 약 34TB 전송 가능하지만 실제는 불안정
- 80TB Snowball Edge로 20TB 오프라인 전송

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| ✅ A | AWS Snowball을 사용하십시오. | ✅ AWS Snowball(A)이 최적 솔루션 |
| B | AWS DataSync를 사용합니다. | ❌ DataSync(B), VPN(C), S3 Transfer Acceleration(D)은 모두 네트워크 기반으로 대역폭 제약 |
| C | 안전한 VPN 연결을 사용하십시오. | ❌ DataSync(B), VPN(C), S3 Transfer Acceleration(D)은 모두 네트워크 기반으로 대역폭 제약 |
| D | Amazon S3 Transfer Acceleration을 사용합니다. | ❌ DataSync(B), VPN(C), S3 Transfer Acceleration(D)은 모두 네트워크 기반으로 대역폭 제약 |

---

# Q332
**정답: B**

**문제 분석:**
- 온프레미스 Windows 파일 서버의 용량 부족, 원격 사용자 증가, 안전한 다운로드
- FSx는 완전 관리형 Windows 파일 시스템으로 자동 확장
- 온프레미스 AD와 통합하여 기존 권한 유지

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | 파일 서버를 퍼블릭 서브넷의 Amazon EC2 인스턴스로 마이그레이션합니다. 인바운드 트래픽을 직원의 IP... | ❌ 퍼블릭 EC2(A)는 보안 위험 |
| ✅ B | 파일을 Amazon FSx for Windows File Server 파일 시스템으로 마이그레이션합니다. A... | ✅ FSx for Windows File Server + Active Directory + AWS Client VPN(B)이 최적 솔루션 |
| C | 파일을 Amazon S3 로 마이그레이션하고 프라이빗 VPC 엔드포인트를 생성합니다. 다운로드를 허용하려면 ... | ❌ S3 프라이빗 엔드포인트(C)는 파일 서버 기능 부족 |
| D | 파일을 Amazon S3 로 마이그레이션하고 퍼블릭 VPC 엔드포인트를 생성합니다. 직원이 AWS IAM I... | ❌ S3 퍼블릭 엔드포인트(D)는 적절한 액세스 제어 어려움 |

---

# Q333
**정답: C**

**문제 분석:**
- 매월 1일 자정 배치 작업으로 CPU 100% 및 애플리케이션 중단
- 예측 가능한 일정의 용량 증가 필요
- 매월 1일 자정 30분 전에 인스턴스 사전 증설

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | ALB 앞에 Amazon CloudFront 배포를 구성합니다. | ❌ CloudFront(A)는 정적 콘텐츠 캐싱용 |
| B | CPU 사용률을 기반으로 EC2 Auto Scaling 단순 조정 정책을 구성합니다. | ❌ 단순 조정 정책(B)은 이미 CPU 100%일 때 반응하여 늦음 |
| ✅ C | 월별 일정을 기반으로 EC2 Auto Scaling 예약 조정 정책을 구성합니다. | ✅ Scheduled scaling policy(C)가 최적 솔루션 |
| D | EC2 인스턴스에서 일부 워크로드를 제거하도록 Amazon ElastiCache를 구성합니다. | ❌ ElastiCache(D)는 배치 처리 워크로드에 부적합 |

---

# Q334
**정답: A**

**문제 분석:**
- 온프레미스 AD 인증으로 S3 파일 SFTP 다운로드, 최소 오버헤드, 클라이언트 변경 없음
- 완전 관리형 SFTP 서비스로 S3를 백엔드로 사용
- 온프레미스 AD와 통합하여 기존 자격 증명 사용

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| ✅ A | Amazon S3 용 SFTP 로 AWS Transfer Family 를 설정합니다. 통합된 Active D... | ✅ AWS Transfer Family for SFTP + AD authentication(A)이 최적 솔루션 |
| B | 온프레미스 클라이언트를 Amazon S3 와 동기화하도록 AWS DMS(AWS Database Migrati... | ❌ DMS(B)는 데이터베이스 마이그레이션용 |
| C | AWS IAM Identity Center(AWS Single Sign-On)를 사용하여 온프레미스 위치와 ... | ❌ DataSync(C)는 SFTP 프로토콜 미지원 |
| D | SFTP로 Windows Amazon EC2 인스턴스를 설정하여 온프레미스 클라이언트를 Amazon S3와 ... | ❌ EC2 SFTP 서버(D)는 관리 오버헤드 증가 |

---

# Q335
**정답: B**

**문제 분석:**
- Auto Scaling 그룹의 대규모 EC2 빠른 초기화, 2배 IOPS 용량 유지
- 스냅샷에서 FSR 활성화하면 EBS 볼륨 초기화 시간 제거
- FSR 활성화 스냅샷으로 AMI 생성

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | aws ec2 register-image 명령을 사용하여 스냅샷에서 AMI 를 생성합니다. AWS Step ... | ❌ aws ec2 register-image(A)는 초기화 지연 해결 안함 |
| ✅ B | 스냅샷에서 Amazon Elastic Block Store(Amazon EBS) 빠른 스냅샷 복원을 활성화합... | ✅ EBS Fast Snapshot Restore(B)가 최적 솔루션 |
| C | Amazon Data Lifecycle Manager(Amazon DLM)에서 AMI 생성을 활성화하고 수명... | ❌ DLM(C)과 AWS Backup(D)은 AMI 관리용이지 초기화 최적화 아님 |
| D | Amazon EventBridge를 사용하여 AMI를 프로비저닝하는 AWS Backup 수명 주기 정책을 호... | ❌ DLM(C)과 AWS Backup(D)은 AMI 관리용이지 초기화 최적화 아님 |

---

# Q336
**정답: A**

**문제 분석:**
- Aurora MySQL DB 자격 증명 암호화, 14일마다 자동 교체, 최소 운영 노력
- Secrets Manager는 DB 자격 증명 암호화 저장
- Aurora와 네이티브 통합으로 자동 교체 및 업데이트

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| ✅ A | 새 AWS Key Management Service(AWS KMS) 암호화 키를 생성합니다. AWS Secr... | ✅ Secrets Manager with KMS key and 14-day rotation(A)가 최적 솔루션 |
| B | AWS Systems Manager Parameter Store 에서 두 개의 매개변수를 생성합니다. 하나는... | ❌ Parameter Store(B)는 자동 순환 및 DB 업데이트 미지원 |
| C | 자격 증명이 포함된 파일을 AWS KMS(AWS Key Management Service) 암호화 Amazo... | ❌ EFS/S3(C, D)는 수동 관리 필요하고 자동 DB 업데이트 없음 |
| D | 애플리케이션이 자격 증명을 로드하는 데 사용하는 AWS KMS(AWS Key Management Servic... | ❌ EFS/S3(C, D)는 수동 관리 필요하고 자동 DB 업데이트 없음 |

---

# Q337
**정답: A**

**문제 분석:**
- RDS MySQL 읽기 복제본의 복제 지연 문제, 저장 프로시저 사용, 최소 코드 변경
- Aurora는 RDS보다 5배 빠른 복제 성능
- Aurora 복제본은 밀리초 수준 지연

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| ✅ A | 데이터베이스를 Amazon Aurora MySQL 로 마이그레이션합니다. 읽기 전용 복제본을 Aurora 복... | ✅ Aurora MySQL with Aurora Replicas(A)가 최적 솔루션 |
| B | 데이터베이스 앞에 Redis 클러스터용 Amazon ElastiCache 를 배포합니다. 응용 프로그램이 데... | ❌ ElastiCache(B)는 복제 지연 해결 안되고 애플리케이션 대폭 수정 필요 |
| C | 데이터베이스를 Amazon EC2 인스턴스에서 실행되는 MySQL 데이터베이스로 마이그레이션합니다. 모든 복... | ❌ EC2 MySQL(C)은 관리 오버헤드 증가 |
| D | 데이터베이스를 Amazon DynamoDB 로 마이그레이션합니다. 필요한 처리량을 지원하고 온디맨드 용량 확... | ❌ DynamoDB(D)는 저장 프로시저 미지원 |

---

# Q338
**정답: B**

**문제 분석:**
- Aurora MySQL의 보조 리전 DR 복제, 비용 효율성 최대화
- Global Database는 리전 간 1초 미만 복제 지연
- 보조 리전에 DB 인스턴스 없이 복제만 유지하여 비용 최소화

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | 보조 리전의 Aurora 클러스터에 MySQL 바이너리 로그 복제를 사용합니다. 보조 리전에서 Aurora ... | ❌ MySQL 바이너리 로그(A)는 수동 관리 필요 |
| ✅ B | DB 클러스터에 대한 Aurora 글로벌 데이터베이스를 설정합니다. 설정이 완료되면 보조 리전에서 DB 인스... | ✅ Aurora Global Database with no DB instance in secondary(B)가 최적 솔루션 |
| C | AWS Database Migration Service(AWS DMS)를 사용하여 데이터를 보조 리전의 Au... | ❌ DMS(C)는 복제 지연 발생 |
| D | DB 클러스터에 대한 Aurora 글로벌 데이터베이스를 설정합니다. 보조 리전에서 최소 하나의 DB 인스턴스... | ❌ 항상 DB 인스턴스 유지(D)는 비용 증가 |

---

# Q339
**정답: C**

**문제 분석:**
- RDS MySQL 자격 증명 내장 애플리케이션의 보안 강화, 최소 프로그래밍 노력
- Secrets Manager는 RDS MySQL과 네이티브 통합
- 자동 교체 일정 설정으로 DB에서 직접 자격 증명 업데이트

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | AWS Key Management Service(AWS KMS)를 사용하여 키를 생성합니다. AWS KMS에... | ❌ KMS(A)는 키 관리용이지 자격 증명 관리 아님 |
| B | 애플리케이션 사용자를 위해 RDS for MySQL 데이터베이스에서 자격 증명을 생성하고 자격 증명을 AWS... | ❌ Lambda 수동 교체(B)는 프로그래밍 노력 증가 |
| ✅ C | 애플리케이션 사용자를 위해 RDS for MySQL 데이터베이스에서 자격 증명을 생성하고 자격 증명을 AWS... | ✅ Secrets Manager with automatic rotation(C)가 최적 솔루션 |
| D | 애플리케이션 사용자를 위해 RDS for MySQL 데이터베이스에서 자격 증명을 생성하고 자격 증명을 AWS... | ❌ Parameter Store(D)는 RDS 자동 교체 미지원 |

---

# Q340
**정답: A**

**문제 분석:**
- ALB 뒤 EC2의 SQL 주입 취약점 해결
- WAF는 ALB와 직접 통합
- SQL 주입 공격 차단 규칙 제공

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| ✅ A | ALB 앞에서 AWS WAF를 사용합니다. 적절한 웹 ACL을 AWS WAF와 연결합니다. | ✅ AWS WAF with web ACL on ALB(A)가 정답 |
| B | 고정 응답으로 SQL 주입에 응답하는 ALB 수신기 규칙을 생성합니다. | ❌ ALB 리스너 규칙(B)은 SQL 주입 탐지 불가 |
| C | 모든 SQL 삽입 시도를 자동으로 차단하려면 AWS Shield Advanced에 가입하십시오. | ❌ Shield Advanced(C)는 DDoS 방어용 |
| D | 모든 SQL 주입 시도를 자동으로 차단하도록 Amazon Inspector를 설정합니다. | ❌ Inspector(D)는 취약점 스캔이지 공격 차단 아님 |

---

# Q341
**정답: D**

**문제 분석:**
- S3 데이터 레이크와 Aurora MySQL 데이터 결합, 열 수준 권한, QuickSight 시각화, 최소 오버헤드
- Lake Formation 청사진으로 Aurora에서 S3 데이터 레이크로 자동 수집
- Lake Formation으로 열 수준 세분화된 권한 제어

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | Amazon EMR을 사용하여 데이터베이스에서 QuickSight SPICE 엔진으로 직접 데이터를 수집하십... | ❌ EMR(A)은 SPICE로 직접 수집 불가 |
| B | AWS Glue Studio 를 사용하여 데이터베이스에서 S3 데이터 레이크로 데이터를 수집합니다. IAM ... | ❌ Glue Studio(B)는 열 수준 권한 제공 안함 |
| C | AWS Glue Elastic Views 를 사용하여 Amazon S3 의 데이터베이스에 대한 구체화된 보기... | ❌ Glue Elastic Views(C)는 S3 버킷 정책으로 열 수준 제어 불가 |
| ✅ D | Lake Formation 청사진을 사용하여 데이터베이스에서 S3 데이터 레이크로 데이터를 수집합니다. La... | ✅ Lake Formation blueprint + column-level security + Athena(D)가 최적 솔루션 |

---

# Q342
**정답: C**

**문제 분석:**
- 매주 배치 작업 30분 전 Auto Scaling 용량 프로비저닝, 최소 오버헤드
- 기계 학습으로 과거 CPU 사용률 패턴 학습
- 자동으로 30분 전에 인스턴스 사전 프로비저닝

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | Auto Scaling 그룹에 대한 동적 조정 정책을 생성합니다. CPU 사용률 메트릭을 기반으로 확장하도록... | ❌ 동적 조정(A)은 이미 60% 도달 후 반응하여 늦음 |
| B | Auto Scaling 그룹에 대한 예약 조정 정책을 생성합니다. 원하는 적정 용량, 최소 용량, 최대 용량... | ❌ 예약 조정(B)은 매번 고정 용량으로 변동하는 트랜잭션 대응 불가 |
| ✅ C | Auto Scaling 그룹에 대한 예측 조정 정책을 생성합니다. 예측을 기반으로 확장하도록 정책을 구성합니... | ✅ Predictive scaling policy(C)가 최적 솔루션 |
| D | Auto Scaling 그룹의 CPU 사용률 지표 값이 60%에 도달하면 AWS Lambda 함수를 호출하는... | ❌ EventBridge + Lambda(D)는 60% 도달 후 반응으로 늦음 |

---

# Q343
**정답: C**

**문제 분석:**
- EC2 MySQL의 다중 리전 DR 아키텍처, 최소 운영 오버헤드
- 완전 관리형으로 운영 오버헤드 최소
- 리전 간 1초 미만 복제

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | MySQL 데이터베이스를 여러 EC2 인스턴스로 마이그레이션합니다. DR 지역에서 대기 EC2 인스턴스를 구... | ❌ EC2 복제(A)는 수동 관리 필요 |
| B | MySQL 데이터베이스를 Amazon RDS 로 마이그레이션합니다. 다중 AZ 배포를 사용합니다. 다른 가용... | ❌ RDS 다중 AZ(B)는 다른 AZ이지 다른 리전 아님 |
| ✅ C | MySQL 데이터베이스를 Amazon Aurora 글로벌 데이터베이스로 마이그레이션합니다. 기본 리전에서 기... | ✅ Aurora Global Database(C)가 최적 솔루션 |
| D | S3 CRR(Cross-Region Replication)용으로 구성된 Amazon S3 버킷에 MySQL ... | ❌ S3 백업(D)는 수동 복원으로 RTO 길고 운영 오버헤드 높음 |

---

# Q344
**정답: A**

**문제 분석:**
- 256KB 초과 메시지를 자동으로 S3에 저장
- SQS에는 S3 포인터만 저장
- 애플리케이션 코드에 라이브러리만 추가하면 됨

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| ✅ A | Java 용 Amazon SQS 확장 클라이언트 라이브러리를 사용하여 Amazon S3 에서 256KB보다 ... | ✅ SQS Extended Client Library for Java(A)가 정답 |
| B | Amazon SQS 대신 Amazon EventBridge 를 사용하여 애플리케이션에서 큰 메시지를 게시합니... | ❌ SQS 메시지 크기 제한(256KB)을 50MB로 확장, 최소 코드 변경 EventBridge(B)도 메시지 크기 제한 있음 |
| C | 256KB보다 큰 메시지를 처리하도록 Amazon SQS의 제한을 변경합니다. | ❌ SQS 제한 변경(C)은 불가능 |
| D | Amazon Elastic File System(Amazon EFS)에 256KB 보다 큰 메시지를 저장합니... | ❌ EFS(D)는 SQS와 통합 안됨 |

---

# Q345
**정답: A**

**문제 분석:**
- 서버리스, 100명 미만 인증, 전역 콘텐츠 전송, 낮은 로그인 지연, 비용 효율
- Cognito는 완전 관리형 인증, 사용자 수에 따라 확장
- Lambda@Edge로 엣지에서 권한 부여 처리 (최저 지연)

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| ✅ A | 인증에 Amazon Cognito 를 사용하십시오. 인증을 위해 Lambda@Edge 를 사용합니다. Ama... | ✅ Cognito + Lambda@Edge + CloudFront(A)가 최적 솔루션 |
| B | 인증을 위해 Microsoft Active Directory용 AWS Directory Service를 사용... | ❌ Lambda(B)는 리전별로 지연 발생 |
| C | 인증에 Amazon Cognito 를 사용합니다. 승인을 위해 AWS Lambda 를 사용합니다. Amazo... | ❌ S3 Transfer Acceleration(C)은 콘텐츠 전송에 부적합 |
| D | 인증을 위해 Microsoft Active Directory용 AWS Directory Service를 사용... | ❌ Directory Service(B, D)는 서버리스 아님 |

---

# Q346
**정답: D**

**문제 분석:**
- 노후 NAS의 SMB/NFS 공유를 S3로 마이그레이션, 수명 주기 정책 사용, 동일한 프로토콜 유지
- SMB 및 NFS 프로토콜 모두 지원
- 로컬 캐시로 자주 액세스하는 데이터 빠른 액세스

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | 볼륨 게이트웨이 | ❌ Volume Gateway(A)는 블록 스토리지(iSCSI)용 |
| B | 테이프 게이트웨이 | ❌ Tape Gateway(B)는 백업용 |
| C | Amazon FSx 파일 게이트웨이 | ❌ FSx File Gateway(C)는 FSx for Windows File Server 캐싱용 |
| ✅ D | Amazon S3 파일 게이트웨이 | ✅ Amazon S3 File Gateway(D)가 정답 |

---

# Q347
**정답: A**

**문제 분석:**
- 3년 비용 절감, 6개월 내 인스턴스 패밀리/크기 변경 가능성
- 인스턴스 패밀리, 크기, AZ, 리전, OS 변경 가능
- 최대 66% 할인

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| ✅ A | 컴퓨팅 절감 플랜(Compute Savings Plan) | ✅ Compute Savings Plan(A)이 최적 솔루션 |
| B | EC2 인스턴스 절감 계획(EC2 Instance Savings Plan) | ❌ EC2 Instance Savings Plan(B)은 패밀리 변경 불가 |
| C | 영역 예약 인스턴스(Zonal Reserved Instances) | ❌ Compute Savings Plan(A)이 최적 솔루션 |
| D | 표준 예약 인스턴스(Standard Reserved Instances) | ❌ Reserved Instances(C, D)는 유연성 낮음 |

---

# Q348
**정답: A**

**문제 분석:**
- DynamoDB 일정하고 예측 가능한 워크로드, 예산 유지
- 예측 가능한 워크로드에 가장 비용 효율적
- 예약 용량으로 추가 할인 (최대 77%)

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| ✅ A | 프로비저닝 모드와 DynamoDB Standard-Infrequent Access(DynamoDB Stand... | ✅ Provisioned mode with reserved capacity(A)가 최적 솔루션 |
| B | 프로비저닝 모드를 사용합니다. RCU(읽기 용량 단위) 및 WCU(쓰기 용량 단위)를 지정합니다. | ❌ Provisioned mode only(B)는 예약 용량 없어 비용 증가 |
| C | 주문형 모드를 사용합니다. 읽기 용량 단위(RCU) 및 쓰기 용량 단위(WCU)를 워크로드의 변경 사항을 수... | ❌ On-demand mode(C, D)는 예측 가능한 워크로드에 비효율적 |
| D | 주문형 모드를 사용합니다. 예약 용량이 있는 RCU(읽기 용량 단위) 및 WCU(쓰기 용량 단위)를 지정합니... | ❌ On-demand mode(C, D)는 예측 가능한 워크로드에 비효율적 |

---

# Q349
**정답: B**

**문제 분석:**
- KMS 고객 관리형 키로 암호화된 Aurora 스냅샷을 다른 계정과 공유
- 인수 회사 계정을 KMS 키 정책에 추가하여 복호화 권한 부여
- 암호화된 스냅샷을 직접 공유

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | 데이터베이스 스냅샷을 생성합니다. 스냅샷을 암호화되지 않은 새 스냅샷에 복사합니다. 인수 회사의 AWS 계정... | ❌ 암호화 해제(A)는 보안 요구사항 위반 |
| ✅ B | 데이터베이스 스냅샷을 생성합니다. 인수 회사의 AWS 계정을 KMS 키 정책에 추가합니다. 인수 회사의 AW... | ✅ Add account to KMS key policy and share snapshot(B)이 정답 |
| C | 다른 AWS 관리형 KMS 키를 사용하는 데이터베이스 스냅샷을 생성합니다. 인수 회사의 AWS 계정을 KMS... | ❌ AWS 관리형 키(C)는 계정 간 공유 불가 |
| D | 데이터베이스 스냅샷을 생성합니다. 데이터베이스 스냅샷을 다운로드합니다. Amazon S3 버킷에 데이터베이스... | ❌ 스냅샷 다운로드/업로드(D)는 불가능 |

---

# Q350
**정답: A, C**

**문제 분석:**
- 단일 AZ RDS의 고가용성 및 자동 복구, 프로덕션 영향 없이 보고 쿼리 실행
- 두 기능 모두 필요

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| ✅ A | 단일 AZ DB 인스턴스에서 다중 AZ 배포로 DB 인스턴스를 수정합니다. | ✅ Multi-AZ deployment(A): 자동 장애 조치로 고가용성 제공 |
| B | 현재 DB 인스턴스의 스냅샷을 찍습니다. 다른 가용 영역의 새 RDS 배포로 스냅샷을 복원합니다. | ❌ 다른 AZ 스냅샷 복원(B)은 자동 복구 제공 안함 |
| ✅ C | 다른 가용 영역에서 DB 인스턴스의 읽기 전용 복제본을 생성합니다. 보고서에 대한 모든 요청은 읽기 전용 복... | ✅ Read replica(C): 읽기 전용 복제본에서 보고 쿼리 실행하여 프로덕션 부하 분리 |
| D | 데이터베이스를 RDS Custom으로 마이그레이션합니다. | ❌ RDS Custom(D)은 관련 없음 |
| E | RDS Proxy를 사용하여 보고 요청을 유지 관리 기간으로 제한합니다. | ❌ RDS Proxy(E)는 연결 관리용 |

---

# Q351
**정답: D**

**문제 분석:**
- 이벤트 기반 데이터 관리 앱, 분산 서버리스 워크플로, 수동 승인 포함, 최소 오버헤드
- 상태 머신으로 복잡한 워크플로 오케스트레이션
- Lambda 함수 호출로 서버리스 구현

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | AWS Glue 에서 워크플로를 구축합니다. AWS Glue 를 사용하여 AWS Lambda 함수를 호출하여... | ❌ Glue(A)는 ETL 전용 |
| B | AWS Step Functions 에서 워크플로를 구축합니다. Amazon EC2 인스턴스에 애플리케이션을 ... | ❌ Step Functions + EC2(B)는 서버리스 아님 |
| C | Amazon EventBridge에서 워크플로를 구축합니다. EventBridge를 사용하여 일정에 따라 A... | ❌ EventBridge(C)는 단순 이벤트 라우팅으로 복잡한 워크플로 부적합 |
| ✅ D | AWS Step Functions 에서 워크플로를 구축합니다. Step Functions 를 사용하여 상태 ... | ✅ AWS Step Functions with Lambda(D)가 최적 솔루션 |

---

# Q352
**정답: B**

**문제 분석:**
- UDP 멀티플레이어 게임, 8개 리전, 최소 지연 및 패킷 손실
- UDP 프로토콜 네이티브 지원
- AWS 글로벌 네트워크로 최적 경로 라우팅

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | 각 리전에서 전송 게이트웨이를 설정합니다. 각 전송 게이트웨이 간에 리전 간 피어링 연결을 생성합니다. | ❌ Transit Gateway(A)는 VPC 연결용 |
| ✅ B | 각 리전에서 UDP 리스너 및 엔드포인트 그룹으로 AWS Global Accelerator 를 설정합니다. | ✅ AWS Global Accelerator with UDP listener(B)가 최적 솔루션 |
| C | UDP 를 켠 상태에서 Amazon CloudFront 를 설정합니다. 각 리전에서 오리진을 구성합니다. | ❌ CloudFront(C)는 UDP 미지원 |
| D | 각 지역 간에 VPC 피어링 메시를 설정합니다. 각 VPC에 대해 UDP를 켭니다. | ❌ VPC 피어링(D)는 지연 최적화 안됨 |

---

# Q353
**정답: B**

**문제 분석:**
- 1TB io2 EBS의 1000 IOPS를 2000 IOPS로 확장, 완전 관리형, 비용 절감, 중단 최소화
- gp3는 3000 IOPS 기본 제공 (요구사항의 2배)
- io2보다 최대 20% 저렴

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | io2 Block Express EBS 볼륨이 있는 MySQL DB 인스턴스용 Amazon RDS 의 다중 ... | ❌ io2 Block Express(A)는 과도하게 비쌈 |
| ✅ B | 범용 SSD(gp2) EBS 볼륨이 있는 MySQL DB 인스턴스용 Amazon RDS 의 다중 AZ 배포를... | ✅ RDS Multi-AZ with gp3(B)가 최적 솔루션 |
| C | Amazon S3 Intelligent-Tiering 액세스 계층을 사용합니다. | ❌ S3(C)는 관계형 데이터베이스 대체 불가 |
| D | 두 개의 큰 EC2 인스턴스를 사용하여 활성-수동 모드에서 데이터베이스를 호스팅합니다. | ❌ EC2 활성-수동(D)은 관리형 아님 |

---

# Q354
**정답: B**

**문제 분석:**
- API Gateway + Lambda + RDS PostgreSQL의 트래픽 급증 시 DB 연결 시간 초과, 최소 코드 변경
- DB 연결 풀링으로 연결 수 효율적 관리
- Lambda의 동시 실행 증가 시에도 안정적 연결

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | Lambda 동시성 비율을 줄입니다. | ❌ Lambda 동시성 감소(A)는 처리량 감소 |
| ✅ B | RDS DB 인스턴스에서 RDS 프록시를 활성화합니다. | ✅ RDS Proxy(B)가 최적 솔루션 |
| C | 더 많은 연결을 허용하도록 RDS DB 인스턴스 클래스의 크기를 조정합니다. | ❌ DB 크기 증가(C)는 비용 증가 및 근본 해결 안됨 |
| D | 온디맨드 확장을 통해 데이터베이스를 Amazon DynamoDB로 마이그레이션합니다. | ❌ DynamoDB(D)는 대규모 마이그레이션 필요 |

---

# Q356
**정답: B**

**문제 분석:**
- S3 Standard의 75% 데이터가 30일 후 거의 액세스 안됨, 즉시 액세스 필요, 고가용성 유지
- Standard-IA는 즉시 액세스 가능 (검색 지연 없음)
- Standard와 동일한 고가용성 및 내구성 (99.9% 가용성)

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | 30일 후에 데이터 객체를 S3 Glacier Deep Archive로 이동합니다. | ❌ Glacier Deep Archive(A)는 검색에 12시간 소요 |
| ✅ B | 30 일 후에 데이터 객체를 S3 Standard-Infrequent Access(S3 Standard-IA... | ✅ S3 Standard-IA after 30 days(B)가 최적 솔루션 |
| C | 30 일 후에 데이터 객체를 S3 One Zone-Infrequent Access(S3 One Zone-IA... | ❌ One Zone-IA(C, D)는 단일 AZ로 고가용성 불일치 |
| D | 데이터 객체를 S3 One Zone-Infrequent Access(S3 One Zone-IA)로 즉시 이동... | ❌ One Zone-IA(C, D)는 단일 AZ로 고가용성 불일치 |

---

# Q357
**정답: A, D**

**문제 분석:**
- EC2 Windows 애플리케이션, ALB, 고가용성 스토리지, 정적 파일과 동적 서버 측 코드
- FSx는 Windows 네이티브 파일 시스템으로 SMB 프로토콜 지원

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| ✅ A | Amazon S3에 정적 파일을 저장합니다. Amazon CloudFront를 사용하여 엣지에서 객체를 캐싱... | ✅ S3 + CloudFront for static files(A): 정적 파일을 S3에 저장하고 CloudFront로 엣지 캐싱 |
| B | 정적 파일을 Amazon S3 에 저장합니다. Amazon ElastiCache 를 사용하여 엣지에서 객체를... | ❌ EC2 Windows 애플리케이션, ALB, 고가용성 스토리지, 정적 파일과 동적 서버 측 코드 |
| C | Amazon Elastic File System(Amazon EFS)에 서버 측 코드를 저장합니다. 파일을 ... | ❌ EFS(C)는 Linux용으로 Windows EC2에 부적합 |
| ✅ D | Windows File Server 용 Amazon FSx 에 서버 측 코드를 저장합니다. 파일을 공유할 각... | ✅ FSx for Windows File Server for server-side code(D): 동적 코드를 FSx에 저장하고 모든 EC2 인스턴스에 마운트하여 공유 |
| E | 범용 SSD(gp2) Amazon Elastic Block Store(Amazon EBS) 볼륨에 서버 측 ... | ❌ EBS(E)는 단일 인스턴스에만 연결 가능 |

---

# Q358
**정답: C**

**문제 분석:**
- 10억+ S3 이미지, 초당 수천 이미지 처리, 동적 크기 조정 및 형식 변환, 최소 운영 오버헤드
- CloudFront 엣지에서 이미지 처리로 지연 최소화
- User-Agent 헤더 기반 적절한 형식 자동 선택

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | EC2 인스턴스에 외부 이미지 관리 라이브러리를 설치합니다. 이미지 관리 라이브러리를 사용하여 이미지를 처리... | ❌ EC2 라이브러리(A)는 확장성 제한 |
| B | CloudFront 오리진 요청 정책을 생성합니다. 정책을 사용하여 자동으로 이미지 크기를 조정하고 요청의 ... | ❌ Origin request policy(B)는 이미지 처리 불가 |
| ✅ C | 외부 이미지 관리 라이브러리와 함께 Lambda@Edge 함수를 사용합니다. Lambda@Edge 함수를 이... | ✅ Lambda@Edge with image library(C)가 최적 솔루션 |
| D | CloudFront 응답 헤더 정책을 생성합니다. 정책을 사용하여 자동으로 이미지 크기를 조정하고 요청의 U... | ❌ Response header policy(D)는 이미지 처리 불가 |

---

# Q359
**정답: C**

**문제 분석:**
- S3 PHI 데이터의 전송 및 저장 중 암호화, 규정 준수 팀이 암호화 키 관리
- SecureTransport 조건으로 HTTPS(TLS) 연결만 허용 (전송 중 암호화)
- SSE-KMS로 미사용 데이터 암호화

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | AWS Certificate Manager(ACM)에서 퍼블릭 SSL/TLS 인증서를 생성합니다. 인증서를 ... | ❌ ACM 인증서(A)는 버킷 암호화 제공 안함 |
| B | S3 버킷 정책에서 aws:SecureTransport 조건을 사용하여 HTTPS(TLS)를 통한 암호화된 ... | ❌ SSE-S3(B)는 AWS 관리 키로 규정 준수 팀 관리 불가 |
| ✅ C | S3 버킷 정책에서 aws:SecureTransport 조건을 사용하여 HTTPS(TLS)를 통한 암호화된 ... | ✅ aws:SecureTransport condition + SSE-KMS(C)가 정답 |
| D | S3 버킷 정책에서 aws:SecureTransport 조건을 사용하여 HTTPS(TLS)를 통한 암호화된 ... | ❌ Macie(D)는 암호화 제공 안함 |

---

# Q360
**정답: B**

**문제 분석:**
- 동일 VPC의 두 프라이빗 API Gateway가 인터넷 대신 VPC를 통해 통신, 최소 코드 변경
- API Gateway용 인터페이스 엔드포인트 생성
- 프라이빗 API가 VPC 내에서 ENI를 통해 통신

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | 인증을 위해 HTTP 헤더에 X-API-Key 헤더를 추가합니다. | ❌ X-API-Key(A)는 인증용이지 경로 변경 아님 |
| ✅ B | 인터페이스 엔드포인트를 사용합니다. | ✅ Interface VPC endpoint(B)가 정답 |
| C | 게이트웨이 엔드포인트를 사용합니다. | ❌ Gateway endpoint(C)는 S3/DynamoDB만 지원 |
| D | 두 REST API 사이에 Amazon Simple Queue Service(Amazon SQS) 대기열을 ... | ❌ SQS(D)는 동기 API 호출을 비동기로 변경하여 요구사항 불일치 |

---

# Q361
**정답: C**

**문제 분석:**
- Sub-millisecond latency reads, one-time queries on historical data, least overhead
- DynamoDB: 한 자릿수 밀리초 읽기 성능
- DAX: 마이크로초 수준 읽기 캐싱

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | Use Amazon RDS for data that is frequently accessed. Run a p... | ❌ RDS(A)는 sub-millisecond 성능 불가 |
| B | Store the data directly in an Amazon S3 bucket. Implement an... | ❌ S3 직접 저장(B)는 빠른 읽기 불가 |
| ✅ C | Use Amazon DynamoDB with DynamoDB Accelerator (DAX) for data... | ✅ DynamoDB with DAX + export to S3 + Athena(C)가 최적 솔루션 |
| D | Use Amazon DynamoDB for data that is frequently accessed. Tu... | ❌ Kinesis(D)는 복잡하고 실시간 스트리밍 불필요 |

---

# Q362
**정답: B, E**

**문제 분석:**
- 결제 ID별 메시지 순서 보장, 잘못된 처리 방지
- 두 솔루션 모두 결제 ID별 순서 보장

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | 결제 ID를 파티션 키로 사용하여 Amazon DynamoDB 테이블에 메시지를 씁니다. | ❌ DynamoDB(A)는 메시징 서비스 아님 |
| ✅ B | 결제 ID를 파티션 키로 사용하여 Amazon Kinesis 데이터 스트림에 메시지를 씁니다. | ✅ Kinesis Data Streams with payment ID as partition key(B): 동일한 파티션 키는 동일한 샤드로 전송되어 순서 보장 |
| C | 결제 ID 를 키로 사용하여 Amazon ElastiCache for Memcached 클러스터에 메시지를 ... | ❌ ElastiCache(C)는 메시지 큐 아님 |
| D | Amazon Simple Queue Service(Amazon SQS) 대기열에 메시지를 씁니다. 결제 ID... | ❌ 표준 SQS(D)는 순서 보장 안됨 |
| ✅ E | Amazon Simple Queue Service(Amazon SQS) FIFO 대기열에 메시지를 씁니다. ... | ✅ SQS FIFO with message group as payment ID(E): FIFO 큐는 메시지 그룹별 순서 보장 |

---

# Q363
**정답: B**

**문제 분석:**
- 게임 이벤트를 여러 서비스에 동시 전송, 이벤트 순서 보장
- FIFO로 이벤트 순서 엄격히 보장
- 여러 구독자(리더보드, 매치메이킹, 인증)에 동시 전송

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | Amazon EventBridge 이벤트 버스 | ❌ EventBridge(A)는 순서 보장 안됨 |
| ✅ B | Amazon Simple Notification Service(Amazon SNS) FIFO 주제 | ✅ SNS FIFO topic(B)가 최적 솔루션 |
| C | Amazon Simple Notification Service(Amazon SNS) 표준 주제 | ❌ SNS 표준 주제(C)도 순서 보장 안됨 |
| D | Amazon Simple Queue Service(Amazon SQS) FIFO 대기열 | ❌ SQS FIFO(D)는 단일 소비자용 |

---

# Q364
**정답: B, D**

**문제 분석:**
- SQS/SNS 저장 및 전송 중 암호화, 승인된 직원만 액세스
- 두 서비스 모두 암호화 및 액세스 제어 필요

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | SQS 구성 요소에서 서버 측 암호화를 켭니다. 기본 키 정책을 업데이트하여 인증된 보안 주체 집합으로 키 ... | ❌ 기본 키(A, C)는 고객이 관리 불가 |
| ✅ B | AWS Key Management Service(AWS KMS) 고객 관리 키를 사용하여 SNS 구성 요소에... | ✅ SNS with KMS CMK + key policy(B): 고객 관리형 키로 SNS 암호화, 키 정책으로 액세스 제한 |
| C | SNS 구성 요소에서 암호화를 켭니다. 기본 키 정책을 업데이트하여 인증된 보안 주체 집합으로 키 사용을 제... | ❌ 기본 키(A, C)는 고객이 관리 불가 |
| ✅ D | AWS Key Management Service(AWS KMS) 고객 관리 키를 사용하여 SQS 구성 요소에... | ✅ SQS with KMS CMK + queue policy with SecureTransport(D): 고객 관리형 키로 SQS 암호화, SecureTransport 조건으로 TLS... |
| E | AWS Key Management Service(AWS KMS) 고객 관리 키를 사용하여 SQS 구성 요소에... | ❌ IAM 정책(E)은 키 정책 대신 사용 불가 |

---

# Q365
**정답: C**

**문제 분석:**
- 지난 30일 중 5분 전 상태로 DB 복원 가능
- 자동 백업은 1-35일 보관 (30일 설정)
- 5분 간격 트랜잭션 로그로 PITR(Point-In-Time Recovery) 가능

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | 읽기 복제본 | ❌ 읽기 복제본(A)은 복원 기능 없음 |
| B | 수동 스냅샷 | ❌ 수동 스냅샷(B)은 수동 생성 필요 |
| ✅ C | 자동 백업 | ✅ Automated backups(C)가 정답 |
| D | 다중 AZ 배포 | ❌ Multi-AZ(D)는 고가용성용이지 복원 기능 아님 |

---

# Q366
**정답: D**

**문제 분석:**
- Cognito 사용자의 프리미엄 콘텐츠 구독 기반 액세스 제어, 최소 운영 오버헤드
- API Gateway usage plan으로 구독자에게 API 키 발급
- API 키로 프리미엄 콘텐츠 엔드포인트 액세스 제어

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | API Gateway API에서 API 캐싱 및 제한을 활성화합니다. | ❌ API 캐싱/제한(A)은 액세스 제어 아님 |
| B | API Gateway API 에서 AWS WAF 를 설정합니다. 구독이 있는 사용자를 필터링하는 규칙을 만듭... | ❌ WAF(B)는 IP 기반 필터링으로 구독 확인 불가 |
| C | DynamoDB 테이블의 프리미엄 콘텐츠에 세분화된 IAM 권한을 적용합니다. | ❌ IAM 권한(C)은 DynamoDB 테이블 수준으로 세분화 어려움 |
| ✅ D | 구독하지 않은 사용자의 액세스를 제한하기 위해 API 사용 계획 및 API 키를 구현하십시오. | ✅ API usage plans and API keys(D)가 최적 솔루션 |

---

# Q367
**정답: A**

**문제 분석:**
- 온프레미스 UDP 애플리케이션, 전 세계 사용자, Route 53 지연 시간 기반 라우팅, 성능 및 가용성 개선
- NLB는 UDP 프로토콜 지원
- 온프레미스 엔드포인트를 NLB 대상으로 등록

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| ✅ A | 3 개의 AWS 리전에서 3 개의 NLB(Network Load Balancer)를 구성하여 온프레미스 엔드... | ✅ 3 NLB + AWS Global Accelerator(A)가 최적 솔루션 |
| B | 3 개의 AWS 리전에서 3 개의 Application Load Balancer(ALB)를 구성하여 온프레미... | ❌ 3 NLB + AWS Global Accelerator(A)가 최적 솔루션 |
| C | 3 개의 AWS 리전에서 3 개의 NLB(Network Load Balancer)를 구성하여 온프레미스 엔드... | ❌ CloudFront(C, D)도 UDP 미지원 |
| D | 온프레미스 엔드포인트를 처리하기 위해 3 개의 AWS 리전에서 3 개의 ALB(Application Load... | ❌ ALB(B, D)는 UDP 미지원 CloudFront(C, D)도 UDP 미지원 |

---

# Q368
**정답: A**

**문제 분석:**
- 모든 신규 IAM 사용자의 암호 복잡성 및 교체 기간 설정
- AWS 계정의 암호 정책은 모든 IAM 사용자에게 적용
- 복잡성 요구사항 및 교체 기간 설정

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| ✅ A | 전체 AWS 계정에 대한 전반적인 암호 정책을 설정합니다. | ✅ Set account-wide password policy(A)가 정답 |
| B | AWS 계정의 각 IAM 사용자에 대한 암호 정책을 설정합니다. | ❌ 개별 사용자 정책(B)은 비효율적 |
| C | 타사 공급업체 소프트웨어를 사용하여 암호 요구 사항을 설정합니다. | ❌ 타사 소프트웨어(C)는 불필요 |
| D | Amazon CloudWatch 규칙을 Create_newuser 이벤트에 연결하여 적절한 요구 사항으로 암... | ❌ CloudWatch 규칙(D)은 암호 정책 설정 불가 |

---

# Q369
**정답: A**

**문제 분석:**
- EC2의 여러 1시간 작업, 다양한 언어, 스케줄 실행, 최소 운영 오버헤드
- Batch는 다양한 런타임 지원 (컨테이너 기반)
- 자동 스케일링으로 성능 및 확장성 문제 해결

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| ✅ A | AWS Batch 를 사용하여 작업을 작업으로 실행합니다. Amazon EventBridge(Amazon C... | ✅ AWS Batch + EventBridge(A)가 최적 솔루션 |
| B | EC2 인스턴스를 컨테이너로 변환합니다. AWS App Runner를 사용하여 작업을 작업으로 실행할 온디맨... | ❌ App Runner(B)는 지속 실행 서비스용 |
| C | 작업을 AWS Lambda 함수에 복사합니다. Amazon EventBridge(Amazon CloudWat... | ❌ Lambda(C)는 15분 제한으로 1시간 작업 불가 |
| D | 작업을 실행하는 EC2 인스턴스의 Amazon 머신 이미지(AMI)를 생성합니다. AMI로 Auto Scal... | ❌ AMI + Auto Scaling(D)는 스케줄링 및 작업 관리 복잡 |

---

# Q370
**정답: C**

**문제 분석:**
- 프라이빗 서브넷 EC2의 인터넷 아웃바운드 액세스, 최소 유지 보수
- NAT Gateway는 완전 관리형으로 유지 보수 불필요
- 자동 스케일링 및 고가용성

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | 퍼블릭 서브넷에서 NAT 인스턴스를 프로비저닝합니다. NAT 인스턴스를 가리키는 기본 경로로 각 프라이빗 서... | ❌ NAT Gateway in public subnet(C)가 정답 |
| B | 프라이빗 서브넷에서 NAT 인스턴스를 프로비저닝합니다. NAT 인스턴스를 가리키는 기본 경로로 각 프라이빗 ... | ❌ NAT 인스턴스(A, B)는 수동 관리 필요 |
| ✅ C | 퍼블릭 서브넷에서 NAT 게이트웨이를 프로비저닝합니다. NAT 게이트웨이를 가리키는 기본 경로로 각 프라이빗... | ✅ NAT Gateway in public subnet(C)가 정답 |
| D | 프라이빗 서브넷에서 NAT 게이트웨이를 프로비저닝합니다. NAT 게이트웨이를 가리키는 기본 경로로 각 프라이... | ❌ 프라이빗 서브넷의 NAT Gateway(D)는 작동 불가 |

---

# Q371
**정답: C, D**

**문제 분석:**
- EKS 클러스터의 EBS 볼륨 암호화, 고객 관리형 KMS 키 사용, 최소 운영 오버헤드
- 자동화로 운영 오버헤드 최소

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | 고객 관리 키를 사용하는 Kubernetes 플러그인을 사용하여 데이터 암호화를 수행합니다. | ❌ Kubernetes 플러그인(A)은 복잡함 |
| B | EKS 클러스터 생성 후 EBS 볼륨을 찾습니다. 고객 관리형 키를 사용하여 암호화를 활성화합니다. | ❌ 생성 후 암호화(B)는 수동 작업 |
| ✅ C | EKS 클러스터가 생성될 AWS 리전에서 기본적으로 EBS 암호화를 활성화합니다. 고객 관리형 키를 기본 키... | ✅ Enable EBS encryption by default in region(C): 리전의 기본 EBS 암호화 활성화로 모든 신규 볼륨 자동 암호화 |
| ✅ D | EKS 클러스터를 생성합니다. 고객 관리형 키에 대한 권한을 부여하는 정책이 있는 IAM 역할을 생성합니다.... | ✅ Create IAM role with KMS permissions for EKS(D): EKS 클러스터가 KMS 키 사용 권한을 가진 IAM 역할 필요 |
| E | 고객 관리형 키를 EKS 클러스터에 Kubernetes 비밀로 저장합니다. 고객 관리형 키를 사용하여 EBS... | ❌ Kubernetes secret(E)는 부적절 |

---

# Q372
**정답: B**

**문제 분석:**
- 수백만 GIS 이미지(지리코드 키), 자연재해 시 급증 업데이트, 고가용성 및 확장성
- S3는 무제한 확장, 99.999999999% 내구성
- DynamoDB는 자동 스케일링으로 급증 처리

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | 이미지와 지리적 코드를 데이터베이스 테이블에 저장합니다. Amazon RDS 다중 AZ DB 인스턴스에서 실... | ❌ RDS(A, D)는 수백만 대용량 이미지 저장에 부적합하고 비용 증가 |
| ✅ B | Amazon S3 버킷에 이미지를 저장합니다. 지리적 코드를 키로, 이미지 S3 URL을 값으로 사용하여 A... | ✅ S3 for images + DynamoDB with geocode as key(B)가 최적 솔루션 |
| C | Amazon DynamoDB 테이블에 이미지와 지리적 코드를 저장합니다. 부하가 높은 시간 동안 Dynamo... | ❌ DynamoDB에 이미지 저장(C)은 400KB 항목 제한으로 불가능 |
| D | Amazon S3 버킷에 이미지를 저장합니다. 지리 코드와 이미지 S3 URL 을 데이터베이스 테이블에 저장... | ❌ RDS(A, D)는 수백만 대용량 이미지 저장에 부적합하고 비용 증가 |

---

# Q373
**정답: A**

**문제 분석:**
- IoT 센서 S3 데이터, 수조 객체, 일일 30일 데이터 ML, 연 4회 12개월 분석, 1년 즉시 액세스, 이후 아카이빙
- Intelligent-Tiering은 자동으로 액세스 패턴에 따라 계층 이동
- 30일 빈번 액세스와 90일 비활성 데이터 모두 최적화

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| ✅ A | S3 Intelligent-Tiering 스토리지 클래스를 사용합니다. 1 년 후 객체를 S3 Glacier... | ✅ S3 Intelligent-Tiering + lifecycle to Glacier Deep Archive(A)가 최적 솔루션 |
| B | S3 Intelligent-Tiering 스토리지 클래스를 사용합니다. 1년 후 자동으로 객체를 S3 Gla... | ❌ Intelligent-Tiering 자체 이동(B)은 기능 없음 |
| C | S3 Standard-Infrequent Access(S3 Standard-IA) 스토리지 클래스를 사용합니... | ❌ Standard-IA(C)는 자동 최적화 없음 |
| D | S3 Standard 스토리지 클래스를 사용합니다. 30일 후에 객체를 S3 Standard-Infreque... | ❌ 30일 후 Standard-IA(D)는 비효율적 |

---

# Q374
**정답: D**

**문제 분석:**
- 3개 VPC 간 통신, 온프레미스와 대역폭 집약적 연결, 비용 효율성 극대화
- Transit Gateway로 3개 VPC 중앙 허브 연결
- 단일 Direct Connect 연결로 비용 최소화

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | 데이터 센터에서 AWS 로 3 개의 AWS Site-to-Site VPN 연결을 구성합니다. 각 VPC 에 ... | ❌ 3개 Site-to-Site VPN(A)은 대역폭 제한 |
| B | 각 VPC 에서 타사 가상 네트워크 어플라이언스를 시작합니다. 데이터 센터와 각 가상 어플라이언스 간에 IP... | ❌ 타사 어플라이언스(B)는 관리 복잡 |
| C | 데이터 센터에서 us-east-1 의 Direct Connect 게이트웨이로 3 개의 AWS Direct C... | ❌ 3개 Direct Connect(C)는 비용 증가 |
| ✅ D | 데이터 센터에서 AWS 로 하나의 AWS Direct Connect 연결을 설정합니다. 전송 게이트웨이를 생... | ✅ 1 Direct Connect + Transit Gateway(D)가 최적 솔루션 |

---

# Q375
**정답: A**

**문제 분석:**
- 분산 주문 처리 앱, 여러 Lambda 함수 결합, 수동 승인 포함, EC2/컨테이너/온프레미스 오케스트레이션, 최소 오버헤드
- 복잡한 워크플로 오케스트레이션
- Lambda, EC2, 컨테이너, 온프레미스 모두 통합

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| ✅ A | AWS Step Functions를 사용하여 애플리케이션을 구축하십시오. | ✅ AWS Step Functions(A)가 최적 솔루션 |
| B | AWS Glue 작업에서 모든 애플리케이션 구성 요소를 통합합니다. | ❌ Glue(B)는 ETL 전용 |
| C | Amazon Simple Queue Service(Amazon SQS)를 사용하여 애플리케이션을 구축합니다. | ❌ SQS(C)는 복잡한 워크플로 오케스트레이션 불가 |
| D | AWS Lambda 함수와 Amazon EventBridge 이벤트를 사용하여 애플리케이션을 구축합니다. | ❌ Lambda + EventBridge(D)는 수동 승인 복잡 |

---

# Q376
**정답: A**

**문제 분석:**
- 서버리스 앱의 RDS MySQL 연결 거부, 트래픽 변동, 최소 오버헤드
- 연결 풀링으로 DB 연결 효율적 관리
- 서버리스 워크로드의 급격한 연결 증가 처리

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| ✅ A | RDS Proxy 에서 프록시를 생성합니다. RDS Proxy 를 통해 DB 인스턴스를 사용하도록 사용자 애... | ✅ RDS Proxy(A)가 최적 솔루션 |
| B | 사용자 애플리케이션과 DB 인스턴스 간에 Amazon ElastiCache for Memcached 를 배포... | ❌ ElastiCache(B)는 연결 문제 해결 안됨 |
| C | I/O 용량이 더 큰 다른 인스턴스 클래스로 DB 인스턴스를 마이그레이션합니다. 새 DB 인스턴스를 사용하도... | ❌ 인스턴스 크기 증가(C)는 비용 증가 |
| D | DB 인스턴스에 대한 다중 AZ 를 구성합니다. DB 인스턴스 간에 전환하도록 사용자 애플리케이션을 구성합니... | ❌ Multi-AZ(D)는 연결 관리 개선 안됨 |

---

# Q377
**정답: B**

**문제 분석:**
- Auto Scaling 그룹 EC2의 시작/종료 시 감사 시스템에 즉시 보고, 효율적 솔루션
- 인스턴스 시작/종료 시 자동으로 커스텀 스크립트 실행
- 즉시 감사 시스템에 데이터 전송

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | 예약된 AWS Lambda 함수를 사용하고 모든 EC2 인스턴스에서 원격으로 스크립트를 실행하여 데이터를 감... | ❌ Lambda 스케줄(A)은 즉시 보고 불가 |
| ✅ B | EC2 Auto Scaling 수명 주기 후크를 사용하여 인스턴스가 시작되고 종료될 때 감사 시스템에 데이터... | ✅ Auto Scaling lifecycle hooks(B)가 최적 솔루션 |
| C | EC2 Auto Scaling 시작 구성을 사용하여 사용자 데이터를 통해 사용자 지정 스크립트를 실행하여 인... | ❌ 시작 구성 사용자 데이터(C)는 종료 시 실행 안됨 |
| D | 인스턴스 운영 체제에서 사용자 지정 스크립트를 실행하여 데이터를 감사 시스템으로 보냅니다. 인스턴스가 시작되... | ❌ 인스턴스 OS 스크립트(D)는 Auto Scaling 통합 안됨 |

---

# Q378
**정답: B**

**문제 분석:**
- UDP 실시간 게임, Auto Scaling, 비관계형 게이머 데이터, 자동 스케일링 DB
- NLB는 UDP 프로토콜 지원
- Auto Scaling 그룹과 통합

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | 트래픽 분산에는 Amazon Route 53 을 사용하고 데이터 저장에는 Amazon Aurora Serve... | ❌ Route 53(A)은 로드 밸런싱 제한적, Aurora는 관계형 DB |
| ✅ B | 트래픽 분산을 위해 Network Load Balancer 를 사용하고 데이터 저장을 위해 주문형 Amazo... | ✅ NLB + DynamoDB on-demand(B)가 최적 솔루션 |
| C | 트래픽 분산을 위해 Network Load Balancer 를 사용하고 데이터 저장을 위해 Amazon Au... | ❌ Aurora Global(C)는 비관계형 데이터에 부적합 |
| D | 트래픽 분산을 위해 Application Load Balancer 를 사용하고 데이터 저장을 위해 Amazo... | ❌ ALB(D)는 UDP 미지원 |

---

# Q379
**정답: B**

**문제 분석:**
- API Gateway + Lambda + RDS, 많은 라이브러리 로드, 응답 지연 감소, 최소 운영 변경
- 프로비저닝된 동시성은 Lambda 함수를 미리 초기화
- 콜드 스타트 제거

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | API 를 우회하여 쿼리 속도를 높이려면 프런트엔드 애플리케이션과 데이터베이스 사이에 연결을 설정합니다. | ❌ DB 직접 연결(A)은 보안 위험 |
| ✅ B | 요청을 처리하는 Lambda 함수에 대해 프로비저닝된 동시성을 구성합니다. | ✅ Provisioned concurrency for Lambda(B)가 최적 솔루션 |
| C | 유사한 데이터 세트를 더 빠르게 검색하기 위해 쿼리 결과를 Amazon S3에 캐시합니다. | ❌ S3 캐싱(C)은 복잡하고 동적 데이터에 부적합 |
| D | Lambda가 한 번에 설정할 수 있는 연결 수를 늘리려면 데이터베이스 크기를 늘립니다. | ❌ DB 크기 증가(D)는 연결 수 증가이지 지연 감소 아님 |

---

# Q380
**정답: D**

**문제 분석:**
- 업무 시간 외 EC2/RDS 자동 시작/중지, 최소 비용 및 인프라 유지
- Lambda로 EC2/RDS 시작/중지 API 호출
- EventBridge로 스케줄링 (cron 표현식)

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | 탄력적 크기 조정을 사용하여 EC2 인스턴스를 확장합니다. 업무 시간 외에는 DB 인스턴스를 0으로 조정합니... | ❌ Elastic 크기 조정(A)은 시작/중지 아님 |
| B | 일정에 따라 EC2 인스턴스와 DB 인스턴스를 자동으로 시작 및 중지하는 파트너 솔루션에 대한 AWS Mar... | ❌ Marketplace 솔루션(B)은 비용 증가 |
| C | 다른 EC2 인스턴스를 시작합니다. 일정에 따라 기존 EC2 인스턴스와 DB 인스턴스를 시작 및 중지하는 셸... | ❌ cron EC2(C)는 추가 인스턴스 비용 |
| ✅ D | EC2 인스턴스와 DB 인스턴스를 시작하고 중지할 AWS Lambda 함수를 생성합니다. 일정에 따라 Lam... | ✅ Lambda + EventBridge scheduled(D)가 최적 솔루션 |

---

# Q381
**정답: B**

**문제 분석:**
- PostgreSQL 메타데이터, 월간 보고 쿼리 몇 시간 소요, 프로덕션 영향 방지, 최소 코드 변경
- Aurora 복제본에서 보고 쿼리 실행하여 프로덕션 분리
- 관계형 쿼리 완벽 지원

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | 읽기 전용 복제본이 포함된 새로운 Amazon DocumentDB(MongoDB 호환) 클러스터를 설정합니다... | ❌ DocumentDB(A)는 MongoDB 호환으로 PostgreSQL과 다름 |
| ✅ B | Aurora 복제본이 포함된 새로운 Amazon Aurora PostgreSQL DB 클러스터를 설정합니다.... | ✅ Aurora PostgreSQL with Aurora Replicas(B)가 최적 솔루션 |
| C | PostgreSQL 다중 AZ DB 인스턴스용 새 Amazon RDS를 설정합니다. 보고 모듈이 기본 노드에... | ❌ RDS Multi-AZ(C)의 보조 노드는 읽기 불가 |
| D | 문서를 저장할 새 Amazon DynamoDB 테이블을 설정합니다. 새 문서 항목을 지원하려면 고정된 쓰기 ... | ❌ DynamoDB(D)는 관계형 쿼리 지원 안됨 |

---

# Q382
**정답: A**

**문제 분석:**
- NLB → EC2 웹 계층 → EC2 앱 계층 → DB, 전송 중 데이터 보안 개선
- NLB TLS 리스너로 클라이언트-NLB 간 암호화
- 서버 인증서 배포로 TLS 종료

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| ✅ A | TLS 수신기를 구성합니다. NLB에 서버 인증서를 배포합니다. | ✅ TLS listener on NLB with server certificate(A)가 정답 |
| B | AWS Shield Advanced를 구성합니다. NLB에서 AWS WAF를 활성화합니다. | ❌ Shield Advanced(B)는 DDoS 방어, 암호화 아님 |
| C | 로드 밸런서를 Application Load Balancer(ALB)로 변경합니다. ALB 에서 AWS WA... | ❌ WAF(C)는 애플리케이션 보호, 전송 암호화 아님 |
| D | AWS Key Management Service(AWS KMS)를 사용하여 EC2 인스턴스에서 Amazon ... | ❌ KMS(D)는 저장 데이터 암호화 |

---

# Q383
**정답: A**

**문제 분석:**
- 소켓/코어 기반 소프트웨어 라이센스, 용량/가동 시간 예측 가능, 기존 라이센스 사용
- Dedicated Host는 물리적 서버로 소켓/코어 라이센스 지원
- Reserved로 1-3년 약정 할인

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| ✅ A | 전용 예약 호스트(Dedicated Reserved Hosts) | ✅ Dedicated Reserved Hosts(A)가 최적 솔루션 |
| B | 전용 온디맨드 호스트(Dedicated On-Demand Hosts) | ❌ On-Demand(B)는 비용 높음 |
| C | 전용 예약 인스턴스(Dedicated Reserved Instances) | ❌ Dedicated Instances(C, D)는 소켓/코어 가시성 없음 |
| D | 전용 온디맨드 인스턴스(Dedicated On-Demand Instances) | ❌ Dedicated Instances(C, D)는 소켓/코어 가시성 없음 |

---

# Q384
**정답: C**

**문제 분석:**
- 다중 AZ EC2 Linux, POSIX 호환, 고가용성, 최대 내구성, 인스턴스 간 공유, 30일 후 액세스 감소
- EFS는 POSIX 호환 파일 시스템
- 다중 AZ 자동 복제로 고가용성 및 최대 내구성

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | Amazon S3 Standard 스토리지 클래스를 사용하십시오. S3 수명 주기 정책을 생성하여 자주 액세... | ❌ 다중 AZ EC2 Linux, POSIX 호환, 고가용성, 최대 내구성, 인스턴스 간 공유, 30일 후 액세스 감소 |
| B | Amazon S3 Standard 스토리지 클래스를 사용합니다. S3 수명 주기 정책을 생성하여 자주 액세스... | ❌ S3(A, B)는 POSIX 호환 아님 |
| ✅ C | Amazon Elastic File System(Amazon EFS) Standard 스토리지 클래스를 사용... | ✅ EFS Standard + lifecycle to EFS Standard-IA(C)가 최적 솔루션 |
| D | Amazon Elastic File System(Amazon EFS) One Zone 스토리지 클래스를 사용... | ❌ EFS One Zone(D)는 단일 AZ로 고가용성 불일치 |

---

# Q385
**정답: C**

**문제 분석:**
- ALB → 웹 서버 → MySQL, HTTPS만 사용, 최소 권한 원칙
- 웹 서버 SG: ALB에서 포트 443 허용 (0.0.0.0/0 아님)
- MySQL SG: 웹 서버 SG에서 포트 3306 허용

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | 웹 서버용 보안 그룹을 생성하고 0.0.0.0/0에서 포트 443을 허용합니다. MySQL 서버용 보안 그룹... | ❌ 0.0.0.0/0(A)는 과도한 권한 |
| B | 웹 서버용 네트워크 ACL 을 생성하고 0.0.0.0/0 에서 포트 443 을 허용합니다. MySQL 서버용... | ❌ ALB → 웹 서버 → MySQL, HTTPS만 사용, 최소 권한 원칙 |
| ✅ C | 웹 서버용 보안 그룹을 만들고 로드 밸런서에서 포트 443을 허용합니다. MySQL 서버용 보안 그룹을 만들... | ✅ Web SG from ALB + MySQL SG from Web SG(C)가 정답 |
| D | 웹 서버에 대한 네트워크 ACL 을 생성하고 로드 밸런서에서 포트 443 을 허용합니다. MySQL 서버용 ... | ❌ 네트워크 ACL(B, D)은 불필요하게 복잡 |

---

# Q386
**정답: B**

**문제 분석:**
- EC2 백엔드가 RDS MySQL에서 동일 데이터 반복 조회로 성능 저하
- 자주 조회하는 데이터를 ElastiCache에 캐싱
- DB 부하 대폭 감소

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | Amazon SNS를 구현하여 데이터베이스 호출을 저장합니다. | ❌ SNS(A)는 캐싱 아님 |
| ✅ B | Amazon ElastiCache를 구현하여 대규모 데이터 세트를 캐싱합니다. | ✅ ElastiCache to cache large datasets(B)가 정답 |
| C | 데이터베이스 호출을 캐시하기 위해 RDS for MySQL 읽기 전용 복제본을 구현합니다. | ❌ 읽기 복제본(C)도 캐싱 아님, 여전히 DB 쿼리 필요 |
| D | Amazon Kinesis Data Firehose를 구현하여 호출을 데이터베이스로 스트리밍합니다. | ❌ Kinesis Firehose(D)는 스트리밍용 |

---

# Q387
**정답: D, E**

**문제 분석:**
- CloudFormation 작업 수행, 최소 권한 원칙
- 서비스 역할로 최소 권한 실현

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | 배포 엔지니어가 AWS CloudFormation 스택 작업을 수행하기 위해 AWS 계정 루트 사용자 자격 ... | ❌ 루트 사용자(A)는 최대 권한 |
| B | 배포 엔지니어를 위한 새 IAM 사용자를 생성하고 PowerUsers IAM 정책이 연결된 그룹에 IAM 사... | ❌ PowerUsers(B)는 과도한 권한 |
| C | 배포 엔지니어를 위한 새 IAM 사용자를 생성하고 AdministratorAccess IAM 정책이 연결된 ... | ❌ AdministratorAccess(C)는 최대 권한 |
| ✅ D | 배포 엔지니어를 위한 새 IAM 사용자를 생성하고 AWS CloudFormation 작업만 허용하는 IAM ... | ✅ Create IAM user with CloudFormation-only policy(D): CloudFormation 스택 작업만 허용하는 IAM 정책 |
| ✅ E | 배포 엔지니어를 위한 IAM 역할을 생성하여 해당 IAM 역할을 사용하여 AWS CloudFormation ... | ✅ Create IAM role for stack with specific permissions(E): CloudFormation이 리소스 생성 시 사용할 IAM 역할, 필요한 권한만... |

---

# Q388
**정답: D**

**문제 분석:**
- 웹 계층 EC2가 프라이빗 서브넷 RDS 연결 불가, 기본 구성 유지
- RDS 보안 그룹에 웹 계층 보안 그룹에서의 트래픽 허용
- 기본 네트워크 ACL은 모든 트래픽 허용

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | 프라이빗 서브넷의 네트워크 ACL 에 명시적 규칙을 추가하여 웹 티어의 EC2 인스턴스에서 오는 트래픽을 허... | ❌ 프라이빗 서브넷 네트워크 ACL(A)은 기본으로 허용 |
| B | 웹 계층의 EC2 인스턴스와 데이터베이스 계층 간의 트래픽을 허용하도록 VPC 경로 테이블에 경로를 추가합니... | ❌ 라우팅 추가(B)는 불필요 (VPC 내 기본 라우팅) |
| C | 웹 계층의 EC2 인스턴스와 데이터베이스 계층의 RDS 인스턴스를 두 개의 개별 VPC 에 배포하고 VPC ... | ❌ VPC 피어링(C)은 불필요 (동일 VPC) |
| ✅ D | 데이터베이스 계층 RDS 인스턴스의 보안 그룹에 인바운드 규칙을 추가하여 웹 계층 보안 그룹의 트래픽을 허용... | ✅ Add inbound rule to RDS SG from web tier SG(D)가 정답 |

---

# Q389
**정답: A**

**문제 분석:**
- 단일 AZ RDS MySQL, 프로덕션 쓰기 영향 없이 비즈니스 보고 쿼리
- 읽기 전용 복제본에서 보고 쿼리 실행
- 프로덕션 DB 부하 분리

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| ✅ A | RDS 읽기 복제본을 배포하여 비즈니스 보고 쿼리를 처리합니다. | ✅ RDS read replica(A)가 정답 |
| B | DB 인스턴스를 Elastic Load Balancer 뒤에 배치하여 수평으로 확장합니다. | ❌ ELB(B)는 DB에 사용 불가 |
| C | DB 인스턴스를 더 큰 인스턴스 유형으로 확장하여 쓰기 작업 및 쿼리를 처리합니다. | ❌ 스케일 업(C)은 쓰기 영향 여전히 존재 |
| D | 비즈니스 보고 쿼리를 처리하기 위해 여러 가용 영역에 DB 인스턴스를 배포합니다. | ❌ 다중 AZ(D)는 고가용성용이지 읽기 부하 분산 아님 |

---

# Q390
**정답: B, D**

**문제 분석:**
- 전자상거래 세션 관리 최적화, 세션 데이터 지속 저장
- 둘 다 세션 저장에 적합하며 지속성 제공

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | ALB에서 고정 세션 기능(세션 선호도)을 켭니다. | ❌ ALB 고정 세션(A)은 인스턴스 종료 시 세션 손실 |
| ✅ B | Amazon DynamoDB 테이블을 사용하여 고객 세션 정보를 저장합니다. | ✅ DynamoDB for session data(B): 완전 관리형, 자동 스케일링, 빠른 액세스 |
| C | Amazon Cognito 사용자 풀을 배포하여 사용자 세션 정보를 관리합니다. | ❌ Cognito(C)는 사용자 인증용이지 세션 데이터 저장 아님 |
| ✅ D | Amazon ElastiCache for Redis 클러스터를 배포하여 고객 세션 정보를 저장합니다. | ✅ ElastiCache for Redis for session data(D): 인메모리 캐시, 마이크로초 수준 지연, 세션 데이터 TTL 지원 |
| E | 애플리케이션에서 AWS Systems Manager Application Manager를 사용하여 사용자 세... | ❌ Systems Manager Application Manager(E)는 세션 관리 기능 없음 |

---

# Q391
**정답: C**

**문제 분석:**
- 상태 비저장 웹 앱, Auto Scaling EC2, PostgreSQL RDS, 2시간 RPO, 확장성 및 리소스 최적화
- 상태 비저장이므로 EC2는 최신 AMI만 유지하면 됨
- 임시 로컬 스토리지 불필요로 EC2 백업 불필요

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | RPO 를 충족하기 위해 2 시간마다 EC2 인스턴스 및 데이터베이스의 Amazon Elastic Block... | ❌ 상태 비저장 웹 앱, Auto Scaling EC2, PostgreSQL RDS, 2시간 RPO, 확장성 및 리소스 최적화 |
| B | Amazon Elastic Block Store(Amazon EBS) 스냅샷을 생성하도록 스냅샷 수명 주기 ... | ❌ EC2 EBS 스냅샷(A, B, D)은 상태 비저장 앱에 불필요 |
| ✅ C | 웹 및 애플리케이션 계층의 최신 Amazon 머신 이미지(AMI)를 유지합니다. Amazon RDS에서 자동... | ✅ Maintain latest AMI + enable RDS automated backups with PITR(C)가 최적 솔루션 |
| D | 2시간마다 EC2 인스턴스의 Amazon Elastic Block Store(Amazon EBS) 볼륨의 스... | ❌ EC2 EBS 스냅샷(A, B, D)은 상태 비저장 앱에 불필요 |

---

# Q392
**정답: A**

**문제 분석:**
- 퍼블릭 웹 앱, 전 세계 동적 IP 고객, EC2 웹 서버, RDS MySQL
- 웹 서버는 인터넷(0.0.0.0/0)에서 HTTPS(443) 허용
- DB는 웹 서버 보안 그룹에서만 MySQL(3306) 허용

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| ✅ A | 0.0.0.0/0 에서 포트 443 의 인바운드 트래픽을 허용하도록 웹 서버에 대한 보안 그룹을 구성합니다.... | ✅ Web SG allow 0.0.0.0/0:443 + DB SG allow web SG:3306(A)이 정답 |
| B | 고객의 IP 주소에서 포트 443 의 인바운드 트래픽을 허용하도록 웹 서버에 대한 보안 그룹을 구성합니다. ... | ❌ Web SG allow 0.0.0.0/0:443 + DB SG allow web SG:3306(A)이 정답 |
| C | 고객의 IP 주소에서 포트 443 의 인바운드 트래픽을 허용하도록 웹 서버에 대한 보안 그룹을 구성합니다. ... | ❌ 고객 IP 제한(B, C)은 동적 IP로 불가능 |
| D | 0.0.0.0/0 에서 포트 443 의 인바운드 트래픽을 허용하도록 웹 서버에 대한 보안 그룹을 구성합니다.... | ❌ DB를 0.0.0.0/0(D)는 보안 위험 |

---

# Q393
**정답: C**

**문제 분석:**
- 음성 통화 S3 오디오 파일에서 텍스트 추출 및 PII 제거
- Transcribe는 오디오를 텍스트로 자동 변환
- PII 수정 기능으로 개인 정보 자동 마스킹

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | Amazon Kinesis Video Streams 를 사용하여 오디오 파일을 처리합니다. AWS Lambd... | ❌ Kinesis Video Streams(A)는 라이브 비디오용 |
| B | 오디오 파일이 S3 버킷에 업로드되면 AWS Lambda 함수를 호출하여 Amazon Textract 작업을... | ❌ Textract(B)는 문서 이미지용, 오디오 미지원 |
| ✅ C | PII 수정을 켠 상태로 Amazon Transcribe 전사 작업을 구성합니다. 오디오 파일이 S3 버킷에... | ✅ Amazon Transcribe with PII redaction(C)가 최적 솔루션 |
| D | 트랜스크립션이 켜진 오디오 파일을 수집하는 Amazon Connect 고객 응대 흐름을 생성합니다. 알려진 ... | ❌ Connect(D)는 과도한 설계 |

---

# Q394
**정답: C**

**문제 분석:**
- RDS MySQL 2TB gp3, 20000 IOPS 초과 시 성능 저하
- gp3는 최대 16000 IOPS (3000 기본 + 추가 프로비저닝)
- 20000 IOPS 요구사항은 gp3 한계 초과

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | 볼륨을 마그네틱 볼륨으로 교체합니다. | ❌ 마그네틱(A)은 성능 저하 |
| B | gp3 볼륨의 IOPS 수를 늘립니다. | ❌ gp3 IOPS 증가(B)는 16000 한계 |
| ✅ C | 프로비저닝된 IOPS SSD(io2) 볼륨으로 볼륨을 교체합니다. | ✅ Replace with provisioned IOPS SSD (io2)(C)가 정답 |
| D | 2,000GB gp3 볼륨을 두 개의 1,000GB gp3 볼륨으로 교체합니다. | ❌ 볼륨 분할(D)는 RDS에서 불가능 |

---

# Q395
**정답: C**

**문제 분석:**
- 보안 그룹 구성 변경한 IAM 사용자 식별
- 모든 API 호출 기록 (누가, 언제, 무엇을)
- 보안 그룹 변경 이벤트 추적

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | Amazon GuardDuty | ❌ GuardDuty(A)는 위협 탐지 |
| B | 아마존 인스펙터 | ❌ Inspector(B)는 취약점 스캔 |
| ✅ C | AWS 클라우드트레일 | ✅ AWS CloudTrail(C)이 정답 |
| D | AWS 구성 | ❌ Config(D)는 구성 변경 추적이지만 사용자 식별은 CloudTrail |

---

# Q396
**정답: A**

**문제 분석:**
- 자체 관리 DNS 서비스(EC2 + Global Accelerator), DDoS 방어
- Shield Advanced는 DDoS 고급 방어
- Global Accelerator는 Shield Advanced 통합

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| ✅ A | AWS Shield Advanced에 가입하십시오. 보호할 리소스로 액셀러레이터를 추가합니다. | ✅ Shield Advanced + accelerator as protected resource(A)가 정답 |
| B | AWS Shield Advanced에 가입합니다. 보호할 리소스로 EC2 인스턴스를 추가합니다. | ❌ 오답 |
| C | 속도 기반 규칙을 포함하는 AWS WAF 웹 ACL 을 생성합니다. 웹 ACL 을 가속기와 연결합니다. | ❌ 자체 관리 DNS 서비스(EC2 + Global Accelerator), DDoS 방어 |
| D | 비율 기반 규칙을 포함하는 AWS WAF 웹 ACL 을 생성합니다. 웹 ACL 을 EC2 인스턴스와 연결합니... | ❌ WAF(C, D)는 레이어 7만 방어, DNS는 레이어 3/4 DDoS 위협 |

---

# Q397
**정답: C**

**문제 분석:**
- 일일 예약 작업, S3 대용량 객체 처리, 최대 1시간, 일정한 CPU/메모리, 최소 운영 노력
- Fargate는 서버리스 컨테이너로 인프라 관리 불필요
- CPU/메모리 사전 정의 가능

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | Amazon EventBridge 알림이 있는 AWS Lambda 함수를 생성합니다. EventBridge ... | ❌ Lambda(A, B)는 15분 제한 |
| B | AWS Lambda 함수를 생성합니다. Amazon API Gateway HTTP API 를 생성하고 API... | ❌ Lambda(A, B)는 15분 제한 |
| ✅ C | AWS Fargate 시작 유형으로 Amazon Elastic Container Service(Amazon ... | ✅ ECS Fargate with EventBridge scheduled event(C)가 최적 솔루션 |
| D | Amazon EC2 시작 유형이 있는 Amazon Elastic Container Service(Amazon... | ❌ EC2 ECS(D)는 인스턴스 관리 필요 |

---

# Q398
**정답: C**

**문제 분석:**
- 600TB 온프레미스 NAS to AWS, 2주 내, 암호화, 100Mbps 업로드
- 100Mbps × 2주 = 약 150TB (실제는 불안정)
- Snowball Edge 80TB × 8대 = 640TB

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | Amazon S3 멀티파트 업로드 기능을 사용하여 HTTPS를 통해 파일을 전송합니다. | ❌ S3 멀티파트(A)는 네트워크 제약 |
| B | 온프레미스 NAS 시스템과 가장 가까운 AWS 리전 간에 VPN 연결을 생성합니다. VPN 연결을 통해 데이... | ❌ VPN(B)도 대역폭 부족 |
| ✅ C | AWS Snow Family 콘솔을 사용하여 여러 AWS Snowball Edge Storage Optimi... | ✅ Multiple Snowball Edge Storage Optimized(C)가 최적 솔루션 |
| D | 회사 위치와 가장 가까운 AWS 리전 간에 10Gbps AWS Direct Connect 연결을 설정합니다.... | ❌ Direct Connect(D)는 설정 시간 및 비용 과다 |

---

# Q399
**정답: B**

**문제 분석:**
- API Gateway HTTP 플러드 공격 방어, 최소 운영 오버헤드
- WAF는 API Gateway와 직접 통합
- Rate-based rule로 IP당 요청 수 제한

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | 최대 TTL 이 24 시간인 API Gateway 지역 API 엔드포인트 앞에 Amazon CloudFron... | ❌ API Gateway HTTP 플러드 공격 방어, 최소 운영 오버헤드 |
| ✅ B | 속도 기반 규칙을 사용하여 리전 AWS WAF 웹 ACL 을 생성합니다. 웹 ACL 을 API Gateway... | ✅ Regional WAF with rate-based rule(B)가 최적 솔루션 |
| C | Amazon CloudWatch 지표를 사용하여 개수 지표를 모니터링하고 미리 정의된 속도에 도달하면 보안 ... | ❌ CloudWatch(C)는 모니터링만 제공, 차단 불가 |
| D | API Gateway 지역 API 엔드포인트 앞에 Lambda@Edge 를 사용하여 Amazon CloudF... | ❌ CloudFront(A, D)는 추가 계층으로 복잡 |

---

# Q400
**정답: C**

**문제 분석:**
- DynamoDB 새 날씨 이벤트 시 4명 관리자 알림, 현재 앱 성능 영향 없음, 최소 오버헤드
- DynamoDB Streams로 새 항목 자동 감지
- Lambda 트리거로 SNS 주제에 게시

**선택지 분석:**

| 번호 | 방식 | 평가 |
|------|------|------|
| A | DynamoDB 트랜잭션을 사용하여 새 이벤트 데이터를 테이블에 씁니다. 내부 팀에 알리도록 트랜잭션을 구성... | ❌ DynamoDB 트랜잭션(A)은 알림 기능 없음 |
| B | 현재 애플리케이션이 4 개의 Amazon Simple Notification Service(Amazon SN... | ❌ 4개 SNS 주제(B)는 애플리케이션 수정 필요 |
| ✅ C | 테이블에서 Amazon DynamoDB 스트림을 활성화합니다. 트리거를 사용하여 팀이 구독할 수 있는 단일 ... | ✅ DynamoDB Streams + SNS topic(C)가 최적 솔루션 |
| D | 각 레코드에 사용자 정의 속성을 추가하여 새 항목에 플래그를 지정합니다. 새 항목이 있는지 매분 테이블을 스... | ❌ Cron 스캔(D)는 지연 발생 및 성능 영향 |

---
