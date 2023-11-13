# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('test/',views.test_view, name='test_view'),
    path('items/', views.ItemListCreateView.as_view(), name='item-list-create'),
        
]

