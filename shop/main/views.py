from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Product


def index(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'main/index.html', context)


def id_Product(request, id):
    phone = Product.objects.get(id=id)
    context = {
        'phone': phone
    }
    return render(request, 'main/phones.html', context)


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def AddPhones(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        phone = Product(name=name, price=price, description=description, image=image)
        phone.save()
    return render(request, 'main/addphone.html')


def UpdatePhone(request, id):
    phone = Product.objects.get(id=id)
    if request.method == 'POST':
        phone.name = request.POST.get('name')
        phone.price = request.POST.get('price')
        phone.description = request.POST.get('description')
        phone.image = request.FILES.get('upload')
        phone.save()
        return redirect('/')

    context = {
        'phone': phone
    }
    return render(request, 'main/updatephone.html', context)


def DeletePhone(request, id):
    phone = Product.objects.get(id=id)
    if request.method == 'POST':
        phone.delete()
        return redirect('/')
    context = {
        'phone': phone
    }
    return render(request, 'main/deletephone.html', context)


