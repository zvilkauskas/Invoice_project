from django.contrib import admin
from .models import Client, Product, Service, Invoice


class ClientAdmin(admin.ModelAdmin):
    # Changes default date and time format (date: M-D-Y, time: a.m./p.m.) to desired format in admin page
    @admin.display(description='Sukurtas')
    def admin_date_created(self, obj):
        return obj.date_created.strftime('%Y-%m-%d, %H:%M')
        # return obj.date_created.strftime('%Y-%m-%d, %H:%M')

    # This one does the same in the next column
    @admin.display(description='Redaguotas')
    def admin_last_updated(self, obj):
        return obj.last_updated.strftime('%Y-%m-%d, %H:%M')

    list_display = (
        'client_id', 'client_name', 'registration_number', 'vat_number', 'address',
        'email_address', 'phone_number', 'admin_date_created', 'admin_last_updated'
    )


class ProductAdmin(admin.ModelAdmin):
    @admin.display(description='Sukurta')
    def admin_date_created(self, obj):
        return obj.date_created.strftime('%Y-%m-%d, %H:%M')

    @admin.display(description='Redaguota')
    def admin_last_updated(self, obj):
        return obj.last_updated.strftime('%Y-%m-%d, %H:%M')

    list_display = (
        'product_id', 'product_name', 'product_code', 'product_description', 'product_quantity',
        'product_price', 'admin_date_created', 'admin_last_updated'
    )


class ServiceAdmin(admin.ModelAdmin):
    @admin.display(description='Sukurtas')
    def admin_date_created(self, obj):
        return obj.date_created.strftime('%Y-%m-%d, %H:%M')

    @admin.display(description='Redaguotas')
    def admin_last_updated(self, obj):
        return obj.last_updated.strftime('%Y-%m-%d, %H:%M')

    list_display = (
        'service_id', 'service_name', 'service_code', 'service_description', 'service_quantity',
        'service_price', 'admin_date_created', 'admin_last_updated'
    )


class InvoiceAdmin(admin.ModelAdmin):
    @admin.display(description='Sukurta')
    def admin_date_created(self, obj):
        return obj.date_created.strftime('%Y-%m-%d, %H:%M')

    @admin.display(description='Redaguota')
    def admin_last_updated(self, obj):
        return obj.last_updated.strftime('%Y-%m-%d, %H:%M')

    @admin.display(description='Apmokėti iki')
    def admin_due_date(self, obj):
        return obj.due_date.strftime('%Y-%m-%d')

    list_display = (
        'invoice_id', 'invoice_name', 'invoice_number', 'admin_date_created',
        'admin_due_date', 'admin_last_updated', 'invoice_status', 'invoice_total', 'client')# 'product', 'service',)


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Invoice, InvoiceAdmin)
