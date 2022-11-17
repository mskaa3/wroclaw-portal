import sqlite3

#Open database
conn = sqlite3.connect('docs_db.db')

#Create table
conn.execute('''CREATE TABLE IF NOT EXISTS categories
        (category_id INTEGER PRIMARY KEY AUTOINCREMENT, 
        category_name TEXT NOT NULL
        )''')

conn.execute('''CREATE TABLE IF NOT EXISTS documents
        (document_id INTEGER PRIMARY KEY AUTOINCREMENT,
        document_name TEXT NOT NULL,
        document_link TEXT NOT NULL,
        category_id INTEGER NOT NULL,
        CONSTRAINT fk_categories
        FOREIGN KEY(category_id) REFERENCES categories(category_id)
        ON DELETE CASCADE
        )''')

conn.close()

