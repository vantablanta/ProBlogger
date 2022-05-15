from . import db, login_manager
from flask_login import UserMixin, current_user
from werkzeug.security import generate_password_hash, check_password_hash

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    secure_password = db.Column(db.String, nullable=False)
    blog_id=db.relationship('Blogs', backref='user')
    role=db.relationship('Roles', backref='user')

    @property
    def password(self):
        raise AttributeError("You can't read the password")

    @password.setter
    def password(self,password):
        self.secure_password=generate_password_hash(password)   

    def verify_password(self,password):
        return check_password_hash(self.secure_password,password) 
    
    def __repr__(self):
        return f"User('{self.name}')"

class Roles(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    role_id= db.Column(db.String)
    user_id=db.Column(db.Integer, db.ForeignKey('users.id'))


class Blogs(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key=True)
    heading = db.Column(db.String, nullable=False)
    body = db.Column(db.String, nullable=False)
    user_id=db.Column(db.String, db.ForeignKey('users.id'))
   