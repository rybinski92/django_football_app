from django.contrib.auth.models import User 
from rest_framework import serializers 
from .models import Football

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User 
        fields = ['id', 'username', 'email']


class FootballSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Football 
        fields = ['tytul', 'rok', 'opis']

