from django import forms
from django.contrib.auth.models import User
from .models import Client, Product, Service, Invoice


class DateInputForm(forms.ModelForm):
    input_type = 'date'

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = (
            'client_name', 'registration_number', 'vat_number', 'address', 'email_address', 'phone_number',
        )

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'product_name', 'product_code', 'product_description', 'product_quantity', 'product_price',
        )

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = (
            'service_name', 'service_code', 'service_description', 'service_quantity', 'service_price',
        )

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = (
            'invoice_name', 'invoice_number', 'due_date', 'payment_terms', 'invoice_status', 'client',
            'product', 'service',
        )
        widgets = {'due_date': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),}

class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'username', 'password',
        )