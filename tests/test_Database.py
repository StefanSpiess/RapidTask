import pytest
from modules.database.Database import Database
from unittest.mock import patch, MagicMock

@pytest.fixture
def db_instance():
    """Fixture to create a Database instance."""
    return Database(host="localhost", port=5432, database="test_db", user="test_user", password="test_password")

@patch("modules.database.Database.psycopg2.connect")
def test_connect_success(mock_connect, db_instance):
    """Test successful database connection."""
    mock_connect.return_value = MagicMock()
    db_instance.connect()
    assert db_instance.connection is not None
    mock_connect.assert_called_once_with(
        host="localhost",
        port=5432,
        database="test_db",
        user="test_user",
        password="test_password"
    )

@patch("modules.database.Database.psycopg2.connect")
def test_connect_failure(mock_connect, db_instance):
    """Test database connection failure."""
    mock_connect.side_effect = Exception("Connection error")
    db_instance.connect()
    assert db_instance.connection is None

def test_disconnect(db_instance):
    """Test disconnecting from the database."""
    db_instance.connection = MagicMock()
    db_instance.disconnect()
    db_instance.connection.close.assert_called_once()
    assert db_instance.connection is None

@patch("modules.database.Database.psycopg2.connect")
def test_execute_query_success(mock_connect, db_instance):
    """Test successful query execution."""
    mock_connect.return_value = MagicMock()
    db_instance.connect()
    db_instance.connection.cursor.return_value.__enter__.return_value.execute = MagicMock()
    db_instance.execute_query("SELECT * FROM test_table")
    db_instance.connection.cursor.return_value.__enter__.return_value.execute.assert_called_once_with(
        "SELECT * FROM test_table", None
    )

@patch("modules.database.Database.psycopg2.connect")
def test_execute_query_failure(mock_connect, db_instance):
    """Test query execution failure."""
    mock_connect.return_value = MagicMock()
    db_instance.connect()
    db_instance.connection.cursor.return_value.__enter__.return_value.execute.side_effect = Exception("Query error")
    db_instance.execute_query("SELECT * FROM test_table")
    db_instance.connection.rollback.assert_called_once()

@patch("modules.database.Database.psycopg2.connect")
def test_fetch_results_success(mock_connect, db_instance):
    """Test successful fetching of query results."""
    mock_connect.return_value = MagicMock()
    db_instance.connect()
    mock_cursor = db_instance.connection.cursor.return_value.__enter__.return_value
    mock_cursor.fetchall.return_value = [("row1",), ("row2",)]
    results = db_instance.fetch_results("SELECT * FROM test_table")
    mock_cursor.execute.assert_called_once_with("SELECT * FROM test_table", None)
    assert results == [("row1",), ("row2",)]

@patch("modules.database.Database.psycopg2.connect")
def test_fetch_results_failure(mock_connect, db_instance):
    """Test failure in fetching query results."""
    mock_connect.return_value = MagicMock()
    db_instance.connect()
    results = db_instance.fetch_results("SELECT * FROM test_table...")
    assert results is None