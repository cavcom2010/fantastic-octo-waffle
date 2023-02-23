from django.db import models
from django.contrib.auth.models import User
from django.forms import Textarea

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(
            max_length=1000, help_text='Enter text please')
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
