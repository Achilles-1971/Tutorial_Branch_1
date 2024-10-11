from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Person
from django.http import *
from django.shortcuts import render
def index(request):
    people = Person.objects.all()
    return render(request, "index.html", {"people": people})
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

def create(request):
 if request.method == "POST":
    klient = Person()
    klient.name = request.POST.get("name")
    klient.age = request.POST.get("age")
    klient.save()
 return HttpResponseRedirect("/")

