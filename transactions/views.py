from django.shortcuts import render
from rest_framework import viewsets
from .serializer import Transaction_detailSerializer
from .models import Transaction_detail

# Create your views here.

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction_detail.objects.all().order_by('-id')
    serializer_class = Transaction_detailSerializer
