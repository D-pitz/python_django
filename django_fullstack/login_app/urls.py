from django.urls import path

from . import views

urlpatterns = [
    path('', views.login),
    path('users/create', views.create_user),
    path('users/login', views.user_login),
    path('users/logout', views.logout),
    ]
