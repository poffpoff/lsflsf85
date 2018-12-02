from django.shortcuts import render

# Create your views here.

def index(request):
    firstPage = models.FirstPage.objects.all()
    if (firstPage):
        firstPage = firstPage[0]
        indexes = models.Index.objects.filter(firstPage = firstPage)
        title = firstPage.title
        font_style = firstPage.font_style
        color_1 = firstPage.color_1
        color_2 = firstPage.color_2
        context = {
            'firstPage': firstPage,
            'indexes': indexes,
            'title': title,
            'font_style': font_style,
            'color_1': color_1,
            'color_2': color_2,
        }

        template = loader.get_template('festival/index.html')
        return HttpResponse(template.render(context, request))
    else:
        raise Http404("Index does not exist")