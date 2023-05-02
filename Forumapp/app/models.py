from django.db import models

#profil
class Administrateur(models.Model):
    email = models.EmailField(verbose_name='Adresse Email', max_length=255, unique=True)
    nom = models.CharField(verbose_name='Nom', max_length=30)
    prenom = models.CharField(verbose_name='Prenom', max_length=40)
    telephone = models.CharField(verbose_name='Telephone', max_length=20)
    mot_de_passe = models.CharField(verbose_name='Mot de passe', max_length=255)
    
    def seConnecter(self):
        pass


class Utilisateur(models.Model):
    email = models.EmailField(verbose_name='Adresse Email', max_length=255, unique=True)
    nom = models.CharField(verbose_name='Nom', max_length=30)
    prenom = models.CharField(verbose_name='Prenom', max_length=40)
    telephone = models.CharField(verbose_name='Telephone', max_length=20)
    image = models.ImageField(upload_to='utilisateur/', blank=True)
    role = models.CharField(verbose_name='Role', max_length=30)
    mot_de_passe = models.CharField(verbose_name='Mot de passe', max_length=255)
    administrateur = models.ForeignKey(Administrateur, on_delete=models.CASCADE)
    
    def connecter(self):
        pass
    
    def seDeconnecter(self):
        pass
    
    def creer(self):
        pass
    
    def modifier(self):
        pass
    
    def ajouter(self):
        pass

class Moderateur(Utilisateur): # this?
    identifiant = models.CharField(verbose_name='Identifiant', max_length=30)

class Discussion(models.Model):
    nom = models.CharField(verbose_name='nom', max_length=20)
    theme = models.CharField(verbose_name='theme', max_length=30)
    comment = models.CharField(verbose_name='comment', max_length=3000, blank=True)
    auteur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    moderateurs = models.ManyToManyField(Moderateur, related_name='moderateur') # Which table are you linking to here?
    
    def Creer(self):
        pass
    
    def modifier(self):
        pass
    
    def chercher(self):
        pass
    
    def commenter(self):
        pass


    

class Client(Utilisateur):
    identifiant = models.CharField(verbose_name='Identifiant', max_length=30)


class Commentaire(models.Model):
    auteur = models.CharField(max_length=200)
    texte = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    
    def ajouter(self):
        pass
    
    def supprimer(self):
        pass


class Publication(models.Model):
    def ajouter(self):
        pass
    
    def supprimer(self):
        pass


class Notification(models.Model):
    identifiant = models.CharField(verbose_name="Identifiant", max_length=50)
    date = models.DateField(verbose_name="Date de Notification", auto_now=False, auto_now_add=False)
    heure = models.TimeField()
    
    def recevoir(self):
        pass

# class Test(models.Model):
#     name = models.CharField(max_length=200)
    
# class AddTest(models.Model):
#     phone = models.CharField(max_length=100)
#     add_test = models.ManyToManyField(Test)