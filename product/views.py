from django.shortcuts import render
from  django.views.generic.list import ListView
from  django.views.generic.detail import DetailView
from django.views import View
from django.http import HttpResponse
from . import models
# Create your views here.

class ProductList(ListView):
    model = models.Product
    template_name = 'product/List.html'
    context_object_name = "products"
    paginate_by = 10

class ProductDetail(DetailView):
    model = models.Product
    template_name = 'product/Detail.html'
    context_object_name = "product"
    slug_url_kwarg = 'slug'

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
