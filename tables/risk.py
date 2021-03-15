# 최종수정일자 : 2021.03.15 

############# 테이블 목록 #############
# KICS_CNTR_RISK_NL
######################################

import sqlite3

conn = sqlite3.connect('kics.db')
cur = conn.cursor()

# (수정) KICS_CNTR_RISK_NL(지역별 요구자본)
cur.execute("""
    CREATE TABLE IF NOT EXISTS KICS_CNTR_RISK_NL (
        BASE_DATE TEXT,
        KICS_CNTR_CATG_CD TEXT,
        CNTR_RISK NUMERIC,
        LAST_MODIFIED_BY TEXT,
        LAST_UPDATE_DATE TEXT,
        PRIMARY KEY (BASE_DATE, KICS_CNTR_CATG_CD)
    )
""")