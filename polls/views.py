from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def index(request):
    all_posts = Post.objects.all()
    context = {
        'posts': all_posts
    }
    return render(request, 'polls/index.html', context)

def details(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'polls/details.html', {'post':post})