from django.contrib.auth.models import User, Group
from twibit_app.models import Twibit
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
	fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer): 
    class Meta:
	model = Group
	fields = ('url', 'name')

class TwibitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
	model = Twibit
