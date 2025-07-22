from django.template import Library
from django import template
from utils import utils

register = template.Library()

@register.filter
def format_price(val):
    return utils.format_price(val)