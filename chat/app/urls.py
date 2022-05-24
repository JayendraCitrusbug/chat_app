from django.urls import path
from app import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('check/', views.CheckView.as_view(), name='check'),
    path('room/<str:room>/', views.RoomView.as_view(), name='room'),
    path('send/', views.SendView.as_view(), name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
]
