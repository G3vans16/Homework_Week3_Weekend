from flask import render_template, request, redirect
from app import app
from models.books import books, add_new_book, delete_book_at_index
from models.book import *

@app.route('/books')
def index():
    return render_template('index.html', title='Home', books=books)

@app.route('/books/<index>', methods= ['GET'])
def book(index):
    return render_template('book.html', title="Book", book=books[int(index)])

@app.route('/books', methods=['POST'])
def add_book():
  title = request.form['title']
  author = request.form['author']
  genre = request.form['genre']
  new_book = Book(title=title, author=author, genre=genre)
  add_new_book(new_book)
  return redirect('/books')

@app.route('/books/delete/<index>', methods=['POST'])
def delete(index):
  delete_book_at_index(int(index))
  return redirect('/books')