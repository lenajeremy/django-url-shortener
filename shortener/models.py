from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
  pass

class Url(models.Model):
  redirectToUrl = models.TextField()
  createdUrl = models.TextField(blank = True)
  visits = models.IntegerField(default = 0)
  alias = models.CharField(unique = True, max_length = 20)
  text_to_remember = models.CharField(max_length = 20)
  creator = models.ForeignKey(to = User, on_delete= models.CASCADE, related_name = 'urls', blank = True, null =True)
