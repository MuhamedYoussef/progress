from django.urls import path
from . import views

urlpatterns = [
    path('', views.progress, name='progress'),
    path('add', views.add, name='add')
]
