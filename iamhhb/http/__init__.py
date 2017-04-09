from flask import Flask, render_template
from iamhhb import consts
from . import blog


def create_app():
    app = Flask(__name__,
                template_folder=consts.http['templates_folder'],
                static_folder=consts.http['static_folder'])

    @app.route('/')
    def hello():
        return render_template('index.html.j2')

    app.register_blueprint(blog.bp, url_prefix='/blogs')

    return app
