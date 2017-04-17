from flask import Flask, render_template, g
from iamhhb import consts, models
from iamhhb.libs import database, datastructures
from . import blog, assets, reading, wikis


def create_app():
    app = Flask(__name__,
                template_folder=consts.http['templates_folder'],
                static_folder=consts.http['static_folder'])

    app.before_request(before_request)
    app.teardown_request(teardown_request)

    @app.context_processor
    def register_context():
        return dict(
            assets=assets.env,
            title='I am HHB'
        )

    @app.route('/')
    def hello():
        return render_template('index.html.j2')

    @app.route('/about-me')
    def about_me():
        return render_template('about-me.html.j2')

    app.register_blueprint(blog.bp, url_prefix='/blogs')
    app.register_blueprint(wikis.bp, url_prefix='/wikis')
    app.register_blueprint(reading.bp, url_prefix='/reading')

    return app


def before_request():
    g.db = database.DB(consts.database['path'])
    g.repos = datastructures.NameSpace(
        blog=models.BlogRepository(g.db)
    )


def teardown_request(exc):
    g.db.close()
