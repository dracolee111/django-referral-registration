from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import template
from django.template import loader
from django.contrib.auth.decorators import login_required

# Create your views here.
## view for displaying the homepage 'index.html'
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('main/index.html')
    return HttpResponse(html_template.render(context, request))

## view for displaying other pages. all urls end in .html
@login_required()
def pages(request):
    user = request.user
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('main/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('main/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('main/page-500.html')
        return HttpResponse(html_template.render(context, request))