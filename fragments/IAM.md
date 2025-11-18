#IAM

**AWS 리소스에 대한 인증(Authentication) & 인가(Authorization)를 관리하는 서비스.**
> “누가(WHO) 무엇을(WHAT) 어디서(FROM WHERE) 어떻게(HOW) 할 수 있는지”  

# 요약

- **IAM User** = 사람
    
- **IAM Role** = 애플리케이션 · AWS 서비스가 사용하는 권한
    
- **IAM Group** = 유저 그룹
    
- **Policy** = JSON 권한이 담긴 문서
    
- **Principal** = API 호출자(Role/User/Service)
    
- **Role Assume** = 앱이 Role 신분증 빌림
    
- **Root 사용 X**
    
- **Deny > Allow**

---

# IAM의 핵심 구성 요소 4가지

## Identity (정체성)
> *AWS에 접근할 수 있는 **“사용자”** 또는 “**엔티티”***

- **IAM User**: 사람(직원)이 AWS 콘솔/API 사용
- **IAM Group**: 여러 유저를 묶은 것
- **IAM Role**: 애플리케이션·AWS 서비스가 “Assume”해서 사용하는 정체성
- **Federated User**: 기업 SSO, Cognito 등 외부 IdP 사용자
---

## Policy (정책)

>***권한을 정의한 JSON 문서**  - 정체성에 “무엇을 할 수 있다/없다”를 명시*

- Allow / Deny
- Resource 단위로 허용
- 조건(Condition) 포함 가능
---

## Principle (주체 / Principal)
>*AWS API 호출을 “하는 주체”*

✔ IAM User  
✔ IAM Role  
✔ AWS 서비스 (ec2.amazonaws.com 등)  
✖ Application 자체(역할 Assume 한 Role이 주체)

---

## Authentication & Authorization

- 인증(Authentication): 누구인지 증명
    - Access Key / Secret / MFA
- 인가(Authorization): 무엇을 할 수 있는지
    - IAM Policy 적용

---

# IAM Role

> IAM Role은 "권한을 가진 신분증(Identity)"

그리고 EC2/Lambda/EKS가 Need Access → “역할을 Assume”

**Role이 필요한 이유**
- 애플리케이션에 AccessKey 저장 X → 보안 최강
- Rotate 필요 없음
- IAM Policy를 Role에 붙이고, 인스턴스에 Role을 부여

**대표 유형**
- **EC2 Instance Role**
- **Lambda Execution Role**
- **EKS Pod Role(IRSA)**
- **Cross-account Role**



---
# AA 시험에서 나오는 IAM 문제 패턴

## 패턴 1) EC2에서 S3 접근

✔ EC2 Instance Role  
✖ Access Key 넣기

## 패턴 2) Cross-account S3 접근

✔ Bucket Policy + AssumeRole  
✖ User 직접 주기

## 패턴 3) Lambda에서 DynamoDB/CloudWatch 필요

✔ Execution Role에 정책 추가

## 패턴 4) 조직 전체 권한 제한

✔ SCP(Service Control Policy)

## 패턴 5) 회사 직원 로그인

✔ IAM User + MFA  
✔ 또는 SSO(SAML, IAM Identity Center)

---
