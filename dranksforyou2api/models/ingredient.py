from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=100, default='default_image_url.jpg')
