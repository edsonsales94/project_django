import email
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib import auth

from Webapp.models import Postagem

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        print(nome , email, senha, senha2)
        if not nome.strip():
            print('o Nome nao pode ficar em branco')
            return redirect('cadastro')
        if not email.strip():
            print('o email nao pode ficar em branco')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            print('Usuario já cadastrado')
            return redirect('cadastro')
        user = User.objects.create_user(username=nome,email=email,password=senha)
        user.save()
        print('Usuario cadastrado com sucesso')
        return redirect('login')
    else:
        return render(request,'usuario/cadastro.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if email == "" or senha == "":
            print('email ou senha precisam ser preenchidos')
            return redirect('login')
        if User.objects.filter(email=email).exists():   #---->>> Se o email existe na base 
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()    #---->>> filtro os valores do usuario , trago o username.
            user = auth.authenticate(request, username=nome, password=senha)    #---->>> faz a autenticação comparando o user name e a senha inseridos com os da base
            if user is not None:
                auth.login(request, user)
                print('Login realizado com sucesso')
                return redirect('dashboard')
                
    return render(request, 'usuario/login.html')
 
def logout(request):
    auth.logout(request)
    return redirect('index')

def dashboard(request):
    if request.user.is_authenticated:
        id = request.user.id
        postagem = Postagem.objects.order_by('-data').filter(autor=id)
        poster = {
            'postagem': postagem
        }
        return render(request, 'usuario/dashboard.html', poster)
    else:
        return redirect('index')

def criar_poster(request):
    if request.method == 'POST':
        titulo = request.POST['nome_publicacao']
        resumo = request.POST['resumo']
        publicacao = request.POST['publicacao']
        citacao = request.POST['citacao']
        foto_publicar = request.FILES['foto_publiacar']
        twiter_pub = request.POST['twiter_pub']
        facebook_pub = request.POST['facebook_pub']


        user = get_object_or_404(User, pk=request.user.id)
        postagem = Postagem.objects.create(
            autor = user,
            titulo = titulo,
            resumo = resumo,
            paragrafo = publicacao,
            citacao = citacao,
            foto_postagem = foto_publicar,
            twiter = twiter_pub,
            facebook = facebook_pub
            
        )
        postagem.save()
        return redirect('dashboard')
    else:
        return render(request, 'usuario/criar_poster.html' )

def dashboard(request):
    Postagem_post = Postagem.objects.all()
    post_a_exibir = {
    'poster_use': Postagem_post,
    }
    
    return render(request,'usuario/dashboard.html' , post_a_exibir)



