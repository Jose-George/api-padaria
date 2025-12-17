from django.db import models
from suppliers.models import Supplier

class Product(models.Model):
    name = models.CharField(max_length=200)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='products')
    qtd_atual = models.IntegerField(default=0)
    qtd_minima = models.IntegerField(default=0)
    validade = models.DateField()
    lote = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
