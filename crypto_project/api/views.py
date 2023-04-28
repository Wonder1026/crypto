from rest_framework import viewsets

from .api import update_crypto_currencies
from django.http import HttpResponse
from .models import CryptoCurrency
from django.shortcuts import render


def crypto_list(request):
    currencies = CryptoCurrency.objects.all()
    context = {"currencies": currencies}
    return render(request, "base.html", context)
# class CryptoCurrencyViewSet(viewsets.ModelViewSet):
#     queryset = CryptoCurrency.objects.all()
#     # serializer_class = CryptocurrencySerializer


def update_crypto_view(request):
    update_crypto_currencies()
    return HttpResponse('Crypto currencies updated')


