from django.urls import path

from . import views

app_name = "sessions_example"

urlpatterns = [
    path("", views.home_view, name="home"),
]
