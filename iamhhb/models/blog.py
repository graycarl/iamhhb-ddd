import arrow
from .base import Entity, Repository


# TODO Features: Custom Style / Commentable / Fixtop / Status
class Blog(Entity):

    def __init__(self, title, sub_title, content,
                 content_type='markdown', created_at=None):
        self.title = title
        self.sub_title = sub_title
        self.content = content
        self.content_type = content_type
        self.created_at = created_at or arrow.now()


class BlogRepository(Repository):

    def add(self, blog):
        pass

    def get(self, id):
        pass

    def gets(self, **kwargs):
        pass
