from django.contrib import admin
from store.models import Product, Order, Card

# Register your models here.
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Card)