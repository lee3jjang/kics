import os
from pathlib import Path
import sqlite3
import pandas as pd

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
    kics_corr_boz_nl = pd.read_excel(path_sample_data / 'KICS_CORR_BOZ_NL.xlsx')
    kics_corr_boz_nl.to_sql('KICS_CORR_BOZ_NL', conn, index=False, if_exists='append')
    conn.close()

