from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user

from ..models import User, db
from werkzeug.security import check_password_hash

import secrets

auth = Blueprint('auth', __name__, template_folder='templates/auth')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        username = request.form.get('username').strip()
        password = request.form.get('password').strip()

        user = User.query.filter_by(username=username).first()

        if not user:
            flash("The username is incorrect.", "login_error")
            return redirect(url_for('auth.login'))

        if not check_password_hash(user.password_hash, password):
            flash("password is incorrect", "login_error")
            return redirect(url_for('auth.login'))

        login_user(user)
        flash("yeah! coming in", "login_success")

        return redirect(url_for('main.index'))

    return render_template('auth/login.html')

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':

        username = request.form.get("username").strip()
        password = request.form.get("password").strip()
        email = request.form.get("email").strip()

        if not username or not password or not email:
            flash("All fields are required.", "error")
            return redirect(url_for("auth.signup"))

        if User.query.filter_by(username=username).first():
            flash("Username already exists.", "error")
            return redirect(url_for("auth.signup"))

        if User.query.filter_by(email=email).first():
            flash("Email already registered.", "error")
            return redirect(url_for("auth.signup"))

        user = User(
            username=username,
            email=email,
        )
        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        flash("Account created successfully! Please login.", "success")

        return redirect(url_for("auth.login"))

    return render_template('auth/signup.html')

@auth.route('/forget', methods=['GET', 'POST'])
def forget_password():

    if request.method == 'POST':
        email = request.form.get("email").strip()

        user = User.query.filter_by(email=email).first()
        if not user:
            flash("No user found with the email.", "error")
            return redirect(url_for("auth.forget_password"))

        token = secrets.token_hex(16)
        user.reset_token = token
        db.session.commit()

        flash("Reset link created! (Temporary).", "info")

        return redirect(url_for("auth.set_password", token=token))

    return render_template('auth/forget.html')

@auth.route('/set-password/<token>', methods=['GET', 'POST'])
def set_password(token):

    user = User.query.filter_by(reset_token=token).first()

    if not user:
        flash("Invalid or expired reset link.", "error")
        return redirect(url_for("auth.forget_password"))

    if request.method == "POST":
        new_password = request.form.get("password").strip()

        if not new_password:
            return redirect(url_for("auth.set_password", token=token))

        user.set_password(new_password)
        user.reset_token = None
        db.session.commit()

        flash("Password updated successfully!", "success")
        return redirect(url_for("auth.login"))

    return render_template('auth/setpassword.html', token=token)