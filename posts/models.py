from django.db import models


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
