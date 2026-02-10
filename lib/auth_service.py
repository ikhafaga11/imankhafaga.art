from lib.auth_repository import AuthRepository
from lib.auth_errors import InvalidCredentialsError
from lib.auth import Auth

def authenticate(username: str, password: str, repo: AuthRepository) -> Auth:
    user = repo.get_user(username=username)

    if password != user.password:
        raise InvalidCredentialsError('User does not exist')
    
    return user