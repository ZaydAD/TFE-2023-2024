
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('friend/<str:pk>', views.chat, name="chat"),
    path("update_profile", views.update_profile, name="update_profile"),
    path('user_login/', views.user_login, name="user_login"),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
]
