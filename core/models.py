from django.db import models

# Create your models here.

class Funcionario(models.Model):
    nome_completo = models.CharField(max_length=200)
    matricula = models.CharField(max_length=20, unique=True)
    setor = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    observacoes = models.TextField(blank=True, null=False, default='')

    def __str__(self):
        return self.nome_completo
