"""empty message

Revision ID: 3585df57adf
Revises: 44872ba647b
Create Date: 2015-02-23 16:07:34.510333

"""

# revision identifiers, used by Alembic.
revision = '3585df57adf'
down_revision = '44872ba647b'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('timestamp', sa.Column('ip_address', sa.String(length=60), nullable=True))
    op.add_column('timestamp', sa.Column('user_agent', sa.String(length=255), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('timestamp', 'user_agent')
    op.drop_column('timestamp', 'ip_address')
    ### end Alembic commands ###
