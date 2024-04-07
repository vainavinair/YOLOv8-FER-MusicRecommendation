from app.users import bp
from flask import flash, redirect, render_template, request, session, url_for
import pandas as pd


user_data = pd.read_csv('app/static/user_data.csv')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_row = user_data[(user_data['UserName'] == username)]
        # Dummy authentication, replace with your own authentication logic
        if not user_row.empty and password == 'admin':
            session['username'] = username
            # Redirect to a different page after successful login
            return redirect(url_for('main.home'))
        else:
            flash('Invalid username or password', 'danger')
            return render_template('login.html')
            
    
    # Render login form template for GET requests
    return render_template('login.html')

@bp.route('/logout')
def logout():
    session.pop('username', None)
    flash('Login to Continue', 'secondary')

    return redirect(url_for('users.login'))
