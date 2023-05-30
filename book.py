import sqlite3

from flask import Flask, request

app = Flask(__name__)

def db_connect():
    conn = None
    try:
        conn = sqlite3.connect('books.sqlite')
    except sqlite3.Error as e:
        print(e)
    return conn

@app.route('/books', methods=['GET', 'POST'])
def books():
    conn = db_connect()
    c = conn.cursor()
    if request.method == 'GET':
        c.execute("SELECT * FROM books")
        books = c.fetchall()
        return {"books": books}
    elif request.method == 'POST':
        request_data = request.get_json()
        new_book = {
            "title": request_data['title'],
            "author": request_data['author'],
            "language": request_data['language']
        }
        c.execute("INSERT INTO books (title, author, language) VALUES (?, ?, ?)",
                  (new_book['title'], new_book['author'], new_book['language']))
        conn.commit()
        return new_book, 201

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    conn = db_connect()
    c = conn.cursor()
    request_data = request.get_json()
    updated_book = {
        "title": request_data['title'],
        "author": request_data['author'],
        "language": request_data['language']
    }
    c.execute("UPDATE books SET title = ?, author = ?, language = ? WHERE id = ?",
              (updated_book['title'], updated_book['author'], updated_book['language'], book_id))
    conn.commit()
    return updated_book

if __name__ == '__main__':
    app.run(port=3500, debug=True)
