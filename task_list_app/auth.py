"""
Concepts covert here:
- Views grouped into a Blueprint to be ingested by the app
- register - includes saving a user into the database
- login - includes retrieving a user from the database; saves the user id to the session
- logout - removes the user id from the session
- session - stores data across requests
- user_logged_in - run a task before each request to add a logged in user to the global 
context of the application - g
- require authentication in other views?
"""
from flask import (
    Blueprint, request, flash, redirect, url_for, render_template, session, g
)
from werkzeug.security import check_password_hash, generate_password_hash

from db import engine, create_user, get_user

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.before_app_request
def load_logged_in_user():
    if not session.get('user_id', None):
        g.user = None
    else:
        try:
            with engine.connect() as connection:
                g.user = get_user(connection, {'id': session.get('user_id')})
        except Exception as e:
            flash(f"Error retrieving the user for the current request: {e}")
            g.user = None

@bp.route('/register', methods=('GET','POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        email = request.form['email']
        error = None

        if not username:
            error = 'Please provide a username...'
        elif not password or not confirm_password:
            error = 'Please provide a password...'
        elif not email:
            error = 'Please provide a valid email...'

        if error is None:
            user_data = {
                'name': username,
                'email': email,
                'password': password
            }
            try:
                with engine.connect() as connection:
                    create_user(connection, user_data)
            except Exception as e:
                error = f"Couldn't save the user: {e}"
            else:
                return redirect(url_for('auth/login'))

        flash(error)
    
    return render_template('auth/register.html')

@bp.route('/login', methods=('GET','POST'))
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        error = None
        user = None

        user_data = {
            'email': email
        }
        try:
            with engine.connect() as connection:
                user = get_user(connection, user_data)
        except Exception as e:
            error = "Couldn't get user..."
            flash(error)
        
        if user is None:
            error = 'Incorrect user...'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password...'
        
        if error is None:
            session.clear()
            session['user_id'] = user['id']
            g.user = user
            return redirect(url_for('index'))
        
        flash(error)
    
    return render_template('auth/login.html')

@bp.route('/logout')
def logout():
    session.clear()
    g.user = None
    return redirect(url_for('index'))
