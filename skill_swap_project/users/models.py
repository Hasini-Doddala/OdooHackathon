from django.db import models
from django.contrib.auth.models import User
from skills.models import Skill

AVAILABILITY_CHOICES = [
    ('Weekends', 'Weekends'),
    ('Evenings', 'Evenings'),
    ('Flexible', 'Flexible'),
]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100, blank=True, null=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    availability = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, default='Flexible')
    is_profile_public = models.BooleanField(default=True)
    is_banned = models.BooleanField(default=False)
    skills_offered = models.ManyToManyField(Skill, related_name='offered_by', blank=True)
    skills_wanted = models.ManyToManyField(Skill, related_name='wanted_by', blank=True)



    def __str__(self):
        return f"{self.user.username}'s profile"
     
# Create your models here.

