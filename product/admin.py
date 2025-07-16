from django.contrib import admin
from .models import Product, Variation
from . import models

class VariationInLine(admin.TabularInline):
    model = models.Variation
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "short_description", "price_marketing", "price_marketing_off"]

    inlines = [
        VariationInLine
    ]

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Variation)