from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import *
from cart_app.models import *
from user_app.models import *



def show_menu(request):
    context = {}
    all_products = Product.objects.all()
    context['all_products'] = all_products
    if request.method == 'POST':
        product_pk = request.POST.get('product_pk')
        count = int(request.POST.get('count', 1))
        is_in_cart = False

        if request.user.is_authenticated:
            account = Account.objects.get(user=request.user)
            product = Product.objects.get(pk=product_pk)
            cart_item, created = CartItem.objects.get_or_create(
                product=product,
                account=account,
                defaults={'count': count}
            )
            if not created:
                cart_item.count = count
                cart_item.save()
        else:
            session_key = request.session.session_key
            if not session_key:
                request.session.cycle_key()
                session_key = request.session.session_key
            product = Product.objects.get(pk=product_pk)
            cart_item, created = ProductInCart.objects.get_or_create(
                product=product,
                session_key=session_key,
                defaults={'count': count}
            )
            if not created:
                cart_item.count = count
                cart_item.save()
            else:
                is_in_cart = True
        
        return JsonResponse({'is_in_cart': is_in_cart})

    return render(request, 'menu.html', context)


def show_product(request, product_pk):
    if request.method == 'POST':
        is_in_cart = False
        if request.user.is_authenticated:
            account = Account.objects.get(user=request.user)
            product = Product.objects.get(pk=product_pk)
            count = int(request.POST.get('count', 1))
            cart_item, created = CartItem.objects.get_or_create(
                product=product,
                account=account,
                defaults={'count': count}
            )
            if not created:
                cart_item.count = count
                cart_item.save()
            else:
                is_in_cart = True

            try:
                username = request.POST.get('username')
                rating = request.POST.get('rating')
                review = request.POST.get('review')
                Comment.objects.create(username=username, review=review, rating=rating, product_id=product_pk)
            except:
                pass
        else:
            session_key = request.session.session_key
            if not session_key:
                request.session.cycle_key()
                session_key = request.session.session_key
            product = Product.objects.get(pk=product_pk)
            count = int(request.POST.get('count', 1))
            cart_item, created = ProductInCart.objects.get_or_create(
                product=product,
                session_key=session_key,
                defaults={'count': count}
            )
            if not created:
                cart_item.count = count
                cart_item.save()
            else:
                is_in_cart = True

            try:
                username = request.POST.get('username')
                rating = request.POST.get('rating')
                review = request.POST.get('review')
                Comment.objects.create(username=username, review=review, rating=rating, product_id=product_pk)
            except:
                pass
        return JsonResponse({'is_in_cart': is_in_cart})
        
    product = get_object_or_404(Product, pk=product_pk)
    comments = Comment.objects.filter(product_id=product_pk)
    comment_amount = 0
    comment_rating = 0
    for comment in comments:
        comment_rating += comment.rating
        comment_amount += 1
    try:
        final_rating = comment_rating/comment_amount
    except:
        final_rating = 0
    return render(request, "product.html", context = {'product': product, 'comments': comments, 'final_rating': round(final_rating, 1)})
