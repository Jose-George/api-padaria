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

class Product(models.Model):
    name = models.CharField(max_length=200)
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        related_name='products'
    )
    qtd_atual = models.IntegerField(default=0)
    qtd_minima = models.IntegerField(default=0)
    validade = models.DateField()
    lote = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
