from datetime import timedelta
from django.utils import timezone
from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    supplier_id = serializers.PrimaryKeyRelatedField(
        queryset=Product._meta.get_field('supplier').remote_field.model.objects.all(),
        source='supplier',
        write_only=True
    )

    class Meta:
        model = Product
        fields = '_all_'
        depth = 1

    def validate_minimum_quantity(
        self,
        qtd_atual: int,
        qtd_minima: int,
        alerta: bool = True
    ) -> bool:
       
        if qtd_atual < 0:
            raise serializers.ValidationError(
                "A quantidade atual deve ser maior ou igual a zero."
            )

        if qtd_minima < 0:
            raise serializers.ValidationError(
                "A quantidade mínima deve ser maior ou igual a zero."
            )

        if alerta and qtd_atual < qtd_minima:
            return True

        return False

    def validate_validity_date(self, value):
        hoje = timezone.now().date()

        if value <= hoje:
            raise serializers.ValidationError(
                "A data de validade deve ser uma data futura."
            )
        return value

    def validate(self, attrs):
        qtd_atual = attrs.get('quantity')
        qtd_minima = attrs.get('minimum_quantity')
        validade = attrs.get('validity_date')

        if qtd_atual is not None and qtd_minima is not None:
            estoque_baixo = self.validate_minimum_quantity(
                qtd_atual=qtd_atual,
                qtd_minima=qtd_minima
            )

            if estoque_baixo:
                attrs['alerta_quantidade'] = (
                    "Aviso: a quantidade atual está abaixo da quantidade mínima."
                )

        if validade:
            hoje = timezone.now().date()
            dias_para_vencer = (validade - hoje).days

            if dias_para_vencer <= 7:
                attrs['alerta_vencimento'] = (
                    "Atenção: produto próximo do vencimento."
                )

        return attrs