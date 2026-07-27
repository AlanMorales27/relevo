from abc import ABC, abstractmethod

from ....domain.entities.user import User


class IUserRepository(ABC):

    @abstractmethod
    def create(self, user: User) -> User: ...

    @abstractmethod
    def get_by_email(self, email: str) -> User | None: ...

    @abstractmethod
    def get_by_username(self, username: str) -> User | None: ...
