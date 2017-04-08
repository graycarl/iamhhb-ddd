from flask import Flask, render_template
from iamhhb import consts


def create_app():
    app = Flask(__name__,
                template_folder=consts.http['templates_folder'],
                static_folder=consts.http['static_folder'])

    @app.route('/')
    def hello():
        return render_template('home/index.html.j2')

    return app
