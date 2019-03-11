from face import db, login_manager
from flask_login import UserMixin
from face import app, bcrypt
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    username = db.Column(db.String(60), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    image_file = db.Column(db.String(60), nullable=False, default='default.jpg')
    password = db.Column(db.String(60))
    posts = db.relationship('Post', backref='author', lazy=True)

    def __init__(self, name, username, email, password):
        self.name = name
        self.username = username
        self.email = email
        self.password = bcrypt.generate_password_hash(password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def get_reset_token(self, time_exp=1800):
        s = Serializer(app.config['SECRET_KEY'], time_exp)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    # def __repr__(self):
    #     return f"User('{self.name}','{self.username}','{self.email}','{self.image_file}','{self.password}')"

    def __repr__(self):
        return '<name - {}>'.format(self.name)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), nullable=False)
    date_pasted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # def __init__(self, title, content, user_id):
    #     self.title = title
    #     self.content = content
    #     self.user_id = user_id

    def __repr__(self):
        return 'Post<title {}'.format(self.title)
