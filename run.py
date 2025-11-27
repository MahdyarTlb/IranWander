from iranwander import create_app
from flask_compress import Compress
from flask import send_from_directory


app = create_app()
Compress(app)

@app.route('/static/<path:path>')
def send_static(path):
    response = send_from_directory('static', path)
    response.headers['Cache-Control'] = 'public, max-age=31536000, immutable'
    return response

if __name__ == '__main__':
    app.run(debug=True)