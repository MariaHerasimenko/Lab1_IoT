from marshmallow import Schema, fields
from domain.gps import Gps
from projectSchema.gps_schema import GpsSchema

class ParkingSchema(Schema):
    free_parking = fields.Boolean()
    gps = fields.Nested(GpsSchema)