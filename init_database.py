import sqlite3

# 创建数据库连接
conn = sqlite3.connect('game.db')
c = conn.cursor()

# 创建 ranks 表
c.execute('''
CREATE TABLE IF NOT EXISTS ranks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    score INTEGER NOT NULL
)
''')

# 插入一些模拟用户数据
mock_data = [
    ('Alice', 1500),
    ('Bob', 1200),
    ('Charlie', 1800),
    ('David', 1600),
    ('Eve', 1700)
]

c.executemany('INSERT INTO ranks (name, score) VALUES (?, ?)', mock_data)

# 提交事务并关闭连接
conn.commit()
conn.close()