from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.
class School(models.Model):
    """docstring for School"""

    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('basic_app:detail', kwargs={'pk': self.pk})


class Student(models.Model):
    """docstring for Student"""
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, related_name='students')

    def __str__(self):
        return self.name
