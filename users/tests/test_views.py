from urllib import response
import ipdb

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.views import status
from rest_framework.authtoken.models import Token

from users.models import User

class UserRegisterViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.base_url = reverse("user-create")
        
        cls.user_login = {"username": "g12","password": "123"}
        cls.user = {
            "username": "g12",
            "email": "1234@gmail.com",
            "password": "123",
            "wallet": 10.1,
            "plan": "Base"
        }

        cls.admin_data = {
            "username": "g12",
            "email": "1234@gmail.com",
            "password": "123",
            "wallet": 10.1,
            "plan": "Base"
        }

        cls.user_error = {}
    
    def test_create_user(self):
        response = self.client.post(self.base_url,self.user)

        expected_status_code = status.HTTP_201_CREATED
        result_status_code = response.status_code
        
        self.assertEqual(expected_status_code, result_status_code)
    
    def test_error_user_comum(self):
        response = self.client.get(self.base_url)

        expected_status_code = status.HTTP_401_UNAUTHORIZED
        result_status_code = response.status_code
        
        self.assertEqual(expected_status_code, result_status_code)
    
    def test_error_keys_user(self):
        response = self.client.post(self.base_url,self.user_error)

        expected_status_code = status.HTTP_400_BAD_REQUEST
        result_status_code = response.status_code
        
        self.assertEqual(expected_status_code, result_status_code)
    
    def test_error_duplicate_user(self):
        self.client.post(self.base_url,self.user)
        response = self.client.post(self.base_url,self.user)

        expected_status_code = status.HTTP_400_BAD_REQUEST
        result_status_code = response.status_code
        
        self.assertEqual(expected_status_code, result_status_code)