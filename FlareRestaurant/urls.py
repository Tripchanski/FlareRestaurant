"""FlareRestaurant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from main_page.views import *
from user_app.views import *
from menu_app.views import *
from contact_app.views import *
from cart_app.views import *

from FlareRestaurant.settings import DEBUG, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_main, name='main'),
    path('menu/', show_menu, name='menu'),  
    path('menu/<product_pk>', show_product, name='product'),

    path('contacts/', show_contact, name='contacts'),

    path('cart/', show_cart, name='cart'),
    path('delete_from_cart/', delete_from_cart, name='delete_from_cart'),
    path('order/', get_receipt, name='order'),

    path('login/', show_login_form, name='login'),
    path('registration/', show_reg_form, name='registration'),
    path('logout/', user_logout, name = 'logout'),
    path('ask_logout/', show_profile, name='ask_logout'),
    path('profile/love_product/', show_first_block, name = 'love_product'),
    path('profile/all_receipt/', show_second_block, name='all_receipt'),
    path('profile/all_cards/', show_third_block, name='all_cards'),
    # path('profile/show_present_card/', show_fourth_block, name='show_present_card')
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)