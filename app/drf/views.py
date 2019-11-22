from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from drf.serializers import User_Serializers, Group_Serializers, Bank_Serializers
from .models import Bank

class User_Viewset(viewsets.ModelViewSet):
    """
        API endpoint that allows users to edit views or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = User_Serializers

class Group_Viewset(viewsets.ModelViewSet):
    """
        API endpoint that allows users to edit views or edited
    """
    queryset = Group.objects.all()
    serializer_class = Group_Serializers

class Bank_Viewset(viewsets.ModelViewSet):
    """
        API endpoint that allows users to edit views or edited
    """
    queryset = Bank.objects.all()
    serializer_class = Bank_Serializers

