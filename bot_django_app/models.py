from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    eamil = models.EmailField()
    date_of_birth = models.DateField()
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
