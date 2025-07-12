from django.db import models
from django.contrib.auth.models import User
from skills.models import Skill

class SwapRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('cancelled', 'Cancelled'),
    ]

    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_swaps')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_swaps')
    offered_skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='offered_in_swaps')
    wanted_skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='wanted_in_swaps')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.username} offers {self.offered_skill.name} for {self.receiver.username}'s {self.wanted_skill.name}"

# Create your models here.
