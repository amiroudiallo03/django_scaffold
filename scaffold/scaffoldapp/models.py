from django.db import models
from faicon.fields import FAIconField
from colorfield.fields import ColorField



# Create your models here.
class Banner(models.Model):
    titre = models.CharField(max_length= 200)
    image = models.ImageField(upload_to = 'Banner')
    description = models.CharField(max_length= 500)
    
    # Champs obligatoires (Convention de NaN)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'ExModel'
        verbose_name_plural = 'ExModels'

    def __str__(self):
        return self.titre

class About(models.Model):
    image = models.ImageField(upload_to = 'Abouts')
    titre = models.CharField(max_length= 200)
    sous_titre = models.TextField(max_length= 500)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'ExModel'
        verbose_name_plural = 'ExModels'

    def __str__(self):
        return self.titre

class Prestation(models.Model):
    titre = models.CharField(max_length= 200)
    description = models.TextField(max_length= 500)
    image = models.ImageField(upload_to = 'Banner')
    

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'ExModel'
        verbose_name_plural = 'ExModels'

    def __str__(self):
        return self.titre
    

class Card(models.Model):
    icone = models.FileField(upload_to= "card")
    titre = models.CharField(max_length= 200)
    description = models.CharField(max_length= 200)
    color = models.CharField(max_length= 200)
    categorie = models.ForeignKey("scaffoldapp.Categorie", related_name='categorie_cards', null=True, on_delete=models.CASCADE)


    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'ExModel'
        verbose_name_plural = 'ExModels'

    def __str__(self):
        return self.titre

class Categorie(models.Model):
    nom = models.CharField(max_length= 200, null= False, blank= True)

    # Champs obligatoires (Convention de NaN)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'ExModel'
        verbose_name_plural = 'ExModels'

    def __str__(self):
        return self.nom
    
class Image(models.Model):
    projet = models.ForeignKey(Card, null= True, on_delete= models.SET_NULL, blank= False, related_name='card_images')
    image = models.ImageField()
    titre = models.CharField(max_length= 200)
    details = models.TextField()
    titre_details = models.CharField(max_length=200)

    # Champs obligatoires (Convention de NaN)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'ExModel'
        verbose_name_plural = 'ExModels'

    def __str__(self):
        return self.titre


class Testimonial(models.Model):
    description = models.TextField()
    image = models.ImageField()
    nom = models.CharField(max_length= 200)
    travail = models.CharField(max_length= 200)

    # Champs obligatoires (Convention de NaN)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'ExModel'
        verbose_name_plural = 'ExModels'

    def __str__(self):
        return self.titre

class Team(models.Model):
    image = models.ImageField()
    nom = models.CharField(max_length= 200)
    poste = models.TextField()
    twitter = models.URLField()
    facebook = models.URLField()
    instagram = models.URLField()
    linkedin = models.URLField()

    # Champs obligatoires (Convention de NaN)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'ExModel'
        verbose_name_plural = 'ExModels'

    def __str__(self):
        return self.titre

class Partenaire(models.Model):
    logo = models.ImageField()
    nom = models.CharField

    # Champs obligatoires (Convention de NaN)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'ExModel'
        verbose_name_plural = 'ExModels'

    def __str__(self):
        return self.titre


class Pack(models.Model):
    nom = models.CharField(max_length= 200, null= False, blank= False)
    prix = models.FloatField()
    periode = models.DateField()
    etiquettes = models.BooleanField(default= False)
    couleur = models.TextField(default= '#009cea')


    # Champs obligatoires (Convention de NaN)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'ExModel'
        verbose_name_plural = 'ExModels'

    
    def __str__(self):
        return self.nom

class Avantage(models.Model):
    libele = models.CharField(max_length= 200)
    libele_barre = models.BooleanField(default= False)
    pack = models.ForeignKey(Pack, on_delete = models.SET_NULL, null= True)


    # Champs obligatoires (Convention de NaN)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'ExModel'
        verbose_name_plural = 'ExModels'

    
    def __str__(self):
        return self.libele

class Faq(models.Model):
    question = models.TextField(max_length= 1000)
    reponse = models.TextField(max_length=1000)


    # Champs obligatoires (Convention de NaN)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'ExModel'
        verbose_name_plural = 'ExModels'

    
    def __str__(self):
        return self.question


class Contact(models.Model):
    nom = models.CharField(max_length=200)
    email = models.EmailField()
    sujet = models.TextField(max_length= 1000)
    message = models.TextField(max_length=1000)


    # Champs obligatoires (Convention de NaN)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'ExModel'
        verbose_name_plural = 'ExModels'

    
    def __str__(self):
        return self.nom

    
class Newsletter(models.Model):
    email = models.EmailField()


    # Champs obligatoires (Convention de NaN)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'ExModel'
        verbose_name_plural = 'ExModels'

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


    # Champs obligatoires (Convention de NaN)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'ExModel'
        verbose_name_plural = 'ExModels'

    def __str__(self):
        return self.titre
    
    
    