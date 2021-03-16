import os
import sys
import sqlite3
import subprocess
from pathlib import Path


class KicsMain():
    
    def __init__(self, file_name, base_date):
        os.environ['BASE_DATE'] = base_date
        os.environ['DATABASE_NAME'] = file_name

    def run(self):
        self._run_etl()

    def _run_etl(self):
        call_etl = lambda program_name: subprocess.call(f'python {str(Path("kics/etl"))}/{program_name}.py', shell=True)

        call_etl('KAJC0011LM')


if __name__ == '__main__':
    kics_main = KicsMain(file_name='kics.db', base_date='20191231')
    kics_main.run()