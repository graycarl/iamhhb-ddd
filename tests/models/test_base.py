import mock
from iamhhb.models.base import Repository


def test_repo_base():
    r = Repository(None)
    # test to columns
    obj = mock.Mock(key='thekey', vv=u'thename')
    columns = r.to_columns(obj, 'key', 'vv')
    assert columns == dict(key='thekey', vv=u'thename')

    # test parse_order
    assert r.parse_order('-created_at') == '`created_at` DESC'
    assert r.parse_order('created_at') == '`created_at` ASC'
    assert r.parse_order('+created_at') == '`created_at` ASC'


def test_repo_save_and_get(db):
    from iamhhb.models import Blog, BlogRepository
    blog_repo = BlogRepository(db)
    b1 = Blog(
        title='测试文章',
        slogan='test-article',
        sub_title='这是一个副标题',
        content='这里是文章的内容'
    )
    b2 = blog_repo.save(b1)
    assert b2 is b1

    b3 = blog_repo.get(b2.id)
    for key in ('title', 'sub_title', 'content', 'content_type'):
        assert getattr(b3, key) == getattr(b2, key)
    assert b3.created_at == b3.updated_at
    assert b3.created_at is not None

    b3.content = u'New Content'
    blog_repo.save(b3)
    b4 = blog_repo.get(b3.id)
    assert b4.content == u'New Content'

    blogs, total = blog_repo.gets(limit=20)
    blogs = list(blogs)
    assert len(blogs) == total == 1
    assert blogs[0].id == b2.id
    blog_repo.save(Blog(
        slogan='test-new-title',
        title='New Title',
        sub_title='aaaa',
        content='bbb'
    ))
    blogs, total = blog_repo.gets(limit=20, order='created_at')
    assert total == 2
    assert [b.id for b in blogs] == [1, 2]
    blogs, total = blog_repo.gets(limit=20, order='-created_at')
    assert total == 2
    assert [b.id for b in blogs] == [2, 1]
