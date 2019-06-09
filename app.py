from flask import Flask
from flask_restful import Api, Resource
from flask_jwt import JWT

app = Flask(__name__)
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity)

if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)