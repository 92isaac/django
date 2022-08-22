from django.db import models
from datetime import datetime

# Create your models here.

class Transaction_detail(models.Model):
    transaction_name = models.CharField(max_length=255, null=True)
    amount = models.IntegerField(default=0, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=False)



    @property
    def interest(self):
        amo = int(self.amount)
        montly_interest = amo / 12
        return montly_interest

    @property
    def daily_interest(self):
        now = datetime.now()
        # dt = datetime.datetime.now()
        seq = int(now.strftime("%Y%m%d%H%M%S"))
        d_int = 0
        for i in range(now.second):
            if i == 1:
                d_int = self.interest / 30
                d_int += d_int
        return d_int

