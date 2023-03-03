"""
Описание моделей приложения
"""
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSONB


db = SQLAlchemy()


class Example(db.Model):
    __tablename__ = "examples"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(JSONB(), nullable=False)
    created = db.Column(db.DateTime(), nullable=True, default=datetime.utcnow)

    def __repr__(self):
        return f"<Example {self.id}, {self.created}>"
