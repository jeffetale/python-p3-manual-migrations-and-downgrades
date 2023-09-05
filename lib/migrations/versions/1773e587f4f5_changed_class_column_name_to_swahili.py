"""changed class column name to swahili

Revision ID: 1773e587f4f5
Revises: fabab2fa9a64
Create Date: 2023-09-05 11:38:22.405997

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1773e587f4f5'
down_revision = 'fabab2fa9a64'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('grade', 'darasa')


def downgrade() -> None:
    op.alter_column('darasa', 'grade')
