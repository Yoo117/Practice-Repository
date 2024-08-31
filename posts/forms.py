from django import forms
from taggit.forms import TagWidget
from taggit.models import Tag

from .models import Post

class PostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(), 
        widget=forms.CheckboxSelectMultiple, # 여러 개 선택 가능하도록 체크박스 사용
        required=False # 선택사항이 없어도 가능하게 구현
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'tags', 'image']
