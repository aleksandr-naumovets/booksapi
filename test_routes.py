from models import BookModel, ReviewModel
from routes import *
from repository import Repository
from unittest.mock import MagicMock
from flask import Request
from app import app

book1 = BookModel('The Hobbit', 'J R R Tolkien', 1)
book2 = BookModel('The Lord Of The Rings', 'J R R Tolkien', 2)
review1 = ReviewModel('a timeless classic', 1)
review2 = ReviewModel('I hated it', 1)
review3 = ReviewModel('an even more timeless classic', 2)
review4 = ReviewModel('I hated it even more', 2)

def test_booklist_get():
    repo = MagicMock(spec=Repository)
    repo.books_get_all.return_value = [book1, book2]
    books = BookList(repo).get()
    assert books[0]['bookId'] == 1
    assert books[1]['title'] == 'The Lord Of The Rings'

def test_booklist_post():
    with app.test_request_context():
        repo = MagicMock(spec=Repository)
        req = MagicMock(spec=Request)
        data = BookModel('Elementary', 'Kevin Rattan')
        req.json.return_value = data.__dict__
        repo.book_add.return_value = BookModel('Elementary',
                                       'Kevin Rattan', 100, '')
        book = BookList(repo).post(req)
        assert int(book['bookId']) == 100
        assert book['title'] == 'Elementary'

def test_book_get():
    repo = MagicMock(spec=Repository)
    repo.book_get_by_id.return_value = book2
    book = Book(repo).get(1)
    assert int(book['bookId']) == 2
    assert book['title'] == 'The Lord Of The Rings'
    
def test_reviewlist_book_get():
    repo = MagicMock(spec=Repository)
    repo.reviews_get_all.return_value = [review1,review2]
    reviews = ReviewList(repo).get()
    assert reviews[0]['bookId'] == 1
    assert reviews[1]['content'] == 'I hated it'
    
def test_reviewlist_post():
    with app.test_request_context():
        repo = MagicMock(spec=Repository)
        req = MagicMock(spec=Request)
        data = ReviewModel('genius', 1)
        req.json.return_value = data.__dict__
        repo.review_add.return_value = ReviewModel('genius', 1, 100)
        review = ReviewList(repo).post(req)
        assert int(review['id']) == 100
        assert review['content'] == 'genius'   
        
     
