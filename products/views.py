from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related('supplier').all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['validade', 'supplier', 'name']
