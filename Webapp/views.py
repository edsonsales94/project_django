from datetime import date
import re
from django.shortcuts import get_object_or_404, render
from Webapp.models import Postagem

# Função que retorna do DB as postagem e ditribui entre destaques e outros

def index(request):
    
    post_destaque = Postagem.objects.order_by('id').filter(publicar=True).reverse()[:4]
    post_outros =  Postagem.objects.order_by('id').filter(publicar=True).reverse()[4:10]
   
    conteudo = {
        'destaque': post_destaque,
        'outros': post_outros,
    }

    return render(request,'index.html',conteudo)

#Função que Redireciona para pagina da postagem para leitura

def post(request, post_id):

    abri_post = get_object_or_404(Postagem, pk=post_id)
    post_a_exibir = {
    'link_post':abri_post
    }
    
    return render(request,'post.html' , post_a_exibir)

#Função que retorna a postagem de acordo com filtro 

def buscar(request):
    
    post_buscar = Postagem.objects.order_by('id').filter(publicar=True)
    if 'buscar' in request.GET: # se existe o valor digitado no campo buscar na requisição
        a_buscar = request.GET['buscar'] 
        if a_buscar: 
            #Filtra o que esta sendo buscado em alguns dos campos declarado no models
            post_buscar = post_buscar.filter(titulo__icontains=a_buscar) |  post_buscar.filter(resumo__icontains=a_buscar) | post_buscar.filter(paragrafo__icontains=a_buscar)
    
    conteudo = {
        'destaque': post_buscar, 
    }

    return render(request,'buscar.html',conteudo)  
    #todo conteudo e renderizado no template

def author(request):
    return render(request,'author.html')


  # titulo_featured = {
    #     1:'O jogo nao é fácil, mas eai ? vamos vencer ?',
    #     2:'vamos vencer ?',
    #     3:' mas eai ? vamos vencer ?',
    #     4:'O jogo nao é fácil de vencer ?',
    #     # 5:'O tempo nao para',
    #     # 6:'Encare a vida',
    #     # 7:' nem tudo que reluz é ouro',
    #     # 8:'O jogo nao é fácil de vencer ?',
    #     # 9:'cada coisa que acontece',
    #     # 10:'nao desista dos teus sonhos',
    # }
    

    # titulo_post = {
    #     5:'O tempo nao para',
    #     6:'Encare a vida',
    #     7:' nem tudo que reluz é ouro',
    #     8:'O jogo nao é fácil de vencer ?',
    #     9:'cada coisa que acontece',
    #     10:'nao desista dos teus sonhos',
    # }

    # titulo_list = {
    #     'titulo_fet' : titulo_featured,
    #     'titulo_post': titulo_post
    #     }