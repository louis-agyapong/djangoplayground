from django.contrib import admin
from .models import Post, Comment
from import_export.admin import ExportActionMixin
from import_export import resources
from import_export.fields import Field


class PostResource(resources.ModelResource):
    author = Field()
    liked = Field()
    created = Field()
    comments = Field()

    class Meta:
        model = Post
        fields = ("id", "author", "title", "body", "liked", "created")
        export_order = fields

    def dehydrate_author(self, post) -> str:
        return str(post.author.username)

    def dehydrate_liked(self, post) -> str:
        data = [x.username for x in post.liked.all()]
        users_liked = ", ".join(data)
        return str(users_liked)

    def dehydrate_created(self, post) -> str:
        return str(post.created.strftime("%d-%m-%Y"))

    def dehydrate_comments(self, post) -> str:
        data = [x.body for x in post.comments]
        comments = ", ".join(data)
        return str(comments)


@admin.register(Post)
class PostAdmin(ExportActionMixin, admin.ModelAdmin):
    search_fields = ("author", "title")
    list_filter = ("author", "created")
    list_per_page = 10
    resource_class = PostResource


admin.site.register(Comment)
