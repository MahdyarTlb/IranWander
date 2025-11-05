from flask import Blueprint, render_template, redirect, url_for, request, abort, flash
from flask_login import current_user, login_required, login_user, logout_user
from ..models import User

admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin.dashboard'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username, is_admin=True).first()

        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('admin.dashboard'))
        else:
            flash('Invalid username or password')

    return render_template('admin/login.html')

@admin.route('/dashboard')
@login_required
def dashboard():

    if not current_user.isadmin:
        return redirect(url_for('admin.login'))

    return render_template('admin/dashboard.html')

@admin.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('admin.login'))

