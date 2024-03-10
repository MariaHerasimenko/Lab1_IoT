from marshmallow import Schema, fields
from projectSchema.accelerometer_schema import AccelerometerSchema
from projectSchema.gps_schema import GpsSchema
from projectSchema.parking_schema import ParkingSchema
from domain.aggregated_data import AggregatedData

class AggregatedDataSchema(Schema):
    accelerometer = fields.Nested(AccelerometerSchema)
    gps = fields.Nested(GpsSchema)
    time = fields.DateTime('iso')
    parking = fields.Nested(ParkingSchema)