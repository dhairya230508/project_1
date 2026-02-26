from django.db import models

from django.contrib.auth.models import User

class Tweet(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField(max_length=240)
    photo = models.ImageField(upload_to='photos/',blank=True,null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    like = models.ManyToManyField(User, related_name='liked_tweets',blank=True)
    # comment = models.TextField(max_length=2000)
    def __str__(self):
        return f'{self.user.username} - {self.text[:10]}'
    def total_likes(self):
        return self.like.count()

class Comment(models.Model):
    tweet = models.ForeignKey(
        Tweet,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)