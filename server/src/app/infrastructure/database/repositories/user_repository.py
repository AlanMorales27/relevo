import logging

from sqlalchemy.orm import Session

from ...application.interfaces.repositories.i_user_repository import IUserRepository
from ...domain.entities.user import User
from ..models import User as UserModel


class UserSQLAlchemyRepository(IUserRepository):

    def __init__(self, session: Session):
        self._session = session

    def create(self, user: User) -> User:
        try:
            model = UserModel(
                id=user.id,
                username=user.username,
                email=user.email,
                password=user.password
            )

            self._session.add(model)
            self._session.commit()
            self._session.refresh(model)
            return User(
                id=model.id,
                username=model.username,
                email=model.email,
                password=model.password
            )
        except Exception as e:
            logging.error(f"Error creating user: {e}")
            self._session.rollback()
            raise

    def get_by_email(self, email: str) -> User | None:
        ...

    def get_by_username(self, username: str) -> User | None:
        ...
