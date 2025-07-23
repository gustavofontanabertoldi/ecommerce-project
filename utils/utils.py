def format_price(val):
    return f"R$ {val:.2f}".replace('.', ',')

def cart_total_qtd(cart):
    return sum([item['quantity'] for item in cart.values()])