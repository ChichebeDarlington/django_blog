from django.shortcuts import render, redirect
from .models import Post
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

# Create your views here.
def posts_lists(request):
    posts = Post.objects.all().order_by("-date")
    context= {"posts":posts}
    return render(request, "posts/posts_lists.html", context)

def post_page(request, slug):
     post = Post.objects.get(slug=slug)
     context= {"post":post}
     return render(request, "posts/post_page.html", context)

@login_required(login_url="/users/login/")
def new_post(request):
    if request.method == "POST":
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid:
            # save form with user creator
            newpost = form.save(commit=False)
            newpost.author = request.user
            newpost.save()
            return redirect('posts:lists')
    form = forms.CreatePost()
    context = {"form":form}
    return render(request, "posts/new_post.html", context)


@login_required
def delete_view_post(request, id):
    post = get_object_or_404(Post, id=id)

    # Optional: ensure only author can delete
    if post.author != request.user:
        return redirect("posts:lists")
        messages.success(request, "Post deleted successfully!")
    if request.method == "POST":
        post.delete()
        return redirect("posts:lists")
    return render(request, "posts/confirm_delete.html", {"post": post})

@login_required
def update_view_post(request, id):
    post = get_object_or_404(Post, id=id)

    # security: only author can edit
    if post.author != request.user:
        return redirect("posts:lists")

    if request.method == "POST":
        form = forms.CreatePost(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("posts:page", slug=post.slug)
    else:
        form = forms.CreatePost(instance=post)

    return render(request, "posts/update.html", {
        "form": form,
        "post": post
    })