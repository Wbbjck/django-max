from django.db.models.aggregates import Max
from rest_framework import serializers
import os
import urllib.parse


from django.contrib.auth.models import User
from django.db.models import Sum

from myapp.models import (
    Protocols
)

class ProtocolsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Protocols
        fields = '__all__'


