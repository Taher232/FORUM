from django.contrib import admin
from .models import Administrateur, Utilisateur, Moderateur, Discussion, Client, Commentaire, Publication, Notification

# Register your models here.

admin.site.register(Administrateur)
admin.site.register(Utilisateur)
admin.site.register(Moderateur)
admin.site.register(Discussion)
admin.site.register(Client)
admin.site.register(Commentaire)
admin.site.register(Publication)
admin.site.register(Notification)