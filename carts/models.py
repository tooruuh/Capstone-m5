import uuid

from django.db import models


class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_itens = models.IntegerField()

    user = models.OneToOneField("users.User", on_delete=models.CASCADE)
    products = models.ManyToManyField("products.Product", related_name="products")
