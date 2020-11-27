from rest_framework.viewsets import ModelViewSet

from subscriptions.models import Subscription
from subscriptions.serializers import SubscriptionSerializer


class SubscriptionViewSet(ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
