import sqlite3
import os

DB_NAME = "movies.db"

def init_db():
    print("🔥 init_db called")
    print("📁 Creating DB at:", os.path.abspath(DB_NAME))

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        rating REAL,
        genre TEXT,
        runtime INTEGER,
        year INTEGER,
        watched INTEGER DEFAULT 0
    )
    """)

    conn.commit()
    conn.close()


def insert_movies(movies):
    print("🔥 insert_movies called")
    print("Number of movies:", len(movies))

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    for m in movies:
        cur.execute("""
        INSERT INTO movies (title, rating, genre, runtime, year)
        VALUES (?, ?, ?, ?, ?)
        """, (
            m['title'],
            m['rating'],
            m['genre'],
            m['runtime'],
            m['year']
        ))

    conn.commit()
    conn.close()