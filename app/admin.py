from django.contrib import admin
from .models import Biblioteca, Usuario, Libro, Prestamo

admin.site.site_header = 'Gestión de Biblioteca'
admin.site.site_title = 'Administración de Biblioteca'
admin.site.index_title = 'Panel de Administración'

admin.site.register(Biblioteca)
admin.site.register(Usuario)
admin.site.register(Libro)
admin.site.register(Prestamo)