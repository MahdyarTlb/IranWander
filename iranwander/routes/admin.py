import os

from flask import Blueprint, render_template, redirect, url_for, request, flash, current_app
from flask_login import current_user, login_required, login_user, logout_user
from ..models import db, User, City, Place
from werkzeug.utils import secure_filename


admin = Blueprint('admin', __name__, url_prefix='/admin')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in current_app.config.get('ALLOWED_EXT', {'png','jpg','jpeg','gif'})

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

    if not current_user.is_admin:
        return redirect(url_for('admin.login'))

    return render_template('admin/dashboard.html')

@admin.route('/cities')
@login_required
def manage_cities():

    cities = City.query.order_by(City.id.desc()).all()

    return render_template('admin/cities.html',cities=cities)

@admin.route('/cities/add', methods=['GET', 'POST'])
@login_required
def add_city():
    if request.method == 'POST':

        name = request.form.get('name')
        description = request.form.get('description')

        image_file = request.files.get('image')
        if image_file and image_file.filename != '' and allowed_file(image_file.filename):

            file_name = secure_filename(image_file.filename)
            upload_path = os.path.join(current_app.config['UPLOAD_FOLDER'], file_name)
            image_file.save(upload_path)

        if not name:
            flash('name is required!', 'error')

            return redirect(url_for('admin.add_city'))

        new_city = City(name=name, description=description, image=file_name)

        db.session.add(new_city)
        db.session.commit()

        flash(f'add {name} successfully!')

        return redirect(url_for('admin.manage_cities'))

    return render_template('admin/add_city.html')


@admin.route('/cities/edit/<int:city_id>', methods=['GET', 'POST'])
@login_required
def edit_city(city_id):
    city = City.query.get_or_404(city_id)

    if request.method == 'POST':

        city.name = request.form.get('name')
        city.description = request.form.get('description')
        image_file = request.files.get('image')

        if image_file and image_file.filename != '' and allowed_file(image_file.filename):
            if city.image:
                try:
                    old_path = os.path.join(current_app.config['UPLOAD_FOLDER'], city.image)
                    if os.path.exists(old_path):
                        os.remove(old_path)
                except Exception as e:
                    flash(f'error via saving image: {e}')

            file_name = secure_filename(image_file.filename)
            image_file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], file_name))
            city.image = file_name

        db.session.commit()

        flash(f'city {city.name} updated successfully!')
        return redirect(url_for('admin.manage_cities'))

    return render_template('admin/edit_city.html', city=city)

@admin.route('/cities/delete/<int:city_id>', methods=['POST'])
@login_required
def delete_city(city_id):
    city = City.query.get_or_404(city_id)

    if city.image:
        try:
            path = os.path.join(current_app.config['UPLOAD_FOLDER'], city.image)
            if os.path.exists(path):
                os.remove(path)
        except Exception as e:
            flash(f'error via deleting image: {e}')
    db.session.delete(city)
    db.session.commit()
    flash(f'city {city.name} deleted successfully!')
    return redirect(url_for('admin.manage_cities'))

@admin.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('admin.login'))

