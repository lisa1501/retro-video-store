"""adds customer  model

Revision ID: d177b34e3140
Revises: f5bec0e03b05
Create Date: 2021-05-18 16:59:54.620196

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd177b34e3140'
down_revision = 'f5bec0e03b05'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('customer', 'videos_checked_out_count')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customer', sa.Column('videos_checked_out_count', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###