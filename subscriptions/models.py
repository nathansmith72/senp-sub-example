import datetime

from dateutil.relativedelta import relativedelta
from django.core.mail import send_mail
from django.db import models

from accounts.models import User


class Subscription(models.Model):
    BRONZE = "Bronze"
    SILVER = "Silver"
    GOLD = "Gold"
    TIERS = (
        (BRONZE, BRONZE),
        (SILVER, SILVER),
        (GOLD, GOLD)
    )
    PRICES = {
        BRONZE: 9.99,
        SILVER: 19.99,
        GOLD: 29.99
    }
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tier = models.CharField(max_length=10, choices=TIERS, null=False, blank=False)
    last_payment_date = models.DateField()

    @property
    def price(self):
        return self.PRICES.get(self.tier)

    @property
    def payment_due(self):
        payment_day = self.last_payment_date + relativedelta(months=1)
        return datetime.datetime.now() > payment_day

    @property
    def active(self):
        # Remove users subscription privileges if they are 5 days or more behind on their payments
        cutoff_day = self.last_payment_date + relativedelta(months=1, days=5)
        return datetime.datetime.now() > cutoff_day

    def send_renewal_notification_email(self, renewed):
        if renewed:
            template = 'email/successful_renewal.html'
            send_mail('Your subscription has been renewed!', template, 'noreply@ourcompany.com', [self.user.email])
        else:
            template = 'email/failed_renewal.html'
            send_mail('We failed to renew your subscription!', template, 'noreply@ourcompany.com', [self.user.email])
