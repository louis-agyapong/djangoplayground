from django.shortcuts import render
from .models import Post


def post_list(request) -> render:
    posts = Post.published.all()
    return render(request, "blog/post_list.html", {"posts": posts})
