from django.db import models

# Create your models here.

"""
imagine le produit comment se presente dans db
Product
- Nom
- Prix (float)
- Quantite en stock (nombre entier)
- Description (chaine de caracteres)
- Image
"""

class Product(models.Model):
    name = models.CharField(max_length=128)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to="products", blank=True, null=True)
