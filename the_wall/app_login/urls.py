from django.urls import path

from . import views

urlpatterns = [
    path('', views.login),
    path('user/create', views.create_user),
    path('user/login', views.user_login),
    path('logout', views.logout)
    ]
