from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    tel_number = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
