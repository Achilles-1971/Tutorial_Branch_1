from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.template.response import TemplateResponse
from django.http import *
from django.shortcuts import render
def index(request):
    cat = []
    return render(request, "WEB1/index.html", context={"cat": cat})
def about(request):
    return HttpResponse("About")
def contact(request):
    return HttpResponseRedirect("/about")
def details(request):
    return HttpResponsePermanentRedirect("/")
def product_list(request):
    products = [
    {'name': 'Игорь', 'age': 23 },
    ]