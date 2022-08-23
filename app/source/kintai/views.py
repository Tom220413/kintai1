from django.shortcuts import render

# from django.http import HttpResponse

from . import views
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'kintai/index.html'
