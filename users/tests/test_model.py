import ipdb

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.views import status

class UserModelTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        ...