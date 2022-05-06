from ast import mod
from datetime import datetime
from email.mime import image
from pickle import TRUE
from tkinter import CASCADE
from turtle import update
from django.db import models
from django.forms import CharField
from django.contrib.auth.models import User

class Postagem(models.Model):
    autor = models.ForeignKey(User,on_delete=models.CASCADE)
    titulo = models.CharField(max_length=120)
    resumo = models.CharField(max_length=300)
    data = models.DateTimeField(default=datetime.now, blank=True)
    citacao = models.CharField( max_length=1000, default='SOME STRING')
    paragrafo = models.TextField(default='SOME STRING')
    publicar = models.BooleanField(default=False)
    foto_postagem = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=TRUE)
    local_postagem = CharField(max_length=120)
    twiter = models.CharField(max_length=120)
    facebook = models.CharField(max_length=120)
