from django.db import models

class User(models.Model):
    name = models.CharField(max_length=55)
    email = models.EmailField()
    username = models.CharField(max_length=200)
    admin = models.BooleanField(default=False)
    uid = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
