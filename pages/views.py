from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.views.generic import TemplateView, RedirectView
# import asyncio
# from time import sleep
# from asgiref.sync import sync_to_async
# from .long_functions import long_task
from .tasks import long_task

# Class based view
class Home_view(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        day = datetime.now().day
        bg_img = 'img/bg/'+ str(day) +'.jpg'
        context['bg_img'] = bg_img
        return context


# Redirect View
class Redirect_soe(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'pages:soe_destination'
    def get_redirect_url(self, *args, **kwargs):
        request_instance = {
            'user': str(self.request.user),
            'agent': self.request.headers['User-Agent'],
            'clicked': 'redirect'
        }
        print(request_instance)
        return super().get_redirect_url(*args, **kwargs)
    
class MM_geo_view(TemplateView):
    template_name = 'mm_geo_api.html'
    
    
class Redirect_preloads_mm_geo_api(RedirectView):
    
    query_string = True
    pattern_name = 'pages:redirect_mm_geo_api'
    
    def get_redirect_url(self, *args, **kwargs):
        long_task.delay(self.request.GET.get('lat_long', 'abc'))
        print('This run')
        return super().get_redirect_url(*args, **kwargs)
    
    
def redirect_mm_geo_api(request, *args, **kwargs):
    dest_url = 'https://soepaing.pythonanywhere.com/api/' + request.GET.get('lat_long', 'abc')
    return redirect(dest_url)
    



# Create your views here.
# The Old home_view
# def home_view(request, *args, **kwargs):
#     # print(request)
#     # print(request.method)
#     # print(request.path)
#     # print(request.path_info)
#     # print(request.COOKIES)
#     # print(request.META)
#     # print(request.user)
#     # print(request.headers)
#     # print(request.headers['User-Agent'])
#     # return HttpResponse('<h2>Hello World</h2>')
#     day = datetime.now().day
#     bg_img = 'img/bg/'+ str(day) +'.jpg'
#     context = {
#         'bg_img': bg_img
#     }
#     return render(request, 'home.html', context)

# def patients_view(request, *args, **kwargs):
#     print(request)
#     print(request.path)
#     return HttpResponse('<h2>Patients</h2>')

def result_view(request, *args, **kwargs):
    ss = request.GET.get('ss', None)
    return render(request, 'home.html', {'ss': ss})
