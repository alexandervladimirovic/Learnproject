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

    # http://127.0.0.1:8000/addphone
    path('addphone/', views.AddPhones, name='addphone'),

    # http://127.0.0.1:8000/updatephone/*id
    path('updatephone/<int:id>/', views.UpdatePhone, name='UpdatePhone'),

    # http://127.0.0.1:8000/deletephone/*id
    path('deletephone/<int:id>/', views.DeletePhone, name='DeletePhone'),


]