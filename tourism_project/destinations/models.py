from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    city = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

