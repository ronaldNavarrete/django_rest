from django.contrib import admin
from .models import Sede, Ventanilla

admin.site.site_header = "Administración de Ventanilla"

admin.site.register(Sede)
admin.site.register(Ventanilla)