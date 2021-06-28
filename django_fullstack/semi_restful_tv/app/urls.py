from django.urls import path

from . import views

urlpatterns = [
    path('', views.toshow),
    path('shows', views.shows),
    path('shows/new', views.new_show),
    path('shows/create', views.create_show),
    path('shows/<int:show_id>', views.display_show),
    path('shows/<int:show_id>/destroy', views.destroy),
    path('shows/<int:show_id>/edit', views.edit),
    path('shows/<int:show_id>/update', views.update)
]