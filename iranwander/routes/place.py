from flask import Blueprint, render_template
from ..models import Place

place = Blueprint('place', __name__, template_folder='templates', url_prefix='/place')

@place.route('/')
def list_places():
    places = Place.query.all()
    return render_template('places/list.html', places=places)

@place.route('/<int:id>')
def details_place(id):
    place = Place.query.get_or_404(id)
    return render_template('places/details.html', place=place)