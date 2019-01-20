from django.urls import path
from . import views

urlpatterns = [
    path('', views.progress, name='progress'),
    path('add', views.add, name='add'),
    path('remove/<int:id>', views.remove, name='remove'),
]
