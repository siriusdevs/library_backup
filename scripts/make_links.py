from psycopg2 import connect
from dotenv import load_dotenv
from os import getenv
from random import choice

load_dotenv()
credentials = {
    'host' : getenv('PG_HOST'),
    'port' : int(getenv('PG_PORT')),
    'user' : getenv('PG_USER'),
    'password' : getenv('PG_PASSWORD'),
    'dbname' : getenv('PG_DBNAME')
}

connection = connect(**credentials)
cursor = connection.cursor()

get_ids = 'select id from'
cursor.execute(f'{get_ids} library.book')
book_ids = [id[0] for id in cursor.fetchall()]

cursor.execute(f'{get_ids} library.author')
author_ids = [id[0] for id in cursor.fetchall()]

request = "INSERT INTO library.book_author (book_id, author_id) VALUES ('{0}', '{1}')"
i = 0
with_books = set()
for book_id in book_ids:
    author_id = choice(author_ids)
    with_books.add(author_id)
    cursor.execute(request.format(book_id, author_id))
    print(f'Current progress (with_books): {i / len(book_ids) * 100}%')
    i += 1

without_books = set(author_ids) - with_books
i = 0
for author_id in without_books:
    book_id = choice(book_ids)
    cursor.execute(request.format(book_id, author_id))
    print(f'Current progress (without_books): {i / len(without_books) * 100}%')
    i += 1

connection.commit()
cursor.close()
connection.close()
