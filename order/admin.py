from django.contrib import admin
from . import models
# Register your models here.

class OrderItemInLine(admin.TabularInline):
    model = models.OrderItem
    extra=1

class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderItemInLine
    ]

admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.OrderItem)