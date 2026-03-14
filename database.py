import sqlite3

DB_NAME = "courses.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            platform TEXT,
            url TEXT,
            completed INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

def add_course(title, platform, url):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO courses (title, platform, url) VALUES (?, ?, ?)", (title, platform, url))
    conn.commit()
    conn.close()

def list_courses():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, platform, url, completed FROM courses")
    rows = cursor.fetchall()
    conn.close()
    return rows
