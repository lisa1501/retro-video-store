"""adds customer  model

Revision ID: 787e2b5d45f2
Revises: e28d3e300687
Create Date: 2021-05-18 14:00:53.467749

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '787e2b5d45f2'
down_revision = 'e28d3e300687'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customer', sa.Column('videos_checked_out_count', sa.Integer(), nullable=True, default_value=0))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('customer', 'videos_checked_out_count')
    # ### end Alembic commands ###
