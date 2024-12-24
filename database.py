
import sqlite3

conn = sqlite3.connect('game.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS ranks (id INTEGER PRIMARY KEY, name TEXT, score INTEGER)''')
conn.commit()
conn.close()