#ManagementTools

# AWS Config

리소스 구성 추적
>*AWS 리소스의 설정(구성) 변경을 자동으로 기록하고, 규정 준수 여부를 평가함*

```
“S3 버킷이 모두 암호화되어 있는지 자동으로 검사”  
→ Config 규칙으로 `S3-BUCKET-ENCRYPTED` 평가
```

---

# AWS CloudTrail

API 활동 로그
>*모든 AWS 계정의 API 호출(누가, 언제, 무엇을 했는지)을 기록*

```
“누가 EC2 인스턴스를 종료했는지 확인”  
→ CloudTrail 이벤트에서 `TerminateInstances` 검색
```

---

# AWS Service Catalog

표준 서비스 포트폴리오 제공

>*관리자가 승인된 EC2, RDS, Lambda 템플릿을 만드어 사용자에게 셀프 서비스 배포 제공*

```
개발팀은 허용된 EC2 템플릿으로만 인스턴스 생성
```

---

# AWS Systems Manager (SSM)

인프라 운영 관리 [link](https://aws.amazon.com/ko/systems-manager)

>*EC2, 온프레미스 서버, 하이브리드 환경을 중앙에서 제어 및 자동화*

```
1000대 서버에 보안 패치 명령 동시 실행
-> SSM run Command 사용
```

[[AWS Systems Manager (SSM)|Patch Manager vs RunCommand]]

---

# AWS Billing and Cost Management

비용 분석 및 관리

>*비용 대시보드, 예산 설정, Cost Explorer 등으로 청구 및 예산 추적*

```
이번달 EC2 비용이 예산을 초과할 것 같으면 알림 발송
```

---

# AWS Resource Explorer

리소스 검색

>*여러 리전에 걸친 AWS 리소스 빠르게 검색*

```
내 계정에서 `prod` 태그가 붙은 모든 EC2 인스턴스 찾기
```

---

# AWS Organizations

다계정 중앙 관리
>*여러 AWS 계정을 중앙에서 관리하고 정책 적용(SCP)*

```
보안 계정은 루트 사용자 로그인 차단
 -> Organizations의 Service Control Policy(SCP)로 설정
```


---

# AWS Compute Optimizer

성능 및 비용 최적화 추천
>*CPU, 메모리, 네트워크 사용률 분석해 더 적합한 인스턴스 타입 추천*

```
t2.large인스턴스 과하게 사용중 -> m5.large로 변경  추천
```