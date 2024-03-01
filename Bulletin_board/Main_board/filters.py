from django_filters import FilterSet
from .models import Post, Response

class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'author': ['exact'],
            'category': ['exact']
        }
        
class SingleUserPostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'category': ['exact'],
        }
        
class ResponseFilter(FilterSet):
    class Meta:
        model = Response
        fields = {
            'post': ['exact'],
        }
        
