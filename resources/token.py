from flask import request
from http import HTTPStatus
from flask_restful import Resource
from flask_jwt_extended import create_access_token
from models.user import User


class TokenResource(Resource):

    def post(self):
        """POST Method for User TokenResource."""
        json_data = request.get_json()
        username = json_data.get("username")
        password = json_data.get("password")

        user = User.get_by_username(username)

        # Returns true if normal password and hashed password correspond 
        # otherwise false
        if not user or not User.verify_password(password, user.password):
            return {"message": "login data is incorrect"}, HTTPStatus.UNAUTHORIZED
        
        access_token = create_access_token(identity=user.id)

        return {"access_token": access_token}, HTTPStatus.OK