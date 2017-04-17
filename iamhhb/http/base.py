import functools


def page_title(bp, title):

    def decorator(f):
        @functools.wraps(f)
        def _(*args, **kwargs):
            return f(*args, **kwargs)
        return _

    return decorator
