from django import forms
from .models import Post
from django.utils.html import format_html, html_safe

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content',]
        # widgets = {'content': forms.Textarea(attrs={'cols':80})}

