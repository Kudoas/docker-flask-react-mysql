from flask import jsonify
from flask_restful import Resource, Api

from .models import User as UserModel, to_dict

api = Api()


class User(Resource):
    def get(self):
        return jsonify([to_dict(user) for user in UserModel.query.all()])


api.add_resource(User, '/')
