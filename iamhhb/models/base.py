class Entity(object):
    pass


class Factory(object):
    pass


class Service(object):
    pass


class Repository(object):

    def __init__(self, db):
        self.db = db

    def to_columns(self, obj, *keys):
        return {k: getattr(obj, k) for k in keys}

    def parse_order(self, order):
        if order.startswith('-'):
            suffix = 'DESC'
        else:
            suffix = 'ASC'
        return '`{}` {}'.format(order.strip('-+'), suffix)
