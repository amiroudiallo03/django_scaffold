from django.db import models
from faicon.fields import FAIconField
from colorfield.fields import ColorField



# Create your models here.
class Team(models.Model):
    image = models.ImageField()
    nom = models.CharField(max_length= 200)
    poste = models.TextField()
    twitter = models.URLField()
    facebook = models.URLField()
    instagram = models.URLField()
    linkedin = models.URLField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'

    def __str__(self):
        return self.titre




class Pack(models.Model):
    nom = models.CharField(max_length= 200, null= False, blank= False)
    prix = models.FloatField()
    periode = models.DateField()
    etiquettes = models.BooleanField(default= False)
    couleur = models.TextField(default= '#009cea')
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Pack'
        verbose_name_plural = 'Packs'

    
    def __str__(self):
        return self.nom







    






class CardProject(models.Model):
    titre_detail = models.CharField(max_length= 200)
    detail = models.TextField()
    Categorie_client = models.TextField(max_length= 200)
    project_date = models.DateField()
    project_url = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nom

    class Meta():
        verbose_name = 'CardProject'
        verbose_name_plural = ' CardProjects'
    
class ImageCard(models.Model):
    image = models.ImageField()
    card = models.ForeignKey("portofolioapp.Card", related_name= "image_card", null=True, on_delete=models.CASCADE)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'ImageCard'
        verbose_name_plural = 'ImageCards'

    def __str__(self):
        return self.nom

