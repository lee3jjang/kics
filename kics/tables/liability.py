# 최종수정일자 : 2021.03.22

##################### 테이블 목록 ######################
# (수정) KICS_PREM_EXPO_NL_G
# (삭제) KICS_PAY_CF_INTERFACE (KAJC0003LM, KAJC0012LM)
# (수정) KICS_PAY_CF_NL (KAJC0012LM, KAJC0016LM, KAJC0017LM, KAJC0018LM)
# (수정) KICS_DISC_FAC_NL (KAJC0004LM)
# (수정) KICS_ASSUM_NL (KAJC0002LM)
# (신규) KICS_USER_ASSUM_NL (XXXX0000LM)
# (신규) KICS_APLY_ASSUM_NL (XXXX0000LM)
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

        # (수정) KICS_ASSUM_NL(가정)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS KICS_ASSUM_NL (
                BASE_DATE TEXT,                 /* 기준일자 */
                RRNR_DVCD TEXT,                 /* 재보험구분코드 */
                DMFR_DVCD TEXT,                 /* 국내외구분코드 */
                BOZ_CD TEXT,                    /* 보종코드 */
                RY_RT NUMERIC,                  /* 회수율 */
                RISK_RT NUMERIC,                /* 최종손해율 */
                PREM_DAG_IVMT_RT NUMERIC,       /* 보험료부채손조비율 */
                EXP_RT NUMERIC,                 /* 유지비율 */
                IBNR_RT NUMERIC,                /* IBNR율 */
                RSV_DAG_IVMT_RT NUMERIC,        /* 보험금부채손조비율 */
                LAST_MODIFIED_BY TEXT,
                LAST_UPDATE_DATE TEXT,
                PRIMARY KEY (BASE_DATE, RRNR_DVCD, DMFR_DVCD, BOZ_CD)
            )
        """)

        # (신규) KICS_USER_ASSUM_NL(가정-수기입력)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS KICS_USER_ASSUM_NL (
                BASE_DATE TEXT,                 /* 기준일자 */
                RRNR_DVCD TEXT,                 /* 재보험구분코드 */
                DMFR_DVCD TEXT,                 /* 국내외구분코드 */
                BOZ_CD TEXT,                    /* 보종코드 */
                RY_RT NUMERIC,                  /* 회수율 */
                RISK_RT NUMERIC,                /* 최종손해율 */
                PREM_DAG_IVMT_RT NUMERIC,       /* 보험료부채손조비율 */
                EXP_RT NUMERIC,                 /* 유지비율 */
                IBNR_RT NUMERIC,                /* IBNR율 */
                RSV_DAG_IVMT_RT NUMERIC,        /* 보험금부채손조비율 */
                LAST_MODIFIED_BY TEXT,
                LAST_UPDATE_DATE TEXT,
                PRIMARY KEY (BASE_DATE, RRNR_DVCD, DMFR_DVCD, BOZ_CD)
            )
        """)

        # (신규) KICS_APLY_ASSUM_NL(가정-적용)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS KICS_USER_ASSUM_NL (
                BASE_DATE TEXT,                 /* 기준일자 */
                ASSUM_DVCD TEXT,                /* 가정구분코드 */
                RRNR_DVCD TEXT,                 /* 재보험구분코드 */
                DMFR_DVCD TEXT,                 /* 국내외구분코드 */
                BOZ_CD TEXT,                    /* 보종코드 */
                RY_RT NUMERIC,                  /* 회수율 */
                RISK_RT NUMERIC,                /* 최종손해율 */
                PREM_DAG_IVMT_RT NUMERIC,       /* 보험료부채손조비율 */
                EXP_RT NUMERIC,                 /* 유지비율 */
                IBNR_RT NUMERIC,                /* IBNR율 */
                RSV_DAG_IVMT_RT NUMERIC,        /* 보험금부채손조비율 */
                LAST_MODIFIED_BY TEXT,
                LAST_UPDATE_DATE TEXT,
                PRIMARY KEY (BASE_DATE, ASSUM_DVCD, RRNR_DVCD, DMFR_DVCD, BOZ_CD)
            )
        """)

        conn.close()