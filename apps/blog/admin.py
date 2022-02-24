from django.contrib import admin
from .models import Post, Comment
from import_export.admin import ExportActionMixin
from import_export import resources


class PostResource(resources.ModelResource):
    class Meta:
        model = Post
        fields = ("id", "author", "title", "body", "liked", "created")


@admin.register(Post)
class PostAdmin(ExportActionMixin, admin.ModelAdmin):
    search_fields = ("author", "title")
    list_filter = ("author", "created")
    list_per_page = 10
    resource_class = PostResource


admin.site.register(Comment)
