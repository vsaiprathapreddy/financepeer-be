from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)

class Article(models.Model):
    title = models.CharField(max_length=500)
    body = models.CharField(max_length=2000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
