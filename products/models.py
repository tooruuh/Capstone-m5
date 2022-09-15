import uuid
from django.db import models

class CategorysChoices(models.TextChoices):
    ROUPAS     = "Roupas"
    ACESSORIOS = "Acessórios"
    JOIAS      = "Jóias"
    RELOGIOS   = "Relógios"
    BOLSAS     = "Bolsas"
    CALÇADOS   = "Calçados"
    DEFAULT    = "Geral"
    

class Product(models.Model):
    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image       = models.CharField(max_length=257)
    name        = models.CharField(max_length=128)
    description = models.TextField()
    price       = models.DecimalField(max_digits=10, decimal_places=2) 
    category    = models.CharField(max_length=20, choices=CategorysChoices.choices, default=CategorysChoices.DEFAULT)
    is_active   = models.BooleanField(default=True)
    is_new      = models.BooleanField()
    
    seller = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name="products" )
    