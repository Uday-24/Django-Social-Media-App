from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from .models import Post
from .forms import PostCreateForm, CommentForm
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
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        new_comment = comment_form.save(commit=False)
        post_id = request.POST.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        new_comment.post = post
        new_comment.save()
    else:
        comment_form = CommentForm()
    posts = Post.objects.all()
    logged_user = request.user

    return render(request, "posts/feed.html", {'posts':posts, 'logged_user':logged_user, 'comment_form':comment_form})

def like_post(request):
    if request.method == "POST":
        post_id = request.POST.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        
        # Check if the user has already liked the post
        if post.liked_by.filter(id=request.user.id).exists():
            # If the user already liked the post, remove the like
            post.liked_by.remove(request.user)
            message = "Unliked"
        else:
            # If the user hasn't liked the post, add the like
            post.liked_by.add(request.user)
            message = "Liked"
        
        # Optional: Return a JSON response for more flexibility
        return HttpResponse(message)
    else:
        return HttpResponse("Invalid request method.", status=400)