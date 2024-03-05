from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
class PostSummernote(SummernoteModelAdmin):
    summernote_fields = ('text',)
    fields = ['title', 'text', 'category', 'slug']
    list_display = ( 'id', 'slug',  'author', 'category', 'edit_date', 'creation_date')
    prepopulated_fields = {"slug": ("title",)}
    
    def save_model(self, request, obj, form, change) -> None:
        obj.author = request.user
        return super().save_model(request, obj, form, change)
    
admin.site.register(Post, PostSummernote)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
admin.site.register(Category, CategoryAdmin)

class ResponseAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'date')
    prepopulated_fields = {"slug": ("text",)}
admin.site.register(Response, ResponseAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active', )

admin.site.register(User, UserAdmin)