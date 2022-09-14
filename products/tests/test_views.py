from django.urls import reverse
from products.models import Product
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework.views import status
from users.models import User


class ProductViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.base_url = reverse("product-view")

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
            "is_selled": False,
            "image": "dfsfdsgsdgsldgs",
        }
        cls.user = User.objects.create_user(**cls.user_data)
        cls.token_user = Token.objects.create(user=cls.user)

        cls.user_nopermission = User.objects.create_user(**cls.user_data_no_permission)
        cls.token_user_nopermission = Token.objects.create(user=cls.user_nopermission)

    def test_create_product(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_user.key)
        response = self.client.post(self.base_url, data=self.product_data)

        expected_status_code = status.HTTP_201_CREATED
        result_status_code = response

    def test_list_products(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_user.key)
        response = self.client.get(self.base_url)

        expected_status_code = status.HTTP_201_CREATED
        result_status_code = response

    def test_create_product_user_no_permission(self):
        self.client.credentials(
            HTTP_AUTHORIZATION="Token " + self.token_user_nopermission.key
        )
        response = self.client.post(self.base_url, data=self.product_data)

        expected_status_code = status.HTTP_403_FORBIDDEN
        result_status_code = response

    def test_list_products_user_no_permission(self):
        self.client.credentials(
            HTTP_AUTHORIZATION="Token " + self.token_user_nopermission.key
        )
        response = self.client.get(self.base_url)

        expected_status_code = status.HTTP_403_FORBIDDEN
        result_status_code = response


class ProductDetailViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:

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
        cls.user = User.objects.create_user(**cls.user_data)
        cls.token_user = Token.objects.create(user=cls.user)

        cls.user_nopermission = User.objects.create_user(**cls.user_data_no_permission)
        cls.token_user_nopermission = Token.objects.create(user=cls.user_nopermission)

        cls.product = Product.objects.create(**cls.product_data, seller_id=cls.user.id)

        cls.base_url = reverse("product-detail", kwargs={"product_id": cls.product.id})

    def test_deleted_product(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_user.key)
        response = self.client.delete(self.base_url)

        expected_status_code = status.HTTP_204_NO_CONTENT
        result_status_code = response.status_code

        self.assertEqual(expected_status_code, result_status_code)

    def test_updated_product(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_user.key)
        response = self.client.patch(self.base_url, data={"name": "Bolsa UPDATE"})

        expected_status_code = status.HTTP_200_OK
        result_status_code = response.status_code

        self.assertEqual(response.data["name"], "Bolsa UPDATE")
        self.assertEqual(expected_status_code, result_status_code)

    def test_deleted_product_error_user_nopermission(self):
        self.client.credentials(
            HTTP_AUTHORIZATION="Token " + self.token_user_nopermission.key
        )
        response = self.client.delete(self.base_url)

        expected_status_code = status.HTTP_403_FORBIDDEN
        result_status_code = response.status_code

        self.assertEqual(expected_status_code, result_status_code)

    def test_updated_product_error_user_nopermission(self):
        self.client.credentials(
            HTTP_AUTHORIZATION="Token " + self.token_user_nopermission.key
        )
        response = self.client.patch(self.base_url, data={"name": "Bolsa UPDATE"})

        expected_status_code = status.HTTP_403_FORBIDDEN
        result_status_code = response.status_code

        self.assertEqual(expected_status_code, result_status_code)
