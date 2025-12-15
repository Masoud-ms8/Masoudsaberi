from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
