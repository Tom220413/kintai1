from django.shortcuts import render

# from django.http import HttpResponse

from . import views
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'kintai/index.html'

    def get(self, request):
        return render(request, 'kintai/index.html')
    
    # def post(self, request):
    #     if request.method == 'POST':
    #         if "syukkin-btn" in request.POST:
    #             return "hogehoge"
    #         elif "taikin-btn" in request.POST:
    #             return "aaaa"
    def post(self, request):
        return render(request, 'kintai/hoge.html')