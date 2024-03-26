from django.urls import path
# import all views from app1/views.py
from . import views

urlpatterns = [
    path('hello/', views.say_hello),
    path('profile/', views.return_json)
]