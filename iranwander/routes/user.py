from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user, logout_user

from ..models import db

user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('/panel')
@login_required
def panel():
    return render_template('panel_admin.html', current_user=current_user)


@user_bp.route('/change_password', methods=['POST'])
@login_required
def change_password():
    new = request.form.get('new_password')
    confirm = request.form.get('confirm_password')

    if not new or not confirm:
        flash('همه فیلدها را پر کنید.', 'error')
    elif new != confirm:
        flash('رمزهای جدید با هم برابر نیستند.', 'error')
    elif len(new) < 6:
        flash('رمز عبور باید حداقل ۶ کاراکتر باشد.', 'error')
    else:
        current_user.set_password(new)
        db.session.commit()
        flash('password was changed successfully!', 'success')

    return redirect(url_for('user.panel'))

@user_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash("you have been logged out!", 'success')
    return redirect(url_for('main.index'))
