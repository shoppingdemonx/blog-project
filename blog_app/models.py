from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.CharField(max_length=200)
    profile_pic = models.ImageField(upload_to='profile_pics/',blank=True,default='profile_pics/default_profile_pic.svg')
    
    def __str__(self):
        return self.user.username
    
STATUS_CHOICES = (
    ('Drafted','Drafted'),
    ('Published','Published')
)

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True,blank=True)
    content = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='Drafted')
    
    def __str__(self):
        return self.title
    

# Benefits of creating PostImages model:
#   -> Multiple images per post
#   -> Cleaner structure
#   -> Easy gallery support

class PostImages(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/%Y/%m/%d/',blank=True)
    
    def __str__(self):
        return f'{self.post.author.username}-{self.post.title}'