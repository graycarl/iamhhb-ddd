def test_add_blog(app):
    assert '创建文章'.encode('utf-8') in app.get('/blogs/new').data

    resp = app.post('/blogs/new', data=dict(
        title='一个测试文章',
        slogan='a-testing-blog-1',
        sub_title='ajajaja',
        content='ajajajajja'
    ))
    assert resp.status_code == 302
