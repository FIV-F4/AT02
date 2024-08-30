import sqlite3

def init_db():
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL);''')

    return conn

def add_user(conn, name, age):
    c = conn.cursor()
    c.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    #return c.lastrowid

def get_users(conn, name):
    c = conn.cursor()
    c.execute('''SELECT * FROM users WHERE name =?''', (name,))
    return c.fetchone()
def check(number):
    return number % 2 == 0

def is_polindrom(number):
    return str(number) == str(number)[::-1]


def sort_list(list):
    return sorted(list)

