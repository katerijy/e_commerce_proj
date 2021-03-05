"""empty message

Revision ID: fe156c1a3b42
Revises: 0905da48453a
Create Date: 2021-03-05 14:27:04.400166

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fe156c1a3b42'
down_revision = '0905da48453a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('phone', sa.String(length=150), nullable=False))
    op.drop_constraint('user_phone_number_key', 'user', type_='unique')
    op.create_unique_constraint(None, 'user', ['phone'])
    op.drop_column('user', 'phone_number')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('phone_number', sa.VARCHAR(length=150), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'user', type_='unique')
    op.create_unique_constraint('user_phone_number_key', 'user', ['phone_number'])
    op.drop_column('user', 'phone')
    # ### end Alembic commands ###