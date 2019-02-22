from rest_framework import serializers
from django.contrib.auth.models import User
from vehicles.models import Requests, District, TypeRequest, TypeCar, Car, Department, ModelCar



class UserSerializer(serializers.ModelSerializer):
    """Сериализация пользователей"""
    class Meta:
        model = User
        fields = (
            "id",
            "username",
        )

class DepartmentSerializer(serializers.ModelSerializer):
    """Сериализация спр служб"""
    class Meta:
        model = Department
        fields = (
            "id",
            "name",
        )

class FilterDepartmentSerializer(serializers.ModelSerializer):
    """Сериализация спр служб"""
    class Meta:
        model = Department
        fields = (
            "name",
        )

class DistrictSerializer(serializers.ModelSerializer):
    """Сериализация спр. районов"""
    class Meta:
        model = District
        fields = (
            "id",
            "name",
        )

class TypeRequestSerializer(serializers.ModelSerializer):
    """Сериализация спр. тип заявки"""
    class Meta:
        model = TypeRequest
        fields = (
            "id",
            "name",
        )

class TypeCarSerializer(serializers.ModelSerializer):
    """Сериализация спр. типов АТС"""
    class Meta:
        model = TypeCar
        fields = (
            "id",
            "name",
        )

class ModelCarSerializer(serializers.ModelSerializer):
    """Сериализация моделей АТС"""
    class Meta:
        model = ModelCar
        fields = (
            "id",
            "name",
        )

class CarSerializer(serializers.ModelSerializer):
    """Сериализация спр. автомобилей"""
    car_model = ModelCarSerializer()
    type_car = TypeCarSerializer()
    district = DistrictSerializer()
    class Meta:
        model = Car
        fields = (
            "id",
            "car_model",
            "gos_nomer",
            "type_car",
            "district",
        )

class RequestsSerializer(serializers.ModelSerializer):
    """Сериализация заявок"""
    type_request = TypeRequestSerializer()
    car = CarSerializer()
    department = DepartmentSerializer()
    creater = UserSerializer()

    class Meta:
        model = Requests
        fields = (
            "id",
            "type_request",
            "car", "department",
            "date_request",
            "time_start_request",
            "time_end_request",
            "description",
            "comment",
            "creater",
            "date_creater",
            "status",
        )

class RequestsPostSerializer(serializers.ModelSerializer):
    """Сериализация заявок"""
    type_request = TypeRequestSerializer()
    car = CarSerializer()
    department = DepartmentSerializer()
    creater = UserSerializer()

    class Meta:
        model = Requests
        fields = (
            "type_request",
            "car", "department",
            "date_request",
            "time_start_request",
            "time_end_request",
            "description",
            "comment",
            "creater",
            "status",
        )