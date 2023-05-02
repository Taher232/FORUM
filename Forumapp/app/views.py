from django.shortcuts import render, redirect
from django.http import HttpResponse
# from .models import Administrateur, Utilisateur, Moderateur, client, Discussion, commentaire, publication, notification
from .models import *

def se_connecter(request):
    if request.method == 'POST':
        email = request.POST['email']
        mot_de_passe = request.POST['mot_de_passe']
        try:
            utilisateur = Utilisateur.objects.get(email=email, mot_de_passe=mot_de_passe)
            # Connectez-vous et redirigez l'utilisateur vers une autre page
            return redirect('page_accueil')
        except Utilisateur.DoesNotExist:
            # Affichez un message d'erreur à l'utilisateur
            return_html = "<h1>Hello</h1>"
            return HttpResponse(return_html)
    else:
        return render(request, 'se_connecter.html')

def se_deconnecter(request):
    # Déconnectez l'utilisateur et redirigez-le vers la page de connexion
    return redirect('se_connecter')

def creer_utilisateur(request):
    if request.method == 'POST':
        email = request.POST['email']
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        telephone = request.POST['telephone']
        role = request.POST['role']
        mot_de_passe = request.POST['mot_de_passe']
        administrateur = Administrateur.objects.first() # Utilisez le premier administrateur pour l'instant
        utilisateur = Utilisateur(email=email, nom=nom, prenom=prenom, telephone=telephone,role=role, mot_de_passe=mot_de_passe, administrateur=administrateur)
        utilisateur.save()
        # Redirigez l'utilisateur vers la page de profil
        return redirect('profil', utilisateur.id)
    else:
        return render(request, 'test.html')

def creer_discussion(request):
    if request.method == 'POST':
        nom = request.POST['nom']
        theme = request.POST['theme']
        comment = request.POST['comment']
        auteur = Moderateur.objects.first() # Utilisez le premier modérateur pour l'instant
        discussion = Discussion(nom=nom, theme=theme, comment=comment, auteur=auteur)
        discussion.save()
        # Redirigez l'utilisateur vers la page de la discussion
        
  
        return redirect('discussion', discussion.id)
    else:
        return render(request, 'creer_discussion.html')

def ajouter_commentaire(request, discussion_id):
    if request.method == 'POST':
        auteur = request.POST['auteur']
        texte = request.POST['texte']
        discussion = Discussion.objects.get(id=discussion_id)
        commentaire = discussion.commentaire_set.create(auteur=auteur, texte=texte)
        # Redirigez l'utilisateur vers la page de la discussion
        return redirect('discussion', discussion.id)
    else:
        return render(request, 'ajouter_commentaire.html')
