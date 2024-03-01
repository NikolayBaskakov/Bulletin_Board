from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', PostList.as_view(), name='post-list'),
    path('search/', search, name='search'),
    path('delerror/', delerror, name='delerror'),
    path('create/', PostCreate.as_view(), name='post-edit'),
    path('profile/', profile, name='profile'),
    path('posts/',  UserPostsView.as_view(), name='user-posts'),
    path('responses/', UserResponsesView.as_view(), name='user-responses'),
    path('<slug:slug>/', PostDetail.as_view(), name='post-detail'),
    path('<slug:slug>/update/', PostUpdate.as_view(), name='update-view'),
    path('<slug:slug>/delete/', PostDelete.as_view(), name='post-delete'),
    path('<slug:slug>/setresponse/', ResponseCreate.as_view(), name='set-response'),
    
]
