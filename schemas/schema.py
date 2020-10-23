from marshmallow import Schema, fields, pre_load, post_load

class AcceptSchema(Schema):
    response_id = fields.UUID()
    lead_id = fields.Str()
    bac_score = fields.Str()
    accept_at_lead_price = fields.Int()
    decision = fields.Str(default='accept')
