from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    # http://127.0.0.1:8000
    path('', views.index, name='index'),
    # http://127.0.0.1:8000/id
    path('<int:id>/', views.id_Product, name='phones'),

    # http://127.0.0.1:8000/about
    path('about/', views.about, name='about'),

    # http://127.0.0.1:8000/contacts
    path('contacts/', views.contacts, name='contacts'),

]