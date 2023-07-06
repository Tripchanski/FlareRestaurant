from django.shortcuts import render
from random import *
from menu_app.models import Product
from contact_app.models import Contact
from user_app.models import CartItem, Account
from cart_app.models import ProductInCart



def show_main(request):
    context = {}
    counter = 0

    all_products = Product.objects.all()
    for product in all_products:
        counter+=1
    random = randint(0, counter-1)
    random_2 = randint(0, counter-1)
    random_3 = randint(0, counter-1)
    rec_product = all_products[random]
    rec_product_2 = all_products[random_2]
    rec_product_3 = all_products[random_3]
    context['rec_product'] = rec_product
    context['rec_product_2'] = rec_product_2
    context['rec_product_3'] = rec_product_3
    


    all_contacts = Contact.objects.all()
    context['all_contacts'] = all_contacts

    return render(request, 'main.html', context)
