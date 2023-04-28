from django.db import models


class CryptoCurrency(models.Model):
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    current_price = models.DecimalField(max_digits=18, decimal_places=4)
    price_change_24h = models.DecimalField(max_digits=18, decimal_places=4)
    volume_24h = models.DecimalField(max_digits=26, decimal_places=4)

    def __str__(self):
        return f"{self.name} ({self.symbol})"

    def __str__(self):
        return self.symbol

    class Meta:
        ordering = ['symbol']


# class Favorite(models.Model):
#     user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
#     cryptocurrency = models.ForeignKey(Cryptocurrency, on_delete=models.CASCADE)
#
#     class Meta:
#         unique_together = ('user', 'cryptocurrency',)
