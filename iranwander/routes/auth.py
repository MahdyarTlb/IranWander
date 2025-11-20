from flask import Blueprint, render_template, request, redirect, url_for

auth = Blueprint('auth', __name__, template_folder='templates') 

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')

@auth.route('/forget', methods=['GET', 'POST'])
def forget_password():
    return render_template('forget.html')

@auth.route('/set-password/<token>', methods=['GET', 'POST'])
def set_password(token):
    return render_template('setpassword.html', token=token)