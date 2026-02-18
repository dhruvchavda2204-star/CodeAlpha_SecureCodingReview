import sqlite3

def secure_login():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    print("\n--- Secure Login System ---")

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    # ✅ Secure Parameterized Query
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    cursor.execute(query, (username, password))

    result = cursor.fetchone()

    if result:
        print("Login Successful")
    else:
        print("Invalid Credentials")

    conn.close()


if __name__ == "__main__":
    secure_login()
