"""adds customer  model

Revision ID: cd9fd5136e7e
Revises: ab1e57abf110
Create Date: 2021-05-18 13:40:57.749104

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'cd9fd5136e7e'
down_revision = 'ab1e57abf110'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customer', sa.Column('name', sa.String(), nullable=True))
    op.add_column('customer', sa.Column('phone', sa.String(), nullable=True))
    op.add_column('customer', sa.Column('postal_code', sa.String(), nullable=True))
    op.add_column('customer', sa.Column('registered_at', sa.DateTime(), nullable=True))
    op.drop_column('customer', 'customer_postal_code')
    op.drop_column('customer', 'customer_phone')
    op.drop_column('customer', 'customer_registered_at')
    op.drop_column('customer', 'customer_name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customer', sa.Column('customer_name', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('customer', sa.Column('customer_registered_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('customer', sa.Column('customer_phone', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('customer', sa.Column('customer_postal_code', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('customer', 'registered_at')
    op.drop_column('customer', 'postal_code')
    op.drop_column('customer', 'phone')
    op.drop_column('customer', 'name')
    # ### end Alembic commands ###
