from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    national_id = models.CharField(max_length=20, unique=True)
    badge_number = models.CharField(max_length=50, unique=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Profile - {self.department}"