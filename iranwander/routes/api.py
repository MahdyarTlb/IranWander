from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from ..models import db, City
import re

api = Blueprint('api', __name__, url_prefix='/api')

subscribers = set()

@api.route("/subscribe", methods=["POST"])
def subscribe():
    try:
        data = request.get_json()
        email = data.get("email", "").strip().lower()

        if not email or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return jsonify({"success": False, "error": "email is incorrect"})

        if email in subscribers:
            return jsonify({"success": True, "message": "again!?"})

        with open("emails.txt", "a") as f:
            f.write(email + "\n")

        subscribers.add(email)
        print(f"new user: {email}")

        return jsonify({"success": True})

    except Exception as e:
        return jsonify({"success": False, "error": "server error"})

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
        current_user.favorites.remove(city)
        action = 'unliked'
    else:
        current_user.favorites.append(city)
        action = 'liked'

    db.session.commit()

    return jsonify({'ok': True, 'action': action, 'city_id': city_id})