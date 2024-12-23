"""Models for Blogly."""
# connect SQLAlchemy to the flask app
from flask_sqlalchemy import SQLAlchemy



# create a SQLAlchemy instance
db = SQLAlchemy()

# create logic to connect to the database
def connect_db(app):
    db.app = app
    db.init_app(app)

# models for the database
class User(db.Model):
    """User."""
    # table name
    __tablename__ = "users" 
    # columns
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    image_url = db.Column(db.String(255), nullable=False, default='https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png') 

    def full_name(self):
        # return f"{self.first_name} {self.last_name}"
        return f"{self.first_name} {self.last_name}"
    
    