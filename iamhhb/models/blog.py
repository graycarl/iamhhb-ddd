import arrow
from .base import Entity, Repository


# TODO Features: Custom Style / Commentable / Fixtop / Status
class Blog(Entity):

    def __init__(self, title, sub_title, content,
                 content_type='markdown', created_at=None, updated_at=None):
        self.id = None
        self.title = title
        self.sub_title = sub_title
        self.content = content
        self.content_type = content_type
        self.created_at = created_at
        self.updated_at = updated_at


class BlogRepository(Repository):
    tablename = 'blog'

    def save(self, blog):
        now = arrow.now().to('utc').datetime
        if blog.id is None:
            columns = self.to_columns(
                blog, 'title', 'sub_title', 'content', 'content_type')
            columns['created_at'] = columns['updated_at'] = now
            id = self.db.insert(self.tablename, columns)
            blog.id = id
        else:
            columns = self.to_columns(
                blog, 'title', 'sub_title', 'content', 'content_type')
            columns['updated_at'] = now
            self.db.update_by_id(self.tablename, blog.id, columns)
        return blog

    def get(self, id):
        row = self.db.query_by_id(self.tablename, id)
        if not row:
            return None
        return self.reconstruct(row)

    def gets(self, limit, offset=0, order='-created_at', **filters):
        if filters:
            raise NotImplementedError
        sql = 'SELECT * FROM {} ORDER BY {} LIMIT ? OFFSET ?'.format(
            self.tablename, self.parse_order(order)
        )
        rows = self.db.query(sql, (limit, offset))
        total = self.db.query(
            'SELECT count(1) FROM {}'.format(self.tablename), one=True)[0]
        return map(self.reconstruct, rows), total

    def reconstruct(self, row):
        blog = Blog(
            title=row['title'],
            sub_title=row['sub_title'],
            content=row['content'],
            content_type=row['content_type'],
            created_at=arrow.get(row['created_at'], tzinfo='utc').to('local'),
            updated_at=arrow.get(row['updated_at'], tzinfo='utc').to('local')
        )
        blog.id = row['id']
        return blog
