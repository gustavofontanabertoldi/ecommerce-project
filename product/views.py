from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from  django.views.generic.list import ListView
from  django.views.generic.detail import DetailView
from django.views import View
from django.http import HttpResponse
from django.contrib import messages
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
    def get(self, *args, **kwargs):
        http_referer = self.request.META.get(
            'HTTP_REFERER',
            reverse('product:list')
        )
        variation_id = self.request.GET.get('vid')
        if not variation_id:
            messages.error(
                self.request,
                'product do not exist'
            )
            return redirect(http_referer)
        
        variation = get_object_or_404(models.Variation, id=variation_id)

        if not self.request.session.get("cart"):
            self.request.session['cart'] = {}
            self.request.session.save()
        
        cart = self.request.session['cart']

        if variation_id in cart:
            #TODO: variação existe no carrinho
            pass
        else:
            #TODO: variação não existe no carrinho
            pass
        return HttpResponse(f'{variation.product} {variation.name}')

class RemoveFromCart(View):
    def get(*args, **kwargs):
        return HttpResponse("RemoveFromCart")

class Cart(View):
    def get(*args, **kwargs):
        return HttpResponse("Cart")

class Finish(View):
    def get(*args, **kwargs):
        return HttpResponse("Finish")
