from modules.baseclass.BaseClass import BaseClass
import psycopg2
from psycopg2 import sql

class Database(BaseClass):
    def __init__(self, host, port, database, user, password):
        super().__init__()
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def connect(self):
        """Establish a connection to the PostgreSQL database."""
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password
            )
            print("Database connection established.")
        except psycopg2.Error as e:
            print(f"Error connecting to the database: {e}")
            self.connection = None

    def disconnect(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")
            self.connection = None

    def execute_query(self, query, params=None):
        """Execute a query on the database."""
        if not self.connection:
            print("No active database connection.")
            return None
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, params)
                self.connection.commit()
                print("Query executed successfully.")
        except psycopg2.Error as e:
            print(f"Error executing query: {e}")
            self.connection.rollback()

    def fetch_results(self, query, params=None):
        """Fetch results from a SELECT query."""
        if not self.connection:
            print("No active database connection.")
            return None
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, params)
                results = cursor.fetchall()
                return results
        except psycopg2.Error as e:
            print(f"Error fetching results: {e}")
            return None