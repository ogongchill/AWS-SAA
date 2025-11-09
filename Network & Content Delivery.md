#NETWORK/CONENT-DELIVERY
#NetworkContent-Delivery 
# **Amazon VPC (Virtual Private Cloud)**

가상 네트워크 환경

> _사용자가 정의한 가상 네트워크 안에서 AWS 리소스를 안전하게 배치할 수 있는 격리된 환경._

`서브넷(공용/사설) 구성 → EC2 배치   보안그룹 / NACL 설정 → 네트워크 접근 제어`

---

# **Amazon VPC Lattice**

서비스 간 네트워크 통합

> _마이크로서비스 간 통신을 안전하고 일관되게 관리할 수 있는 서비스 네트워크._

`VPC 간 마이크로서비스 트래픽 관리   서비스별 인증·인가 정책 설정`

---

# **AWS Verified Access**

VPN 없는 애플리케이션 보안 접속

> _VPN 없이 제로 트러스트(Zero-Trust) 방식으로 내부 애플리케이션에 안전하게 접근._

`사내 직원이 VPN 없이 내부 대시보드 접속   ID 기반 정책으로 접근 제어`

---

# **AWS Direct Connect**

전용 회선 연결

> _온프레미스 데이터센터와 AWS 간을 전용 물리 회선으로 연결하여 안정적이고 저지연 통신._

`기업 데이터센터 ↔ AWS VPC 간 전용선 연결   고속·보안 통신 (인터넷 우회)`

---

# **AWS App Mesh**

서비스 메시(Service Mesh)

> _마이크로서비스 간 트래픽을 세밀하게 모니터링하고 제어할 수 있는 서비스 네트워크._

`마이크로서비스 간 요청 라우팅 / 리트라이 / 모니터링   Envoy 프록시 기반 통신 제어`

---

# **AWS Cloud WAN**

글로벌 WAN 네트워크 관리

> _전 세계 VPC와 온프레미스 네트워크를 단일 글로벌 네트워크로 구성 및 관리._

`서울 ↔ 도쿄 ↔ 오하이오 리전 간 연결   글로벌 기업용 백본망 구축`

---

# **AWS Transit Gateway**

VPC 간 중앙 허브

> _여러 VPC, 계정, 온프레미스 네트워크를 하나의 허브로 연결하여 확장성 있는 네트워크 구성._

`여러 VPC를 Transit Gateway에 연결   VPC 간 트래픽 라우팅 단순화`

---

# **Amazon Route 53**

DNS(도메인 네임 시스템)

> _확장 가능한 클라우드 기반 DNS 서비스로, 트래픽을 다양한 리전으로 라우팅 가능._

`도메인 등록 및 DNS 라우팅 → www.example.com → CloudFront   지리 기반 트래픽 라우팅`

---

# **AWS VPN (Site-to-Site / Client)**

보안 VPN 연결

> _인터넷을 통해 AWS VPC와 온프레미스 네트워크를 안전하게 연결._

`온프레미스 방화벽 ↔ AWS VPN 게이트웨이   사용자 VPN 클라이언트 ↔ AWS VPC 접속`

---

# **AWS Global Accelerator**

글로벌 네트워크 최적화

> _AWS 글로벌 네트워크를 통해 트래픽을 최적의 엔드포인트로 라우팅, 지연시간 단축._

`글로벌 사용자 → 가장 가까운 리전 엔드포인트로 라우팅   웹 애플리케이션 응답속도 개선`

---

# **Elastic Load Balancing (ELB)**

트래픽 분산

> _들어오는 요청을 여러 EC2, 컨테이너, Lambda로 자동 분산시켜 가용성 향상._

`Application Load Balancer → HTTP/HTTPS 요청 분산   Network Load Balancer → TCP/UDP 트래픽 처리`

---

# **AWS PrivateLink**

서비스 프라이빗 액세스

> _VPC 내부에서 AWS 서비스나 타 계정의 서비스에 프라이빗하게 접근 가능._

`S3 / API Gateway / Partner 서비스에 Private Endpoint로 접근   인터넷 우회 없이 내부 트래픽만 사용`

---

# **Amazon CloudFront**

콘텐츠 전송 네트워크 (CDN)

> _글로벌 엣지 로케이션을 통해 정적·동적 콘텐츠를 빠르고 안전하게 전달._

`정적 웹사이트, 이미지, 동영상 → CloudFront 캐싱   S3 + CloudFront → 전 세계 콘텐츠 배포`

---

# **Amazon API Gateway**

API 관리 서비스

> _REST / WebSocket API를 생성, 배포, 관리할 수 있는 완전관리형 서비스._

`백엔드 Lambda / EC2 API를 외부에 공개   사용자 인증·요금제·API 키 관리`

---

# **AWS Cloud Map**

서비스 디스커버리

> _애플리케이션 리소스(서비스, DB 등)를 이름 기반으로 자동 등록하고 검색 가능._

`EC2 / ECS 서비스가 자동으로 DNS 이름으로 등록   서비스 간 동적 연결 구성`