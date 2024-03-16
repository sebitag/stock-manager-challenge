"""Add mock user

Revision ID: 3e7ba2cc7202
Revises: bad0210abdb6
Create Date: 2024-03-16 18:37:42.397973

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e7ba2cc7202'
down_revision = 'bad0210abdb6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute('INSERT INTO "user" (id, cash_balance) VALUES (1, 1000)')
    pass


def downgrade() -> None:
    pass
