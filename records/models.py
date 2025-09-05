from django.db import models
from django.contrib.auth.models import User
class List(models.Model):
    name = models.CharField(max_length=25)
    phone = models.CharField(max_length=14)
    nationality = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='photo/', null=True, blank=True)
    national_id = models.CharField(max_length=15)
    crime_details = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"self.name"