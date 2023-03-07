from django.urls import path
from . import views

urlpatterns = [
    path('car_list/', views.car_list, name='car_list'),
    path('car_list/<int:car_id>/', views.car_detail, name='car_detail'),
]
