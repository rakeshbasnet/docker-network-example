from flask import Flask, jsonify
from dotenv import load_dotenv
import os
import psycopg2
import redis

app = Flask(__name__)
load_dotenv()
# Connect to Redis
cache = redis.Redis(host='redis', port=6379)

# Connect to PostgreSQL
def get_db_connection():
    conn = psycopg2.connect(host=os.environ.get('POSTGRES_HOST'),
                            port=os.environ.get('POSTGRES_PORT'),
                            database=os.environ.get('POSTGRES_DB'),
                            user=os.environ.get('POSTGRES_USER'),
                            password=os.environ.get('POSTGRES_PASSWORD'))
    return conn

@app.route('/')
def hello():
    return "Hello, Docker Multi-Container!"

@app.route('/users')
def get_users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users;")
    users = cur.fetchall()
    cur.close()
    conn.close()

    return jsonify(users)

@app.route('/cache')
def cache_example():
    if cache.get('key'):
        return f"Cache Hit: {cache.get('key')}"
    else:
        cache.set('key', 'Hello from Redis Cache!')
        return "Cache Miss: Key Set"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)