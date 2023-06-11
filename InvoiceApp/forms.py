from django import forms
from django.contrib.auth.models import User
from .models import Client, Product, Service, Invoice
from django_select2 import forms as s2forms


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
        fields = ('invoice_name', 'invoice_number', 'payment_terms', 'invoice_status',)# 'client', 'product', 'service',)
        #widgets = {'due_date': forms.HiddenInput()}



# type="email" class="form-control" id="floatingInput" placeholder="name@example.com"
class UserLoginForm(forms.ModelForm):
    # username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'id': 'floatingInput', 'for':"floatingInput"}), required=True)
    # password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mb-3', 'id': 'floatingPassword'}), required=True)

    class Meta:
        model = User
        fields = (
            'email', 'password',
        )


class SelectProductForm(s2forms.ModelSelect2Widget):
    class Meta:
        model = Product
        fields = ['product_name']


class SelectClientForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['client']