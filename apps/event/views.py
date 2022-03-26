from django.shortcuts import render, get_object_or_404
from .models import Event


def event_detail(request, pk):
    return render(request, "event/event_detail.html", {"event_detail": get_object_or_404(Event, pk=pk)})