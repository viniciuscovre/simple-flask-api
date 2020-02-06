from marshmallow import Schema, fields, validate


class UserSchema(Schema):
    name = fields.Str(required=True)
    date_of_birth = fields.Str(required=True, validate=validate.Length(min=10))
    job = fields.Str(required=True, validate=validate.Length(min=2))
