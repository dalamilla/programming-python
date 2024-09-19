from django.http import HttpResponse
from django.template import loader


def file_metadata_index(request):
    template = loader.get_template("front/index.html")
    context = {
        "title": "Form File",
    }
    return HttpResponse(template.render(context, request))
