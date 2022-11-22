from django.db import models
from django.contrib.auth.models import User



# Create your models her

class Post(models.Model):
    title = models.CharField(max_length=10)
    image = models.ImageField()
    description = models.TextField()
    rate = models.IntegerField()
    hashtags = models.ManyToManyField("Hashtag", blank=True)


class Hashtag(models.Model):
    text = models.TextField()
    posts = models.ManyToManyField(Post, blank=True)

class Coments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
