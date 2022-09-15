import ipdb
from django.test import TestCase
from users.models import User


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user_login = {"email": "1234@gmail.com", "password": "123"}

        cls.user_data = {
            "name": "Teste User",
            "email": "teste@email.com",
            "username": "user_1",
            "password": "123",
            "plan": "Base",
        }

    def test_user_fields(self):
        self.user = User.objects.create_user(**self.user_data)

        self.assertEqual(self.user_data["name"], self.user.name)
        self.assertEqual(self.user_data["email"], self.user.email)
        self.assertEqual(self.user_data["username"], self.user.username)
        self.assertEqual(self.user_data["plan"], self.user.plan)
