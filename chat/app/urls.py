from django.urls import path
from app import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('<str:room>/', views.RoomView.as_view(), name='room'),
    path('check/', views.CheckView.as_view(), name='check'),
]
