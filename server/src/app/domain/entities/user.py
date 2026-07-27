import datetime
import uuid

from dataclasses import dataclass, field


@dataclass
class User:
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    username: str
    email: str
    password: str
