
AWS 시험에서 **“두 개를 고르시오(2-of-N)” 문제**가 나오고,

- **하나는 ‘쿼리/분석(Athena, QuickSight 등)’이 거의 확실해 보이는 선택지**라면
    
- **나머지 하나는 99% 확률로 ‘데이터 수집·정제·저장 단계(Glue, Kinesis, Lake Formation 등)’이다.**
    

즉 **분석 단계 하나 + 데이터 준비 단계 하나**의 조합이 정답 패턴이라고 보면 됨.

---

# ✅ 왜 항상 이런 조합이 되는가?

AWS Data Analytics / Architect 문제는 일반적으로 데이터 흐름을 이렇게 나눔:

1. **데이터 수집(Ingest)**
    
2. **저장(Storage / Data Lake / Data Warehouse)**
    
3. **처리/변환(ETL, Stream Processing)**
    
4. **분석/쿼리(Query, BI Tool)**
    
5. **시각화(Dashboard / KPI)**
    

문제에서 "두 개 선택"이라면 대부분:

### ✔ 하나는 ‘분석·시각화 단계’를 담당

예:

- Athena
    
- QuickSight
    
- Redshift Query Editor
    
- EMR for analysis (稀有)
    

### ✔ 다른 하나는 ‘데이터 준비 단계’를 담당

예:

- AWS Glue
    
- Lake Formation
    
- Kinesis → S3
    
- Firehose → S3
    
- Redshift COPY
    
- DMS → S3
    

AWS 시험은 전체 파이프라인(ETL → Storage → Query)을 묻는 구조라서 조합이 반드시 이렇게 나옴.

---

# 🔥 실제 시험 패턴 예시

## ❗ 패턴 1:

- **Athena 또는 QuickSight** 등장 → 무조건 분석/시각화 단계  
    → 나머지 하나는 Glue, LF, Firehose, Kinesis 중 하나
    

## ❗ 패턴 2:

- **Redshift Spectrum 사용**  
    → 나머지 하나는 S3 + Parquet 변환(Glue)
    

## ❗ 패턴 3:

- **KPI / Dashboard라는 단어가 나옴**  
    → QuickSight 선택  
    → 나머지는 Data Lake에 넣는 선택지
    

---

# ❌ 반대 패턴이 거의 없음

예를 들어 분석 단계 + 분석 단계 (Athena + QuickSight + Kinesis Analytics) 같이  
"분석-분석" 조합이 정답인 경우는 사실상 없음.

왜냐하면 문제는 "파이프라인을 구성하라"이기 때문.


# ✅ 1. Athena / QuickSight 등장 → **분석·시각화 단계 확정**

### 🔥 다른 하나는 100% **데이터 준비(ETL) 또는 저장 단계**

- Glue (ETL)
    
- Lake Formation (데이터 레이크)
    
- Firehose → S3
    
- S3 Parquet 저장
    
- DMS → S3
    

### ❗ 예시

- “일회성 쿼리” → **Athena + Glue**
    
- “KPI 대시보드 생성” → **QuickSight + Glue/LF**
    

### ❌ 금지

- Athena + QuickSight (둘 다 분석/시각화)
    
- Athena + Kinesis Analytics (둘 다 분석)
    

---

# ✅ 2. Kinesis 등장 → **실시간 수집/처리 단계 확정**

### 🔥 함께 고를 짝은 “저장” 또는 “분석”

- Firehose → S3
    
- Streams → Lambda → S3
    
- Kinesis Analytics + S3
    
- Firehose → Redshift
    
- Firehose → Glue → Parquet
    

### ❗ 예시

- “실시간 로그를 데이터 레이크에 넣기”  
    → **Firehose + S3/Glue**
    
- “스트림을 분석 후 저장”  
    → **Kinesis Data Analytics + S3**
    

### ❌ 금지

- Kinesis + Athena (분석 + 분석)
    
- Firehose + Streams (둘 다 수집)
    

---

# ✅ 3. Glue 등장 → **ETL/정제 단계 확정**

### 🔥 함께 고를 짝은 “저장/분석”

- S3 (Parquet)
    
- Lake Formation
    
- Athena
    
- QuickSight
    
- Redshift COPY
    

### ❗ 예시

- “데이터를 변환 후 쿼리”  
    → **Glue + Athena**
    
- “정제 후 BI 시각화”  
    → **Glue + QuickSight**
    

### ❌ 금지

- Glue + Glue (중복 단계)
    
- Glue + Kinesis Analytics (둘 다 변환/처리 계열)
    

---

# ✅ 4. Redshift 등장 → **데이터 웨어하우스 단계 확정**

### 🔥 함께 고를 짝은 “ETL/수집”

- Firehose → Redshift
    
- Glue ETL + Redshift COPY
    
- Redshift Spectrum + Glue (Parquet)
    

### ❗ 예시

- “실시간 데이터 → Redshift”  
    → **Firehose + Redshift**
    
- “S3 외부 테이블 쿼리”  
    → **Redshift Spectrum + Glue**
    

### ❌ 금지

- Redshift + Athena (둘 다 분석 엔진)
    

---

# 🧠 **최종 압축 암기(10초)**

### ✔ Athena/QuickSight → 남은 하나 = **ETL/Storage 단계**

### ✔ Kinesis → 남은 하나 = **저장/분석 단계**

### ✔ Glue → 남은 하나 = **저장/분석 단계**

### ✔ Redshift → 남은 하나 = **수집/ETL 단계**

### ✔ 같은 역할끼리는 절대 정답 X

(분석+분석 / ETL+ETL / 수집+수집 조합은 아예 나오지 않음)