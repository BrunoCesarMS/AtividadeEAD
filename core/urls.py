# core/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # rota vazia redireciona para o cadastro
    path('cadastro/', views.cadastrar_funcionario, name='cadastrar_funcionario'),
    path('funcionarios/', views.listar_funcionarios, name='listar_funcionarios'),
]