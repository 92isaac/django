from django.db import models
from datetime import datetime

# Create your models here.

class Transaction_detail(models.Model):
    transaction_name = models.CharField(max_length=255, null=True)
    amount = models.IntegerField(default=0, null=True, blank=True)
    # date_created = models.DateTimeField(auto_now_add=True)



    @property
    def interest(self):
        amo = int(self.amount)
        montly_interest = amo / 12
        return montly_interest

    @property
    def daily_interest(self):
        now = datetime.now()
        d_int = 0
        if now.second == 0:
            d_int = self.interest / 30
            d_int += d_int
        return d_int

        # montlyinterest = self.amount / 12
        # dailyinterest = montlyinterest / 30
        # tnow = datetime.now()
        # seconds = tnow.seconds
        # if seconds == 30:
        #     self.daily_interest = self.daily_interest + dailyinterest
        # return self.daily_interest
