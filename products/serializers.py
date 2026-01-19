from rest_framework import serializers
from .models import Product
from suppliers.models import Supplier

class ProductSerializer(serializers.ModelSerializer):
    supplier_id = serializers.PrimaryKeyRelatedField(
        queryset=Supplier.objects.all(),
        source='supplier',
        write_only=True
    )

    class Meta:
        model = Product
        fields = '__all__'
        depth = 1