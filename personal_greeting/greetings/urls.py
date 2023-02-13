from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.greeting_view, name='greeting'),
]