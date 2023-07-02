from django.db import models
from django.utils import timezone
# Create your models here.


class Post (models.Model):
    content = models.TextField (max_length=10000)
    image = models.ImageField (upload_to= 'postImages')
    date = models.DateTimeField(timezone.now)
    user = models.ForeignKey ('User' , related_name='Post_User', on_delete=models.CASCADE)
    def __str__(self):
        return str(self.user)

class User (models.Model):
    
    name = models.CharField (max_length=50)
    bio = models.CharField (max_length=100)
    image = models.ImageField(upload_to='Uimages')
    def __str__(self):
        return self.name

class Like (models.Model):
    like = models.IntegerField()
    user = models.ManyToManyField (Post , related_name= 'Like_Post')
    
    def __str__(self):
        return str(self.user)
class Comment (models.Model):
    content = models.CharField (max_length= 500)
    date = models.DateTimeField (timezone.now)
    user = models.ForeignKey (User , related_name= 'Comment_User', on_delete=models.CASCADE)
    post = models.ForeignKey (Post , related_name= 'comment_Post' , on_delete= models.CASCADE)
    def __str__(self):
        return str(self.user)
