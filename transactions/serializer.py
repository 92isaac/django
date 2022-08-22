from rest_framework import serializers
from .models import Transaction_detail

class Transaction_detailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction_detail
        fields = ['transaction_name', 'amount', 'interest', 'daily_interest']