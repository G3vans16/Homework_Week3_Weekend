from models.book import *

book1 = Book("To Kill a Mockingbird", "Harper Lee", "Southern Gothic Fiction")
book2 = Book("Dracula", "Bram Stoker", "Horror")
book3 = Book("1984", "George Orwell", "Dystopian")

books = [book1, book2, book3]

def add_new_book(book):
    books.append(book)

def delete_book_at_index(index):
    books.pop(index)