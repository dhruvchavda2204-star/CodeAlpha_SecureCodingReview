import sqlite3

def initialize_database():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
    """)

    # Insert admin user only if not exists
    cursor.execute("SELECT * FROM users WHERE username = 'admin'")
    if not cursor.fetchone():
        cursor.execute("INSERT INTO users (username, password) VALUES ('admin', '1234')")
        conn.commit()

    conn.close()


def vulnerable_login():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    print("\n--- Vulnerable Login System ---")

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    # ❌ Vulnerable Query
    query = f"SELECT * FROM users WHERE username = '{username}' OR password = '{password}'"
    cursor.execute(query)

    result = cursor.fetchone()

    if result:
        print("Login Successful")
    else:
        print("Invalid Credentials")

    conn.close()


if __name__ == "__main__":
    initialize_database()
    vulnerable_login()
