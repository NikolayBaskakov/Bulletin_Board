from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Post

class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=30)
    
    class Meta:
        model = Post
        fields = [
            'title',
            'text',
            'category'
        ]
        widgets = {
            'text': SummernoteWidget()
        }