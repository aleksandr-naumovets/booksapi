from flask import Flask
from flask import g
from routes import Book, BookList, Review, ReviewList
from flask_restful import Api
from flask_cors import CORS
from psycopg2 import pool
import os

BASE_URL = os.environ.get("BASE_URL")
HOST=os.environ.get("HOST")
DATABASE=os.environ.get("DATABASE")
DB_PORT=os.environ.get("DB_PORT")
DB_USER=os.environ.get("DB_USER")
DB_PASSWORD=os.environ.get("DB_PASSWORD")
MIN=os.environ.get("MIN")
MAX=os.environ.get("MAX")
DEBUG=os.environ.get("DEBUG")

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(BookList, f'{BASE_URL}/Books')
api.add_resource(Book, f'{BASE_URL}/Book/<book_id>')
api.add_resource(ReviewList, f'{BASE_URL}/Reviews')
api.add_resource(Review, f'{BASE_URL}/Review/<book_id>')

app.config['pSQL_pool'] = pool.SimpleConnectionPool(MIN,
                                                        MAX,
                                                        user=DB_USER,
                                                        password=DB_PASSWORD,
                                                        host=HOST,
                                                        port=DB_PORT,
                                                        database=DATABASE)

@app.teardown_appcontext
def close_conn(e):
    db = g.pop('db', None)
    if db is not None:
        app.config['pSQL_pool'].putconn(db)
        print('released connection back to pool')

if __name__ == '__main__': 
    app.run(debug=DEBUG)
