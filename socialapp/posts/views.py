from django.shortcuts import render
from .forms import PostCreateForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from .models import Post
# Create your views here.


@login_required(login_url='login')
def post_create(request):
    if request.method == "POST":
        form = PostCreateForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
    else:
        form = PostCreateForm()
    
    return render(request, 'posts/create.html', {'form': form})


def feed(request):
    posts = Post.objects.all()
    return render(request, "posts/feed.html", {'posts':posts})

def like_post(request):
    if request.method == "POST":
        post_id = request.POST.get('post_id')
        post = get_object_or_404(Post, id = post_id)
        if post.liked_by.filter(id=request.uer.id).exists():
            post.liked_by.remove(request.user)
        else:
            post.liked_by.filter(request.user)