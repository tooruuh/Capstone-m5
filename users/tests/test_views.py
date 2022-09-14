
from urllib import response

import ipdb
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework.views import status
from users.models import User


class UserRegisterViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.base_url = reverse("user-create")

        cls.user_login = {"email": "1234@gmail.com", "password": "123"}
        cls.user = {
            "name": "g12",
            "email": "1234@gmail.com",
            "password": "123",
            "plan": "Base",
        }

        cls.admin_data = {
            "name": "g12",
            "email": "1234@gmail.com",
            "password": "123",
            "plan": "Base",
        }

        cls.user_error = {}

    def test_create_user(self):
        response = self.client.post(self.base_url, self.user)

        expected_status_code = status.HTTP_201_CREATED
        result_status_code = response.status_code

        self.assertEqual(expected_status_code, result_status_code)

    def test_error_user_comum(self):
        response = self.client.get(self.base_url)

        expected_status_code = status.HTTP_401_UNAUTHORIZED
        result_status_code = response.status_code

        self.assertEqual(expected_status_code, result_status_code)

    def test_error_keys_user(self):
        response = self.client.post(self.base_url, self.user_error)

        expected_status_code = status.HTTP_400_BAD_REQUEST
        result_status_code = response.status_code

        self.assertEqual(expected_status_code, result_status_code)

    def test_error_duplicate_user(self):
        self.client.post(self.base_url, self.user)
        response = self.client.post(self.base_url, self.user)

        expected_status_code = status.HTTP_400_BAD_REQUEST
        result_status_code = response.status_code

        self.assertEqual(expected_status_code, result_status_code)


class UserUpdateViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user_login = {"email": "1234@gmail.com", "password": "123"}
        cls.user_data = {
            "name": "g12",
            "username": "test",
            "email": "1234@gmail.com",
            "password": "123",
            "plan": "Base",
        }

        cls.admin_data = {
            "name": "g12",
            "email": "1234@gmail.com",
            "username": "test1",
            "password": "123",
            "plan": "Base",
        }

        cls.user = User.objects.create_user(**cls.user_data)
        cls.token_user = Token.objects.create(user=cls.user)

        cls.base_url = reverse("user-update", kwargs={"user_id": cls.user.id})
        cls.login_url = reverse("user-login")

    def test_login_user(self):
        response = self.client.post(self.login_url, self.user_login)

        expected_status_code = status.HTTP_200_OK
        result_status_code = response.status_code

        self.assertIn("token", response.data)
        self.assertEqual(expected_status_code, result_status_code)

    def test_updated_user(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_user.key)
        response = self.client.patch(self.base_url, data={"name": "wellington"})

        expected_status_code = status.HTTP_200_OK
        result_status_code = response.status_code

        self.assertEqual(response.data["name"], "wellington")
        self.assertEqual(expected_status_code, result_status_code)

    def test_deleted_user(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_user.key)
        response = self.client.delete(self.base_url)

        expected_status_code = status.HTTP_204_NO_CONTENT
        result_status_code = response.status_code

        self.assertEqual(expected_status_code, result_status_code)
