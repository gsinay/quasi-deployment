from django.db import models
from django.contrib.auth.models import User

class UserProfileinfo(models.Model):
    user = models.OneToOneField(User)
    date_of_birth = models.DateField()
    profile_pic = models.ImageField(null = True, blank = True)

    def __str__(self):
        return self.user.username
class Feedback(models.Model):
    name = models.CharField(max_length=120)
    details = models.TextField()
    happy = models.BooleanField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name






# Create your models here.
