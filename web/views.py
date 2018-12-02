from django.shortcuts import render

# Create your views here.

def index(request):
    template = loader.get_template('web/html5up-story/index.html')
    return HttpResponse(template.render(context, request))
