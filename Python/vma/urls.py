from django.urls import path
from . import views

# URLConfiguration
# This is to call functions.
urlpatterns = [
    path('hello', views.say_hello) 
]