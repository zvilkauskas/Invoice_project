from django import forms
from django.contrib.auth.models import User
from .models import Client, Product, Service, Invoice


class DateInputForm(forms.ModelForm):
    input_type = 'date'


class AddNewClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = (
            'client_name', 'registration_number', 'vat_number', 'address', 'email_address', 'phone_number',
        )


class AddNewProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'product_name', 'product_code', 'product_description', 'product_quantity', 'product_price',
        )


class AddNewServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = (
            'service_name', 'service_code', 'service_description', 'service_quantity', 'service_price',
        )


class CreateNewInvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ('invoice_name', 'invoice_number', 'payment_terms', 'invoice_status', 'client',
                  'invoice_total')  # , 'product', 'service',)
        widgets = {
            'invoice_total': forms.NumberInput(attrs={
                'class': 'totalSum',
                'name': 'total_price',
                'readonly': True
            })
        }

        # {{form.field_name}}


class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'email', 'password',
        )

class EditInvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ('invoice_name', 'invoice_number', 'payment_terms', 'invoice_status', 'client',
                  'invoice_total')
