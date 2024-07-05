# tree/urls.py

from django.urls import path
from . import views

app_name = 'tree'

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_person, name='add_person'),
    path('api/persons/', views.person_list, name='person_list'),
]
