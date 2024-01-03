"""empty message

Revision ID: beacd0de013f
Revises: 99e55868cc5a
Create Date: 2024-01-04 01:38:08.025049

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'beacd0de013f'
down_revision: Union[str, None] = '99e55868cc5a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('like', sa.Integer(), nullable=False, server_default='0'))
    op.add_column('comment', sa.Column('unlike', sa.Integer(), nullable=False, server_default='0'))
    op.add_column('thread', sa.Column('like', sa.Integer(), nullable=False, server_default='0'))
    op.add_column('thread', sa.Column('unlike', sa.Integer(), nullable=False, server_default='0'))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('thread', 'unlike')
    op.drop_column('thread', 'like')
    op.drop_column('comment', 'unlike')
    op.drop_column('comment', 'like')
    # ### end Alembic commands ###
