import sqlite3

class DatabaseConnection:
    """
    A custom context manager to handle opening and closing database connections automatically.
    """

    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        """
        Open the database connection when entering the context.
        """
        self.connection = sqlite3.connect(self.db_name)
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Close the database connection when exiting the context.
        """
        if self.connection:
            self.connection.close()

# Demonstration of using the context manager
if __name__ == "__main__":
    db_name = "example.db"

    # Setup: Create the 'users' table and add some sample data for demonstration purposes
    with DatabaseConnection(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
        cursor.execute("INSERT INTO users (name) VALUES ('Alice'), ('Bob'), ('Charlie')")
        conn.commit()

    # Use the context manager to query the database
    with DatabaseConnection(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        results = cursor.fetchall()

        for row in results:
            print(row)
