from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .filters import *
from .models import *
from .forms import *
from.signals import response_apply
from .custom_utils import make_slug
from django.urls import reverse_lazy
# Create your views here.
class PostList(ListView):
    model = Post
    ordering = ['creation_date']
    template_name = 'post_list.html'
    context_object_name = 'posts'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs
    
class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

def search(request):
    queryset = Post.objects.all()
    filterset = PostFilter(request.GET, queryset)
    context = {'filterset': filterset}
    return render(request, 'search.html', context)

def response_search(request):
    queryset = Response.objects.filter(post__author=request.user)
    filterset = ResponseFilter(request.GET, queryset)
    context = {'filterset': filterset}
    return render(request, 'response_search.html', context)

def post_search(request):
    queryset = Post.objects.filter(author=request.user)
    filterset = SingleUserPostFilter(request.GET, queryset)
    context = {'filterset': filterset}
    return render(request, 'post_search.html', context)

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

class UserResponsesView(LoginRequiredMixin, ListView):
    model = Response
    template_name = 'responses.html'
    context_object_name = 'responses'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = Response.objects.filter(post__author=self.request.user).order_by('date')
        self.filterset = ResponseFilter(self.request.GET, queryset)
        return self.filterset.qs
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'My responses'
        return context
    
    def post(self, request, *args, **kwargs):
            response_id = self.request.POST.get('response_id')
            response_obj = Response.objects.get(id=response_id)
            action = self.request.POST.get('action')
            
            if action == 'apply':
                response_obj.applied = True
                response_obj.save()
                response_apply.send(sender=self.__class__, class_obj=response_obj)
            elif action == 'deny':
                response_obj.delete()
            return HttpResponseRedirect('/mainboard/responses')
    
class UserPostsView(LoginRequiredMixin, ListView):
    model = Post
    ordering = ['creation_date']
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = Post.objects.filter(author=self.request.user)
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'My posts'
        return context
    
class ResponseCreate(LoginRequiredMixin, CreateView):
    template_name = 'response_create.html'
    form_class = ResponseForm
    success_url = ''
    model = Response
    success_url = '/mainboard/'
    
    
    def get_queryset(self):
        return Post.objects.all()
    
    def get(self, request, *args, **kwargs):
        if request.user == self.get_object().author:
            return HttpResponseRedirect('/mainboard/responses')
        else:
            return super().get(request, *args, **kwargs)
        
    def post(self, request, *args, **kwargs):
        reset = self.request.POST.get('reset')
        if reset == 'deny':
            return HttpResponseRedirect('/mainboard/')
        else:
            return super().post(request, *args, **kwargs)
        
    def form_valid(self, form):
        new_response = form.save(commit=False)
        if self.request.method == 'POST':
            new_response.author = self.request.user
            new_response.slug = make_slug(new_response.text[:10])
            new_response.post = self.get_object()
        new_response.save()
        return super().form_valid(form)
    
@login_required
def profile(request):
    context = {'user': request.user}
    return render(request, 'profile.html', context)