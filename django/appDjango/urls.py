from ptdlog.urls import path
#from django.ptdlog.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('react/', TemplateView.as_view(template_name='appreact/build/index.html')),
    path('template/', views.template_view, name='template_view'),
    path('test/', views.test_view, name='test_view'),
    
    # Autres URLs spécifiques à votre application
]


