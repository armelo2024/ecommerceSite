from django.contrib import admin
from .models import Produit, Category, Commande
# heard work
admin.site.site_header = ("E-COMMERCE")
admin.site.site_title = ("OneditalMarket")
admin.site.index_title = ("Manageur")

class AdminCategorie(admin.ModelAdmin):
    list_display = ['name', 'date_sent']

class AdminProduct(admin.ModelAdmin):
    list_display = ['title', 'price', 'category', 'date_sent']
    search_fields = ["title"] 
    list_editable = ["price"]
admin.site.register(Produit, AdminProduct)

class AdminCommande(admin.ModelAdmin):
    list_display = ['item', 'nom', 'email', 'number', 'date_commande', 'ville', 'total']

admin.site.register(Category, AdminCategorie)
admin.site.register(Commande, AdminCommande)
