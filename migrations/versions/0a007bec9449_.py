"""Add default user

Revision ID: 0a007bec9449
Revises: 
Create Date: 2017-02-11 15:42:35.218093

"""
from alembic import op
import sqlalchemy as sa
from werkzeug.security import generate_password_hash
from app import db
from app.models.user import User


# revision identifiers, used by Alembic.
revision = '0a007bec9449'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    user = User("Demo User", "test@test.com", generate_password_hash("demo") )
    db.session.add(user)
    db.session.commit()
    pass


def downgrade():
    pass
