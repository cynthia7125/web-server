import sqlite3

def connect_db():
    return sqlite3.connect('webserver.db')

def create_users_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE,
            userName TEXT,
            password TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def insert_user(email, userName, password):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (email, userName, password) VALUES (?, ?, ?)",
                       (email, userName, password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False  
    finally:
        conn.close()

def check_user_credentials(email, password):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT userName FROM users WHERE email = ? AND password = ?", (email, password))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None
