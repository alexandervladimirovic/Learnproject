from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotFound, JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import DeleteView
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import json
import stripe

from .models import Product, OrderPhone


def index(request):
    page_obj = products = Product.objects.all()

    item_name = request.GET.get('search')
    if item_name != '' and item_name is not None:
        page_obj = products.filter(name__icontains=item_name)

    paginator = Paginator(page_obj, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'main/index.html', context)


class ProductListView(ListView):
    model = Product
    template_name = 'main/index.html'
    context_object_name = 'products'
    paginate_by = 1


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
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super(ProductPhoneView, self).get_context_data(**kwargs)
        context['stripe_publishable_key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context


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


@csrf_exempt
def create_checkout_session(request, id):
    product = get_object_or_404(Product, pk=id)
    stripe.api_key = settings.STRIPE_SECRET_KEY
    checkout_session = stripe.checkout.Session.create(
        customer_email=request.user.email,
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': product.name,
                    },
                    'unit_amount': int(product.price * 100),
                },
                'quantity': 1,
            }
        ],
        mode="payment",
        success_url=request.build_absolute_uri(reverse('main:success'))
                    + '?session_id+{CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri(reverse('main:failed')),
    )
    order = OrderPhone()
    order.customer_username = request.user.username
    order.product = product
    order.stripe_payment_intent = checkout_session['payment_intent']
    order.amount = int(product.price * 100)
    order.save()
    return JsonResponse({'sessionId': checkout_session.id})


class PaymentSuccessView(TemplateView):
    template_name = 'main/payment_success.html'

    def get(self, request, *args, **kwargs):
        session_id = request.GET.get('session_id')
        if session_id is None:
            return HttpResponseNotFound
        session = stripe.checkout.Session.retrieve(session_id)
        stripe.api_key = settings.STRIPE_SECRET_KEY
        order = get_object_or_404(OrderPhone, stripe_payment_intent=session.session.payment_intent)
        order.has_paid = True
        order.save()
        return render(request, self.template_name)


class PaymentFailedView(TemplateView):
    template_name = 'main/payment_failed.html'
