from app import app, db
from db import User

# Import all models here
from db import User

def create_tables():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    create_tables()
