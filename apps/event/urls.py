from django.urls import path
from . import views

app_name = "event"

urlpatterns = [
    path("<int:pk>/", views.event_detail, name="event-detail"),
]
