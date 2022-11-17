from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('pricing/', views.pricing, name='pricing'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
]
