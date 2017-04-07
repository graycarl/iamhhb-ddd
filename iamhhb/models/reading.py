from .base import Entity, Repository


class ReadingNote(Entity):

    def __init__(self, book, content, content_type='markdown'):
        self.book = book
        self.content = content
        self.content_type = content_type


class Book(Entity):

    def __init__(self, isbn, title, sub_title, cover):
        self.isbn = isbn
        self.title = title
        self.sub_title = sub_title
        self.cover = cover


class ReadingNoteRepository(Repository):

    def get(self, id):
        pass

    def gets(self):
        pass
