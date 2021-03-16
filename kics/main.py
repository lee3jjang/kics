import os
import sys
import sqlite3

class KicsMain():
    
    def __init__(self, file_name, base_date):
        os.environ['BASE_DATE'] = base_date
        os.environ['DATABASE_NAME'] = sys.argv[0]

    def run(self):
        pass

if __name__ == '__main__':
    kics_main = KicsMain(file_name='kics.db', base_date='20191231')
    kics_main.run()