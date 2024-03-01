from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView, FormView
from .filters import PostFilter
from .models import *
from .forms import PostForm, ResponseForm
from .custom_utils import make_slug
from django.urls import reverse_lazy
# Create your views here.
class PostList(ListView):
    model = Post
    ordering = ['creation_date']
    template_name = 'post_list.html'
    context_object_name = 'posts'
    paginate_by = 2
    
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context
    
class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

def search(request):
    queryset = Post.objects.all()
    filterset = PostFilter(request.GET, queryset)
    context = {'filterset': filterset}
    return render(request, 'search.html', context)

class PostCreate(LoginRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Create Post'
        return context
    
    def form_valid(self, form):
        new_post = form.save(commit=False)
        if self.request.method == 'POST':
            new_post.author = self.request.user
            new_post.slug = make_slug(new_post.title)
        new_post.save()
        return super().form_valid(form)

class PostUpdate(LoginRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Update Post'
        return context
    
    def form_valid(self, form):
        if self.request.method == "POST":
            if self.request.user == self.get_object().author:
                return super().form_valid(form)
            elif self.request.user != self.get_object().author:
                return HttpResponseRedirect('/mainboard/delerror')
    
class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Delete Post'
        return context
    
    def form_valid(self, form):
        if self.request.method == "POST":
            if self.request.user == self.get_object().author:
                return super().form_valid(form)
            elif self.request.user != self.get_object().author:
                return HttpResponseRedirect('/mainboard/delerror')
            
def delerror(request):
    return render(request, 'delerror.html')

def start_page(request):
    return HttpResponseRedirect('/mainboard/')

class ProfileView(LoginRequiredMixin, ListView):
    model = Post
    ordering = ['creation_date']
    template_name = 'profile.html'
    context_object_name = 'posts'
    paginate_by = 2
    
    def get_queryset(self):
        return Post.objects.filter(author=self.request.user).order_by('creation_date')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['path'] = self.request.path
        return context
    
class ResponseCreate(LoginRequiredMixin, CreateView):
    template_name = 'response_create.html'
    form_class = ResponseForm
    success_url = ''
    model = Response
    success_url = '/mainboard/'
    
    def get_queryset(self):
        return Post.objects.all()
    
    def form_valid(self, form):
        new_response = form.save(commit=False)
        if self.request.method == 'POST':
            new_response.author = self.request.user
            new_response.slug = make_slug(new_response.text[:10])
            new_response.post = self.get_object()
        new_response.save()
        return super().form_valid(form)