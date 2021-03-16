import os
import sqlite3
from kics.etl.risk import *


class KicsMain():
    
    def __init__(self, file_name):
        os.environ['DATABASE_NAME'] = file_name

    def run(self, base_date):
        kics_boz_cd_risk_nl = KAKD0008LM(base_date)
        kics_tot_risk_nl = KAJC0011LM(base_date)


if __name__ == '__main__':
    kics_main = KicsMain(file_name='kics.db')
    kics_main.run(base_date='20181231')
    