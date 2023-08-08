from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#  title 
#  status
#  date - current 
#  user 
#  priority

    
# class UploadedPicture(models.Model):
#     id = models.AutoField(primary_key=True)
#     foodName = models.CharField(max_length=100)
#     description = models.TextField(max_length=200)
#     image_url = models.URLField()

# class foodCard(models.Model):
#     id = models.AutoField(primary_key=True)
#     foodName = models.CharField(max_length=100)
#     comments = models.TextField(max_length=200)
#     image_url = models.URLField()
    

class foodCard3(models.Model):
    id = models.AutoField(primary_key=True)
    foodName = models.CharField(max_length=100)
    comments = models.TextField(max_length=200)
    author = models.CharField(max_length=20)
    like_count = models.PositiveIntegerField(default=0)
    dislike_count = models.PositiveIntegerField(default=0)
    image_url = models.URLField()