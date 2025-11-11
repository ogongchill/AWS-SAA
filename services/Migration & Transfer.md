#Migration/Transfer

|목적|선택 서비스|한 줄 설명|
|---|---|---|
|**서버 전체를 그대로 클라우드로 옮기기**|**MGN**|Lift & Shift (VM → EC2)|
|**NAS / 파일서버 / S3 / EFS 이동**|**DataSync**|파일/디렉토리 단위 동기화|
|**DB를 다운타임 거의 없이 옮기기**|**DMS**|DB 마이그레이션 + 실시간 CDC|

---


# AWS Migration Hub

_마이그레이션 진행 상황을 한 곳에서 추적_

`여러 마이그레이션 도구(DMS, MGN 등)를 사용 중일 때 `
`마이그레이션 상태, 진척률, 오류 등을 중앙에서 관리하고 싶을 때`

---

# AWS Application Discovery Service

_온프레미스 서버와 애플리케이션 정보를 자동 수집_

`온프레 환경에 어떤 서버가 어떤 앱을 돌리고 있는지 파악이 필요할 때`
`마이그레이션 전에 워크로드 현황을 분석하여 계획을 세울 때`

---

# AWS Mainframe Modernization

_메인프레임 워크로드를 AWS 환경으로 이전 및 현대화_

`COBOL 등 메인프레임 시스템을 클라우드로 이전할 때`
`기존 애플리케이션을 리호스트하거나 리팩토링해야 할 때`

---

# AWS Application Migration Service (MGN)

_서버 단위 Lift & Shift 자동화_

`온프레미스 또는 다른 클라우드 VM을 AWS로 그대로 이전할 때`
`EC2로 그대로 옮기는 Lift & Shift 마이그레이션이 목표일 때`

---

# Migration Evaluator (formerly TSO Logic)

_클라우드 이전 비용 분석 및 비즈니스 케이스 산출_

`온프레 대비 AWS로 옮겼을 때 비용 효율이 얼마나 되는지 계산할 때`
`마이그레이션 ROI 보고서를 준비해야 할 때`

---

# AWS Transfer Family

_SFTP, FTPS, FTP를 완전관리형으로 제공_

`기존 회사 내부에서 FTP 서버를 운영 중일 때`
`FTP 기반 데이터 교환을 중단하지 않고 AWS로 이전하고 싶을 때`

---

# AWS DataSync

_대량 데이터를 빠르고 안전하게 전송_

`온프레 NAS, 파일 서버 데이터를 S3, EFS, FSx로 이전할 때`
`대규모 파일 시스템 복사 또는 동기화가 필요할 때`

---

# AWS Database Migration Service (DMS)

_데이터베이스를 중단 최소화로 마이그레이션 / 실시간 복제_

` MySQL → Aurora, Oracle → PostgreSQL 등 DB 간 이전할 때`
`운영 중인 DB를 끊지 않고 CDC 기반 실시간 복제해야 할 때`

---
