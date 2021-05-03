from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('icone', 'titre', 'description', 'color', 'categorie', 'date_add','date_update', 'status')
    search_fields = ['titre']

@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('projet', 'image', 'titre', 'details', 'titre_details', 'date_add','date_update', 'status')
    search_fields = ['titre']

@admin.register(models.Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom', 'date_add', 'date_update', 'status')
    search_fields = ['nom']

@admin.register(models.Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('description', 'image', 'nom', 'travail', 'date_add', 'date_update', 'status' )
    search_fields = ['nom']

@admin.register(models.Partenaire)
class PartenaireAdmin(admin.ModelAdmin):
    list_display = ('logo', 'nom', 'date_add', 'date_update', 'status')
    search_fields = ['nom']