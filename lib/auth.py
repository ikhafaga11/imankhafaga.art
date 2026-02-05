class Auth:
    def __init__(self, id:int, username: str, password: str) -> None:
        self.id = id
        self.username = username
        self.password = password
    
    def __repr__(self):
        return f"Auth({self.id},{self.username!r},{self.password!r})"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__