from models import BookModel, ReviewModel
from flask import g, current_app

book1 = BookModel('The Hobbit', 'J R R Tolkien', 1)
book2 = BookModel('The Lord Of The Rings', 'J R R Tolkien', 2)
review1 = ReviewModel('a timeless classic', 1)
review2 = ReviewModel('I hated it', 1)
review3 = ReviewModel('an even more timeless classic', 2)
review4 = ReviewModel('I hated it even more', 2)

class Repository():

    def get_db(self):
        if 'db' not in g:
            g.db = current_app.config['pSQL_pool'].getconn()
        return g.db
    
    def books_get_all(self): 
        conn = self.get_db() 
        if (conn):
            ps_cursor = conn.cursor()
            ps_cursor.execute(
                "select title, author, bookId, cover from book order by title")
            book_records = ps_cursor.fetchall() 
            book_list = []
            for row in book_records:
                book_list.append(BookModel(row[0], row[1], row[2], row[3])) 
            ps_cursor.close()
        return book_list
        
    
    def book_get_by_id(self, book_id):
        books=[book1, book2]
        return next((x for x in books if x.bookId == book_id), None)
    
    def reviews_get_all(self):
        return [review1, review2, review3, review4]
    
    def review_get_by_id(self, review_id):
        reviews=[review1, review2, review3, review4]
        return next((x for x in reviews if x.review_id == review_id), None)
    
    def review_add(self, data):
        return ReviewModel(data['content'], 3)
        
    def book_add(self, data):
        conn = None
        try:
            conn = self.get_db()
            if (conn):
                ps_cursor = conn.cursor()
                ps_cursor.execute("INSERT INTO book(title,cover,author) VALUES (%s, %s, %s) RETURNING bookId ",
                                  (data['title'], data['cover'], data['author']))
                conn.commit()
                id = ps_cursor.fetchone()[0]
                ps_cursor.close()
                return BookModel(data['title'], data['cover'], id, data['author'])
        except Exception as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
