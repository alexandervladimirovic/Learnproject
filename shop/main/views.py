from django.http import HttpResponse
from django.shortcuts import render

from .models import Product


def index(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'main/index.html', context)


def id_Product(request, id):
    phones = Product.objects.get(id=id)
    context = {
        'phones': phones
    }
    return render(request, 'main/phones.html', context)


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')
