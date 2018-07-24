from django.db import models

# Create your models here.

class UserModel(models.Model):  # We need to inherit the parent class for our custom model to be a valid model which is models.Model.
  email = models.EmailField()
  name = models.CharField(max_length=120)
  username = models.CharField(max_length=120)
  password = models.CharField(max_length=40)
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.username
