from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/',LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('seller-profile/<int:id>/', views.seller_profile, name='seller_profile'),
]