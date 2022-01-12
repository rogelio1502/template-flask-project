"""empty message

Revision ID: f871c98ac68a
Revises: ee6844d64370
Create Date: 2022-01-12 15:25:42.212555

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f871c98ac68a'
down_revision = 'ee6844d64370'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('model', sa.Column('last_name', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('model', 'last_name')
    # ### end Alembic commands ###