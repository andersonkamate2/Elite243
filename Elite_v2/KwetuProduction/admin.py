from django.contrib import admin
from .models import tproduit, tentreprsie,tcathegorie

@admin.register(tproduit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ('nomp', 'prix', 'description', 'image')

@admin.register(tentreprsie)
class EntrepAdmin(admin.ModelAdmin):
    list_display = ('nomE', 'emailE')

@admin.register(tcathegorie)
class CathAdmin(admin.ModelAdmin):
    list_display = ('nomCat',)
    search_fields = ('nomCat',)


