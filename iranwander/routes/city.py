from flask import Blueprint, render_template, abort, jsonify, url_for, request
from ..models import City, Place 
from sqlalchemy import func

city = Blueprint('city', __name__, url_prefix='/city')

@city.route('/')
def list_cities():
    q = request.args.get('q', '').strip()

    if q:
        cities = City.query.filter(City.name.ilike(f'%{q}%')).order_by(City.name).all()
    else:
        cities = City.query.order_by(City.name).all()

    return render_template('cities/list.html', cities=cities, search_query=q)

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