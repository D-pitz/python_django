from django.db import models

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = 'Title should be at least 2 characters'
        if len(postData['network']) < 3:
            errors['network'] = 'network must be at lest 3 characters'
        if len(postData['desc']) < 10:
            errors['desc'] = 'Description must be at least at least 10 characters'
        if Show.objects.filter(title= postData['title']):
            errors['title'] = 'This show already exists'
            return errors

class Show(models.Model):
    title = models.CharField(max_length=50)
    network = models.CharField(max_length=25)
    release_date = models.DateField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()