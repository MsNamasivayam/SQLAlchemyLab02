"""
The model classes. Each class maps to one table in vet.db,
and each attribute maps to one column.
"""

from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from database import Base

# TODO: Create the models