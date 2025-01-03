from flask import render_template, request, redirect, url_for, flash, session
from . import app, db
from .models import Users


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']

        existing_users = Users.query.filter_by(name=name).first()
        if existing_users:
            flash('This username is already taken.', 'error')
            return redirect(url_for('register'))

        db.session.add(Users(name=name, password=password, win_plays=0, all_plays=0))
        db.session.commit()

        flash('Registration was successful!', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        user = Users.query.filter_by(name=name).first()

        if not user:
            flash('Wrong username.', 'error')
            return redirect(url_for('login'))

        if user.password != password:
            flash('Wrong password.', 'error')
            return redirect(url_for('login'))

        session['user_id'] = user.id
        return redirect(url_for('home'))

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('home'))
