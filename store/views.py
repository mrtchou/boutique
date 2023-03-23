from django.urls import reverse
from django.shortcuts import redirect, render, get_object_or_404
from store.models import Product, Card, Order
from django.http import HttpResponse

# Create your views here.





def index(request):
    products = Product.objects.all()
    return render(request, 'store/index.html', context={"products": products})






def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'store/detail.html', context={"product":product})


#function pour ajouter produit au panier

def add_to_card(request, slug):
    user = request.user
    product = get_object_or_404(Product, slug=slug)
    #ici on recupere deux elements a droites, donc besoin
    #deux variable a gauche, le _ underscore signifi par 
    # convention une variable qui ne sera pas utilisé 
    # par la suite
    card, _ = Card.objects.get_or_create(user=user)


    #donc cela verifie si un produit est associé avec cet user, donc on recupere
    #si non on cré un new card(created)
    order, created = Order.objects.get_or_create(user=user,
                                                 product=product)
    
    
    #cas ou n'existais pas, donc créé
    if created:
        #donc dans card(panier) on ajoute dans champ orders dans db le order(produit) plus haut l'element qu'on a recuperé avec le bouton ajouter au panier...
        card.orders.add(order)
        card.save()
    else:
        order.quantity += 1
        order.save()

    return redirect(reverse("product", kwargs={"slug":slug}))


def card(request):
    card = get_object_or_404(Card, user=request.user)
    return render(request, 'store/card.html', context={"orders": card.orders.all()})


def delete_card(request):
    card = request.user.card
    if card:
        card.orders.all().delete()
        card.delete()

    return redirect('index')