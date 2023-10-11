"""It adds columns space in column password_hash 

Revision ID: 013e5cfdaf3d
Revises: 610c7f0207b6
Create Date: 2023-10-10 19:33:42.378216

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '013e5cfdaf3d'
down_revision = '610c7f0207b6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('password_hash',
               existing_type=mysql.VARCHAR(length=120),
               type_=sa.String(length=300),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('password_hash',
               existing_type=sa.String(length=300),
               type_=mysql.VARCHAR(length=120),
               existing_nullable=True)

    # ### end Alembic commands ###
