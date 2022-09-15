from carts.models import Cart
from django.test import TestCase
from products.models import Product
from users.models import User


class CartModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user_data = {
            "name": "Teste User",
            "email": "teste@email.com",
            "username": "test1",
            "password": "123",
            "plan": "Base",
        }
        cls.user = User.objects.create_user(**cls.user_data)

        cls.product_data = {
            "name": "Bolsa",
            "description": "Bolsa preta com detalhes dourado",
            "price": 18000,
            "category": "Acessórios",
            "is_active": True,
            "is_new": True,
            "image": "dfsfdsgsdgsldgs",
            "seller_id": cls.user.id,
        }
        cls.product = Product.objects.create(**cls.product_data)

    def test_cart_field(self):
        self.favorite = Cart.objects.create(product=self.product, user=self.user)

        self.assertEqual(self.favorite.product.id, self.product.id)
        self.assertEqual(self.favorite.user.id, self.user.id)
