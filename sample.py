import time

from marshmallow import Schema, validate, fields, post_dump


class User(object):
    user_id: str
    name: str
    email: str

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def __repr__(self):
        return f"<{self.name}, {self.email}>"


class UserSchema(Schema):
    class Meta:
        strict = True

    user_id = fields.String(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(min=1, max=64))
    email = fields.Email(required=True, validate=validate.Email(error='Not a valid email address'))

    @post_dump(pass_many=False)
    def _post_dump(self, data, many=False, original_data=None):
        assert many is False, "@post_dump is set to pass_many=False. This function should not receive many=True"

        data['dumped_at'] = int(time.time())
        return data
