from django_filters import FilterSet
from .models import Post

class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'creation_date': ['gt'],
            'author': ['exact'],
            'category': ['exact']
        }