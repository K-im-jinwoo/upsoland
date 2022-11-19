from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('', views.post_list, name='post_list'),
]