from django.urls import path
from . import views

urlpatterns = [
    path('', views.consulting, name='consulting'),
]