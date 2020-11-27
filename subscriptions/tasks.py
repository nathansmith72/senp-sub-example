import datetime
import random

from celery import shared_task

from subscriptions.models import Subscription


@shared_task
def start_payment_tasks():
    for subscription in Subscription.objects.all():
        if subscription.payment_due and subscription.active:
            process_payment.delay(subscription)


@shared_task
def process_payment(subscription):
    # Mocking API
    success = random.choice(True, False)

    if success:
        subscription.last_payment_date = datetime.datetime.now()
        subscription.save()
        subscription.send_renewal_notification_email(renewed=True)
    else:
        subscription.send_renewal_notification_email(renewed=False)
