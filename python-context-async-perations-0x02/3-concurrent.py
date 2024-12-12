import aiosqlite
import asyncio
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

# Asynchronous functions for fetching data
async def async_fetch_users(db_name):
    """Fetch all users from the database asynchronously."""
    async with aiosqlite.connect(db_name) as db:
        cursor = await db.execute("SELECT * FROM users")
        rows = await cursor.fetchall()
        await cursor.close()
        return rows

async def async_fetch_older_users(db_name):
    """Fetch users older than 40 from the database asynchronously."""
    async with aiosqlite.connect(db_name) as db:
        cursor = await db.execute("SELECT * FROM users WHERE age > 40")
        rows = await cursor.fetchall()
        await cursor.close()
        return rows

async def fetch_concurrently(db_name):
    """Run multiple queries concurrently."""
    results = await asyncio.gather(
        async_fetch_users(db_name),
        async_fetch_older_users(db_name)
    )
    print("All Users:", results[0])
    print("Users Older Than 40:", results[1])

# Demonstration of using the ExecuteQuery context manager and async queries
if __name__ == "__main__":
    db_name = "example.db"

    # Setup: Create the 'users' table and add some sample data for demonstration purposes
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
        cursor.executemany(
            "INSERT INTO users (name, age) VALUES (?, ?)",
            [("Alice", 30), ("Bob", 20), ("Charlie", 35), ("Diana", 45)]
        )
        conn.commit()

    # Run the asynchronous fetch concurrently
    asyncio.run(fetch_concurrently(db_name))
