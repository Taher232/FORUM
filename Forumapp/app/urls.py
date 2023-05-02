from django.urls import path
from .import views

urlpatterns = [
    # path('app', views.index, name='index'),
    # path('utilisateurs/', views.liste_utilisateurs, name='liste_utilisateurs'), # where is this view?
    path('utilisateurs/creer/', views.creer_utilisateur, name='creer_utilisateur'),
    # path('utilisateurs/modifier/<int:id>/', views.modifier_utilisateur, name='modifier_utilisateur'),
    # path('utilisateurs/supprimer/<int:id>/', views.supprimer_utilisateur, name='supprimer_utilisateur'),
    # path('discussions/', views.liste_discussions, name='liste_discussions'),
    path('discussions/creer/', views.creer_discussion, name='creer_discussion'),
    # path('discussions/modifier/<int:id>/', views.modifier_discussion, name='modifier_discussion'),
    # path('discussions/supprimer/<int:id>/', views.supprimer_discussion, name='supprimer_discussion'),
    path('commentaires/ajouter/', views.ajouter_commentaire, name='ajouter_commentaire'),
    # path('commentaires/supprimer/<int:id>/', views.supprimer_commentaire, name='supprimer_commentaire'),
]
