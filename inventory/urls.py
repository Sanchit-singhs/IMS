from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('User_s/<int:pk>/', views.user_detail, name='user_detail'),
]