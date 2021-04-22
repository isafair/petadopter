from django import forms
from . import models

# Create your views here.


class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title', 'slug', 'author',
                  'content', 'thumb']
