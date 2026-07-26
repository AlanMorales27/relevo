import datetime
import uuid

from sqlalchemy import DateTime, Uuid
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass

class UUIDBase(Base):
    """
    Use this base when the table contains a unique identifier. If you want to 
    use a different identifier, or if it is an intermediate table, you can 
    just use the Base class.
    """
    __abstract__ = True

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid.uuid4
    ) 

class AuditableMixin:
    """
    Mixin that adds audit fields for tracking creation and update timestamps.
    """
    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone = True), 
        default=datetime.timezone.utc
    )
    
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone =True),
        default=datetime.timezone.utc,
        onupdate=datetime.timezone.utc
    )
