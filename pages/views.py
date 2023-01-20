from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    print(request)
    print(request.method)
    print(request.path)
    print(request.path_info)
    print(request.COOKIES)
    print(request.META)
    return HttpResponse('<h2>Hello World</h2>')

def patients_view(request, *args, **kwargs):
    print(request)
    print(request.path)
    return HttpResponse('<h2>Patients</h2>')
