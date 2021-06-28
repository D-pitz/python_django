from django.db import models
from app_login.models import User

class MessageManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['message']) < 2 or len(postData['message']) > 500:
            errors['message'] = 'Message must be at least 2 characters'
        return errors

class CommentManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['comment']) < 2 or len(postData['comment']) >500 :
            errors['comment'] = 'Comment must be at least 2 characters'
        return errors

class Message(models.Model):
    message = models.TextField()
    user = models.ForeignKey(User, related_name= 'messages', on_delete= models.CASCADE) 
    #message
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = MessageManager()

class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, related_name= 'comments', on_delete= models.CASCADE)
    message = models.ForeignKey(Message, related_name='comments', on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CommentManager()
