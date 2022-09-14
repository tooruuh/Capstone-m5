import uuid

from django.db import models


class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_finalized = models.BooleanField(default=False)

    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="carts")
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE, related_name="products")