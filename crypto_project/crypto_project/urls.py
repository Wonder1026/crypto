from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
# from api.views import CryptoCurrencyViewSet
from api.views import crypto_list, update_crypto_view

urlpatterns = [
    # path('', include(router.urls)),
    path("admin/", admin.site.urls),
    path('crypto/', crypto_list, name='crypto_list'),
    path('update-crypto/', update_crypto_view, name='update_crypto'),
    # path('binance_acc/', view_binance, name='view_binance'),
    # path('binance_tokens/', binance_tokens_view, name='binance_tokens'),
]
