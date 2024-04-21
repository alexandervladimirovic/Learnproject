from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView

from .models import Product


# def index(request):
#     products = Product.objects.all()
#     context = {
#         'products': products
#     }
#     return render(request, 'main/index.html', context)


class ProductListView(ListView):
    model = Product
    template_name = 'main/index.html'
    context_object_name = 'products'


# def id_Product(request, id):
#     phone = Product.objects.get(id=id)
#     context = {
#         'phone': phone
#     }
#     return render(request, 'main/phones.html', context)


class ProductPhoneView(DetailView):
    model = Product
    template_name = 'main/phones.html'
    context_object_name = 'phone'


@login_required
def AddPhones(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        seller = request.user
        phone = Product(name=name, price=price, description=description, image=image, seller=seller)
        phone.save()
    return render(request, 'main/addphone.html')


@login_required
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


@login_required
def DeletePhone(request, id):
    phone = Product.objects.get(id=id)
    if request.method == 'POST':
        phone.delete()
        return redirect('/')
    context = {
        'phone': phone
    }
    return render(request, 'main/deletephone.html', context)


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('main:index')

