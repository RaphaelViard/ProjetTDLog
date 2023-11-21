# myapp/urls.py
from django.urls import path
from . import views
from .views import ProfilUtilisateurListe, ProfilUtilisateurDetail, EvenementListe, EvenementDetail, TicketListe, TicketDetail, AchatListe, AchatDetail, CommentaireListe, CommentaireDetail

urlpatterns = [
    path('utilisateurs/', ProfilUtilisateurListe.as_view(), name='utilisateur-liste'),
    path('utilisateurs/<int:pk>/', ProfilUtilisateurDetail.as_view(), name='utilisateur-detail'),
    path('evenements/', EvenementListe.as_view(), name='evenement-liste'),
    path('evenements/<int:pk>/', EvenementDetail.as_view(), name='evenement-detail'),
    path('tickets/', TicketListe.as_view(), name='ticket-liste'),
    path('tickets/<int:pk>/', TicketDetail.as_view(), name='ticket-detail'),
    path('achats/', AchatListe.as_view(), name='achat-liste'),
    path('achats/<int:pk>/', AchatDetail.as_view(), name='achat-detail'),
    path('commentaires/', CommentaireListe.as_view(), name='commentaire-liste'),
    path('commentaires/<int:pk>/', CommentaireDetail.as_view(), name='commentaire-detail'),
]
