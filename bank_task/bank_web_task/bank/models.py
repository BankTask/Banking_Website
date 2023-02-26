from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=250)
    password = models.CharField(max_length=50)
    cpassword = models.CharField(max_length=50)

    def __str__(self):
        return self.username

class District(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class City(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

