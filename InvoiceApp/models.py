from django.db import models
from django.contrib.auth.models import User
# pip install uuid
import uuid
from django.utils import timezone, dateformat
from datetime import datetime


class Client(models.Model):
    # Basic data
    client_id = models.AutoField(primary_key=True)
    client_name = models.CharField("Kliento pavadinimas", max_length=200, blank=False, null=False)
    registration_number = models.CharField("Įmonės kodas", max_length=50, blank=True, null=True)
    vat_number = models.CharField("PVM kodas", max_length=50, blank=True, null=True)
    address = models.TextField("Adresas", max_length=200, blank=True, null=True)
    email_address = models.EmailField("El. paštas", max_length=100, blank=True, null=True)
    phone_number = models.CharField("Telefono numeris", max_length=20, blank=True, null=True)
    # Additional data
    date_created = models.DateTimeField(verbose_name="Sukurtas", blank=True, null=True, default=datetime.now)
    last_updated = models.DateTimeField(verbose_name="Redaguotas", blank=True, null=True)

    def __str__(self):
        return f"{self.client_name} " \
               f"{self.registration_number} " \
               f"{self.vat_number} " \
               f"{self.address} " \
               f"{self.email_address} " \
               f"{self.phone_number} " \
               f"{self.date_created} " \
               f"{self.last_updated} "

    # Saves date_created and last_updated data in desired formatting
    # Settings.py USE_TZ = False.
    def save(self, *args, **kwargs):
        formatted_date = dateformat.format(timezone.now(), 'Y-m-d H:i')

        if self.date_created is None:
            self.date_created = formatted_date

        self.last_updated = formatted_date

        super(Client, self).save(*args, **kwargs)

    #
    # def save(self, *args, **kwargs):
    #
    #     if self.date_created is None:
    #         self.date_created = timezone.localtime(timezone.now())
    #
    #     self.last_updated = timezone.localtime(timezone.now())
    #
    #     super(Client, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"


class Product(models.Model):
    # Basic data
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField("Prekės pavadinimas", max_length=500, blank=False, null=False)
    product_code = models.CharField("Prekės kodas", max_length=50, blank=False, null=False)
    product_description = models.TextField("Prekės aprašymas", max_length=1000, blank=True, null=True)
    product_quantity = models.FloatField("Kiekis", blank=True, null=True)
    product_price = models.FloatField("Kaina", blank=True, null=True)
    # Additional data
    date_created = models.DateTimeField(verbose_name="Sukurta", blank=True, null=True, default=datetime.now)
    last_updated = models.DateTimeField(verbose_name="Redaguota", blank=True, null=True)

    def __str__(self):
        return f"{self.product_name} " \
               f"{self.product_code} " \
               f"{self.product_description} " \
               f"{self.product_quantity} " \
               f"{self.product_price} " \
               f"{self.date_created} " \
               f"{self.last_updated}"

    def save(self, *args, **kwargs):
        formatted_date = dateformat.format(timezone.now(), 'Y-m-d H:i')

        if self.date_created is None:
            self.date_created = formatted_date

        self.last_updated = formatted_date

        super(Product, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class Service(models.Model):
    # Basic data
    service_id = models.AutoField(primary_key=True)
    service_name = models.CharField("Paslaugos pavadinimas", max_length=500, blank=False, null=False)
    service_code = models.CharField("Paslaugos kodas", max_length=50, blank=False, null=False)
    service_description = models.TextField("Paslaugos aprašymas", max_length=1000, blank=True, null=True)
    service_quantity = models.FloatField("Kiekis", blank=True, null=True)
    service_price = models.FloatField("Kaina", blank=True, null=True)
    # Additional data
    date_created = models.DateTimeField(verbose_name="Sukurtas", blank=True, null=True, default=datetime.now)
    last_updated = models.DateTimeField(verbose_name="Redaguotas", blank=True, null=True)

    def __str__(self):
        return f"{self.service_name} " \
               f"{self.service_code} " \
               f"{self.service_description} " \
               f"{self.service_quantity} " \
               f"{self.service_price} " \
               f"{self.date_created} " \
               f"{self.last_updated}"

    def save(self, *args, **kwargs):
        formatted_date = dateformat.format(timezone.now(), 'Y-m-d H:i')

        if self.date_created is None:
            self.date_created = formatted_date

        self.last_updated = formatted_date

        super(Service, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"


class Invoice(models.Model):
    # Basic data
    invoice_id = models.AutoField(primary_key=True)
    invoice_name = models.CharField("Pavadinimas", max_length=200, blank=False, null=False)
    invoice_number = models.IntegerField("Sąskaitos numeris", blank=False, null=False)
    due_date = models.DateField("Apmokėti iki", blank=False, null=False)
    TERMS_OF_PAYMENT = [
        ('1d', '1 diena'),
        ('3d', '3 dienos'),
        ('5d', '5 dienos'),
        ('7d', '7 dienos'),
        ('14d', '14 dienų'),
        ('30d', '30 dienų'),
        ('60d', '60 dienų'),
    ]
    payment_terms = models.CharField(max_length=10, blank=False, null=False, choices=TERMS_OF_PAYMENT, default='30d')
    STATUS_OF_INVOICE = [
        ('l', 'Laukiama apmokėjimo'),
        ('a', 'Apmokėta'),
        ('p', 'Pradelsta'),
    ]
    invoice_status = models.CharField(max_length=20, blank=False, null=False, choices=STATUS_OF_INVOICE, default='l')
    # Related data
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, blank=True, null=True)
    # Additional data
    date_created = models.DateTimeField(verbose_name="Sukurta", blank=True, null=True, default=datetime.now)
    last_updated = models.DateTimeField(verbose_name="Redaguota", blank=True, null=True)

    def __str__(self):
        return f"{self.invoice_number} {self.invoice_name} {self.due_date} {self.date_created} {self.invoice_status} "

    def save(self, *args, **kwargs):
        formatted_date = dateformat.format(timezone.now(), 'Y-m-d H:i')

        if self.date_created is None:
            self.date_created = formatted_date

        self.last_updated = formatted_date

        super(Invoice, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Invoice"
        verbose_name_plural = "Invoices"
