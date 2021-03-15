# 최종수정일자 : 2021.03.15 

############# 테이블 목록 ##############
# KICS_CNTR_GRP_NL
#######################################

import sqlite3

conn = sqlite3.connect('kics.db')
cur = conn.cursor()

# KICS_CNTR_GRP_NL(국가그룹 -> KICS국가그룹 맵핑)
cur.execute("""
    CREATE TABLE IF NOT EXISTS KICS_CNTR_GRP_NL (
        CNTR_CATG_CD TEXT,              /* 국가그룹코드 */
        CNTR_CATG_NM TEXT,              /* 국가그룹명 */
        KICS_CNTR_CATG_CD TEXT,         /* KICS국가그룹코드 */
        KICS_CNTR_CATG_NM TEXT,         /* KICS국가그룹명 */
        LAST_MODIFIED_BY TEXT,
        LAST_UPDATE_DATE TEXT,
        PRIMARY KEY (CNTR_CATG_CD)
    )
""")

# (수정) KICS_BOZ_GRP_MAP_NL(보장단위 -> 보장그룹 맵핑)
cur.execute("""
    CREATE TABLE IF NOT EXISTS KICS_BOZ_GRP_MAP_NL (
        BOZ_CD TEXT,                    /* 보종코드 */
        BOZ_CATG_CD TEXT,               /* 보장그룹코드 */
        LAST_MODIFIED_BY TEXT,
        LAST_UPDATE_DATE TEXT,
        PRIMARY KEY (BOZ_CD)
    )
""")