from django.db import models
from .user import User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_total = models.DecimalField(max_digits=10, decimal_places=2)
    payment_type = models.CharField(max_length=50)
