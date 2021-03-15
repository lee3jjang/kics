# 최종수정일자 : 2021.03.15 

############ 상관계수 순서 ############
# 1. 보험가격 및 준비금 상관계수 (0.25)
# 2. 보장그룹내 상관계수 (0.25~1)
# 3. 보장그룹간 상관계수 (0.5)
# 4. 지역간 상관계수 (0.25)
# 5. 대재해-일반손해간 상관계수 (0.25)
######################################

# KICS_CORR_PREM_RSV_NL
# KICS_CORR_BOZ_INR_NL (신규)
# KICS_CORR_BOZ_NL
# KICS_CORR_CNTR_NL
# KICS_CORR_SCR_NL


import sqlite3

conn = sqlite3.connect('../kics.db')
cur = conn.cursor()

# 1. KICS_CORR_PREM_RSV_NL(보험가격 및 준비금 상관계수)
cur.execute("""
    CREATE TABLE IF NOT EXISTS KICS_CORR_PREM_RSV_NL (
        CNTR_CATG_CD TEXT,              /* 국가그룹코드 */
        BOZ_CD TEXT,                    /* 보종코드 */
        PREM_RSV_CD,                    /* 보험가격준비금코드 */
        OTH_PREM_RSV_CD,                /* 상대보험가격준비금코드 */
        APLY_STRT_DATE TEXT,            /* 적용시작일자 */
        APLY_END_DATE TEXT,             /* 적용종료일자 */
        CORR_COEF NUMERIC,              /* 상관계수 */
        LAST_MODIFIED_BY TEXT,
        LAST_UPDATE_DATE TEXT,
        PRIMARY KEY (CNTR_CATG_CD, BOZ_CD, PREM_RSV_CD, OTH_PREM_RSV_CD, APLY_STRT_DATE, APLY_END_DATE)
    )
""")

# 2. (신규) KICS_CORR_BOZ_INR_NL(보장단위간 상관계수)
cur.execute("""
    CREATE TABLE IF NOT EXISTS KICS_CORR_BOZ_INR_NL (
        BOZ_CATG_CD TEXT,               /* 보장그룹코드 */
        BOZ_CD TEXT,                    /* 보장단위코드 */
        OTH_BOZ_CD TEXT,                /* 상대방보장단위코드 */
        APLY_STRT_DATE TEXT,            /* 적용시작일자 */
        APLY_END_DATE TEXT,             /* 적용종료일자 */
        CORR_COEF NUMERIC,              /* 상관계수 */
        LAST_MODIFIED_BY TEXT,
        LAST_UPDATE_DATE TEXT,
        PRIMARY KEY (BOZ_CATG_CD, BOZ_CD, OTH_BOZ_CD, APLY_STRT_DATE, APLY_END_DATE)
    )
""")

# 3. KICS_CORR_BOZ_NL(보장그룹간 상관계수)
cur.execute("""
    CREATE TABLE IF NOT EXISTS KICS_CORR_BOZ_NL (
        KICS_CNTR_CATG_CD TEXT,         /* KICS국가그룹코드 */
        BOZ_CATG_CD TEXT,               /* 보장그룹코드 */ 
        OTH_BOZ_CATG_CD TEXT,           /* 상대보장그룹코드 */
        APLY_STRT_DATE TEXT,            /* 적용시작일자 */
        APLY_END_DATE TEXT,             /* 적용종료일자 */
        CORR_COEF NUMERIC,              /* 상관계수 */
        LAST_MODIFIED_BY TEXT,
        LAST_UPDATE_DATE TEXT,
        PRIMARY KEY (KICS_CNTR_CATG_CD, BOZ_CATG_CD, OTH_BOZ_CATG_CD, APLY_STRT_DATE, APLY_END_DATE)
    );
""")

# 4. KICS_CORR_CNTR_NL(지역간 상관계수)
cur.execute("""
    CREATE TABLE IF NOT EXISTS KICS_CORR_CNTR_NL (
        KICS_CNTR_CATG_CD TEXT,         /* KICS국가그룹코드 */
        KICS_OTH_CNTR_CATG_CD TEXT,     /* 상대KICS국가그룹코드 */
        APLY_STRT_DATE TEXT,            /* 적용시작일자 */
        APLY_END_DATE TEXT,             /* 적용종료일자 */
        CORR_COEF NUMERIC,              /* 상관계수 */
        LAST_MODIFIED_BY TEXT,
        LAST_UPDATE_DATE TEXT,
        PRIMARY KEY (KICS_CNTR_CATG_CD, KICS_OTH_CNTR_CATG_CD, APLY_STRT_DATE, APLY_END_DATE)
    )
""")

# 5. KICS_CORR_SCR_NL(보험가격준비금위험액 및 대재해위험액 상관계수)
cur.execute("""
    CREATE TABLE IF NOT EXISTS KICS_CORR_SCR_NL (
        SCR_CD TEXT,                    /* 요구자본코드 */
        OTH_SCR_CD TEXT,                /* 상대요구자본코드 */
        APLY_STRT_DATE TEXT,            /* 적용시작일자 */
        APLY_END_DATE TEXT,             /* 적용종료일자 */
        CORR_COEF NUMERIC,              /* 상관계수 */
        LAST_MODIFIED_BY TEXT,
        LAST_UPDATE_DATE TEXT,
        PRIMARY KEY (SCR_CD, OTH_SCR_CD, APLY_STRT_DATE, APLY_END_DATE)
    )
""")