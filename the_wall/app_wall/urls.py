from django.urls import path

from . import views

urlpatterns = [
    path('', views.the_wall),
    path('message', views.post_message),
    path('comment/post/<int:post_id>', views.post_comment),
    path('destroy/message/<int:post_id>', views.destroy_message),
    path('destroy/comment/<int:comment_id>', views.destroy_comment)
    ]