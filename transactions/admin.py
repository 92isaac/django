from django.contrib import admin
from .models import *
# Register your models here.


class TransactionAdmin(admin.ModelAdmin):
    list_display=('transaction_name', 'amount', 'interest', 'montly_interest', 'daily_interest')
    list_filter=()


admin.site.register(Transaction_detail, TransactionAdmin)