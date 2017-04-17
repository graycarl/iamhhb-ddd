from flask import Blueprint, render_template, g

bp = Blueprint('blogs', __name__)


@bp.route('')
def index():
    # TODO: paginate
    blogs, _ = g.repos.blog.gets(100)
    return render_template(
        'blogs/index.html.j2',
        title='文章列表',
        blogs=blogs
    )


@bp.route('/new')
def new():
    return render_template(
        'blogs/new.html.j2',
        title='创建文章'
    )


@bp.route('/<id>')
def item(id):
    blog = g.repos.blog.get(id)
    return render_template(
        'blogs/show.html.j2',
        title=blog.title,
    )


@bp.route('/<id>/edit')
def edit(id):
    blog = g.repos.blog.get(id)
    return render_template(
        'blogs/edit.html.j2',
        title='修改文章',
        blog=blog
    )
