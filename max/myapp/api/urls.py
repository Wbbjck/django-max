from myapp.api.views import (
    ProtocolsViewSet,
    ReestrTSZHViewSet,
    ScansViewSet
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'protocols',ProtocolsViewSet, basename='protocols')
router.register(r'reestrTSZH',ReestrTSZHViewSet, basename='reestrTSZH')
router.register(r'scans',ScansViewSet, basename='scans')
urlpatterns = router.urls
