from django import forms
from taggit.forms import TagWidget
from .models import Post

class PostForm(forms.ModelForm):
    tags = forms.CharField(
        widget=TagWidget(),  
        required=False
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'tags', 'image']