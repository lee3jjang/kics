# 최종수정일자 : 2021.03.22

############### 테이블 목록 ################
# (수정) KICS_PAY_CF_INTERFACE (KAJC0003LM)

import sqlite3

class Liability():

    @classmethod
    def create_table(cls, database_name):
        conn = sqlite3.connect(database_name)

        # (수정) KICS_PAY_CF_INTERFACE(지급보험금 인터페이스)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS KICS_PAY_CF_INTERFACE (
                BSE_YM TEXT,                    /* 기준년월 */
                RRNR_DVCD TEXT,                 /* 재보험구분코드 */
                DMFR_DVCD TEXT,                 /* 국내외구분코드 */
                BOZ_CD TEXT,                    /* 보종코드 */
                YEAR INTEGER,                   /* 지급년도 */
                PAY_CF NUMERIC,                 /* 지급보험금 */
                LAST_MODIFIED_BY TEXT,
                LAST_UPDATE_DATE TEXT,
                PRIMARY KEY (BSE_YM, RRNR_DVCD, DMFR_DVCD, BOZ_CD, YEAR)
            )
        """)

        conn.close()