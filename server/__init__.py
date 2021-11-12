from flask.app import Flask
from flask.globals import request

# SQL alchemy is how we connect to psql
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Text, Integer

def create_app():
    app = Flask("SQUIDbook")
    app.config.from_pyfile("server/config.py")
    db = SQLAlchemy(app)

    # This is our model for interacting with our sql database
    # But we need postgres to be running and the table to already be created
    # SQL Command to create the table
    # CREATE TABLE squid_users (id serial PRIMARY KEY, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL, debt INTEGER);
    class User(db.Model):
        __tablename__="squid_users"
        id = Column(Integer, primary_key=True)
        name = Column(Text)
        email = Column(Text)
        debt = Column(Integer)

        def __str__(self):
            return self.name


    @app.route("/", methods=["GET", "POST"])
    def index():
        return "Hello <br/> UwU"

    # squid game  id
    # name
    # debt
    # email
    # addresss
    # size
    @app.route("/profile/<id>", methods=["POST"])
    def add_user(id):
        req = request.get_json(force=True)
        print(req)
        user = User()
        user.id = id
        user.name = req["name"]
        user.email = req["email"]
        user.debt = req["debt"]
        db.session.add(user)
        db.session.commit()

        return f"I added the user with id:{id} to the database"


    @app.route("/profile", methods=["GET"])
    def get_user():
        users = User.query.all()
        return str([str(u)+"<br/>" for u in users])

    return app