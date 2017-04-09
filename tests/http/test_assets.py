def test_assets_js(app):
    assert b'This is a index page' in app.get('/').data
