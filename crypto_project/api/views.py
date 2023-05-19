from rest_framework import viewsets

from crypto_project.settings import API_BINANCE_KEY, API_BINANCE_SECRET
from .utils import update_crypto_currencies
from django.http import HttpResponse
from .models import CryptoCurrency
from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpRequest
from binance.client import Client


def crypto_list(request: HttpRequest):
    currencies = CryptoCurrency.objects.all()
    query = request.GET.get('search')
    if query:
        currencies = currencies.filter(name__icontains=query) | currencies.filter(symbol__icontains=query)
    context = {"currencies": currencies}
    paginator = Paginator(currencies, 20)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context['page'] = page
    return render(request, "base.html", context)


# class CryptoCurrencyViewSet(viewsets.ModelViewSet):
#     queryset = CryptoCurrency.objects.all()
#     # serializer_class = CryptocurrencySerializer


def update_crypto_view(request: HttpRequest) -> None:
    update_crypto_currencies()
    return HttpResponse('Crypto currencies updated')



