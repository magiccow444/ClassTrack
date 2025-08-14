"""init1 assignments lol

Revision ID: e37999fbf77a
Revises: 9efff5e9c49f
Create Date: 2025-08-13 19:03:55.480135

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'e37999fbf77a'
down_revision: Union[str, Sequence[str], None] = '9efff5e9c49f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'assignments',
        sa.Column('id', sa.BigInteger, primary_key=True),
        sa.Column('course', sa.Text, nullable=False),
        sa.Column('title', sa.Text, nullable=False),
        sa.Column('type', sa.Text),
        sa.Column('due_at_utc', sa.TIMESTAMP(timezone=True)),
        sa.Column('url', sa.Text),
        sa.Column('hash', sa.Text, nullable=False, unique=True),
        sa.Column('status', sa.Text, server_default='pending'),
        sa.Column('last_seen', sa.TIMESTAMP(timezone=True), server_default=sa.text('NOW()')),
        sa.Column('event_id', sa.Text, unique=True),
    )
    op.create_index('idx_assignments_due', 'assignments', ['due_at_utc'])
    op.create_index('idx_assignments_course', 'assignments', ['course'])

def downgrade():
    op.drop_index('idx_assignments_course', table_name='assignments')
    op.drop_index('idx_assignments_due', table_name='assignments')
    op.drop_table('assignments')