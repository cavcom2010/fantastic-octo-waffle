from django.contrib import admin
from django.contrib.auth.models import User

from .models import Post

admin.site.register(Post)
# admin.site.register(User) aleady registered in settings

class PostAdmin(admin.ModelAdmin):
    exclude = 'author'


