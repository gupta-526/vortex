"""empty message

Revision ID: 548dd7efc5c2
Revises: 194a4d3d9aa8
Create Date: 2016-05-20 14:14:21.200889

"""

# revision identifiers, used by Alembic.
revision = '548dd7efc5c2'
down_revision = '194a4d3d9aa8'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_user_file_saved_file', table_name='user_file')
    op.drop_column('user_file', 'saved_file')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_file', sa.Column('saved_file', sa.VARCHAR(length=200), autoincrement=False, nullable=True))
    op.create_index('ix_user_file_saved_file', 'user_file', ['saved_file'], unique=False)
    ### end Alembic commands ###
