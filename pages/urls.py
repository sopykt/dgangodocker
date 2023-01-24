from django.urls import path
from django.views.generic import TemplateView, RedirectView
from .views import Home_view, Redirect_soe, MM_geo_view, Redirect_preloads_mm_geo_api ,redirect_mm_geo_api
from .extracontext import bg_img, about_context, contact_context

app_name = 'pages'
urlpatterns = [
    path('', Home_view.as_view(), name='home'),
    path('about/', TemplateView.as_view(template_name='about.html', extra_context=about_context()), name='about'),
    path('contact/', TemplateView.as_view(template_name='contact.html', extra_context=contact_context()), name='contact'),
    # path('soepaing/', RedirectView.as_view(url='https://soepaing.com'), name='redirect'),
    
    path('soepaing/', Redirect_soe.as_view(), name='redirect'),
    path('soepaings/', RedirectView.as_view(url='https://soepaing.com'), name='soe_destination'),
    
    path('mm_geo_api_page/', MM_geo_view.as_view(), name='mm_geo_api_page'),
    path('preloads_mm_geo_api/', Redirect_preloads_mm_geo_api.as_view(), name='preloads_mm_geo_api'),
    path('redirect_mm_geo_api', redirect_mm_geo_api, name='redirect_mm_geo_api')
]