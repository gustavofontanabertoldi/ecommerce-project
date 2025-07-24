def format_price(val):
    return f"R$ {val:.2f}".replace('.', ',')

def cart_total_qtd(cart):
    return sum([item['quantity'] for item in cart.values()])

def cart_total(cart):
    return sum(
        [
            item.get('promotional_total_price')
            if item.get('promotional_total_price')
            else item.get('total_price')
            for item
            in cart.values()
        ]
    )