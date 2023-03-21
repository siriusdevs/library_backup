from psycopg2 import connect
from dotenv import load_dotenv
from os import getenv
from faker import Faker


load_dotenv()
credentials = {
    'host' : getenv('PG_HOST'),
    'port' : int(getenv('PG_PORT')),
    'user' : getenv('PG_USER'),
    'password' : getenv('PG_PASSWORD'),
    'dbname' : getenv('PG_DBNAME')
}

genres = {
    'fantasy': 'every student gets 5 on exam',
    'fiction': 'a great song by Tom Odell',
    'detective': 'find out how to run students homework'
}
    
connection = connect(**credentials)
cursor = connection.cursor()
request = "INSERT INTO library.genre (name, description) VALUES (%s, %s)" 
# fake = Faker()
for name, description in genres.items():
    # full_name: str = str(fake.name())
    cursor.execute(request, (name, description))

connection.commit()
cursor.close()
connection.close()

