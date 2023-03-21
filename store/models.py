from django.db import models
from shop.settings import AUTH_USER_MODEL

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
    slug = models.SlugField(max_length=128)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to="products", blank=True, null=True)

    def __str__(self):
        return f"{self.name}"
    
    def get_absolute_url(self):
        return reverse("product", kwargs={"slug": self.slug})
    




#Article (order)
"""
- utilisateur (celui qui souhaite acheter => champ)
- produit (ce qu'on veut acheter =>)
- Quantité (combien d'articles on veut => int)
- Commandé ou non (commandé donc payé ou pas =>boolean)
"""
class Order(models.Model):
    #un à plusieurs pour la relation. 
    # un user peut avoir plusieur articles, 
    # et supprime en cascade pour supprimer les articles, 
    # si user est supprimer
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE) 
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"





#Panier (Card)
"""
- Utilisateur (chaque utilisateur a un panier =>)
- Articles (plusieurs articles dans le panier =>)
- Commandé ou non (donc passé commande ou pas encore)
- Date de la commande (pour savoir quand la commande a ete faite)
"""

class Card(models.Model):
    #un user peut avoir que un panier(card)
    #supprime en cascade, si pas user donc pas card
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    #plusieurs articles peuvent etre ajouter au panier
    orders = models.ManyToManyField(Order)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.user.username