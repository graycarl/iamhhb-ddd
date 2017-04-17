def test_assets_js(app):
    assert b'<pre>' in app.get('/').data
