from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("polls/", include("apps.polls.urls", namespace="polls")),
    path("blog/", include("apps.blog.urls", namespace="blog")),
    path("event/", include("apps.event.urls", namespace="event")),
    path("sessions_example/", include("apps.sessions_example.urls", namespace="sessions_example")),
    path("admin/", admin.site.urls),
]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += (path("__debug__/", include(debug_toolbar.urls)),)
