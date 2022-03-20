from django.http import HttpResponse
from django.template import Template, Context


def home_view(request):
    num_visits = int(request.session.get("num_visits", 0)) + 1
    request.session["num_visits"] = num_visits
    # if num_visits > 5:
    #     del request.session["num_visits"]
    t = Template("<h1>Visits: {{ visits }}</h1>")
    c = Context({"visits": request.session["num_visits"]})
    return HttpResponse(t.render(c))
