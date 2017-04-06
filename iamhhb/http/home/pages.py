from flask import Blueprint, render_template


bp = Blueprint('pages', __name__)


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/about/me')
def about_me():
    return render_template('about-me.html')


@bp.route('/about/site')
def about_site():
    return render_template('about-site.html')
