import sqlite3

# Open database
conn = sqlite3.connect("news_db.db")

# Create table
conn.execute(
    """CREATE TABLE IF NOT EXISTS source
        (source_id INTEGER PRIMARY KEY AUTOINCREMENT,
        source_name TEXT NOT NULL
        )"""
)

conn.execute(
    """CREATE TABLE IF NOT EXISTS news
        (news_id INTEGER PRIMARY KEY AUTOINCREMENT,
        news_title TEXT NOT NULL,
        news_link TEXT NOT NULL,
        news_description TEXT NOT NULL,
        news_content TEXT NOT NULL,
        image_url TEXT,
        source_id INTEGER NOT NULL,
        published_at DATE NOT NULL,
        CONSTRAINT fk_sources
        FOREIGN KEY(source_id) REFERENCES source(source_id)
        ON DELETE CASCADE
        )"""
)

conn.close()