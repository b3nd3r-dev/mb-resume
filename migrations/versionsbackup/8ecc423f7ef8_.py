"""empty message

Revision ID: 8ecc423f7ef8
Revises: 3a7c9ec34323
Create Date: 2021-07-15 18:52:32.743396

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ecc423f7ef8'
down_revision = '3a7c9ec34323'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('project_tags', sa.Column('show_on_front', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('project_tags', 'show_on_front')
    # ### end Alembic commands ###
