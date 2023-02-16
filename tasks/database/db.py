import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    user_id INT PRIMARY KEY,
                    name VARCHAR(20),
                    gender VARCHAR(8)
);
    ''')




