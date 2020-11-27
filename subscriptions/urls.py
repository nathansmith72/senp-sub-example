from rest_framework import routers

from subscriptions.views import SubscriptionViewSet

router = routers.SimpleRouter()
router.register('subscriptions', SubscriptionViewSet)

urlpatterns = router.urls
