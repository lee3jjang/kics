# 최종수정일자 : 2021.03.15 

############### 테이블 목록 ################
# (수정) KICS_BOZ_CD_RISK_NL (KAKD0008LM)
# (신규) KICS_BOZ_GRP_RISK_NL (XXXX0000LM)
# (수정) KICS_CNTR_RISK_NL (KAKD0002LM)
# KICS_TOT_RISK_NL (KAJC0011LM)
###########################################

################ 일반손해보험위험액 산출순서 ################
# KICS국가그룹, 보장단위별 보험가격/준비금 위험액 (KAKD0008LM)
# KICS국가그룹 및 보장단위별 위험액 (KAKD0008LM)
# KICS국가그룹 및 보장그룹별 위험액 (XXXX0000LM)
# KICS국가그룹별 위험액 (KAKD0002LM)
# 보험가격준비금위험액 위험액 (KAJC0011LM)
# 일반손해보험 위험액 (KAJC0011LM)
###########################################################

import sqlite3

class Risk():

    @classmethod
    def create_table(cls, database_name):
        conn = sqlite3.connect(database_name)

        # (수정) KICS_BOZ_CD_RISK_NL(KICS국가그룹 및 보장단위별 위험액)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS KICS_BOZ_CD_RISK_NL (
                BASE_DATE TEXT,                 /* 기준일자 */
                KICS_CNTR_CATG_CD TEXT,         /* KICS국가그룹코드 */
                BOZ_CD TEXT,                    /* 보종코드 */
                RETAIN_LAPS_PRM NUMERIC,        /* 보험료보유익스포져 */
                RETAIN_RSV_LIAB NUMERIC,        /* 준비금보유익스포져 */
                PREM_RISK_AMT NUMERIC,          /* 보험가격위험액 */
                RSV_RISK_AMT NUMERIC,           /* 준비금위험액 */
                BOZ_CD_RISK NUMERIC,            /* 보장단위별위험액 */
                LAST_MODIFIED_BY TEXT,
                LAST_UPDATE_DATE TEXT,
                PRIMARY KEY (BASE_DATE, KICS_CNTR_CATG_CD, BOZ_CD)
            )
        """)

        # (신규) KICS_BOZ_GRP_RISK_NL(KICS국가그룹 및 보장그룹별 위험액)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS KICS_BOZ_GRP_RISK_NL (
                BASE_DATE TEXT,                 /* 기준일자 */
                KICS_CNTR_CATG_CD TEXT,         /* KICS국가그룹코드 */
                BOZ_CATG_CD TEXT,               /* 보장그룹코드 */
                BOZ_GRP_RISK NUMERIC,           /* 보장그룹별위험액 */
                LAST_MODIFIED_BY TEXT,
                LAST_UPDATE_DATE TEXT,
                PRIMARY KEY (BASE_DATE, KICS_CNTR_CATG_CD, BOZ_CATG_CD)
            )
        """)

        # (수정) KICS_CNTR_RISK_NL(KICS국가그룹별 위험액)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS KICS_CNTR_RISK_NL (
                BASE_DATE TEXT,                 /* 기준일자 */
                KICS_CNTR_CATG_CD TEXT,         /* KICS국가그룹코드 */
                CNTR_RISK NUMERIC,              /* KICS국가그룹별위험액 */
                LAST_MODIFIED_BY TEXT,
                LAST_UPDATE_DATE TEXT,
                PRIMARY KEY (BASE_DATE, KICS_CNTR_CATG_CD)
            )
        """)

        # KICS_TOT_RISK_NL(일반손해보험위험액)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS KICS_TOT_RISK_NL (
                BASE_DATE TEXT,                 /* 기준일자 */
                CAT_CAL_CD TEXT,                /* 대재해위험액산출기준(1: 원수, 2: 보유)
                CNTR_RISK NUMERIC,              /* KICS국가그룹별위험액(합계) */
                KICS_PRM_RSV_RISK NUMERIC,      /* 보험가격준비금위험액 */
                KICS_IND_CAT_RISK NUMERIC,      /* 대재해위험액(단순합계) */
                KICS_CAT_RISK NUMERIC,          /* 대재해위험액(상관관계반영) */
                DVS_EPCT NUMMERIC,              /* 분산효과 */
                KICS_NON_LIKE_RISK NUMERIC,     /* 일반손해보험위험액 */
                LAST_MODIFIED_BY TEXT,
                LAST_UPDATE_DATE TEXT,
                PRIMARY KEY (BASE_DATE, CAT_CAL_CD)
            )
        """)

        conn.close()