from django.db import models

# Create your models here.


class Prestation(models.Model):
    titre = models.CharField(max_length= 200)
    description = models.TextField()
    image = models.ImageField(upload_to = 'Banner')
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)


class Faq(models.Model):
    question = models.TextField()
    reponse = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Faq'
        verbose_name_plural = 'Faqs'

    
    def __str__(self):
        return self.question


class Avantage(models.Model):
    libele = models.CharField(max_length= 200)
    libele_barre = models.BooleanField(default= False)
    pack_avantage = models.ForeignKey("scaffoldapp.Pack",related_name= "avantage_pack", on_delete = models.SET_NULL, null= True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Avantage'
        verbose_name_plural = 'Avantages'

    
    def __str__(self):
        return self.libele
