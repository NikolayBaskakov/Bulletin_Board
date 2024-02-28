from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
class PostSummernote(SummernoteModelAdmin):
    summernote_fields = ('text',)
    list_display = ( 'id', 'slug',  'author', 'category', 'edit_date', 'creation_date')
    prepopulated_fields = {"slug": ("title",)}
    
admin.site.register(Post, PostSummernote)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
admin.site.register(Category, CategoryAdmin)

class ResponseAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'date')
    prepopulated_fields = {"slug": ("title",)}
admin.site.register(Response, ResponseAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active', )

admin.site.register(User, UserAdmin)