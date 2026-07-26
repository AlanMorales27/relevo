from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from ..base import UUIDBase, AuditableMixin


class User(UUIDBase, AuditableMixin):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(String(255))
    username: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    password: Mapped[str] = mapped_column(String(255))


