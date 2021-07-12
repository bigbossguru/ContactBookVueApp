from rest_framework import serializers

from .models import ContactBook

class ContactBookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContactBook
        fields = ('id', 'firstname', 'lastname', 'mobile_phone', 'email', 'department')