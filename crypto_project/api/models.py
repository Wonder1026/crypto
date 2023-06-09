from django.db import models


class CryptoCurrency(models.Model):
    symbol = models.CharField(
        max_length=10
    )
    name = models.CharField(
        max_length=100
    )
    current_price = models.DecimalField(
        max_digits=18,
        decimal_places=2
    )
    price_change_24h = models.DecimalField(
        max_digits=18,
        decimal_places=2
    )
    volume_24h = models.BigIntegerField(
        max_length=26,
    )

    def __str__(self):
        return f"{self.name} ({self.symbol})"

    class Meta:
        ordering = ['-current_price']


# class Favorite(models.Model):
#     user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
#     cryptocurrency = models.ForeignKey(Cryptocurrency, on_delete=models.CASCADE)
#
#     class Meta:
#         unique_together = ('user', 'cryptocurrency',)
