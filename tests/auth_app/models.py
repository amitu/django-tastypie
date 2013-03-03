from django.db import models


class User(models.Model):
    identifier = models.CharField(unique=True, max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'identifier'
