def total_price(products_in_cart):
    full_price = 0
    for product_in_cart in products_in_cart:
        counter_price = product_in_cart.product.price * product_in_cart.count
        full_price += counter_price
        product_in_cart.counter_price = counter_price
    return full_price