from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
db = SQLAlchemy()

# class Breeds(db.Model):
#     """Data on the cat breed"""

#     __tablename__ = "breeds"

#     breed = db.Column(db.Text, primary_key=True, nullable=False)
#     origin = db.Column(db.Text, nullable=False, default='origin unknown') 
#     life_span = db.Column(db.Text, nullable=False, default=' No information')
#     description = db.Column(db.Text, nullable=False, default='No description about this breed')

#     cats = db.relationship("Cats", backref="breeds", cascade="all, delete-orphan")

class User(db.Model):
    """User in the system."""

    __tablename__ = 'users'

    username = db.Column(db.Text, nullable=False, primary_key=True, unique=True)
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)

    # cats = db.relationship("Cats", backref="user", cascade="all, delete")

    @classmethod
    def signup(cls, username, password, email):
        """Sign up user. Hashes password and adds user to system."""

        hashed = bcrypt.generate_password_hash(password)
        hashed_utf8 = hashed.decode("utf8")

        user = User(
            username=username,
            password=hashed_utf8,
            email=email
        )

        db.session.add(user)
        return user


    @classmethod
    def authenticate(cls, username, password):
        """Validate that user exists & password is correct.

        Return user if valid; else return False.
        """

        user = cls.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password, password):
            # return user instance
            return user
        else:
            return False

class Cats(db.Model):
    """Individual cats for adoption"""

    __tablename__ = "cats"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    img = db.Column(db.Text, nullable=False, unique=True)
    breed = db.Column(db.Text, nullable=False)
    # username = db.Column(db.Text, db.ForeignKey('users.username'), nullable=False)


class Adopt(db.Model):
    """The checkout for adopting cats"""

    __tablename__ = "adopt"

    adopt_id =  db.Column(db.Integer, primary_key=True, autoincrement=True)
    user = db.Column(db.Text, nullable=False)
    cat_name = db.Column(db.Text, nullable=False)
    cat_img = db.Column(db.Text, nullable=False)


class Cost(db.Model):
    """The checkout for adopting cats"""

    __tablename__ = "cost"

    cost_id =  db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Text, db.ForeignKey('users.username'), nullable=False)
    price = db.Column(db.Integer, nullable=False)



def connect_db(app):
    db.app = app
    db.init_app(app)