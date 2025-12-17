from django.db import models

class Supplier(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    cnpj = models.CharField(max_length=18, unique=True)

    def __str__(self):
        return self.nome



    class Meta:
        verbose_name = "Fornecedor"
        verbose_name_plural = "Fornecedores"
