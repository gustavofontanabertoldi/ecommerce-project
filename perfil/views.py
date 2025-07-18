from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponse
# Create your views here.

class Create(View):
    def get(*args, **kwargs):
        return HttpResponse("create")

class Update(View):
    def get(*args, **kwargs):
        return HttpResponse("update")

class Login(View):
    def get(*args, **kwargs):
        return HttpResponse("login")

class Logout(View):
    def get(*args, **kwargs):
        return HttpResponse("logout")
