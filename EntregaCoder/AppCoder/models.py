from django.db import models

class productos(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    thumbnail = models.CharField(max_length=400)

class chat(models.Model):
    user = models.EmailField(max_length=100)
    message = models.CharField(max_length=200)
    date = models.DateTimeField()

class infoUsers(models.Model):
    user = models.CharField(max_length=100)
    lastmessagedate = models.DateTimeField()