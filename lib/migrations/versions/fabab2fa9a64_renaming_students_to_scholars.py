"""Renaming students to scholars

Revision ID: fabab2fa9a64
Revises: 791279dd0760
Create Date: 2023-09-05 11:27:13.691620

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fabab2fa9a64'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
