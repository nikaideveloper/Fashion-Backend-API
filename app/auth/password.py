from pwdlib import PasswordHash


password_hash = PasswordHash.recommended()


def hash_password(password : str):
    return password_hash.hash(password)



def verify_password(
        plain_password : bool,
        hashed_password : bool
):
    return password_hash.verify(
        password_hash,
        hash_password
    )


