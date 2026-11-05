"""
Connects to the database.

echo=True prints every SQL statement SQLAlchemy runs, right in the
terminal, so you can match each query you write to the SQL it becomes.
"""

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session

DB_FILE = "vet.db"

engine = create_engine(f"sqlite:///{DB_FILE}", echo=False)


class Base(DeclarativeBase):
    """Every model class extends Base."""
    pass


def init_db():
    """If vet.db doesn't exist, create it: make the tables, then fill them.

    If the file is already there, do nothing. (create_all() never changes a
    table that already exists, so to rebuild the tables after changing
    models.py, delete vet.db and run again.)
    """
    if os.path.exists(DB_FILE):
        return

    import models  # registers the model classes with Base
    from seed import seed_db

    Base.metadata.create_all(engine)
    with Session(engine) as session:
        seed_db(session)
