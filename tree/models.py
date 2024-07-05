# tree/models.py

from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.SET_NULL)
    spouse = models.OneToOneField('self', null=True, blank=True, related_name='partner', on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
