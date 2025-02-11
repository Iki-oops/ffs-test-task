"""init

Revision ID: 3faeba03ada2
Revises: 
Create Date: 2023-07-24 19:23:06.471474

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3faeba03ada2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blocked_tokes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('jti', sa.String(length=36), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_blocked_tokes')),
    sa.UniqueConstraint('id', name=op.f('uq_blocked_tokes_id'))
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_users')),
    sa.UniqueConstraint('username', name=op.f('uq_users_username'))
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('blocked_tokes')
    # ### end Alembic commands ###
