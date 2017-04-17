import pytest
from iamhhb.models import BlogRepository, Blog


@pytest.fixture
def blog_repo(db):
    return BlogRepository(db)


def test_repo(blog_repo):
    b1 = Blog(
        slogan='test-article-1',
        title='测试文章',
        sub_title='这是一个副标题',
        content='这里是文章的内容'
    )
    blog_repo.save(b1)
    assert b1.id is not None
    b1.content = u'New Content'
    blog_repo.save(b1)
    b2 = blog_repo.get(b1.id)
    assert b2.content == u'New Content'
