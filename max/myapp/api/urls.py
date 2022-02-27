from myapp.api.views import (
    ProtocolsViewSet,
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'protocols',ProtocolsViewSet, basename='protocols')

urlpatterns = router.urls
