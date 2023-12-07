"""Renaming students to scholars

Revision ID: 83cf37854acd
Revises: 791279dd0760
Create Date: 2023-12-07 22:01:11.554479

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83cf37854acd'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade():
    pass
    op.alter_column('students', 'name', new_column_name='full_name')


def downgrade():
    pass
    op.alter_column('students', 'full_name', new_column_name='name')
