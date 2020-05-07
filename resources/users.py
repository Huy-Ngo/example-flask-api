from http import HTTPStatus as Http
import sqlite3

from flask_restful import Resource

from models.users import UserModel


class User(Resource):
    def get(self, _id):
        user = UserModel.find_by_id(_id)
        if user is not None:
            return user.json(), Http.OK
        return {'message': 'User does not exist.'}, Http.NOT_FOUND

    def post(self, name):
        user = UserModel.find_by_name(name)
        if user is not None:
            return {'message': 'User already exists.'}, Http.BAD_REQUEST
        user = UserModel(name)

        try:
            user.save_to_db()
        except Exception:
            return {'message': 'An error occurred while adding item.'}, Http.INTERNAL_SERVER_ERROR

    def delete(self, _id):
        user = UserModel.find_by_id(_id)
        if user is None:
            return {'message': 'User does not exist.'}, Http.BAD_REQUEST
        user.delete_from_db()
        return {'message': 'User deleted.'}, Http.OK

    def put(self, _id):
        pass
