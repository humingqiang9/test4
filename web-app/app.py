from flask import Flask
import psycopg2
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Попытка подключения к БД для проверки
    try:
        conn = psycopg2.connect(os.environ.get("DATABASE_URL"))
        conn.close()
        return "Hello, World! Connected to DB."
    except Exception as e:
        return f"Hello, World! DB Connection failed: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)