from distutils.text_file import TextFile
from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=120)
    type = models.CharField(max_length=120, blank=True, null=True)
    ingredients = models.TextField(blank=True, null=True)
    prep_minutes = models.IntegerField(blank=True, null=True)
    number_served = models.IntegerField(blank=True, null=True)
    directions = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


