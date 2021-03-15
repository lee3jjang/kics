# 최종수정일자 : 2021.03.15 

############# 테이블 목록 ##############
# (수정) KICS_CNTR_RISK_NL (KAKD0002LM)
# KICS_TOT_RISK_NL (KAJC0011LM)
#######################################

import sqlite3

conn = sqlite3.connect('kics.db')
cur = conn.cursor()

# (수정) KICS_CNTR_RISK_NL(KICS국가그룹별 요구자본)
cur.execute("""
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
cur.execute("""
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
