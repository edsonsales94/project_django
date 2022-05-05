from pyexpat import model
from re import search
from django.contrib import admin
from Webapp.models import Postagem

class listarPublicacao(admin.ModelAdmin):
    list_display = ('id','titulo','resumo','data')
    list_display_links = ('id','titulo','resumo','data')
    search_fields = ('id','titulo','resumo')
    page_per_page = 1

admin.site.register(Postagem,listarPublicacao)