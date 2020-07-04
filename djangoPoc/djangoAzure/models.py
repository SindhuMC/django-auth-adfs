from django.db import models


class Users(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)