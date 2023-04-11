from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 5) # Show 5 posts per page
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {'posts': posts}
    return render(request, 'myblog/post_list.html', context)

def about(request):
    return render(request, 'myblog/about.html', {})



@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'myblog/post_form.html', {'form':form})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request,'myblog/post_detail.html', {'post':post})

@login_required
def post_update(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=post)
    return render(request,'myblog/post_form.html', {'form':form})

@login_required
def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('post_list')

