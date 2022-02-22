from django.shortcuts import render
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    """
    Will list all posts which have a status = 1 through index.html template
    Showing 6 posts followed by auto django paging
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6
