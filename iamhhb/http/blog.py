from flask import Blueprint, render_template

bp = Blueprint('blogs', __name__)


@bp.route('')
def index():
    return render_template('blogs/index.html.j2')
