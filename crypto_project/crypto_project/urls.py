from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
# from api.views import CryptoCurrencyViewSet
from api.views import crypto_list, update_crypto_view

# router = routers.DefaultRouter()
# router.register(r'cryptocurrencies', CryptoCurrencyViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path("admin/", admin.site.urls),
    path('crypto/', crypto_list, name='crypto_list'),
    path('update-crypto/', update_crypto_view, name='update_crypto'),
]
