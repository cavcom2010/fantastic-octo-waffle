from django import forms
from .models import Post
from django.utils.html import format_html, html_safe

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content',]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'cols': '50', 'rows': '10'}),
        }
        labels = {
            'title': 'Title',
            'content': '',
        }
        # help_texts = {
        #     'title': 'Title here',
        #     'content': 'Content',
        # }
        error_messages = {
            'title': {
              'required': 'Title is required',
            },
            'content': {
            
             'required': 'Content is required',
            },
        }





    




