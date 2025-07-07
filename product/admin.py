from django.contrib import admin
from .models import Product, Variation
from . import models

class VariationInLine(admin.TabularInline):
    model = models.Variation
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [
        VariationInLine
    ]

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Variation)