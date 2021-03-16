import os
import sys
import sqlite3
import subprocess
from pathlib import Path
from kics.etl.risk import *


class KicsMain():
    
    def __init__(self, file_name):
        os.environ['DATABASE_NAME'] = file_name

    def run(self, base_date):
        KAJC0011LM(base_date)


if __name__ == '__main__':
    kics_main = KicsMain(file_name='kics.db')
    kics_main.run(base_date='20181231')