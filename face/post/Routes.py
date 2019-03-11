from face import app, db
from flask import flash, redirect, render_template, url_for, abort, request,Blueprint
from flask_login import current_user
from face.Models import Post
from face.post.Forms import NewPostForm

posts = Blueprint('posts', __name__)

@posts.route('/post/new', methods=['POST', 'GET'])
def new_post():
    form = NewPostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash(f'Post Successfully', 'success')
        return redirect(url_for('main.home'))
    return render_template('CreateNewPost.html', legend='New Post', share='Share Post', form=form)


@posts.route('/post/<int:post_id>', methods=['POST', 'GET'])
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('Post.html', title='Post', post=post)


@posts.route('/post/<int:post_id>/update', methods=['POST', 'GET'])
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(404)
    form = NewPostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash(f'Update Successfully', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('CreateNewPost.html', legend='Update Post', form=form, post=post)



@posts.route('/post/<int:post_id>/delete', methods=['POST', 'GET'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(404)
    db.session.delete(post)
    db.session.commit()
    flash(f'Delete Successfully', 'success')
    return redirect(url_for('main.home'))
