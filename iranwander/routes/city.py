from flask import Blueprint, render_template
from ..models import City

city = Blueprint('city', __name__, template_folder='templates', url_prefix='/city')

@city.route('/')
def list_cities():
    cities = City.query.all()
    return render_template('cities/list.html', cities=cities)

@city.route('/<int:city_id>')
def details_city(city_id):
    city = City.query.get_or_404(city_id)
    return render_template('cities/detail.html', city=city)