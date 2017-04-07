from .base import Entity, Repository


# TODO: Add relationship between Pages
class WikiPage(Entity):

    def __init__(self, id, title, content, content_type):
        self.id = id
        self.title = title
        self.content = content
        self.content_type = content_type


class WikiPageRepository(Repository):

    def get(self, id):
        pass

    def get_index(self):
        pass
