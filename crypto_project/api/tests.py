# from django.db.models import QuerySet
# from django.http import HttpRequest
# from django.test import TestCase
# from django.test.client import Client
# from django.core.paginator import Paginator
# from django.shortcuts import render
#
# from api.models import CryptoCurrency
# from api.views import crypto_list
# from django.urls import reverse
#
# class CryptoListTest(TestCase):
#     def setUp(self) -> None:
#         self.client = Client()
#         self.bitcoin = CryptoCurrency.objects.create(
#             name='Bitcoin',
#             symbol='BTC',
#             current_price=100,
#             price_change_24h=5,
#             volume_24h=5000
#         )
#         self.etherium = CryptoCurrency.objects.create(
#             name='Ethereum',
#             symbol='ETH',
#             current_price=500,
#             price_change_24h=7,
#             volume_24h=6000
#         )
#
#     def test_get_list_without_search(self):
#         response = self.client.get('/crypto/')
#         print(response.content[0]['name'])
#         print(response.content[0]['symbol'])
#         print(response.content[0]['symbol'])
#         print(response.content[0]['symbol'])
#         print(response.content[0]['symbol'])
#
#
#         response.content = str(response.content)
#         self.assertEqual(response.status_code, 200)
#         self.assertIsInstance(response.content, str)
#         self.assertEqual(len(response.content), 2)
#         self.assertEqual(response.content[0]['name'], 'Bitcoin')
#         self.assertEqual(response.content[0]['symbol'], 'BTC')
#         self.assertEqual(response.content[1]['name'], 'Ethereum')
#         self.assertEqual(response.content[1]['symbol'], 'ETH')
#
#     def test_get_list_with_search(self):
#         response = self.client.get('/crypto/?search=bitcoin')
#         self.assertEqual(response.status_code, 200)
#         self.assertIsInstance(response.content, list)
#         self.assertEqual(len(response.content), 1)
#         self.assertEqual(response.content[0]['name'], 'Bitcoin')
#         self.assertEqual(response.content[0]['symbol'], 'BTC')
#
#     def test_get_list_with_invalid_page(self):
#         response = self.client.get('/crypto/?page=100')
#         self.assertEqual(response.status_code, 404)
#
#     def test_crypto_list_with_no_query(self):
#         currency3 = CryptoCurrency.objects.create(
#             name='Litecoin',
#             symbol='LTC',
#             current_price=700,
#             price_change_24h=10,
#             volume_24h=9999
#         )
#         request = self.factory.get('/crypto-list/')
#         response = crypto_list(request)
#
#         self.assertEqual(response.status_code, 200)
#
#         response = self.client.get('/crypto-list/')
#         # self.assertTemplateUsed(response, 'base.html')
#         self.assertEqual(CryptoCurrency.objects.count(), len(response.context['currencies']))
#         self.assertIsInstance(response.context['page'], Paginator)
#
