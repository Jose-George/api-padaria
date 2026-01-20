import re
from rest_framework import serializers
from .models import Supplier


class SupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = ['id', 'nome', 'email', 'telefone', 'cnpj']

    def validate_cnpj(self, value):

        cnpj = re.sub(r'\D', '', value)

        if len(cnpj) != 14:
            raise serializers.ValidationError(
                "CNPJ deve conter 14 dígitos."
            )

        if cnpj == cnpj[0] * 14:
            raise serializers.ValidationError(
                "CNPJ inválido."
            )

        # Validação do primeiro dígito
        pesos_1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        soma = sum(int(cnpj[i]) * pesos_1[i] for i in range(12))
        resto = soma % 11
        digito_1 = 0 if resto < 2 else 11 - resto

        if digito_1 != int(cnpj[12]):
            raise serializers.ValidationError(
                "CNPJ inválido."
            )

        # Validação do segundo dígito
        pesos_2 = [6] + pesos_1
        soma = sum(int(cnpj[i]) * pesos_2[i] for i in range(13))
        resto = soma % 11
        digito_2 = 0 if resto < 2 else 11 - resto

        if digito_2 != int(cnpj[13]):
            raise serializers.ValidationError(
                "CNPJ inválido."
            )

        return cnpj
