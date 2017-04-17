import pytest
from iamhhb.models import BlogRepository, Blog


@pytest.fixture
def blog_repo(db):
    return BlogRepository(db)


def test_add_blog(app):
    assert '创建文章'.encode('utf-8') in app.get('/blogs/new').data

    resp = app.post('/blogs/new', data=dict(
        title='一个测试文章',
        slogan='a-testing-blog-1',
        sub_title='ajajaja',
        content='ajajajajja'
    ))
    assert resp.status_code == 302


def test_edit_blog(app, blog_repo, db):
    b1 = Blog(
        slogan='test-article-1',
        title='TTTT',
        sub_title='这是一个副标题',
        content='这里是文章的内容'
    )
    blog_repo.save(b1)
    db.commit()
    assert blog_repo.get(b1.id).title == 'TTTT'

    resp = app.post('/blogs/%s/edit' % b1.id, data=dict(
        title='AAAA',
        sub_title='这是一个副标题',
        content='这里是文章的内容'
    ))
    assert resp.status_code == 302
    assert blog_repo.get(b1.id).title == 'AAAA'
