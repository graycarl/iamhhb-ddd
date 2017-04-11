from flask import Blueprint, render_template


bp = Blueprint('wikis', __name__)


@bp.route('/')
def index():
    return render_template('wikis/index.html.j2')
