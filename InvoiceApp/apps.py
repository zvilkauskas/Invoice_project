from django.apps import AppConfig


class InvoiceappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'InvoiceApp'

    def ready(self):
        from .signals import create_profile, save_profile
