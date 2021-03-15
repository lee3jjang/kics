# 최종수정일자 : 2021.03.15 

############### 테이블 목록 ################
# (수정) KICS_RISK_COEF_NL
###########################################

import sqlite3

conn = sqlite3.connect('kics.db')
cur = conn.cursor()

# (수정) KICS_RISK_COEF_NL(KICS국가그룹 및 보장단위별 위험계수)
cur.execute("""
    CREATE TABLE IF NOT EXISTS KICS_RISK_COEF_NL (
        KICS_CNTR_CATG_CD TEXT,         /* KICS국가그룹코드 */
        BOZ_CD TEXT,                    /* 보종코드 */
        APLY_STRT_DATE TEXT,            /* 적용시작일자 */
        APLY_END_DATE TEXT,             /* 적용종료일자 */
        PREM_RISK_COEF NUMERIC,         /* 보험가격위험계수 */
        RSV_RISK_COEF NUMERIC,          /* 준비금위험계수 */
        LAST_MODIFIED_BY TEXT,
        LAST_UPDATE_DATE TEXT,
        PRIMARY KEY (KICS_CNTR_CATG_CD, BOZ_CD, APLY_STRT_DATE, APLY_END_DATE)
    )
""")