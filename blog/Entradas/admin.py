from django.contrib import admin
from Entradas.models import categoria
from Entradas.models import entrada
# Register your models here.
admin.site.register(entrada)
admin.site.register(categoria)
