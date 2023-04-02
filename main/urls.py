# -*- encoding: utf-8 -*-


from django.urls import path, re_path
from main import views
from django.views.generic import TemplateView

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    # Other pages from main/*.html and  urls for rendering serviceworker and manifest if needed
    path('manifest.json', TemplateView.as_view(template_name="manifest.json", content_type='application/manifest+json')),
    path('sw.js', TemplateView.as_view(template_name="sw.js", content_type='text/javascript')),


    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]

