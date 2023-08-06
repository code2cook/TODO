from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#  title 
#  status
#  date - current 
#  user 
#  priority

    
class UploadedPicture(models.Model):
    id = models.AutoField(primary_key=True)
    foodName = models.CharField(max_length=100)
    comment = models.TextField(max_length=200)
    image_url = models.URLField()
