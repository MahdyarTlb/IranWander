from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from ..models import db, City

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/like', methods=['POST'])
@login_required
def toggle_like():
    data = request.get_json()
    city_id = data.get('city_id')
    if not city_id:
        return jsonify({'ok': False, 'error': 'no city_id'}), 400

    city = City.query.get(city_id)
    if not city:
        return jsonify({'ok': False, 'error': 'city not found'}), 404

    if city in current_user.favorites:
        # remove
        current_user.favorites.remove(city)
        action = 'unliked'
    else:
        # add
        current_user.favorites.append(city)
        action = 'liked'

    db.session.commit()

    return jsonify({'ok': True, 'action': action, 'city_id': city_id})