"""add tags

Revision ID: 12133277950
Revises: 53b1f1f2c25
Create Date: 2015-10-26 15:31:23.928767

"""

# revision identifiers, used by Alembic.
revision = '12133277950'
down_revision = '53b1f1f2c25'
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
    pass
    ### end Alembic commands ###


def downgrade_auth():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###


def upgrade_amblog():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###


def downgrade_amblog():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###
