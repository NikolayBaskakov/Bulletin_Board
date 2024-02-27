from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'creation_date', 'author', 'category')
    
class PostSummernote(SummernoteModelAdmin):
    summernote_fields = ('text',)
    list_display = ('creation_date', 'id', 'author', 'category')
    
admin.site.register(Post, PostSummernote)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
admin.site.register(Category, CategoryAdmin)

class ResponseAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'date')
    
admin.site.register(Response, ResponseAdmin)