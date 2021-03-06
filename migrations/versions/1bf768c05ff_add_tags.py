"""add tags

Revision ID: 1bf768c05ff
Revises: 23fc26d864b
Create Date: 2015-10-26 15:38:30.422188

"""

# revision identifiers, used by Alembic.
revision = '1bf768c05ff'
down_revision = '23fc26d864b'
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


def upgrade_amblog():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), server_default='', nullable=True),
    sa.Column('author', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('post_and_tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('post', sa.Integer(), nullable=True),
    sa.Column('tag', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['post'], ['posts.id'], ),
    sa.ForeignKeyConstraint(['tag'], ['tag.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_post_and_tag_post'), 'post_and_tag', ['post'], unique=False)
    op.create_index(op.f('ix_post_and_tag_tag'), 'post_and_tag', ['tag'], unique=False)
    ### end Alembic commands ###


def downgrade_amblog():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_post_and_tag_tag'), table_name='post_and_tag')
    op.drop_index(op.f('ix_post_and_tag_post'), table_name='post_and_tag')
    op.drop_table('post_and_tag')
    op.drop_table('tag')
    ### end Alembic commands ###


def upgrade_auth():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###


def downgrade_auth():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###

