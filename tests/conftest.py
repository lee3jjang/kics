import os
import pytest
import tempfile

from kics.tables.coefficient import Coefficient

@pytest.fixture(autouse=True)
def database():
    _, file_name = tempfile.mkstemp()
    os.environ['DATABASE_NAME'] = 'kics.db'
    Coefficient.create_table()
    yield
    os.unlink(file_name)

    