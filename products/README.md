# Products – Atividade 02

Este módulo implementa a **Atividade 02: Gestão de Fornecedores**, criando a API REST responsável por cadastrar, listar, atualizar e remover fornecedores no sistema.

## ✔ O que foi implementado
- Criação do app `products`
- Modelo **Supplier** com os campos:
  - nome  
  - email  
  - telefone  
  - cnpj (único)
- Serializer para o modelo
- ViewSet com CRUD completo usando Django REST Framework
- Registro das rotas via `DefaultRouter`
- Migração inicial do banco de dados

## 📌 Endpoints
Base: `/api/suppliers/`

| Método | Rota                    | Ação |
|--------|--------------------------|------|
| GET    | `/api/suppliers/`        | Listar fornecedores |
| POST   | `/api/suppliers/`        | Criar fornecedor |
| GET    | `/api/suppliers/<id>/`   | Detalhar fornecedor |
| PUT    | `/api/suppliers/<id>/`   | Atualizar fornecedor |
| DELETE | `/api/suppliers/<id>/`   | Remover fornecedor |
