from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def post_list(request) -> render:
    objects_list = Post.published.all()
    # 3 post in each page
    paginator = Paginator(objects_list, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    try:
        posts = page_obj.object_list
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = page_obj.paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = page_obj.paginator.num_pages

    return render(
        request,
        "blog/post_list.html",
        {
            "posts": posts,
            "paginator": paginator,
            "page_number": int(page_number),
        },
    )


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post, slug=post, status="published", publish__year=year, publish__month=month, publish__day=day
    )
    return render(request, "blog/post_detail.html", {"post": post})
