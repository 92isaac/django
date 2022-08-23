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
        annual_interest = amo * 0.15
        return annual_interest


    @property
    def montly_interest(self):
        mont_interest = self.interest / 12
        return mont_interest


    @property
    def daily_interest(self):
        now = datetime.now()
        d_int = 0
        for i in range(now.second):
            if i == 1:
                d_int = self.montly_interest / 30
                d_int += d_int
        return d_int

