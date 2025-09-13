from django.contrib import messages
from django.shortcuts import render , redirect
from .forms import FuncionarioForm
from .models import Funcionario

# Create your views here.

def home(request) :
    return render(request, "tela_base.html")

#def home(request):
#    return redirect('home')

def cadastrar_funcionario(request):
    if request.method == "POST":
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cadastro realizado com sucesso")
            # return redirect('listar_funcionarios')
        else:
           messages.error(request, "Funcionário não cadastrado") 
    else:
        form = FuncionarioForm()
    return render(request, 'my_db.html', {'form': form})

def listar_funcionarios(request):
    funcionarios = Funcionario.objects.all()
    return render(request, 'listar_funcionarios.html', {'funcionarios': funcionarios})

