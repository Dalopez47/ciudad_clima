from django.contrib import admin

# Register your models here.
from ciudades.models import Consulta, Ciudad

admin.site.register(Consulta)
admin.site.register(Ciudad)