from django.urls import path
from .views import ComListCreateView, EvenementListCreateView

urlpatterns = [
    path('coms/', ComListCreateView.as_view(), name='com-list-create'),
    path('evenements/', EvenementListCreateView.as_view(), name='evenement-list-create'),
    path('tickets/', TicketListCreateView.as_view(), name='ticket-list-create'),
]