from django.urls import path, include
from . import views


urlpatterns = [
    path('requests/', views.AllRequest.as_view(), name='requests'),
    path('request/', views.Request.as_view(), name='request'),
    path('districts/', views.Districts.as_view(), name='districts'),
    path('type-requests/', views.TypeRequests.as_view(), name='type_request'),
    path('type-cars/', views.TypeCars.as_view(), name='type_cars'),
    path('cars/', views.Cars.as_view(), name='cars'),
    path('departments/', views.Departments.as_view(), name='departments'),
    path('filter-departments/', views.FilterDepartments.as_view(), name='filter_departments'),
    path('model-cars/', views.ModelCars.as_view(), name='model_cars'),
]