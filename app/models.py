from ..app import db


class User(db.Model):
    """"""
    __tablename__= 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column("username",db.String, unique=True, nullable=False)
    email = db.Column("email",db.String, unique=True, nullable=False)
    password = db.String('password', db.String, nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username
