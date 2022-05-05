from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>', views.post, name='post'),
    path('author', views.author, name='author'),
    path('buscar', views.buscar, name='buscar'),
    path('login', views.buscar, name='login'),
    path('cadastro', views.buscar, name='cadastro'),

]