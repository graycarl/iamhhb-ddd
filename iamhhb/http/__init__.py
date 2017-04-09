from flask import Flask, render_template
from iamhhb import consts
from . import blog, assets


def create_app():
    app = Flask(__name__,
                template_folder=consts.http['templates_folder'],
                static_folder=consts.http['static_folder'])

    @app.context_processor
    def register_context():
        return dict(
            assets=assets.env,
            title='I am HHB'
        )

    @app.route('/')
    def hello():
        return render_template('index.html.j2')

    app.register_blueprint(blog.bp, url_prefix='/blogs')

    return app
