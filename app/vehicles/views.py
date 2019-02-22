from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status

from vehicles.models import Requests, District, TypeRequest, TypeCar, Car, Department, ModelCar
from vehicles.serializers import RequestsSerializer, RequestsPostSerializer, UserSerializer, DistrictSerializer, TypeRequestSerializer, TypeCarSerializer, CarSerializer, DepartmentSerializer, ModelCarSerializer, FilterDepartmentSerializer

def combine(keys, values):
    "generate a dictionary from keys and values"
    out = {}
    for k,v in zip(keys,values):
       out[k] = v
    return out

def combine_each(keys, values):
    "for each pair of keys and values, make a dictionary"
    return [combine(klist, vlist) for (klist,vlist) in zip(keys,values)]

class Departments(APIView):
    """Спр. служб"""
    def get(self, request):
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response({"data": serializer.data})

class FilterDepartments(APIView):
    """Спр. служб"""

    def get(self, request, format=None):
        departments = [department.name for department in Department.objects.all()]
        return Response(departments)
        #departments = []

        #for department in Department.objects.all():

        #    departments.append("{text: '" + department.name + "', value: '" + department.name + "'}")


        #return Response(departments)


class ModelCars(APIView):
    """Модель АТС"""
    def get(self, request):
        model_cars = ModelCar.objects.all()
        serializer = ModelCarSerializer(model_cars, many=True)
        return Response({"data": serializer.data})

class Cars(APIView):
    """АТС"""
    def get(self, request):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response({"data": serializer.data})

class TypeCars(APIView):
    """Типы АТС"""
    def get(self, request):
        type_cars = TypeCar.objects.all()
        serializer = TypeCarSerializer(type_cars, many=True)
        return Response({"data": serializer.data})

class Districts(APIView):
    """Районы"""
    def get(self, request):
        districts = District.objects.all()
        serializer = DistrictSerializer(districts, many=True)
        return Response({"data": serializer.data})

class TypeRequests(APIView):
    """Типы заявок"""
    def get(self, request):
        type_requests = TypeRequest.objects.all()
        serializer = TypeRequestSerializer(type_requests, many=True)
        return Response({"data": serializer.data})

class AllRequest(APIView):
    """Заявки"""

    def get(self, request):
        requests = Requests.objects.all()
        serializer = RequestsSerializer(requests, many=True)
        return Response({"data": serializer.data})


class Request(APIView):
    """Заявка"""

    permission_classes = [permissions.IsAuthenticated, ]
    #permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        record = request.GET.get("id")
        requests = Requests.objects.filter(id=record)
        serializer = RequestsSerializer(requests, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        record_request = RequestsPostSerializer(rec=request.data)
        if record_request.is_valid():
            record_request.save(user=request.user)
            return Response(record_request, status=status.HTTP_201_CREATED)
        else:
            return Response(record_request.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        pass