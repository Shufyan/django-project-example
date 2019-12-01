from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True,max_length=254)

    def __str__(self):
        return str(self.first_name)

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.PROTECT)

    # additional
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username
