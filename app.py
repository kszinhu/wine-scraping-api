from flask import Flask, jsonify
from flask_restplus import Api
from ma import ma
from db import db

from marshmallow import ValidationError

from server.instance import server

api = server.api
app = server.app

@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    server.run()
