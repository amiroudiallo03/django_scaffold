from django.db import models

# Create your models here.
class Banner(models.Model):
    titre = models.CharField(max_length= 200)
    image = models.ImageField(upload_to = 'Banner')
    description = models.CharField(max_length= 500)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'

    def __str__(self):
        return self.titre


class Website(models.Model):
    nom_site = models.CharField(max_length= 200)
    description_service = models.CharField(max_length=200)
    description_partenaire = models.CharField(max_length=200)
    description_Portofolio = models.CharField(max_length= 200)
    description_temoignage = models.CharField(max_length= 200)
    description_team = models.CharField(max_length=200)
    description_partenaire = models.CharField(max_length= 200)
    email = models.EmailField()
    call = models.CharField(max_length=200)
    location = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Website'
        verbose_name_plural = 'Websites'

    def __str__(self):
        return self.titre


class Newsletter(models.Model):
    email = models.EmailField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Newsletter'
        verbose_name_plural = 'Newsletters'

    def __str__(self):
        return self.titre


class Contact(models.Model):
    nom = models.CharField(max_length=200)
    email = models.EmailField()
    sujet = models.TextField()
    message = models.TextField()


    # Champs obligatoires (Convention de NaN)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    
    def __str__(self):
        return self.nom

class SocialAccount(models.Model):
    nom = models.CharField(max_length= 200)
    icone = models.ImageField()
    lien = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'SocialAccount'
        verbose_name_plural = 'SocialAccounts'
    
    def __str__(self):
        return self.nom


class About(models.Model):
    image = models.ImageField()
    titre = models.CharField(max_length= 200)
    sous_titre = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'

    def __str__(self):
        return self.titre