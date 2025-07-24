from django.shortcuts import render
from django.views.generic import View
from django.views.generic.list import ListView
from django.http import HttpResponse
# Create your views here.

class Pay(View):
    def get(*args, **kwargs):
        return HttpResponse("pay")

class SaveOrder(View):
    def get(*args, **kwargs):
        return HttpResponse("closeOrder")

class Detail(View):
    def get(*args, **kwargs):
        return HttpResponse("Detail")
