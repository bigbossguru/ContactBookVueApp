from django.shortcuts import render

# Create your views here.
from .models import ContactBook
from .serializers import ContactBookSerializer

from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter

class ContactBookViewSet(viewsets.ModelViewSet):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated, )
    queryset = ContactBook.objects.all()
    serializer_class = ContactBookSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('firstname', 'lastname', 'department')