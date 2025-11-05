from iranwander import create_app
from iranwander.extensions import db
from iranwander.models import User

app = create_app()

with app.app_context():
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")

    admin = User(username=username, is_admin=True)
    admin.set_password(password)

    db.session.add(admin)
    db.session.commit()

    print("✅ Admin user created successfully!")
