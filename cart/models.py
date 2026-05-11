from django.db import models
from django.contrib.auth.models import User


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    qty = models.IntegerField()

    def __str__(self):
        return f'{self.user.username} - {self.product.name}'
