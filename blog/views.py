from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post
# Create your views here.

class BlogListView(ListView):
    model = Post
    context_object_name = 'all_posts'
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    # the detailed view provides the context 
    # name as either object or lower case nae of our model
    template_name = 'post_detail.html' 
    