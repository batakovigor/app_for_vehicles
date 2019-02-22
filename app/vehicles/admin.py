from django.contrib import admin

from vehicles.models import Requests, District, TypeRequest, TypeCar, Car, Department, ModelCar

class RequestsAdmin(admin.ModelAdmin):

    list_dysplay = ("type_request", "car", "department", "date_request", "time_start_request", "time_end_request", "description", "comment", "creater", "date_creater", "status")

class DistrictAdmin(admin.ModelAdmin):

    list_dysplay = ("name")

class TypeRequestAdmin(admin.ModelAdmin):

    list_dysplay = ("name")

class TypeCarAdmin(admin.ModelAdmin):

    list_dysplay = ("type_car")

class CarAdmin(admin.ModelAdmin):

    list_dysplay = ("car_model", "gos_nomer", "type_car", "district")

class DepartmentAdmin(admin.ModelAdmin):

    list_dysplay = ("name")

class ModelCarAdmin(admin.ModelAdmin):

    list_dysplay = ("name")

admin.site.register(Requests, RequestsAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(TypeRequest, TypeRequestAdmin)
admin.site.register(TypeCar, TypeCarAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(ModelCar, ModelCarAdmin)