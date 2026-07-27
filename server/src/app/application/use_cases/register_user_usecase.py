

from server.src.app.application.interfaces.repositories import IUserRepository
from server.src.app.infrastructure.database import User
from ..interfaces.services.i_password_hasher import IPasswordHasher
from ...presentation.schemas.auth_schemas import RegisterRequest, RegisterResponse


class RegisterUserUseCase:

    def __init__(self, 
        user_repository: IUserRepository, 
        password_hasher: IPasswordHasher
    ):
        self._password_hasher = password_hasher
        self._user_repository = user_repository

    def execute(self, data: RegisterRequest) -> RegisterResponse:
        hashed_password = self._password_hasher.hash(data.password)
        user = self._user_repository.create(
            User(
                username=data.username,
                email=data.email,
                password=hashed_password
            )
        )
        return RegisterResponse(
            id=user.id,
            username=user.username,
            email=user.email
        )
