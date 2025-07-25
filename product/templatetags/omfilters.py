from django.template import Library
from django import template
from utils import utils

register = template.Library()

@register.filter
def format_price(val):
    return utils.format_price(val)

@register.filter
def cart_total_qtd(cart):
    return utils.cart_total_qtd(cart)

@register.filter
def cart_total(cart):
    return utils.cart_total(cart)