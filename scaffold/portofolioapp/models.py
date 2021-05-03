from django.db import models

# Create your models here.

class Card(models.Model):
    icone = models.FileField(upload_to= "card")
    titre = models.CharField(max_length= 200)
    description = models.CharField(max_length= 200)
    color = models.CharField(max_length= 200)
    categorie = models.ForeignKey("portofolioapp.Categorie", related_name='categorie_cards', null=True, on_delete=models.CASCADE)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'

    def __str__(self):
        return self.titre

class Categorie(models.Model):
    nom = models.CharField(max_length= 200, null= False, blank= True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Categorie'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.nom
    
class Image(models.Model):
    projet = models.ForeignKey(Card, null= True, on_delete= models.SET_NULL, blank= False)
    image = models.ImageField()
    titre = models.CharField(max_length= 200)
    details = models.TextField()
    titre_details = models.CharField(max_length=200)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    def __str__(self):
        return self.titre


class Testimonial(models.Model):
    description = models.TextField()
    image = models.ImageField()
    nom = models.CharField(max_length= 200)
    travail = models.CharField(max_length= 200)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'

    def __str__(self):
        return self.titre


class Partenaire(models.Model):
    logo = models.ImageField()
    nom = models.CharField
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Partenaire'
        verbose_name_plural = 'Partenaires'

    def __str__(self):
        return self.nom