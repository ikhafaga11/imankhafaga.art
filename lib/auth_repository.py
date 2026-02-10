from lib.auth import Auth
from lib.database_connection import DatabaseConnection
from lib.auth_errors import InvalidCredentialsError


class AuthRepository:
    def __init__(self, db_connection: DatabaseConnection) -> None:
        self._connection = db_connection

    def get_user(self, username: str) -> Auth:
        rows: list[dict] = self._connection.execute(
            "SELECT * FROM users WHERE username = %s", [username]
        )
        
        if not rows:
            raise InvalidCredentialsError()

        row: dict = rows[0]
        return Auth(id=row["id"], username=row["username"], password=row["password"])
