from django.db import models

class tentreprsie(models.Model):
    nomE = models.CharField(max_length=50, unique=True, null=False, verbose_name="Nom entreprise")
    emailE = models.EmailField(null=False, unique=True, verbose_name="Email")
    descriptionE = models.TextField(blank=True, verbose_name="Description de l'entreprise")

    def __str__(self):
        return self.nomE

class tcathegorie(models.Model):
    nomCat = models.CharField(max_length=50, unique=True, null=False, verbose_name="Cathegorie")

    def __str__(self):
        return self.nomCat

class tproduit(models.Model):
    nomp = models.CharField(max_length=50, unique=True, null=False, verbose_name="Nom produit")
    stock = models.IntegerField(default=1)
    prix = models.IntegerField(default=1)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='produit/', blank=True, null=True)
    idEntrep = models.ForeignKey(tentreprsie,on_delete=models.DO_NOTHING, null=True)
    idCat = models.ForeignKey(tcathegorie, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.nomp