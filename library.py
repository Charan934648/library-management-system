import sqlite3
from datetime import datetime

def add_book(title, author):
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute("INSERT INTO books (title, author, available) VALUES (?, ?, 1)", (title, author))
    conn.commit()
    conn.close()

def remove_book(book_id):
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute("DELETE FROM books WHERE id=?", (book_id,))
    conn.commit()
    conn.close()

def search_book(title):
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute("SELECT * FROM books WHERE title LIKE ?", ('%' + title + '%',))
    results = c.fetchall()
    conn.close()
    return results

def add_user(name):
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (name, borrowed_books) VALUES (?, 0)", (name,))
    conn.commit()
    conn.close()

def issue_book(book_id, user_id):
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute("UPDATE books SET available=0 WHERE id=?", (book_id,))
    c.execute("UPDATE users SET borrowed_books=borrowed_books+1 WHERE id=?", (user_id,))
    c.execute("INSERT INTO transactions (book_id, user_id, issue_date) VALUES (?, ?, ?)",
              (book_id, user_id, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()

def return_book(book_id, user_id):
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute("UPDATE books SET available=1 WHERE id=?", (book_id,))
    c.execute("UPDATE users SET borrowed_books=borrowed_books-1 WHERE id=?", (user_id,))
    c.execute("UPDATE transactions SET return_date=? WHERE book_id=? AND user_id=? AND return_date IS NULL",
              (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), book_id, user_id))
    conn.commit()
    conn.close()