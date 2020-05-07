from http import HTTPStatus as Http
import sqlite3

from flask_restful import Resource

from models.posts import PostModel


class Post(Resource):
    def get(self, _id):
        pass

    def post(self, _id):
        pass

    def delete(self, _id):
        pass

    def put(self, _id):
        pass
