from flask import Blueprint, render_template, g, redirect, url_for, request
from flask import abort
from iamhhb import models

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


@bp.route('/new', methods=['get', 'post'])
def new():
    if request.method == 'POST':
        b = models.Blog(
            slogan=request.form['slogan'],
            title=request.form['title'],
            sub_title=request.form['sub_title'],
            content_type='markdown',
            content=request.form['content']
        )
        g.repos.blog.save(b)
        g.db.commit()
        return redirect(url_for('.item', id=b.id))
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
        blog=blog
    )


@bp.route('/<id>/edit', methods=['get', 'post'])
def edit(id):
    blog = g.repos.blog.get(id)
    if not blog:
        abort(404)
    if request.method == 'POST':
        for key in ('title', 'sub_title', 'content'):
            setattr(blog, key, request.form[key])
        g.repos.blog.save(blog)
        g.db.commit()
        return redirect(url_for('.item', id=id))
    return render_template(
        'blogs/edit.html.j2',
        title='修改文章',
        blog=blog
    )
