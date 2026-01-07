from django.db import models
from django.contrib.auth.models import User
from destinations.models import Destination

class Plan(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    destinations = models.ManyToManyField(Destination)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.title}"
