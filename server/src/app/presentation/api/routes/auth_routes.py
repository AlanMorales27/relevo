from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from server.src.app.application import RegisterUserUseCase
from server.src.app.core.database import get_data_base, UserSQLAlchemyRepository
from server.src.app.infrastructure.security import BcryptPasswordHasher
from ...schemas import RegisterRequest, RegisterResponse

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login")
async def login_user(data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    pass


@router.post("/register", response_model=RegisterResponse)
def register_user(data: RegisterRequest, db: Session = Depends(get_data_base)):
    use_case = RegisterUserUseCase(
        user_repository = UserSQLAlchemyRepository(db),
        password_hasher = BcryptPasswordHasher()
    )

    return use_case.execute(data)
