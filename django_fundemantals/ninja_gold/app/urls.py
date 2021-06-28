from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('process_gold', views.process_gold),
    path('clear', views.clear)
    ]