import os
import pytest
import tempfile

from kics.tables.coefficient import Coefficient
from kics.tables.correlation import Correlation
from kics.tables.exposure import Exposure
from kics.tables.mapping import Mapping
from kics.tables.risk import Risk

@pytest.fixture(autouse=True)
def database():
    # _, file_name = tempfile.mkstemp()
    file_name = 'kics.db'
    os.environ['DATABASE_NAME'] = file_name
    Coefficient.create_table(file_name)
    Correlation.create_table(file_name)
    Exposure.create_table(file_name)
    Mapping.create_table(file_name)
    Risk.create_table(file_name)
    yield
    # os.unlink(file_name)

    