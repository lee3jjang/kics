import os
import sqlite3

def test_sample():
    conn = sqlite3.connect(os.environ['DATABASE_NAME'])
    cur = conn.cursor()
    cur.execute('SELECT * FROM KICS_RISK_COEF_NL')
    res = cur.fetchall()
    conn.close()
    assert len(res) == 1