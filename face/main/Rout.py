from flask import render_template, Blueprint
from face.Models import Post
from flask_login import login_required


main = Blueprint('main', __name__)


@main.route('/', methods=['POST', 'GET'])
@login_required
def home():
    posts = Post.query.order_by(Post.date_pasted.desc())
    return render_template('Home.html', title='Home', posts=posts)
