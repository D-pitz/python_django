from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('counter/increment/<int:counter_id>', views.counter),
    path('destroy_session', views.destroy_session)
    ]