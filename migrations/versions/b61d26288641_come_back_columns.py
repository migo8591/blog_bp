"""Come back columns

Revision ID: b61d26288641
Revises: 023357ddd7db
Create Date: 2023-10-13 12:47:21.291219

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b61d26288641'
down_revision = '023357ddd7db'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.drop_constraint('posts_ibfk_1', type_='foreignkey')
        batch_op.drop_column('poster_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('poster_id', mysql.INTEGER(), autoincrement=False, nullable=True))
        batch_op.create_foreign_key('posts_ibfk_1', 'users', ['poster_id'], ['id'])

    # ### end Alembic commands ###
