from django.urls import path
from .views import *
urlpatterns = [
    path('', index),
    path('add/', add, name='add_reuqest'),
]
