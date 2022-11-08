"""initial migration

Revision ID: a5185ae68a4b
Revises: 
Create Date: 2020-10-11 17:56:44.645702

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "a5185ae68a4b"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "film",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("release_date", sa.Date(), nullable=False),
        sa.Column("uuid", sa.String(length=36), nullable=True),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("distributed_by", sa.String(length=128), nullable=False),
        sa.Column("length", sa.Float(), nullable=True),
        sa.Column("rating", sa.Float(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("uuid"),
    )
    op.create_index(
        op.f("ix_film_release_date"), "film", ["release_date"], unique=False
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_film_release_date"), table_name="film")
    op.drop_table("film")
    # ### end Alembic commands ###
