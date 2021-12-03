from django.db import models


class User(models.Model):
    # id
    # username = models.CharField(max_length=20)  #id

    api_key = models.CharField(max_length=60, primary_key=True)
    api_secret = models.CharField(max_length=60)

    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
