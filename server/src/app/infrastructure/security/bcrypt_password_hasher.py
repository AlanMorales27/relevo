
from ...application.repositories.password_hasher import PasswordHasher

import bcrypt

class BcryptPasswordHasher(PasswordHasher):
    def hash(self, password: str) -> str:
        raw_hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        return raw_hashed.decode()

    def verify(self, password: str, hashed: str) -> bool:
        return bcrypt.checkpw(password.encode(), hashed.encode())
