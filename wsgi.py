# -*- coding: utf-8 -*-
from werkzeug.contrib.fixers import ProxyFix
from iamhhb.http import create_app


app = create_app()

# Proxy fix
app.wsgi_app = ProxyFix(app.wsgi_app)


if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)
    # from werkzeug.serving import run_simple
    # run_simple('0.0.0.0', 5000, app, use_reloader=True, use_debugger=True)
