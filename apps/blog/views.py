from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def post_list(request) -> render:
    objects_list = Post.published.all()
    # 3 post in each page
    paginator = Paginator(objects_list, 3)
    page = request.GET.get("page")
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)

    posts = Post.published.all()
    return render(request, "blog/post_list.html", {"posts": posts, "page": page})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post, slug=post, status="published", publish__year=year, publish__month=month, publish__day=day
    )
    return render(request, "blog/post_detail.html", {"post": post})
