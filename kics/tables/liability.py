# 최종수정일자 : 2021.03.22

##################### 테이블 목록 ######################
# (수정) KICS_PREM_EXPO_NL_G
# (삭제) KICS_PAY_CF_INTERFACE (KAJC0003LM, KAJC0012LM)
# (삭제) KICS_PAY_CF_NL (KAJC0012LM)
# (수정) KICS_DISC_FAC_NL (KAJC0004LM)
#######################################################

import sqlite3

class Liability():

    @classmethod
    def create_table(cls, database_name):
        conn = sqlite3.connect(database_name)

        # (수정) KICS_PREM_EXPO_NL_G(보험료부채 익스포져_일반)
        # TODO: 재작업필요
        conn.execute("""
            CREATE TABLE IF NOT EXISTS KICS_PREM_EXPO_NL_G (
                BASE_DATE TEXT,                 /* 기준년월 */
                RRNR_DVCD TEXT,                 /* 재보험구분코드 */
                DMFR_DVCD TEXT,                 /* 국내외구분코드 */
                BOZ_CD TEXT,                    /* 보종코드 */
                KICS_CNTR_CATG_CD TEXT,         /* KICS국가그룹코드 */
                PDGR_CD TEXT,                   /* 상품군코드 */
                PRON_NOT_PRON_DVCD TEXT,        /* 비례비비례구분코드 */
                CNNT_DMSN_DVCD TEXT             /* 연동수수료구분코드 */
            )
        """)

        # (수정) KICS_PAY_CF_NL(보험금 현금흐름)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS KICS_PAY_CF_NL (
                BASE_DATE TEXT,                    /* 기준일자 */
                RRNR_DVCD TEXT,                 /* 재보험구분코드 */
                DMFR_DVCD TEXT,                 /* 국내외구분코드 */
                BOZ_CD TEXT,                    /* 보종코드 */
                YEAR INTEGER,                   /* 지급년도 */
                PAY_CF NUMERIC,                 /* 지급보험금 */
                PRM_AVR_PAY_TRM,                /* 보험료부채평균지급시점 */
                RSV_AVR_PAY_TRM,                /* 준비금부채평균지급시점 */
                PAY_RT NUMERIC,                 /* 지급율 */
                ADJ_RT NUMERIC,                 /* 조정률 */
                LAST_MODIFIED_BY TEXT,
                LAST_UPDATE_DATE TEXT,
                PRIMARY KEY (BASE_DATE, RRNR_DVCD, DMFR_DVCD, BOZ_CD, YEAR)
            )
        """)

        # (수정) KICS_DISC_FAC_NL(할인요소)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS KICS_DISC_FAC_NL (
                BASE_DATE TEXT,                 /* 기준일자 */
                RRNR_DVCD TEXT,                 /* 재보험구분코드 */
                DMFR_DVCD TEXT,                 /* 국내외구분코드 */
                BOZ_CD TEXT,                    /* 보종코드 */
                PRM_DISC_FC NUMERIC,            /* 보험료부채할인요소 */
                RSV_DISC_FC NUMERIC,            /* 준비금부채할인요소 */
                LAST_MODIFIED_BY TEXT,
                LAST_UPDATE_DATE TEXT,
                PRIMARY KEY (BASE_DATE, RRNR_DVCD, DMFR_DVCD, BOZ_CD)
            )
        """)

        conn.close()