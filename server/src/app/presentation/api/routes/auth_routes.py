from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordRequestForm

from ...schemas import RegisterRequest, RegisterResponse

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login")
async def login_user(data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    pass


@router.post("/register", response_model=RegisterResponse)
async def register_user(data: RegisterRequest) -> RegisterResponse:

    hashed_password = ""

    pass