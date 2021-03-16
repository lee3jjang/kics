# 최종수정일자 : 2021.03.15 

############### 테이블 목록 ################
# (수정) KICS_PRM_RSV_EXPO_NL (KAKD0007LM)
###########################################

import sqlite3

class Exposure():

    @classmethod
    def create_table(cls, database_name):
        conn = sqlite3.connect(database_name)

        # (수정) KICS_PRM_RSV_EXPO_NL(보험가격준비금 익스포져)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS KICS_PRM_RSV_EXPO_NL (
                BASE_DATE TEXT,                     /* 기준일자 */
                KICS_CNTR_CATG_CD TEXT,             /* KICS국가그룹코드 */
                BOZ_CD TEXT,                        /* 보종코드 */
                PRM_INSRD_CNNT NUMERIC,             /* 원수보험료_연동수수료 */
                PRM_INSRD_NON_CNNT NUMERIC,         /* 원수보험료_비연동수수료 */
                PRM_REINSRD_CNNT_PROP NUMERIC,      /* 수재보험료_연동수수료_비례 */
                PRM_REINSRD_CNNT_NON_PROP NUMERIC,  /* 수재보험료_연동수수료_비비례 */
                PRM_REINSRD_NON_CNNT NUMERIC,       /* 수재보험료_비연동수수료 */
                PRM_CEDED_CNNT_PROP NUMERIC,        /* 출재보험료_연동수수료_비례 */
                PRM_CEDED_CNNT_NON_PROP NUMERIC,    /* 출재보험료_연동수수료_비비례 */
                PRM_CEDED_NON_CNNT NUMERIC,         /* 출재보험료_비연동수수료 */
                RSV_INSRD_CNNT NUMERIC,             /* 원수준비금_연동수수료 */
                RSV_INSRD_NON_CNNT NUMERIC,         /* 원수준비금_비연동수수료 */
                RSV_REINSRD_CNNT_PROP NUMERIC,      /* 수재준비금_연동수수료_비례 */
                RSV_REINSRD_CNNT_NON_PROP NUMERIC,  /* 수재준비금_연동수수료_비비례 */
                RSV_REINSRD_NON_CNNT NUMERIC,       /* 수재준비금_비연동수수료 */
                RSV_CEDED_CNNT_PROP NUMERIC,        /* 출재준비금_연동수수료_비례 */
                RSV_CEDED_CNNT_NON_PROP NUMERIC,    /* 출재준비금_연동수수료_비비례 */
                RSV_CEDED_NON_CNNT NUMERIC,         /* 출재준비금_비연동수수료 */
                IA_INSRD NUMERIC,                   /* 원수가입금액 */
                IA_REINSURED NUMERIC,               /* 수재가입금액 */
                IA_CEDED NUMERIC,                   /* 출재가입금액 */
                LAST_MODIFIED_BY TEXT,
                LAST_UPDATE_DATE TEXT,
                PRIMARY KEY (BASE_DATE, KICS_CNTR_CATG_CD, BOZ_CD)
            )
        """)

        conn.close()