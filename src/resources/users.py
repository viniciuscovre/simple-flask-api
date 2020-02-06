from functools import wraps

from flask_restful import Resource
from flask import request
from marshmallow import ValidationError

from src.utils import to_snake_case, to_camel_case
from src.serializers.user import UserSchema
from src.models import db, UserModel


def handle_validation_errors(func):
    @wraps(func)
    def _func(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValidationError as e:
            return e.messages, 400

    return _func


class Users(Resource):

    def get(self, id=None):

        if id is None:
            result = UserModel.query.all()
            users = UserSchema(many=True).dump(result)
            return to_camel_case(users)

        result = UserModel.query.get(id)
        user = UserSchema().dump(result)
        return to_camel_case(user)

    @handle_validation_errors
    def post(self):
        payload = to_snake_case(request.get_json())
        user = UserSchema().load(payload)
        user = UserModel(**user)

        try:
            db.session.add(user)
            db.session.commit()
            return 'User Successfully Created!', 201
        except Exception as e:
            db.session.rollback()
            raise e
