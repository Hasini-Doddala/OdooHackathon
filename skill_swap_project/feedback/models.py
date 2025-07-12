from django.db import models
from django.contrib.auth.models import User
from swaps.models import SwapRequest

class Feedback(models.Model):
    swap = models.OneToOneField(SwapRequest, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comments = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reviewer.username} rated {self.swap}"

# Create your models here.
