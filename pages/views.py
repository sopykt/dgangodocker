from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.views.generic import TemplateView, RedirectView

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
    pattern_name = 'pages:destination'
    def get_redirect_url(self, *args, **kwargs):
        request_instance = {
            'user': str(self.request.user),
            'agent': self.request.headers['User-Agent'],
            'clicked': 'redirect'
        }
        print(request_instance)
        return super().get_redirect_url(*args, **kwargs)


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
