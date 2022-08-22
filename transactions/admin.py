from django.contrib import admin
from .models import *
# Register your models here.


class TransactionAdmin(admin.ModelAdmin):
    list_display=()
    list_filter=()


admin.site.register(Transaction_detail, TransactionAdmin)