from django.urls import path
from django.views.generic import TemplateView, RedirectView
from .views import Home_view
from .extracontext import bg_img, about_context, contact_context

app_name = 'pages'
urlpatterns = [
    path('', Home_view.as_view(), name='home'),
    path('about/', TemplateView.as_view(template_name='about.html', extra_context=about_context()), name='about'),
    path('contact/', TemplateView.as_view(template_name='contact.html', extra_context=contact_context()), name='contact'),
    path('soepaing/', RedirectView.as_view(url='https://soepaing.com'), name='redirect')
]