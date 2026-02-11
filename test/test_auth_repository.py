import pytest
from lib.auth_repository import AuthRepository
from lib.auth import Auth


def test_when_incorrect_username_return_exception(db_connection):
    db_connection.seed("db/seed.sql")
    repo = AuthRepository(db_connection)
    with pytest.raises(Exception) as e:
        username = "ikhafaga"  # missing 1 char
        password = "Password123!"  # correct
        repo.get_user(username, password)
    error_message = str(e.value)
    assert error_message == "User does not exist"


def test_when_incorrect_password_return_exception(db_connection):
    db_connection.seed("db/seed.sql")
    repo = AuthRepository(db_connection)
    with pytest.raises(Exception) as e:
        username = "ikhafaga1"  # correct
        password = "Password123"  # missing ! char
        repo.get_user(username, password)
    error_message = str(e.value)
    assert error_message == "User does not exist"


def test_case_sensitive_username(db_connection):
    db_connection.seed("db/seed.sql")
    repo = AuthRepository(db_connection)
    with pytest.raises(Exception) as e:
        username = "Ikhafaga1"  # uppercase I
        password = "Password123!"  # correct
        repo.get_user(username, password)
    error_message = str(e.value)
    assert error_message == "User does not exist"


def test_case_sensitive_password(db_connection):
    db_connection.seed("db/seed.sql")
    repo = AuthRepository(db_connection)
    with pytest.raises(Exception) as e:
        username = "ikhafaga1"  # correct
        password = "password123!"  # lowecase p
        repo.get_user(username, password)
    error_message = str(e.value)
    assert error_message == "User does not exist"


def test_correct_credentials(db_connection):
    db_connection.seed("db/seed.sql")
    repo = AuthRepository(db_connection)
    username = "ikhafaga1"  # correct
    password = "Password123!"  # correct
    user = repo.get_user(username, password)
    assert user == Auth(1, "ikhafaga1", "Password123!")
