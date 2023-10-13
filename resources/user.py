from flask import request
from flask_restful import Resource
from http import HTTPStatus
from models.user import User


class UserListResource(Resource):
    
    def post(self):

        user_data = request.get_json()

        username = user_data.get("username")
        password = user_data.get("password")

        if User.get_by_username(username=username):
            return {"message": "username already in use"}, HTTPStatus.BAD_REQUEST
        
        hashed_password = User.hash_password(password)

        user = User(
            # right side are user variable from this class
            # left side model class properties
            username=username,
            password=hashed_password
        )

        user.save()

        return user.data, HTTPStatus.CREATED