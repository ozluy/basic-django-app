from __future__ import unicode_literals

from django.db import models

# Create your models here.
"""
Person(
name = 'Daenerys Targaryen',
age = 25,
experience_year =  2,
title = 'Back-end Developer',
location ='Trabzon',
avatar ='daenerys_targaryen.png')
"""

class Person(models.Model):
    name = models.CharField(max_length = 100)
    experience_year = models.IntegerField()
    age = models.IntegerField()
    title = models.CharField(max_length = 100)
    location = models.CharField(max_length = 100)
    avatar = models.CharField(max_length = 500)
    def __str__(self):
        return self.name
