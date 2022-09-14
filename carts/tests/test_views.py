from itertools import product

from django.urls import reverse
from products.models import Product
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework.views import status
from users.models import User


class CartViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.base_url = reverse("cart-view")

        cls.user_login = {"email": "teste@email.com", "password": "123"}
        cls.user_login_nopermission = {
            "email": "teste@nopermission.com",
            "password": "123",
        }
        cls.user_data = {
            "name": "Teste User",
            "email": "teste@email.com",
            "username": "test1",
            "password": "123",
            "plan": "Base",
        }
        cls.user_data_no_permission = {
            "name": "Teste User No Permission",
            "email": "teste@nopermission.com",
            "username": "test2",
            "password": "123",
            "plan": "Base",
        }

        cls.product_data = {
            "name": "Bolsa",
            "description": "Bolsa preta com detalhes dourado",
            "price": 18000,
            "category": "Acessórios",
            "is_active": True,
            "is_new": True,
            "image": "dfsfdsgsdgsldgs",
        }
        cls.product_data2 = {
            "name": "Relógio",
            "description": "Relógio com detalhes dourado",
            "price": 78000,
            "category": "Acessórios",
            "is_active": False,
            "is_new": True,
            "image": "dfsfdsgsdgsldgs",
        }
        cls.user = User.objects.create_user(**cls.user_data)
        cls.token_user = Token.objects.create(user=cls.user)

        cls.user_nopermission = User.objects.create_user(**cls.user_data_no_permission)
        cls.token_user_nopermission = Token.objects.create(user=cls.user_nopermission)

        cls.product = Product.objects.create(**cls.product_data, seller_id=cls.user.id)
        cls.product2 = Product.objects.create(
            **cls.product_data2, seller_id=cls.user.id
        )

    def test_create_cart(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_user.key)

        response = self.client.post(self.base_url, data={"product": self.product.id})

        expected_status_code = status.HTTP_201_CREATED
        result_status_code = response

    def test_create_cart_product_is_not_activate(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_user.key)

        response = self.client.post(self.base_url, data={"product": self.product2.id})

        expected_status_code = status.HTTP_406_NOT_ACCEPTABLE
        result_status_code = response

    def test_list_cart(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_user.key)
        response = self.client.get(self.base_url)

        expected_status_code = status.HTTP_201_CREATED
        result_status_code = response

    def test_create_cart_user_no_permission(self):
        self.client.credentials(
            HTTP_AUTHORIZATION="Token " + self.token_user_nopermission.key
        )
        response = self.client.post(self.base_url, data={"product": self.product.id})

        expected_status_code = status.HTTP_403_FORBIDDEN
        result_status_code = response

    def test_list_cart_user_no_permission(self):
        self.client.credentials(
            HTTP_AUTHORIZATION="Token " + self.token_user_nopermission.key
        )
        response = self.client.get(self.base_url)

        expected_status_code = status.HTTP_403_FORBIDDEN
        result_status_code = response
