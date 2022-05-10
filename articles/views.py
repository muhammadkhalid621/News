from django.shortcuts import render
from .webScrapper import articles
from django.template import loader  
from django.http import HttpResponse  
import os
from django.conf import settings

# Create your views here.
def index(request):
    data = request.POST
    action = data.get("follow")
        
    final_list = articles()
   
    template = loader.get_template('page.html')
    # path_to_file = os.path.join(str(settings.MEDIA_ROOT) , "artices.txt")
    # if os.path.exists(path_to_file):
    #     with open(path_to_file, 'r', encoding='utf-8', errors='ignore') as fh:
    #         response = HttpResponse(fh.read(), content_type="application/force-download")
    #         response['Content-Disposition'] = 'inline; filename=artices.txt'
    #         return response
    # context = {
    #     'list': final_list,
    #     'flag': flag,
    # }
    # print(context)
    return HttpResponse(template.render())

def data(request):
    final_list = articles()
   
    template = loader.get_template('data.html')
    context = {
        'list': final_list,
    }
    return HttpResponse(template.render(context, request))

# def hello(request):
#     articles()
#     template = loader.get_template('page.html')
#     return HttpResponse(template.render())


