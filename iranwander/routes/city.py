from flask import Blueprint, render_template
from ..models import City

city = Blueprint('city', __name__, template_folder='templates', url_prefix='/city')

@city.route('/')
def list_cities():
    cities = City.query.all()
    return render_template('cities/list.html', cities=cities)

@city.route('/<int:id>')
def details_city(id):
    city = City.query.get_or_404(id)
    return render_template('cities/details.html', city=city)