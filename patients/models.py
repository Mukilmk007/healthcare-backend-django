from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)

    age = models.IntegerField()

    gender = models.CharField(max_length=10)

    disease = models.CharField(max_length=255)

    def __str__(self):
        return self.name