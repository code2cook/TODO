from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#  title 
#  status
#  date - current 
#  user 
#  priority
# python manage.py migrate --run-syncdb when make change to the db

class foodCard4(models.Model):
    id = models.AutoField(primary_key=True)
    foodName = models.CharField(max_length=100)
    author = models.CharField(max_length=20)
    like_count = models.PositiveIntegerField(default=0)
    dislike_count = models.PositiveIntegerField(default=0)
    image_url = models.URLField()
    
    def __str__(self):
        return self.foodName
    
    def get_comments(self):
        return Comment.objects.filter(food_card=self)
    
class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    food_card = models.ForeignKey(foodCard4, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    
