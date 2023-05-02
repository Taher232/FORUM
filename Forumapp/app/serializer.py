from rest_framework import serializers
from .models import Administrateur, Utilisateur, Discussion, Moderateur, client, commentaire, publication, notification

class AdministrateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrateur
        fields = '__all__'

class UtilisateurSerializer(serializers.ModelSerializer):
    administrateur = AdministrateurSerializer()

    class Meta:
        model = Utilisateur
        fields = '__all__'

class ModerateurSerializer(serializers.ModelSerializer):
    utilisateur = UtilisateurSerializer()

    class Meta:
        model = Moderateur
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    utilisateur = UtilisateurSerializer()

    class Meta:
        model = client
        fields = '__all__'

class DiscussionSerializer(serializers.ModelSerializer):
    moderateur = ModerateurSerializer(many=True)

    class Meta:
        model = Discussion
        fields = '__all__'

class CommentaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = commentaire
        fields = '__all__'

class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = publication
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = notification
        fields = '__all__'
