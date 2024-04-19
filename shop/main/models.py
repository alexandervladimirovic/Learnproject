from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False, blank=False, verbose_name= 'Наименование')
    price = models.IntegerField(verbose_name='Цена')
    description = models.TextField(max_length=300, verbose_name='Описание')
    image = models.ImageField( blank=True, upload_to='images')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name