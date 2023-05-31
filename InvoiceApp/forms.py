from django import forms
from django.contrib.auth.models import User
<<<<<<< HEAD
from django.contrib.auth.forms import UserCreationForm
from .models import Client, Product, Service, Invoice



=======
from .models import Client, Product, Service, Invoice


>>>>>>> forms
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
<<<<<<< HEAD
=======

>>>>>>> forms
    class Meta:
        model = Invoice
        fields = (
            'invoice_name', 'invoice_number', 'due_date', 'payment_terms', 'invoice_status', 'client',
            'product', 'service',
        )
        widgets = {'due_date': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),}

<<<<<<< HEAD
class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'username', 'password',
        )

# class RegistrationForm(UserCreationForm):
#     username = forms.CharField(max_length=150)
#     first_name = forms.CharField(max_length=150)
#     last_name = forms.CharField(max_length=150)
#     position = forms.CharField(max_length=150)
#     email = forms.EmailField(max_length=150)
#     password1 = forms.CharField(widget=forms.PasswordInput)
#     password2 = forms.CharField(widget=forms.PasswordInput)
#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
#
#     def __init__(self, *args, **kwargs):
#         super(RegistrationForm, self).__init__(*args, **kwargs)
#         self.fields['username'].widget.attrs['class'] = 'form-control'
#         self.fields['first_name'].widget.attrs['class'] = 'form-control'
#         self.fields['last_name'].widget.attrs['class'] = 'form-control'
#         self.fields['email'].widget.attrs['class'] = 'form-control'
#         self.fields['password1'].widget.attrs['class'] = 'form-control'
#         self.fields['password2'].widget.attrs['class'] = 'form-control'
=======


# type="email" class="form-control" id="floatingInput" placeholder="name@example.com"
class UserLoginForm(forms.ModelForm):
    # username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'id': 'floatingInput', 'for':"floatingInput"}), required=True)
    # password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mb-3', 'id': 'floatingPassword'}), required=True)

    class Meta:
        model = User
        fields = (
            'email', 'password',
        )
>>>>>>> forms
