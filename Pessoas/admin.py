from re import A
from django.contrib import admin

from Pessoas.models import Pessoas_cad

class lista_pessoas(admin.ModelAdmin):
    list_display = ('id','nome')
    list_display_links = ('id','nome')
    

admin.site.register(Pessoas_cad,lista_pessoas)
