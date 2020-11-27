from rest_framework import serializers
from rest_framework.exceptions import APIException

from subscriptions.models import Subscription


class SubscriptionFailedException(APIException):
    status_code = 503
    default_detail = 'Unable to create the subscription. Please try again later.'
    default_code = 'subscription_failed'


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription

    def create(self, validated_data):
        # Mock the API
        api_successful_subscription = True
        if api_successful_subscription:
            return super().create(validated_data)
        else:
            raise SubscriptionFailedException


