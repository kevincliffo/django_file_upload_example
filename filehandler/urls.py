from django.urls import path
from . import views

app_name = 'filehandler'

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.list, name='list'),
]