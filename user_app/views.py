from django.shortcuts import render, redirect
from user_app.models import Account
from django.db.utils import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def show_reg_form(request):
    context = {}
    if request.method == 'POST':
        
        name = request.POST.get("name")
        country = request.POST.get("country")
        adress = request.POST.get("adress")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password_confirm")

        try:
            User.objects.get(username = email)
            context['error'] = 'Цей користувач існує'
            return response
        except:
            if password == password_confirm:
                response = render(request, 'main.html', context)
                user = User.objects.create_user(username=email, password=password, first_name = name)
                Account.objects.create(
                    name = name,  
                    phone_number = phone_number, 
                    password = password,
                    country = country,
                    adress = adress,
                    email = email,
                    user=user
                    )
                return redirect('login')
            else:
                context['error'] = 'Паролі не співпадають'

    response = render(request, 'registration.html', context)
    return response






def show_login_form(request):
    context = {}
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = authenticate(username = email, password = password)
            if user is not None:
                login(request, user)
                return redirect('main')
            else:
                context['error'] = "Електронна пошта або пароль невірні"
        except:
            context['error'] = "Такого аккаунту не існує"   

    response = render(request, 'login.html', context)
    return response
    


def user_logout(request):
    logout(request)
    return redirect('login')


def show_profile(request):
    if request.user.is_authenticated:
        account = Account.objects.get(user = request.user)
        context = {'account': account}
    else:
        return redirect('main')
    return render(request, 'ask_logout.html', context)













# -------- Love Product --------
def show_first_block(request):
    return render(request, 'user_profile/love_product.html')

# -------- All Receipt --------
def show_second_block(request):
    return render(request, 'user_profile/all_receipt.html')

# -------- All Cards --------
def show_third_block(request):
    return render(request, 'user_profile/all_cards.html')

# # -------- Shop Present Card --------
# def show_fourth_block(request):
#     return render(request, 'user_profile/shop_present_card.html')