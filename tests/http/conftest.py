# coding=utf-8
import json
import pytest
import urllib
import os
from iamhhb import consts
from iamhhb.http import create_app
from iamhhb.libs.datastructures import NameSpace
from iamhhb.libs.database import DB
from flask.testing import FlaskClient

application = create_app()


@pytest.fixture(scope='session')
def db():
    _db = DB(consts.database['path'])
    _db.conn.executescript(open('assets/db-schema.sql').read())
    yield _db
    _db.close()
    os.unlink(_db.filename)


@pytest.fixture
def app(db):
    application.test_client_class = TestClient
    yield application.test_client()


class TestClient(FlaskClient):

    def __init__(self, *args, **kwargs):
        super(TestClient, self).__init__(*args, **kwargs)
        self.exheaders = {}

    def open(self, path, *args, **kwargs):
        headers = kwargs.get('headers')
        kwargs['environ_overrides'] = {
            'REMOTE_ADDR': '127.0.0.1'
        }
        if not headers:
            headers = self.exheaders
        else:
            headers.update(self.exheaders)
        if 'params' in kwargs:
            assert '?' not in path
            params = kwargs.pop('params')
            params = {k: v.encode('utf8') if isinstance(v, unicode) else v
                      for k, v in params.items()}
            qs = urllib.urlencode(params)
            path = path + '?' + qs
        kwargs['headers'] = headers
        if 'json' in kwargs:
            kwargs.setdefault('content_type', 'application/json')
            kwargs.setdefault('data', json.dumps(kwargs['json']))
            del kwargs['json']
        resp = super(TestClient, self).open(path, *args, **kwargs)
        if resp.content_type == 'application/json':
            resp.json = NameSpace.recursion_fromdict(json.loads(resp.data))
        return resp

    def assert_request_status(self, status_code, method, path, **kwargs):
        resp = self.open(path, method=method, **kwargs)
        assert resp.status_code == status_code

    def assert_request_error(self, code, method, path, **kwargs):
        resp = self.open(path, method=method, **kwargs)
        assert 400 <= resp.status_code < 500
        assert resp.json.code == code
