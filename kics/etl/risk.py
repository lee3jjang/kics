import os
import math
import sqlite3
import numpy as np
import pandas as pd
from datetime import datetime


####################### 프로그램 목록 #######################
# KAKD0008LM : 국가그룹 및 보장단위별 요구자본 산출
# KAKD9001LM : 국가그룹 및 보장그룹별 요구자본 산출 (신규)
# KAKD0002LM : 국가그룹별 요구자본 산출
# KAJC0011LM : 보험가격준비금위험액 및 일반손해보험위험액 산출
############################################################


def KAKD0008LM(base_date: str) -> pd.DataFrame:
    # 최종수정일자 : 2021.03.16
    ########################### KAKD0008LM ###########################
    # DESCRIPTION:
    #   국가그룹 및 보장단위별 요구자본 산출
    # SOURCE:
    #   KICS_CORR_PREM_RSV_NL
    #   KICS_PRM_RSV_EXPO
    #   KICS_RISK_COEF_NL
    #   KICS_BOZ_GRP_MAP_NL (삭제)
    # TARGET: 
    #   KICS_BOZ_CD_RISK_NL
    ##################################################################
    
    base_date0 = datetime.strptime(base_date, '%Y%m%d').strftime('%Y-%m-%d 00:00:00')
    
    conn = sqlite3.connect(os.environ['DATABASE_NAME'])
    cur = conn.cursor()

    # KICS_PRM_RSV_EXPO_NL 추출

    # KICS_RISK_COEF_NL 추출
    cur.execute(f'''
        SELECT BOZ_CD, APLY_STRT_DATE, APLY_END_DATE, PREM_RISK_COEF, RSV_RISK_COEF
          FROM KICS_RISK_COEF_NL
         WHERE APLY_STRT_DATE<=?
           AND APLY_END_DATE>?
    ''', (base_date, base_date))
    risk_coef = pd.DataFrame(cur.fetchall(), columns=[x[0] for x in cur.description]) \
            [['BOZ_CD', 'PREM_RISK_COEF', 'RSV_RISK_COEF']] \
            .sort_values(by='BOZ_CD')

    # KICS_CORR_PREM_RSV_NL 추출
    cur.execute(f'''
        SELECT PREM_RSV_CD, OTH_PREM_RSV_CD, CORR_COEF
          FROM KICS_CORR_PREM_RSV_NL
         WHERE APLY_STRT_DATE<=?
           AND APLY_END_DATE>?
    ''', (base_date, base_date))
    corr_prem_rsv = pd.DataFrame(cur.fetchall(), columns=[x[0] for x in cur.description]) \
        .pivot_table(index='PREM_RSV_CD', columns='OTH_PREM_RSV_CD', values='CORR_COEF', aggfunc=np.sum)

    conn.close()

    # return kics_boz_cd_risk_nl


def KAKD9001LM(base_date: str) -> pd.DataFrame:
    # 신규
    # 최종수정일자 : 2021.03.16
    ########################### KAKD9001LM ###########################
    # DESCRIPTION:
    #   국가그룹 및 보장그룹별 요구자본 산출
    # SOURCE:
    #   KICS_BOZ_CD_RISK_NL (신규)
    #   KICS_CORR_BOZ_INR_NL (신규)
    #   KICS_BOZ_GRP_MAP_NL (신규)
    # TARGET: 
    #   KICS_BOZ_GRP_RISK_NL
    ##################################################################
    pass


def KAKD0002LM(base_date: str) -> pd.DataFrame:
    # 최종수정일자 : 2021.03.16
    ########################### KAKD0002LM ###########################
    # DESCRIPTION:
    #   국가그룹별 요구자본 산출
    # SOURCE:
    #   KICS_BOZ_GRP_RISK_NL
    #   KICS_CORR_BOZ_NL
    # TARGET: 
    #   KICS_CNTR_RISK_NL
    ##################################################################
    pass


def KAJC0011LM(base_date: str) -> pd.DataFrame:
    # 최종수정일자 : 2021.03.16
    ########################### KAJC0011LM ###########################
    # DESCRIPTION:
    #   보험가격준비금위험액 및 일반손해보험위험액 산출
    # SOURCE:
    #   KICS_CNTR_RISK_NL
    #   KICS_CORR_CNTR_NL
    # TARGET: 
    #   KICS_TOT_RISK_NL
    # WARNING:
    #   TARGET 완성을 위해선 대재해위험액 산출관련 SOURCE와 로직이 더 필요
    # TEST:
    #   TARGET 중 CNTR_RISK, KICS_PRM_RSV_RISK 컬럼은 테스트 통과
    ##################################################################   
    
    base_date0 = datetime.strptime(base_date, '%Y%m%d').strftime('%Y-%m-%d 00:00:00')
    
    conn = sqlite3.connect(os.environ['DATABASE_NAME'])
    cur = conn.cursor()

    # KICS_CNTR_RISK_NL 추출
    cur.execute(f'SELECT KICS_CNTR_CATG_CD, CNTR_RISK FROM KICS_CNTR_RISK_NL WHERE BASE_DATE=?', (base_date0,))
    risk_by_cntr = pd.DataFrame(cur.fetchall(), columns=[x[0] for x in cur.description]) \
        .sort_values(by='KICS_CNTR_CATG_CD') \
        .set_index('KICS_CNTR_CATG_CD')['CNTR_RISK']

    # KICS_CORR_CNTR_NL 추출
    cur.execute(f'''
        SELECT KICS_CNTR_CATG_CD, KICS_OTH_CNTR_CATG_CD, CORR_COEF
          FROM KICS_CORR_CNTR_NL
          WHERE APLY_STRT_DATE<=?
            AND APLY_END_DATE>?
    ''', (base_date, base_date))
    corr_btw_cntr = pd.DataFrame(cur.fetchall(), columns=[x[0] for x in cur.description]) \
        .pivot_table(index='KICS_CNTR_CATG_CD', columns='KICS_OTH_CNTR_CATG_CD', values='CORR_COEF', aggfunc=np.sum)

    # KICS_TOT_RISK_NL 생성
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    kics_tot_risk_nl = pd.DataFrame(
        [[base_date, '2', risk_by_cntr.sum(),np.sqrt(risk_by_cntr@corr_btw_cntr@risk_by_cntr), None, None, None, None, 'lee3jjang', now]],
        columns=['BASE_DATE', 'CAT_CAL_CD', 'CNTR_RISK', 'KICS_PRM_RSV_RISK', 'KICS_IND_CAT_RISK', 'KICS_CAT_RISK', 'DVS_EFCT', 'KICS_NON_LIFE_RISK', 'LAST_MODIFIED_BY', 'LAST_UPDATE_DATE']
    )

    conn.close()

    return kics_tot_risk_nl

    