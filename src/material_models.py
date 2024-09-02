from typing import Annotated, Optional, List
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base, str_256

intpk = Annotated[int, mapped_column(primary_key=True)]