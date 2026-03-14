import sqlite3
import pandas as pd

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

def mark_completed(course_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE courses SET completed = 1 WHERE id = ?", (course_id,))
    conn.commit()
    conn.close()

def export_courses(filename="courses_export.xlsx"):
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query("SELECT * FROM courses", conn)
    df.to_excel(filename, index=False)
    conn.close()
