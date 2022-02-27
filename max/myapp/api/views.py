from rest_framework import viewsets
# from rest_framework.permissions import IsAuthenticated
# from django.views.generic import View

from myapp.models import (
    Protocols,
    ReestrTSZH,
    Scans
)
from .serializers import (
    ProtocolsSerializer,
    ReestrTSZHSerializer,
    ScansSerializer
)

class ProtocolsViewSet(viewsets.ModelViewSet):
    serializer_class = ProtocolsSerializer
    queryset = Protocols.objects.all()
class ReestrTSZHViewSet(viewsets.ModelViewSet):
    serializer_class =  ReestrTSZHSerializer
    queryset = ReestrTSZH.objects.all()
class ScansViewSet(viewsets.ModelViewSet):
    serializer_class = ScansSerializer
    queryset = Scans.objects.all()

