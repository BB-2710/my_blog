from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from . models import Post
from . forms import PostForm

def home(req):
    posts = Post.objects.all().order_by("created_at")
    return render(req, "home.html", {"posts": posts})

@login_required
def create_post(req):
    if req.method == "POST":
        form = PostForm(req.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = req.user
            post.save()
            return redirect("home")
    else:
        form = PostForm()
    return render(req, "create_post.html", {"form": form})

@login_required
def edit_post(req, id):
    post = get_object_or_404(Post, id=id)

    if post.author != req.user:
        return redirect("home")
    
    if req.method == "POST":
        form = PostForm(req.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = PostForm(instance=post)
    return render(req, "edit_post.html", {"form": form})

@login_required
def delete_post(req, id):
    post = get_object_or_404(Post, id=id)

    if post.author == req.user:
        post.delete()
    return redirect("home")            



def register_view(req):
    if req.method == "POST":
        form = RegisterForm(req.POST)
        if form.is_valid():
            user = form.save()
            login(req, user)
            return redirect("home")
    else:
        form = RegisterForm()
    return render(req, "register.html", {"form": form})

def login_view(req):
    if req.method == "POST":
        form = AuthenticationForm(data=req.POST)
        if form.is_valid():
            user = form.get_user()
            login(req, user)
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(req, "login.html", {"form": form})

def logout_view(req):
    logout(req)
    return redirect("login")


       












    

