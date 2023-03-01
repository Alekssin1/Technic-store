import base64
from django.shortcuts import render
from django.views.generic.list import ListView
from django.http import HttpResponse


class Home(ListView):

    def get(self, request):
        return HttpResponse("Home")


class Register(ListView):

    def post(self, request, *args, **kwargs):
        return HttpResponse("Register")


class LoginPhone(ListView):

    def post(self, request, *args, **kwargs):
        return HttpResponse("LoginPhone")


class LoginEmail(ListView):

    def post(self, request):
        return HttpResponse("LoginEmail")


def logout_acc(request):
    return HttpResponse("logout_acc")


def addbin(request, id):
    return HttpResponse("addbin")


def del_bin_item(request, id):
    return HttpResponse("del_bin_item")
