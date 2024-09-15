from django.db import models
from .user import User

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=100, default='default_image_url.jpg')
    uid = models.ForeignKey(User, on_delete=models.CASCADE, default='1')
