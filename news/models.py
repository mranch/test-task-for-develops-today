from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField()
    creation_date = models.DateTimeField(default=timezone.now)
    amount_of_upvotes = models.IntegerField(default=0)
    author_name = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField()
    creation_date = models.DateTimeField(default=timezone.now)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    amount_of_upvotes = models.IntegerField(default=0)
    author_name = models.CharField(max_length=50)

    def __str__(self):
        return self.content
