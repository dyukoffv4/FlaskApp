from flask import Flask, render_template
import psycopg2
import os

# SETTINGS

HOST_IP = os.getenv('HOST_IP', '127.0.0.1')

APP_PORT = int(os.getenv('APP_PORT', '80'))
APP_DEBUG = True if os.getenv('APP_DEBUG', 'true').lower() == 'true' else False

DB_USER = os.getenv('POSTGRES_USER', 'admin')
DB_PASS = os.getenv('POSTGRES_PASSWORD', 'admin')
DB_NAME = os.getenv('POSTGRES_DB', 'postgres')

# FUNCTIONS

def fetch_data(sql_request: str):
    connection = psycopg2.connect(host=HOST_IP, database=DB_NAME, user=DB_USER, password=DB_PASS)
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(sql_request)
        result = cursor.fetchall()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if cursor:
            cursor.close()
        connection.close()
    return result

# ROUTING SETUP

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", users_info=fetch_data("SELECT * FROM users"))

# RUN

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=APP_PORT, debug=APP_DEBUG)
