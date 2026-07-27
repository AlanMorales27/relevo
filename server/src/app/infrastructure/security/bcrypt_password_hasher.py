
from ...application.interfaces.services.i_password_hasher import IPasswordHasher

import bcrypt

class BcryptPasswordHasher(IPasswordHasher):
    def hash(self, password: str) -> str:
        raw_hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        return raw_hashed.decode()

    def verify(self, password: str, hashed: str) -> bool:
        return bcrypt.checkpw(password.encode(), hashed.encode())
