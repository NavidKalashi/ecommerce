from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='sotre'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
]
