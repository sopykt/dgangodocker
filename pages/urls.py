from django.urls import path
from django.views.generic import TemplateView
from .views import home_view, result_view
from .extracontext import bg_img, about_context, contact_context

app_name = 'pages'
urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html', extra_context=bg_img()), name='home'),
    path('about/', TemplateView.as_view(template_name='about.html', extra_context=about_context()), name='about'),
    path('contact/', TemplateView.as_view(template_name='contact.html', extra_context=contact_context()), name='contact')
]