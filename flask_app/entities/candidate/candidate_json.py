from marshmallow import Schema, fields


class CandidateJson(Schema):
    first_name = fields.Str(required=True)
    last_name = fields.Str()
    date_of_birth = fields.Date()
    years_of_experience = fields.Date()
    department = fields.Str()
    resume = fields.Str()

