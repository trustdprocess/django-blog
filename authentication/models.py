from django.db import models
from django.contrib.auth.models import User

class MyModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    lastname=models.TextField(max_length=100)
    username=models.TextField(max_length=100)
    password=models.TextField(max_length=100)
    
    def __str__(self):
     return self.name
class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)
    
class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)
    

    

    

