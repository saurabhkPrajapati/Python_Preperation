from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    name = fields.String(required=True, validate=validate.Length(min=5, max=30))
    email = fields.Email(required=True, validate=validate.Length(min=10, max=100))

# Create a schema instance
user_schema = UserSchema()


class RegistrationSchema(Schema):
    username = fields.String(required=True, validate=validate.Length(min=5, max=30))
    password = fields.String(required=True, validate=validate.Length(min=8, max=20))  # Fixed password type

# Create a schema instance
registration_schema = RegistrationSchema()
