from django import forms
from django.contrib.auth.models import User
from .models import Client, Product, Service, Invoice, CompanyInfo


# Date input form
class DateInputForm(forms.ModelForm):
    input_type = 'date'


# User login form
class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'email', 'password',
        )


# ------------------------ ADD OR CREATE COMPANY INFO CLIENT, PRODUCT, SERVICE, INVOICE FORMS --------------------------
class AddCompanyInfoForm(forms.ModelForm):
    class Meta:
        model = CompanyInfo
        fields = (
            'company_name', 'company_registration_number', 'company_vat_number', 'company_address',
            'company_email_address', 'company_phone_number',
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


class AddNewClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = (
            'client_name', 'registration_number', 'vat_number', 'address', 'email_address', 'phone_number',
        )


class CreateNewInvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ('invoice_name', 'invoice_number', 'payment_terms', 'invoice_status', 'client',
                  'invoice_total', 'invoice_products_services')
        widgets = {
            'invoice_total': forms.NumberInput(attrs={
                'class': 'totalSum',
                'name': 'total_price',
                'readonly': True
            }),
            'invoice_products_services': forms.HiddenInput(attrs={
                'class': 'invoiceProductsServices',
                'name': 'invoice_products_services',
                'readonly': True,
            })
        }

    def set_invoice_products_services(self, invoice_description):
        data = self.data.copy()
        data['invoice_products_services'] = invoice_description
        self.data = data

        # {{form.field_name}}


# ----------------------------------- EDIT COMPANY INFO INVOICE, PRODUCT, SERVICE, CLIENT FORMS -------------------------------------
class EditCompanyInfoForm(forms.ModelForm):
    class Meta:
        model = CompanyInfo
        fields = (
            'company_name', 'company_registration_number', 'company_vat_number', 'company_address',
            'company_email_address', 'company_phone_number',
        )


class EditInvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = (
            'invoice_products_services', 'invoice_name', 'invoice_number', 'payment_terms', 'invoice_status', 'client')


class EditProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'product_name', 'product_code', 'product_description', 'product_quantity', 'product_price',
        )


class EditServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = (
            'service_name', 'service_code', 'service_description', 'service_quantity', 'service_price',
        )


class EditClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = (
            'client_name', 'registration_number', 'vat_number', 'address', 'email_address', 'phone_number',
        )
