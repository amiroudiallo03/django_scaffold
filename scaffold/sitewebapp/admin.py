from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('titre', 'image', 'description','date_add', 'date_update', 'status', 'date_add', 'date_update', 'status')
    search_fields = ['titre']


@admin.register(models.Website)
class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('nom_site', 'description_service', 'description_partenaire', 'description_Portofolio', 'description_temoignage', 'description_team', 'description_partenaire', 'email', 'call', 'location', 'date_add', 'date_update', 'status')
    search_fields = ['nom_site']

@admin.register(models.Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_add', 'date_update', 'status')
    search_fields = ['email']

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'sujet', 'message', 'date_add', 'date_update', 'status')


@admin.register(models.SocialAccount)
class SocialAccountAdmin(admin.ModelAdmin):
    list_display = ('nom','icone', 'lien',  'date_add', 'date_update', 'status')
    search_fields = ['nom']


@admin.register(models.About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('image', 'titre', 'sous_titre','date_add','date_update', 'status')
    search_fields =['titre']