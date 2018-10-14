from django.db import models

class Settings(models.Model):
    '''Guarda los settings del sistema'''
    # Datos de la business
    name = models.CharField(max_length=25)
    direction = models.TextField(max_length=100)
    phone = models.CharField(max_length=25)
    email = models.EmailField(null=True, blank=True)
    # Datos de sales
    TIPOS = (
        ('ticket', 'Ticket'),
        ('pagina', 'Página'))
    simbolo_moneda = models.CharField(max_length=10, default='C$')
    ruc = models.CharField(max_length=100, null=True, blank=True)
    tipo_factura = models.CharField(max_length=15, choices=TIPOS, default='ticket')
    # Datos CLOUD
    api_url = models.CharField(max_length=150, default='https://adm-api.herokuapp.com')
    api_key = models.CharField(max_length=200, blank=True, null=True)
