from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, default='1')
    name = models.CharField(max_length=100, unique=True, null=False, blank=False, verbose_name= 'Наименование')
    price = models.IntegerField(verbose_name='Цена')
    description = models.TextField(max_length=300, verbose_name='Описание')
    image = models.ImageField( blank=True, upload_to='images')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


class OrderPhone(models.Model):
    customer_username = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    amount = models.IntegerField()
    stripe_payment = models.CharField(max_length=200)
    has_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)