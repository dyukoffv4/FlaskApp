from flask import Flask, render_template, request, redirect, url_for, flash, session
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

def get_data(sql_request: str):
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


def push_data(sql_request: str):
    connection = psycopg2.connect(host=HOST_IP, database=DB_NAME, user=DB_USER, password=DB_PASS)
    cursor = connection.cursor()
    try:
        cursor.execute(sql_request)
        connection.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if cursor:
            cursor.close()
        connection.close()

# ROUTING SETUP

app = Flask(__name__)
app.secret_key = '0123'


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']

        existing_users = get_data(f"SELECT * FROM users WHERE name = '{name}'")
        if existing_users is not None and len(existing_users) != 0:
            flash('This username is already taken.', 'error')
            return redirect(url_for('register'))

        push_data(f"INSERT INTO users (name, pass, win_plays, all_plays) VALUES ('{name}', '{password}', 0, 0);")

        flash('Registration was successful!', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        users = get_data(f"SELECT * FROM users WHERE name = '{name}'")

        if users is None or len(users) == 0:
            flash('Wrong username.', 'error')
            return redirect(url_for('login'))

        user = users[0]
        if user[2] != password:
            flash('Wrong password.', 'error')
            return redirect(url_for('login'))

        session['user_id'] = user[0]
        return redirect(url_for('home'))

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('home'))

# RUN

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=APP_PORT, debug=APP_DEBUG)
