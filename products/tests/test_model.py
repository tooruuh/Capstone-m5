import ipdb
from django.test import TestCase
from products.models import Product
from users.models import User


class ProductModelTest(TestCase):
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

    def test_product_field(self):
        self.product = Product.objects.create(**self.product_data)

        self.assertEqual(self.product_data["name"], self.product.name)
        self.assertEqual(self.product_data["description"], self.product.description)
        self.assertEqual(self.product_data["price"], self.product.price)
        self.assertEqual(self.product_data["is_active"], self.product.is_active)
        self.assertEqual(self.product_data["is_new"], self.product.is_new)
        self.assertEqual(self.product_data["image"], self.product.image)
