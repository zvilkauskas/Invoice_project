from django.urls import path, include

from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('account/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('logged_out/', views.logged_out, name='logged_out'),
    path('main_page/', views.main_page, name='main_page'),
    path('clients/', views.clients, name='clients'),
    path('clients/add_client/', views.add_client, name='add_client'),
    path('products/', views.products, name='products'),
    path('products/add_product/', views.add_product, name='add_product'),
    path('services/', views.services, name='services'),
    path('services/add_service/', views.add_service, name='add_service'),
    path('invoices/', views.invoices, name='invoices'),
    path('invoices/create_invoice/', views.create_full_invoice, name='create_invoice'),

]