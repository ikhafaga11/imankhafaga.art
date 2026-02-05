from lib.auth import Auth
from lib.database_connection import DatabaseConnection


class AuthRepository:
    def __init__(self, db_connection: DatabaseConnection) -> None:
        self._connection = db_connection

    def get_user(self, username: str, password: str) -> Auth:
        rows: list[dict] = self._connection.execute(
            "SELECT * FROM users WHERE username = %s", [username]
        )
        if(rows == [] or password != rows[0]["password"] or username != rows[0]["username"]):
            raise Exception("User does not exist")
        
        row: dict = rows[0]
        return Auth(id=row["id"], username=row["username"], password=row["password"])
