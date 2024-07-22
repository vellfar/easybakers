from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('product/<int:product_id>/', views.productDetails, name='productDetails'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
