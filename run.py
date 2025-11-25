from iranwander import create_app
from flask_compress import Compress
from flask import send_from_directory

app = create_app()
Compress(app)

@app.route('/static/<path:filename>')
def custom_static(filename):
    response = send_from_directory('static', filename)
    response.headers['Cache-Control'] = 'public, max-age=31536000, immutable'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    return response

if __name__ == '__main__':
    app.run(debug=True)