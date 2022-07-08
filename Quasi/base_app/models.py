from django.db import models
from django.contrib.auth.models import User

class UserProfileinfo(models.Model):
    user = models.OneToOneField(User)
    date_of_birth = models.DateField()
    profile_pic = models.ImageField(upload_to = 'profile_pics', blank = True)

    def __str__(self):
        return self.user.username





# Create your models here.
