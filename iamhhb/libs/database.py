import sqlite3


class DB(object):
    """DataBase Connection Manager"""

    def __init__(self, filename):
        self.filename = filename
        self._conn = None

    @property
    def conn(self):
        if not self._conn:
            self._conn = sqlite3.connect(self.filename)
            # about the `Row`: http://bit.ly/2obFAEW
            self._conn.row_factory = sqlite3.Row
        return self._conn

    def query(self, sql, args=(), one=False):
        result = self.conn.execute(sql, args)
        rows = result.fetchall()
        result.close()
        return (rows[0] if rows else None) if one else rows

    def insert(self, tablename, columns):
        if isinstance(columns, dict):
            cnames = columns.key()
            sql = 'INSERT INTO `{}` ({}) VALUES ({})'.format(
                tablename,
                ', '.join(map(lambda c: '`%s`' % c, cnames)),
                ', '.join(map(lambda c: '?', cnames))
            )
            args = [columns[c] for c in cnames]
            return self.conn.execute(sql, args)
        else:
            raise NotImplementedError

    def close(self):
        if self.conn:
            self.conn.close()
            self._conn = None
