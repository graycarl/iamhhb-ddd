# -*- coding: utf-8 -*-
from werkzeug.serving import run_simple
from werkzeug.contrib.fixers import ProxyFix
from iamhhb.http import create_app


app = create_app()

# Proxy fix
app = ProxyFix(app)


if __name__ == '__main__':
    run_simple('0.0.0.0', 5000, app, use_reloader=True, use_debugger=True)
