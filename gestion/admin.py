from django.contrib import admin
from .models import Editorial, Libro

def formato_pesos(valor):
    return f"${valor:,.0f}".replace(",", ".")

@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais', 'fundacion', 'mostrar_presupuesto')
    search_fields = ('nombre', 'pais')
    list_filter = ('pais',)

    def mostrar_presupuesto(self, obj):
        return formato_pesos(obj.presupuesto)
    mostrar_presupuesto.short_description = "Presupuesto"

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'anio', 'mostrar_precio', 'editorial')
    search_fields = ('titulo', 'autor')
    list_filter = ('editorial',)

    def mostrar_precio(self, obj):
        return formato_pesos(obj.precio)
    mostrar_precio.short_description = "Precio"
