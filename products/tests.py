from datetime import date, timedelta

from django.test import TestCase
from rest_framework.test import APIClient

from suppliers.models import Supplier
from products.models import Product
from products.serializers import ProductSerializer


class ProductSerializerTest(TestCase):

    def setUp(self):
        self.supplier = Supplier.objects.create(
            nome="Fornecedor Teste",
            email="fornecedor@test.com",
            telefone="11999999999",
            cnpj="12345678000199"
        )

    def test_produto_valido(self):
        data = {
            "name": "Produto Teste",
            "supplier_id": self.supplier.id,  # ✅ CORRETO
            "qtd_atual": 10,
            "qtd_minima": 5,
            "validade": date.today() + timedelta(days=30),
            "lote": "L123"
        }

        serializer = ProductSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)

    def test_quantidade_negativa_deve_falhar(self):
        data = {
            "name": "Produto Inválido",
            "supplier_id": self.supplier.id,
            "qtd_atual": -1,
            "qtd_minima": 5,
            "validade": date.today() + timedelta(days=30),
            "lote": "L124"
        }

        serializer = ProductSerializer(data=data)
        self.assertFalse(serializer.is_valid())

        # erro vem do validate(), então é non_field_errors
        self.assertIn("qtd_atual", serializer.errors)

    def test_validade_passada_deve_falhar(self):
        data = {
            "name": "Produto Vencido",
            "supplier_id": self.supplier.id,  # ✅ CORRETO
            "qtd_atual": 10,
            "qtd_minima": 5,
            "validade": date.today() - timedelta(days=1),
            "lote": "L125"
        }

        serializer = ProductSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("validade", serializer.errors)


class ProductViewSetTest(TestCase):

    def setUp(self):
        self.client = APIClient()

        self.supplier = Supplier.objects.create(
            nome="Fornecedor API",
            email="api@fornecedor.com",
            telefone="11888888888",
            cnpj="98765432000188"
        )

        self.product = Product.objects.create(
            name="Produto API",
            supplier=self.supplier,
            qtd_atual=10,
            qtd_minima=5,
            validade=date.today() + timedelta(days=15),
            lote="L200"
        )

    def test_listar_produtos(self):
        response = self.client.get("/api/products/")
        self.assertEqual(response.status_code, 200)

    def test_criar_produto(self):
        data = {
            "name": "Novo Produto",
            "supplier_id": self.supplier.id,
            "qtd_atual": 20,
            "qtd_minima": 5,
            "validade": date.today() + timedelta(days=60),
            "lote": "L201"
        }

        response = self.client.post("/api/products/", data, format="json")
        self.assertEqual(response.status_code, 201)

    def test_relatorio_geral(self):
        response = self.client.get("/api/products/relatorio-geral/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("total_ativos", response.data)