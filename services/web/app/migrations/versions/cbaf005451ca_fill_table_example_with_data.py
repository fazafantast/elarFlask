"""Fill table example with data

Revision ID: cbaf005451ca
Revises: a27ee7fbdae4
Create Date: 2023-03-03 07:19:22.450913

"""
from alembic import op
import sqlalchemy as sa

from models import Example


# revision identifiers, used by Alembic.
revision = 'cbaf005451ca'
down_revision = 'a27ee7fbdae4'
branch_labels = None
depends_on = None


def upgrade():
    op.bulk_insert(
        Example.__table__,
        [
            {'description': {'data': 'some data 1'}},
            {'description': {'data': 'some data 2'}},
            {'description': {'data': 'some data 3'}},
            {'description': {'data': 'some data 4'}},
            {'description': {'data': 'some data 5'}},
            {'description': {'data': 'some data 6'}},
            {'description': {'data': 'some data 7'}},
            {'description': {'data': 'some data 8'}},
            {'description': {'data': 'some data 9'}},
            {'description': {'data': 'some data 10'}},
            {'description': {'data': 'some data 11'}},
            {'description': {'data': 'some data 12'}},
            {'description': {'data': 'some data 13'}},
            {'description': {'data': 'some data 14'}},
            {'description': {'data': 'some data 15'}},
            {'description': {'data': 'some data 16'}},
            {'description': {'data': 'some data 17'}},
            {'description': {'data': 'some data 18'}},
            {'description': {'data': 'some data 19'}},
        ]
    )


def downgrade():
    pass
