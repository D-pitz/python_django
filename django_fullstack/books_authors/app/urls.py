from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('create_book', views.create_book),
    path('books/<int:books_id>', views.view_book),
    path('add_auth/<int:book_id>', views.add_auth),
    path('delete_auth_from_book/<int:book_id>/<int:auth_id>', views.delete_auth_from_book),
    path('return_home_book', views.return_home_book),
    path('author_home', views.author_home),
    path('create_auth', views.create_auth),
    path('author/<int:auth_id>', views.view_author),
    path('add_book/<int:auth_id>', views.add_book),
    path('delete_book_from_auth/<int:auth_id>/<int:book_id>', views.delete_book_from_auth),
    path('delete_author/<int:auth_id>', views.delete_author),
    path('delete_book/<int:book_id>', views.delete_book)
    ]