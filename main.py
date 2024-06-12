from rest_framework.utils import json

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serialized_car = CarSerializer(car)
    return json.dumps(serialized_car)


def deserialize_car_object(json_data: bytes) -> Car:
    deserialized_data = json.loads(json_data)
    car_serializer = CarSerializer(data=deserialized_data)
    if car_serializer.is_valid():
        return car_serializer.save()
    else:
        raise ValueError("Invalid data for deserialization")

