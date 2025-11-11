---

---

# **☁️OBJCET STORAGE**

---

# Amazon S3

오브젝트 단위 저장

>*업계 표준의 확장성과 내구성을 가진 객체 스토리지. 파일을 “객체(Object)”로 저장, 메타데이터와 함께 관리.*

```
앱 로그, 이미지, 백업, 정적 웹사이트, AI 데이터셋 저장
```

[[S3]]

---

# **📁 FILE STORAGE**

---

# Amazon EFS

서버리스 네트워크 파일 시스템



>*여러 EC2 인스턴스가 동시에 접근 가능한 공유 파일시스템. 자동 확장.*

```
여러 EC2가 동시에 접근하는 웹 애플리케이션 로그 디렉토리
```

---

# Amazon FSx

고성능/특화 파일 시스템

>*Windows, Lustre, NetApp ONTAP 등 상용/오픈소스 FS를 완전 관리형으로 제공.*

```
기업용 SMB 파일 서버, HPC(고성능 컴퓨팅), ML 데이터셋
```


---

# **💽BLOCK STORAGE**

---

# Amazon EBS

EC2용 블록 디바이스

>*EC2 인스턴스에 연결되는 디스크 볼륨. SSD/HDD 타입 선택 가능*

```
데이터베이스 스토리지, 트랜잭션 로그, 루트 볼륨
```

---

# **🔄 DATA MIGRATION**

---

# AWS DataSync

온라인 데이터 전송

>*온프레미스 ↔ AWS 간 데이터를 안전하고 빠르게 전송 (증분/병렬 복사).

```
NAS → S3, 파일 서버 → EFS 마이그레이션
```

---

# AWS Snowball

오프라인 대용량 데이터 이동

> _수십~수백TB 데이터를 보안 장비로 물리적으로 전송하는 서비스._
 🚛Snowmobile은 실제로 45피트 컨테이너 트럭입니다! 
  데이터센터 전체를 마이그레이션할 때 사용합니다.

```
연구 데이터센터 → AWS S3 (인터넷 전송 불가 환경)
```

---

# 🌐 **Hybrid cloud storage / Edge computing**

---

# AWS Storage Gateway

온프레미스-클라우드 통합 스토리지

> _로컬 NAS처럼 보이지만 실제 데이터는 S3에 저장되는 하이브리드 저장소._

`온프레미스 백업 → S3(File Gateway)   로컬 볼륨 스냅샷 → EBS Volume Gateway   테이프 백업 → S3 Glacier (Tape Gateway)`

---

# 📤 **Managed file transfer**

---

# AWS Transfer Family

SFTP/FTPS/FTP 기반 파일 전송

> _S3나 EFS를 대상으로 SFTP, FTPS, FTP로 파일을 송수신할 수 있는 완전관리형 서비스._

`파트너사 데이터 업로드 → S3 (SFTP)   내부 사용자 파일 교환 → EFS (FTP)`

---

# 🧩 **Disaster recovery & Backup**

---

# AWS Elastic Disaster Recovery (DRS)

재해 복구 자동화

> _온프레미스 또는 클라우드 환경을 AWS로 복제해 장애 시 신속히 복구._

`데이터센터 장애 발생 시 → AWS 인스턴스로 복구   물리 서버 → EC2 복제`

---

# AWS Backup

중앙 백업 관리

> _EBS, RDS, DynamoDB, EFS 등 AWS 리소스의 백업을 정책 기반으로 자동화._

`EBS/RDS 주기적 백업 → AWS Backup   백업 규정 준수 리포트 생성`

---

