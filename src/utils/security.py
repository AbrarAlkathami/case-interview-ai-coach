import bcrypt


def hash_pwd(password: str, rounds: int = 6) -> bytes:
    return bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt(rounds=rounds)
    )

def check_pwd(password: str, hashed_password: bytes) -> bool:
    return bcrypt.checkpw(
        password.encode(),
        hashed_password
    )
