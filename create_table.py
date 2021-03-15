import sqlite3

conn = sqlite3.connect('kics.db')
cur = conn.cursor()

# 보장그룹간 상관계수
cur.execute("""
    CREATE TABLE IF NOT EXISTS KICS_CORR_BOZ_NL (
        KICS_CNTR_CATG_CD TEXT,     /* KICS국가그룹코드 */
        BOZ_CATG_CD TEXT,           /* 보장그룹코드 */ 
        OTH_BOZ_CATG_CD TEXT,       /* 상대보장그룹코드 */
        APLY_STRT_DATE TEXT,        /* 적용시작일자 */
        APLY_END_DATE TEXT,         /* 적용종료일자 */
        CORR_COEF NUMERIC,          /* 상관계수 */
        LAST_MODIFIED_BY TEXT,
        LAST_UPDATE_DATE TEXT,
        PRIMARY KEY (KICS_CNTR_CATG_CD, BOZ_CATG_CD, OTH_BOZ_CATG_CD, APLY_STRT_DATE, APLY_END_DATE)
    );
""")