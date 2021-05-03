from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Prestation)
class PrestationAdmin(admin.ModelAdmin):
    list_display = ('titre', 'description', 'image', 'date_add', 'date_update', 'status')
    search_fields = ['titre']

@admin.register(models.Avantage)
class AvantageAdmin(admin.ModelAdmin):
    list_display = ('libele', 'libele_barre', 'pack_avantage', 'date_add','date_update', 'status')
    search_fields = ['libele']

@admin.register(models.Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('question', 'reponse', 'date_add', 'date_update', 'status')
    search_fields = ['question']