import sqlite3
conn = sqlite3.connect("user.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS utilisateur (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nom TEXT NOT NULL,
                   prenom TEXT NOT NULL,
                   email TEXT NOT NULL,
                   password TEXT NOT NULL
            )""")