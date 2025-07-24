from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from  django.views.generic.list import ListView
from  django.views.generic.detail import DetailView
from django.views import View
from django.http import HttpResponse
from django.contrib import messages
from . import models
from pprint import pprint
# Create your views here.

class ProductList(ListView):
    model = models.Product
    template_name = 'product/List.html'
    context_object_name = "products"
    paginate_by = 10
    ordering = ['price_marketing_off']

class ProductDetail(DetailView):
    model = models.Product
    template_name = 'product/Detail.html'
    context_object_name = "product"
    slug_url_kwarg = 'slug'

class AddToCart(View):
    def get(self, *args, **kwargs):
        
        # Apaga o carrinho quando necessário
        # TODO: remover essas linhas mais pra frente
        # if self.request.session.get('cart'):
        #     del self.request.session['cart']
        #     self.request.session.save()

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
        stock_variation = variation.stock
        product = variation.product

        product_id = product.id
        product_name = product.name
        variation_name = variation.name or ''
        unit_price = variation.price
        promotional_unit_price = variation.promotional_price
        quantity = 1
        slug = product.slug
        image = product.image

        if image:
            image = image.name
        else:
            image = ''

        if variation.stock < 1:
            messages.error(
                self.request,
                'Estoque insuficiente'
            )
            return redirect(http_referer)

        # O carrinho é um dissionário presente dentro de uma sessão
        if not self.request.session.get("cart"):
            self.request.session['cart'] = {}
            self.request.session.save()
        
        cart = self.request.session.get('cart', {})

        variation_id = str(variation.id)

        #Aqui ele verifica se algumas das chaves de variação existem no carrinho,
        if variation_id in cart:
            cart_amount = cart[variation_id]['quantity']
            cart_amount += 1

            if stock_variation < cart_amount:
                messages.error(
                    self.request,
                    f'Insufficient stock for {cart_amount}x of the product {product_name}.'
                )
                cart_amount = stock_variation
            
            cart[variation_id]['amount'] = cart_amount
            cart[variation_id]['total_price'] = unit_price * cart_amount
            cart[variation_id]['promotional_total_price'] = promotional_unit_price * cart_amount
        else:
            cart[variation_id] = {
                'product_id' : product_id,
                'product_name' : product_name,
                'variation_name': variation_name,
                'variation_id': variation_id,
                'unit_price': unit_price,
                'promotional_unit_price': promotional_unit_price,
                'total_price' : unit_price,
                'promotional_total_price': promotional_unit_price,
                'quantity' : 1,
                'slug': slug,
                'image': image
            }
        
        self.request.session.save()
        messages.success(
            self.request,
            f'{product.name}, {variation.name} was added to the cart.'
        )
        return redirect(http_referer)

class RemoveFromCart(View):
    def get(self, *args, **kwargs):

        http_referer = self.request.META.get(
            'HTTP_REFERER',
            reverse('product:list')
        )
        variation_id = self.request.GET.get('vid')
        
        if not variation_id:
            return redirect(http_referer)
        
        if not self.request.session.get('cart'):
            return redirect(http_referer)
        
        if variation_id not in self.request.session['cart']:
            return redirect(http_referer)
        
        cart = self.request.session['cart'][variation_id]

        messages.success(
            self.request,
            f'Produto {cart['product_name']} {cart['variation_name']} removido do carrinho'
        )

        del self.request.session['cart'][variation_id]
        self.request.session.save()
        return redirect(http_referer)


class Cart(View):
    def get(self, *args, **kwargs):
        context = {
            'cart':self.request.session.get('cart', {}),
        }
        return render(self.request, 'product/cart.html', context)

class PurchaseSummary(View):
    def get(*args, **kwargs):
        return HttpResponse("Finish")
