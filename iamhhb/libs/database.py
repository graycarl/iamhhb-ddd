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

    def query_by_id(self, tablename, id):
        sql = 'SELECT * FROM `{}` WHERE id = ?'.format(tablename)
        return self.query(sql, (id,), one=True)

    def insert(self, tablename, columns):
        cur = self.conn.cursor()
        if isinstance(columns, dict):
            cnames = columns.keys()
            sql = 'INSERT INTO `{}` ({}) VALUES ({})'.format(
                tablename,
                ', '.join(map(lambda c: '`%s`' % c, cnames)),
                ', '.join(map(lambda c: '?', cnames))
            )
            args = [columns[c] for c in cnames]
            cur.execute(sql, args)
            return cur.lastrowid
        else:
            raise NotImplementedError

    def update_by_id(self, tablename, id, columns):
        if isinstance(columns, dict):
            cnames = columns.keys()
            sql = 'UPDATE `{}` SET {} where id=?'.format(
                tablename,
                ', '.join(map(lambda c: '`%s`=?' % c, cnames))
            )
            args = [columns[c] for c in cnames] + [id]
            return self.conn.execute(sql, args)
        else:
            raise NotImplementedError

    def commit(self):
        self.conn.commit()

    def rollback(self):
        self.conn.rollback()

    def close(self):
        if self.conn:
            self.conn.close()
            self._conn = None
