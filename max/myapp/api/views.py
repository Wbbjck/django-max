from rest_framework import viewsets
# from rest_framework.permissions import IsAuthenticated
# from django.views.generic import View

from myapp.models import (
    Protocols
)
from .serializers import (
    ProtocolsSerializer,
)

class ProtocolsViewSet(viewsets.ModelViewSet):
    serializer_class = ProtocolsSerializer
    queryset = Protocols.objects.all()


