from django.db import models
from django.contrib.auth.models import User
from django.forms import Textarea

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-date_posted']
        verbose_name_plural = 'Posts'

