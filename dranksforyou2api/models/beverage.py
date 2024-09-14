from django.db import models


class Beverage(models.Model):
    name = models.CharField(max_length=55)
    liquor_id = models.CharField(max_length=50)
    ingredient_id = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=100, default='default_image_url.jpg')
