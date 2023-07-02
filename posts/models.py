from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Post (models.Model):
    content = models.TextField (max_length=10000)
    image = models.ImageField (upload_to= 'postImages')
    date = models.DateTimeField(timezone.now)
    likes = models.ManyToManyField(User, related_name='post_like')
    user = models.ForeignKey (User , related_name= 'User_Post' , on_delete= models.CASCADE)
    def __str__(self):
        return str(self.user)




    def __str__(self):
        return str(self.user)
class Comment (models.Model):
    content = models.CharField (max_length= 500)
    date = models.DateTimeField (timezone.now)
    user = models.ForeignKey (User , related_name= 'Comment_User', on_delete=models.CASCADE)
    post = models.ForeignKey (Post , related_name= 'comment_Post' , on_delete= models.CASCADE)
    def __str__(self):
        return str(self.user)
