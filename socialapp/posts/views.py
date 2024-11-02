from django.shortcuts import render
from .forms import PostCreateForm
from django.contrib.auth.decorators import login_required
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

