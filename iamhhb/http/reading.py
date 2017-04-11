from flask import Blueprint, render_template


bp = Blueprint('reading', __name__)


@bp.route('/')
def index():
    return render_template('reading/index.html.j2')
