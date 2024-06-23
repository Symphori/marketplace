# Importation des modules nécessaires
from django.contrib import admin
from core.models import CartOrderProducts, Product, Category, Vendor, CartOrder, ProductImages, ProductReview, wishlist_model, Address

# Définition d'une classe d'administration pour les images des produits
class ProductImagesAdmin(admin.TabularInline):
    model = ProductImages  # Utilisation du modèle ProductImages pour l'affichage en ligne tabulaire

# Définition d'une classe d'administration pour les produits
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]  # Afficher les images des produits en ligne dans l'interface d'administration
    list_editable = ['title', 'price', 'featured', 'product_status']  # Champs éditables directement dans la liste
    list_display = ['user', 'title', 'product_image', 'price', 'category', 'vendor', 'featured', 'product_status', 'pid']  # Champs à afficher dans la liste

# Définition d'une classe d'administration pour les catégories
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category_image']  # Champs à afficher dans la liste

# Définition d'une classe d'administration pour les vendeurs
class VendorAdmin(admin.ModelAdmin):
    list_display = ['title', 'vendor_image']  # Champs à afficher dans la liste

# Définition d'une classe d'administration pour les commandes de panier
class CartOrderAdmin(admin.ModelAdmin):
    list_editable = ['paid_status', 'product_status', 'sku']  # Champs éditables directement dans la liste
    list_display = ['user', 'price', 'paid_status', 'order_date', 'product_status', 'sku']  # Champs à afficher dans la liste

# Définition d'une classe d'administration pour les produits des commandes de panier
class CartOrderProductsAdmin(admin.ModelAdmin):
    list_display = ['order', 'invoice_no', 'item', 'image', 'qty', 'price', 'total']  # Champs à afficher dans la liste

# Définition d'une classe d'administration pour les avis sur les produits
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'review', 'rating']  # Champs à afficher dans la liste

# Définition d'une classe d'administration pour la liste de souhaits
class wishlistAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'date']  # Champs à afficher dans la liste

# Définition d'une classe d'administration pour les adresses
class AddressAdmin(admin.ModelAdmin):
    list_editable = ['address', 'status']  # Champs éditables directement dans la liste
    list_display = ['user', 'address', 'status']  # Champs à afficher dans la liste

# Enregistrement des modèles et des classes d'administration associées
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(CartOrder, CartOrderAdmin)
admin.site.register(CartOrderProducts, CartOrderProductsAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(wishlist_model, wishlistAdmin)
admin.site.register(Address, AddressAdmin)
