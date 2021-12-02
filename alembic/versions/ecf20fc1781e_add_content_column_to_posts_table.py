"""add content column to posts table

Revision ID: ecf20fc1781e
Revises: a6b2d1249e49
Create Date: 2021-11-30 20:43:13.777764

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ecf20fc1781e'
down_revision = 'a6b2d1249e49'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
