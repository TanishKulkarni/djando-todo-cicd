"""create sources table

Revision ID: f009609b99b7
Revises: bbc50e852af6
Create Date: 2026-05-31 11:25:51.375126

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f009609b99b7'
down_revision: Union[str, Sequence[str], None] = 'bbc50e852af6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


def upgrade() -> None:
    op.create_table(
        "sources",

        sa.Column(
            "id",
            postgresql.UUID(as_uuid=True),
            primary_key=True
        ),

        sa.Column(
            "project_id",
            postgresql.UUID(as_uuid=True),
            nullable=False
        ),

        sa.Column(
            "source_type",
            sa.String(length=50),
            nullable=False
        ),

        sa.Column(
            "content",
            sa.Text(),
            nullable=False
        ),

        sa.Column(
            "uploaded_by",
            postgresql.UUID(as_uuid=True),
            nullable=True
        ),

        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now()
        ),

        sa.ForeignKeyConstraint(
            ["project_id"],
            ["projects.id"],
            ondelete="CASCADE"
        )
    )


def downgrade() -> None:
    op.drop_table("sources")
