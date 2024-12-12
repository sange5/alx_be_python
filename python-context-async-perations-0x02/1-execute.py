import sqlite3

class ExecuteQuery:
    """
    A custom context manager to execute a given query with parameters, managing the database connection and execution.
    """

    def __init__(self, db_name, query, params=None):
        self.db_name = db_name
        self.query = query
        self.params = params if params else ()
        self.connection = None
        self.result = None

    def __enter__(self):
        """
        Open the database connection and execute the query.
        """
        self.connection = sqlite3.connect(self.db_name)
        cursor = self.connection.cursor()
        cursor.execute(self.query, self.params)
        self.result = cursor.fetchall()
        return self.result

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Close the database connection when exiting the context.
        """
        if self.connection:
            self.connection.close()

# Demonstration of using the ExecuteQuery context manager
if __name__ == "__main__":
    db_name = "example.db"

    # Setup: Create the 'users' table and add some sample data for demonstration purposes
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
        cursor.executemany(
            "INSERT INTO users (name, age) VALUES (?, ?)",
            [("Alice", 30), ("Bob", 20), ("Charlie", 35)]
        )
        conn.commit()

    # Use the context manager to execute the query
    query = "SELECT * FROM users WHERE age > ?"
    param = (25,)

    with ExecuteQuery(db_name, query, param) as results:
        for row in results:
            print(row)
