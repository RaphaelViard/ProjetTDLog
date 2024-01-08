"""Description de la migration

Revision ID: cd8d5d920830
Revises: 
Create Date: 2024-01-08 14:07:02.283074

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd8d5d920830'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ticket',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nom_evenement', sa.String(length=255), nullable=True),
    sa.Column('date_evenement', sa.Date(), nullable=True),
    sa.Column('lieu_evenement', sa.String(length=255), nullable=True),
    sa.Column('prix_ticket', sa.Float(), nullable=True),
    sa.Column('nomUtilisateur', sa.String(length=255), nullable=True),
    sa.Column('en_vente', sa.Boolean(), nullable=True),
    sa.Column('code_secret', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code_secret')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('password', sa.String(length=120), nullable=False),
    sa.Column('money', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('ticket')
    # ### end Alembic commands ###
