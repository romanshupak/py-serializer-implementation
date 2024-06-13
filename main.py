from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from car.models import Car
from car.serializers import CarSerializer
import io


def serialize_car_object(car: Car) -> bytes:
    serialized_car = CarSerializer(car)
    return JSONRenderer().render(serialized_car.data)


def deserialize_car_object(json_data: bytes) -> Car:
    deserialized_data = io.BytesIO(json_data)
    data = JSONParser().parse(deserialized_data)
    car_serializer = CarSerializer(data=data)
    if car_serializer.is_valid():
        car = Car(**car_serializer.validated_data)
        car.save()
        return car
