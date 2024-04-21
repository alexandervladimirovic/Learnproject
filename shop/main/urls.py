from django.urls import path

from . import views
from .views import ProductListView, ProductPhoneView, ProductDeleteView

app_name = 'main'

urlpatterns = [
    # http://127.0.0.1:8000
    path('', ProductListView.as_view(), name='index'),
    # http://127.0.0.1:8000/id
    path('<int:pk>/', ProductPhoneView.as_view(), name='phones'),

    # http://127.0.0.1:8000/addphone
    path('addphone/', views.AddPhones, name='addphone'),

    # http://127.0.0.1:8000/updatephone/*id
    path('updatephone/<int:id>/', views.UpdatePhone, name='UpdatePhone'),

    # http://127.0.0.1:8000/deletephone/*id
    path('deletephone/<int:pk>/', ProductDeleteView.as_view(), name='DeletePhone'),


]