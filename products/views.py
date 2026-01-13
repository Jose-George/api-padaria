from datetime import date, timedelta
from django.db.models import F
from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import Product
from .serializers import ProductSerializer


# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related('supplier').all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['validade', 'supplier', 'name']

    @action(detail=False, methods=['get'], url_path='relatorio-geral')
    def relatorio_geral(self, request):
         hoje = date.today()
         margem = timedelta(days=7) # Considera 7 dias para próximo vencimento

         # 1. Produtos Vencidos
         vencidos = Product.objects.filter(validade__lt=hoje)

         # 2. Produtos Próximos do Vencimento (entre hoje e daqui a 7 dias)
         proximos = Product.objects.filter(validade__gte=hoje, validade__lte=hoje + margem)

         # 3. Produtos com Estoque Baixo (qtd_atual <= qtd_minima)
         estoque_baixo = Product.objects.filter(qtd_atual__lte=F('qtd_minima'))

         # 4. Produtos Ativos (Exemplo: validade em dia)
         ativos = Product.objects.filter(validade__gte=hoje)

         data = {
             'total_ativos': ativos.count(),
             'total_vencidos': vencidos.count(),
             'total_proximos': proximos.count(),
             'total_estoque_baixo': estoque_baixo.count(),
             'lista_estoque_baixo': [p.name for p in estoque_baixo],
             'lista_vencidos': [p.name for p in vencidos]
         }
         
         return Response(data, status=status.HTTP_200_OK)
