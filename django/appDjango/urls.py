from ptdlog.urls import path
#from django.ptdlog.urls import path
from . import views

urlpatterns = [
    path('', views.ma_vue, name='ma_vue'),
    # Autres URLs spécifiques à votre application
]