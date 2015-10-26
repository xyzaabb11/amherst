"""delete category

Revision ID: 23fc26d864b
Revises: 12133277950
Create Date: 2015-10-26 15:33:03.132589

"""

# revision identifiers, used by Alembic.
revision = '23fc26d864b'
down_revision = '12133277950'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_():
    pass


def downgrade_():
    pass


def upgrade_amblog():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('category')
    ### end Alembic commands ###


def downgrade_amblog():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('name', mysql.VARCHAR(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    ### end Alembic commands ###


def upgrade_auth():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###


def downgrade_auth():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###

