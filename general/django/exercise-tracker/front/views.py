from django.http import HttpResponse
from django.template import loader


def exercise_tracker_index(request):
    template = loader.get_template("front/index.html")
    context = {
        "title": "Exercise Tracker",
    }
    return HttpResponse(template.render(context, request))
