from distutils.command.upload import upload
from django.db import models
from django.forms import CharField

class Pessoas_cad(models.Model):   
    nome = models.CharField(max_length=100)
    foto_pessoa = models.ImageField(upload_to ='fotos/%d/%m/%Y/', blank=True)

