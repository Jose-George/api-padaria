from datetime import timedelta
from django.utils import timezone
from rest_framework import serializers
from .models import Product
from typing import Dict, Any

class ProductSerializer(serializers.ModelSerializer):
    supplier = serializers.SerializerMethodField()
    supplier_id = serializers.PrimaryKeyRelatedField(
        queryset=Product._meta.get_field('supplier')
        .remote_field.model.objects.all(),
        source='supplier',
        write_only=True
    )

    class Meta:
        model = Product
        fields = '__all__'

    def get_supplier(self, obj) -> Dict[str, Any]:
        return {
            "id": obj.supplier.id,
            "nome": obj.supplier.nome
    }

    # ✅ valida campo individual
    def validate_qtd_atual(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "A quantidade atual deve ser maior ou igual a zero."
            )
        return value

    # ✅ valida campo individual
    def validate_qtd_minima(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "A quantidade mínima deve ser maior ou igual a zero."
            )
        return value

    # ✅ valida data futura
    def validate_validade(self, value):
        hoje = timezone.now().date()
        if value <= hoje:
            raise serializers.ValidationError(
                "A data de validade deve ser uma data futura."
            )
        return value

    # ✅ regras de negócio + alertas
    def validate(self, attrs):
        qtd_atual = attrs.get('qtd_atual')
        qtd_minima = attrs.get('qtd_minima')
        validade = attrs.get('validade')

        if qtd_atual is not None and qtd_minima is not None:
            if qtd_atual < qtd_minima:
                attrs['alerta_quantidade'] = (
                    "Aviso: a quantidade atual está abaixo da quantidade mínima."
                )

        if validade:
            hoje = timezone.now().date()
            if (validade - hoje).days <= 7:
                attrs['alerta_vencimento'] = (
                    "Atenção: produto próximo do vencimento."
                )

        return attrs