from django.contrib.auth.models import User, Group
from .models import Bank
from rest_framework import serializers


class User_Serializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'url', 
            'username', 
            'email',
            'groups',
        ]

class Group_Serializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = [
            'url',
            'name',
        ]
class Bank_Serializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bank
        fields = [
            'bank_name',
            'bank_phone_number',
        ]