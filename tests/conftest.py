import os
import pdb
import pytest
import sqlite3
import tempfile
import pandas as pd
from pathlib import Path

from kics.tables.coefficient import Coefficient
from kics.tables.correlation import Correlation
from kics.tables.exposure import Exposure
from kics.tables.mapping import Mapping
from kics.tables.risk import Risk


@pytest.fixture(autouse=True)
def database():
    # _, file_name = tempfile.mkstemp()
    file_name = 'kics.db'
    try:
        os.unlink(file_name)
    except:
        pass
    os.environ['DATABASE_NAME'] = file_name
    Coefficient.create_table(file_name)
    Correlation.create_table(file_name)
    Exposure.create_table(file_name)
    Mapping.create_table(file_name)
    Risk.create_table(file_name)
    yield
    # os.unlink(file_name)


@pytest.fixture(autouse=True)
def insert_table_from_sample():
    conn = sqlite3.connect(os.environ['DATABASE_NAME'])
    path_sample_data = Path('tests/sample_data')

    # correlation
    pd.read_excel(path_sample_data / 'KICS_CORR_BOZ_NL.xlsx').to_sql('KICS_CORR_BOZ_NL', conn, index=False, if_exists='append')
    pd.read_excel(path_sample_data / 'KICS_CORR_CNTR_NL.xlsx').to_sql('KICS_CORR_CNTR_NL', conn, index=False, if_exists='append')
    pd.read_excel(path_sample_data / 'KICS_CORR_PREM_RSV_NL.xlsx').to_sql('KICS_CORR_PREM_RSV_NL', conn, index=False, if_exists='append')
    pd.read_excel(path_sample_data / 'KICS_CORR_SCR_NL.xlsx').to_sql('KICS_CORR_SCR_NL', conn, index=False, if_exists='append')

    # mapping
    kics_cntr_grp_nl = pd.read_excel(path_sample_data / 'KICS_CNTR_GRP_NL.xlsx')
    kics_cntr_grp_nl.to_sql('KICS_CNTR_GRP_NL', conn, index=False, if_exists='append')
    pd.read_excel(path_sample_data / 'KICS_BOZ_GRP_MAP_NL.xlsx') \
        .query('BOZ_CD != "A100"') \
        [['BOZ_CD', 'BOZ_CATG_CD']] \
        .to_sql('KICS_BOZ_GRP_MAP_NL', conn, index=False, if_exists='append')

    # coefficient
    pd.read_excel(path_sample_data / 'KICS_RISK_COEF_NL.xlsx') \
        .merge(kics_cntr_grp_nl[['CNTR_CATG_CD', 'KICS_CNTR_CATG_CD']], on='CNTR_CATG_CD', how='left') \
        .drop(['OVS_COVR_CD', 'CNTR_CATG_CD'], axis=1) \
        .query('BOZ_CD != "A100"') \
        .to_sql('KICS_RISK_COEF_NL', conn, index=False, if_exists='append')

    # risk
    pd.read_excel(path_sample_data / 'KICS_BOZ_CD_RISK_NL.xlsx') \
        .merge(kics_cntr_grp_nl[['CNTR_CATG_CD', 'KICS_CNTR_CATG_CD']], on='CNTR_CATG_CD', how='left') \
        .query('RRNR_DVCD != "01"') \
        .groupby(['BASE_DATE', 'KICS_CNTR_CATG_CD', 'BOZ_CD'])[['RETAIN_LAPS_PRM', 'RETAIN_RSV_LIAB', 'PREM_RISK_AMT', 'RSV_RISK_AMT']].sum() \
        .eval('BOZ_CD_RISK = sqrt(PREM_RISK_AMT**2 + RSV_RISK_AMT**2 + 2*0.25*PREM_RISK_AMT*RSV_RISK_AMT)') \
        .assign(LAST_MODIFIED_BY = lambda x: None) \
        .assign(LAST_UPDATE_DATE = lambda x: None) \
        .to_sql('KICS_BOZ_CD_RISK_NL', conn, index=False, if_exists='append')
    pd.read_excel(path_sample_data / 'KICS_CNTR_RISK_NL.xlsx') \
        .drop('BOZ_CD_RISK', axis=1) \
        .to_sql('KICS_CNTR_RISK_NL', conn, index=False, if_exists='append')
    pd.read_excel(path_sample_data / 'KICS_TOT_RISK_NL.xlsx').to_sql('KICS_TOT_RISK_NL', conn, index=False, if_exists='append')

    conn.close()