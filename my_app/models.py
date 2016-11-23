from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Person(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length = 100)
    gender = models.CharField(max_length = 6, default = "male")
    experience_year = models.IntegerField()
    age = models.IntegerField()
    title = models.CharField(max_length = 100)
    location = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = 'person_images', default = 'default.png')
    likes = models.IntegerField(default = 0)
    def __str__(self):
        return 'NAME: ' + self.name + ', TITLE: ' + self.title
