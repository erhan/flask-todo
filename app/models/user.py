from app import db
from app.models.default import Base


class User(Base):
    '''User modeli.'''
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    full_name = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(120), nullable=False)

    todos = db.relationship('Todo', backref='user', lazy='dynamic')

    def __init__(self, full_name, email, password):
        self.full_name = full_name
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.id)
