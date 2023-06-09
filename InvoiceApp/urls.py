from django.urls import path, include

from . import views

urlpatterns = [
    # ------ LOGIN, ACCOUNT, REGISTER, LOGOUT, MAIN PAGE URLS ------
    path('login/', views.login, name='login'),
    path('account/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('logged_out/', views.logged_out, name='logged_out'),
    path('main_page/', views.main_page, name='main_page'),
    # ----- CLIENT URLS -----
    path('clients/', views.clients, name='clients'),
    path('clients/add_client', views.add_client, name='add_client'),
    path('clients/edit_client/<int:pk>', views.edit_client, name='edit_client'),
    path('clients/delete/<int:pk>', views.delete_client, name='delete_client'),
    # ----- PRODUCT URLS -----
    path('products/', views.products, name='products'),
    path('products/add_product', views.add_product, name='add_product'),
    path('products/edit_product/<int:pk>', views.edit_product, name='edit_product'),
    path('products/delete/<int:pk>', views.delete_product, name='delete_product'),
    # ----- SERVICE URLS -----
    path('services/', views.services, name='services'),
    path('services/add_service', views.add_service, name='add_service'),
    path('services/edit_service/<int:pk>', views.edit_service, name='edit_service'),
    path('services/delete/<int:pk>', views.delete_service, name='delete_service'),
    # ----- INVOICE URLS -----
    path('invoices/', views.invoices, name='invoices'),
    path('invoices/create_invoice', views.create_full_invoice, name='create_invoice'),
    path('invoices/edit_invoice/<int:pk>', views.edit_invoice, name='edit_invoice'),
    path('invoices/delete/<int:pk>', views.delete_invoice, name='delete_invoice'),
    # ----- COMPANY URLS -----
    path('company/', views.company_info, name='company_info'),
    path('company/add_company_info', views.add_company_info, name='add_company_info'),
    path('company/edit_company_info/<int:pk>', views.edit_company_info, name='edit_company_info'),
    path('company/delete_company_info/<int:pk>', views.delete_company_info, name='delete_company_info'),
    path('company/ajax_delete_company/', views.ajax_delete_company, name='ajax_delete_company'),
    # ----- TEMPLATES ------
    path('invoices/view_invoice_template/<int:pk>', views.invoice_template, name='invoice_template'),
    # ----- USER: PROFILE AND INVOICES------
    path('profile/', views.profile, name='profile'),
    path('all_user_invoices/', views.all_user_invoices, name='all_user_invoices'),
    # ----- SEARCH URLS ------
    path('search/', views.search, name='search'),
    path('search_clients/', views.search_clients, name='search_clients'),
    path('search_products/', views.search_products, name='search_products'),
    path('search_services/', views.search_services, name='search_services'),
    path('search_invoices/', views.search_invoices, name='search_invoices'),
    path('search_user_invoices/', views.search_user_invoices, name='search_user_invoices'),

    # ----- CHANGE USER PASSWORD ------
    path('change-password/', views.change_password, name='change_password'),
]
