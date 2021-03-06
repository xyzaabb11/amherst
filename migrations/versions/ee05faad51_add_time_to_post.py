"""add time to post

Revision ID: ee05faad51
Revises: 1bf768c05ff
Create Date: 2015-10-27 09:40:24.459364

"""

# revision identifiers, used by Alembic.
revision = 'ee05faad51'
down_revision = '1bf768c05ff'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_():
    pass


def downgrade_():
    pass


def upgrade_auth():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('create_time', sa.DateTime(), nullable=True))
    op.add_column('user', sa.Column('last_login_ip', sa.String(length=30), nullable=True))
    op.add_column('user', sa.Column('last_login_time', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade_auth():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_login_time')
    op.drop_column('user', 'last_login_ip')
    op.drop_column('user', 'create_time')
    ### end Alembic commands ###


def upgrade_amblog():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('last_visit_time', sa.DateTime(), nullable=True))
    op.add_column('posts', sa.Column('view_times', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade_amblog():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'view_times')
    op.drop_column('posts', 'last_visit_time')
    ### end Alembic commands ###

