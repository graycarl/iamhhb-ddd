import pytest
import tempfile
from iamhhb.libs.database import DB


@pytest.fixture(scope='session')
def db():
    with tempfile.NamedTemporaryFile() as f:
        db = DB(f.name)
        # create all the tables
        db.conn.executescript(open('assets/db-schema.sql').read())
        yield db
