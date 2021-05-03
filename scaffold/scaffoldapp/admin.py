from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.CardProject)
class CardProjectAdmin(admin.ModelAdmin):
    list_display = ('titre_detail', 'detail', 'Categorie_client', 'project_date', 'project_url','date_add', 'date_update', 'status')
    search_fields = ['titre_detail']

@admin.register(models.ImageCard)
class ImageCardAdmin(admin.ModelAdmin):
    list_display = ('image', 'card',  'date_add', 'date_update', 'status')
    search_fields = ['image']
@admin.register(models.Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('image', 'nom', 'poste', 'twitter', 'facebook', 'instagram', 'linkedin', 'date_add', 'date_update', 'status')
    search_fields = ['nom']

@admin.register(models.Pack)
class PackAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix', 'periode', 'etiquettes', 'couleur','date_add','date_update', 'status')
    search_fields = ['nom']