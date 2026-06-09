from django.db import models
from django.contrib.auth.models import User
class Post(models.Model):
 user=models.ForeignKey(User,on_delete=models.CASCADE)
 content=models.TextField()
class Comment(models.Model):
 user=models.ForeignKey(User,on_delete=models.CASCADE)
 post=models.ForeignKey(Post,on_delete=models.CASCADE)
 text=models.TextField()
class Like(models.Model):
 user=models.ForeignKey(User,on_delete=models.CASCADE)
 post=models.ForeignKey(Post,on_delete=models.CASCADE)
class Follow(models.Model):
 follower=models.ForeignKey(User,related_name='f1',on_delete=models.CASCADE)
 following=models.ForeignKey(User,related_name='f2',on_delete=models.CASCADE)
