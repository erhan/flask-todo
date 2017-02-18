from app import db
from app.models.default import Base


class Todo(Base):
    '''Todo modeli.'''
    description = db.Column(db.String(500))
    status = db.Column(db.SmallInteger, default=0)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, description, status, owner_id):
        self.description = description
        self.status = status
        self.owner_id = owner_id

    def __repr__(self):
        return '<Todo %r>' % (self.id)