import sqlite3

conn = sqlite3.connect('weather_app.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        city TEXT NOT NULL
    )
''')
conn.commit()
conn.close()