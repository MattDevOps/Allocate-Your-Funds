"""added age and salary

Revision ID: 74febd982fa2
Revises: 467e61e3ea56
Create Date: 2018-07-24 14:31:13.136564

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74febd982fa2'
down_revision = '467e61e3ea56'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('age', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('salary', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'salary')
    op.drop_column('user', 'age')
    # ### end Alembic commands ###