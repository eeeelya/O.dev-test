
from rest_framework.routers import DefaultRouter

from cryptocurrency.views import WalletViewSet

router = DefaultRouter()
router.register(r'wallets', WalletViewSet, basename='wallets')

urlpatterns = router.urls
