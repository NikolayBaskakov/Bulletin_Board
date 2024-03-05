from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', PostList.as_view(), name='post-list'),
    path('search/', search, name='search'),
    path('response-search/', response_search, name='response-search'),
    path('post-search/', post_search, name='post-search'),
    path('delerror/', delerror, name='delerror'),
    path('create/', PostCreate.as_view(), name='post-edit'),
    path('profile/', profile, name='profile'),
    path('posts/',  UserPostsView.as_view(), name='user-posts'),
    path('responses/', UserResponsesView.as_view(), name='user-responses'),
    path('subscriptions/', subscriptions, name='subscriptions'),
    path('verification/', EmailVerifyView.as_view(), name='verification'),
    path('<slug:slug>/', PostDetail.as_view(), name='post-detail'),
    path('<slug:slug>/update/', PostUpdate.as_view(), name='update-view'),
    path('<slug:slug>/delete/', PostDelete.as_view(), name='post-delete'),
    path('<slug:slug>/setresponse/', ResponseCreate.as_view(), name='set-response'),
    
]
