import sqlite3

class DatabaseConnection:
    """
    Custom context manager for handling database connections.
    """

    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        """Establish the database connection."""
        self.connection = sqlite3.connect(self.db_name)
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        """Close the database connection."""
        if self.connection:
            self.connection.close()

# Demonstration of using the context manager
if __name__ == "__main__":
    db_name = "example.db"

    # Setup: Create the 'users' table and add sample data
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
        cursor.executemany(
            "INSERT INTO users (name, age) VALUES (?, ?)",
            [("Alice", 30), ("Bob", 20), ("Charlie", 35), ("Diana", 45)]
        )
        conn.commit()

    # Use the custom context manager to query the database
    with DatabaseConnection(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        print("Query Results:")
        for row in rows:
            print(row)
