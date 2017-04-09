# -*- coding: utf-8 -*-
class NameSpace(dict):
    """用点号访问字典内容"""

    @classmethod
    def recursion_fromdict(cls, d):
        def wrapns(item):
            if isinstance(item, dict):
                item = cls(item)
                for k in item:
                    item[k] = wrapns(item[k])
            elif isinstance(item, (list, tuple)):
                item = map(wrapns, item)
            return item
        return wrapns(d)

    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name)

    def __setattr__(self, name, value):
        self[name] = value


class ImmutableNameSpace(NameSpace):

    def __setattr__(self, name, value):
        raise RuntimeError("Can not modify a ImmutableNameSpace")
