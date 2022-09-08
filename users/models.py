import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser

class plans(models.TextChoices):
    BASE = "Base"
    PROFESSIONNELLE = "Professionnelle"
    PRIME = "Prime"
    DEFAULT = "Libre"

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    plan = models.CharField(max_length=16, choices=plans.choices, default=plans.DEFAULT)
    wallet = models.DecimalField(default=0,max_digits=10, decimal_places=2)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ["email","plan"]