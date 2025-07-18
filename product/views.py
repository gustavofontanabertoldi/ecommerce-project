from django.shortcuts import render
from  django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
from . import models
# Create your views here.

class ProductList(ListView):
    model = models.Product
    template_name = 'product/List.html'
    context_object_name = "products"
    paginate_by = 10

class ProductDetail(View):
    def get(*args, **kwargs):
        return HttpResponse("productDetail")

class AddToCart(View):
    def get(*args, **kwargs):
        return HttpResponse("addToCart")

class RemoveFromCart(View):
    def get(*args, **kwargs):
        return HttpResponse("RemoveFromCart")

class Cart(View):
    def get(*args, **kwargs):
        return HttpResponse("Cart")

class Finish(View):
    def get(*args, **kwargs):
        return HttpResponse("Finish")
