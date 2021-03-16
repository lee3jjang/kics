import os
import pdb
import sqlite3
import pandas as pd
from pathlib import Path

def test_select_table():
    conn = sqlite3.connect(os.environ['DATABASE_NAME'])
    cur = conn.cursor()
    cur.execute('SELECT * FROM KICS_RISK_COEF_NL')
    res = cur.fetchall()
    conn.close()
    assert len(res) == 0

def test_insert_table_from_pandas():
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
    # pd.read_excel(path_sample_data / 'KICS_BOZ_CD_RISK_NL.xlsx').to_sql('KICS_BOZ_CD_RISK_NL', conn, index=False, if_exists='append')
    # pd.read_excel(path_sample_data / 'KICS_CNTR_RISK_NL.xlsx').to_sql('KICS_CNTR_RISK_NL', conn, index=False, if_exists='append')
    # pd.read_excel(path_sample_data / 'KICS_TOT_RISK_NL.xlsx').to_sql('KICS_TOT_RISK_NL', conn, index=False, if_exists='append')

    conn.close()

