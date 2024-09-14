from django.db import models
from .order import Order
from .beverage import Beverage

class OrderBeverage(models.Model):
    order= models.ForeignKey(Order, on_delete=models.CASCADE)
    beverage = models.ForeignKey(Beverage, on_delete=models.CASCADE)