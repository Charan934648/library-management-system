import sqlite3

def create_tables():
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS books
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, author TEXT, available INTEGER)''')
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, borrowed_books INTEGER)''')
    c.execute('''CREATE TABLE IF NOT EXISTS transactions
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, book_id INTEGER, user_id INTEGER, issue_date TEXT, return_date TEXT)''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tables()