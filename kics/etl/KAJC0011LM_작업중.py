import os
import math
import sqlite3
import numpy as np
import pandas as pd
from datetime import datetime

# 최종수정일자 : 2021.03.16

########################### KAJC0011LM ###########################
# DESCRIPTION:
#   국가그룹별 위험액에 상관계수 반영하여 보험가격준비금위험액 산출
# SOURCE:
#   KICS_CNTR_RISK_NL
#   KICS_CORR_CNTR_NL
# TARGET: 
#   KICS_TOT_RISK_NL
##################################################################

########################### TEST(FAIL) ###########################
# WARNING:
#   TARGET 완성을 위해선 대재해위험액 산출관련 SOURCE와 로직이 더 필요
# TARGET 중 CNTR_RISK, KICS_PRM_RSV_RISK 컬럼은 테스트 통과
##################################################################

if __name__ == '__main__':

    os.environ['BASE_DATE'] = '20181231'
    os.environ['DATABASE_NAME'] = 'kics.db'
    base_date = datetime.strptime(os.environ['BASE_DATE'], '%Y%m%d').strftime('%Y-%m-%d 00:00:00')
    
    conn = sqlite3.connect(os.environ['DATABASE_NAME'])
    cur = conn.cursor()

    # KICS_CNTR_RISK_NL 추출
    cur.execute(f'SELECT KICS_CNTR_CATG_CD, CNTR_RISK FROM KICS_CNTR_RISK_NL WHERE BASE_DATE="{base_date}"')
    risk_by_cntr = pd.DataFrame(cur.fetchall(), columns=[x[0] for x in cur.description]) \
        .sort_values(by='KICS_CNTR_CATG_CD') \
        .set_index('KICS_CNTR_CATG_CD')['CNTR_RISK']

    # KICS_CORR_CNTR_NL 추출
    cur.execute(f'''
        SELECT KICS_CNTR_CATG_CD, KICS_OTH_CNTR_CATG_CD, CORR_COEF
          FROM KICS_CORR_CNTR_NL
          WHERE APLY_STRT_DATE<="{os.environ["BASE_DATE"]}"
            AND APLY_END_DATE>="{os.environ["BASE_DATE"]}"
    ''')
    corr_btw_cntr = pd.DataFrame(cur.fetchall(), columns=[x[0] for x in cur.description]) \
        .pivot_table(index='KICS_CNTR_CATG_CD', columns='KICS_OTH_CNTR_CATG_CD', values='CORR_COEF', aggfunc=np.sum)

       
    # KICS_TOT_RISK_NL(TARGET) 추출
    # cur.execute(f'''
    #     SELECT CNTR_RISK, KICS_PRM_RSV_RISK
    #       FROM KICS_TOT_RISK_NL
    #      WHERE BASE_DATE="{base_date}" AND CAT_CAL_CD="2"
    # ''')
    # target = pd.Series(cur.fetchone(), index=[x[0] for x in cur.description])

    # 검증
    # assert target['CNTR_RISK'] == risk_by_cntr.sum()
    # assert np.isclose(target['KICS_PRM_RSV_RISK'], np.sqrt(risk_by_cntr@corr_btw_cntr@risk_by_cntr))    

    conn.close()