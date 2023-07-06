from django import template
from user_app.models import *
from cart_app.models import *

register = template.Library()

@register.simple_tag()
def get_cartitems_amount(request):
    if request.user.is_authenticated:
        account = Account.objects.get(user = request.user)
        cart_item_count = CartItem.objects.filter(account = account).count()
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.cycle_key()
            session_key = request.session.session_key
        cart_item_count = ProductInCart.objects.filter(session_key = session_key).count()
    return cart_item_count