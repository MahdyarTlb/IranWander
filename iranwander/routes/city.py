from flask import Blueprint, render_template, abort
from ..models import City, Place 
from sqlalchemy import func # 💡 برای جستجوی نام بدون حساسیت به حالت حروف

city = Blueprint('city', __name__, url_prefix='/city') 

@city.route('/')
def list_cities():
    cities = City.query.all()
    return render_template('cities/list.html', cities=cities)

@city.route('/<int:id>')
def details_city(id):
    city = City.query.get_or_404(id)
    return render_template('cities/details.html', city=city) 

@city.route('/<string:place_name>') 
def details_place(place_name):
    
    search_name = place_name.replace('-', ' ').lower()

    place = Place.query.filter(func.lower(Place.name) == search_name).first()
    
    if place is None:
        abort(404)
    
    return render_template('cities/attraction_detail.html', attraction=place)