"""Add mock user

Revision ID: b51c5907641b
Revises: d6f7640dd0c4
Create Date: 2024-03-15 16:07:11.995122

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b51c5907641b'
down_revision = 'd6f7640dd0c4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute('INSERT INTO "user" (id, cash_balance) VALUES (1, 1000)')
    pass


def downgrade() -> None:
    pass
