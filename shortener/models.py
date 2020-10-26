from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Url(models.Model):
  redirect = models.TextField()
  visits = models.IntegerField(default = 0)
  alias = models.CharField(unique = True, max_length = 10, default = 'somerandom')

class User(AbstractUser):
  urls = models.ForeignKey(to = Url, on_delete= models.CASCADE, related_name = 'owner', blank = True, null =True)
