# API Padaria

API REST desenvolvida com Django REST Framework para gerenciamento de uma padaria.

## 📋 Sobre o Projeto

Este projeto é uma API REST construída com Django e Django REST Framework, utilizando SQLite como banco de dados. A API foi projetada para fornecer endpoints para gerenciamento de uma padaria.

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Django 6.0** - Framework web Python
- **Django REST Framework 3.16.1** - Framework para construção de APIs REST
- **SQLite** - Banco de dados relacional

## 📁 Estrutura do Projeto

```
Padaria/
├── api_padaria/              # Projeto Django principal
│   ├── __init__.py
│   ├── asgi.py              # Configuração ASGI para servidores assíncronos
│   ├── settings.py          # Configurações do projeto Django
│   ├── urls.py              # URLs principais do projeto
│   └── wsgi.py              # Configuração WSGI para servidores web
├── manage.py                # Script de administração do Django
├── requirements.txt         # Dependências do projeto
├── .gitignore              # Arquivos ignorados pelo Git
├── README.md               # Este arquivo
└── venv/                   # Ambiente virtual Python (não versionado)
```

## ⚙️ Pré-requisitos

Antes de começar, você precisa ter instalado em sua máquina:

- **Python 3.8 ou superior**
- **pip** (gerenciador de pacotes Python)
- **git** (para controle de versão)

## 🚀 Como Rodar o Projeto

### 1. Clone o repositório (se aplicável)

```bash
git clone <url-do-repositorio>
cd Padaria
```

### 2. Crie e ative o ambiente virtual

**No macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**No Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute as migrações do banco de dados

```bash
python manage.py migrate
```

Este comando criará o banco de dados SQLite (`db.sqlite3`) e todas as tabelas necessárias.

### 5. (Opcional) Crie um superusuário para acessar o admin

```bash
python manage.py createsuperuser
```

Siga as instruções no terminal para criar um usuário administrador.

### 6. Inicie o servidor de desenvolvimento

```bash
python manage.py runserver
```

O servidor estará rodando em `http://127.0.0.1:8000/`

### 7. Acesse a API

- **API Admin Django:** http://127.0.0.1:8000/admin/
- **API Root:** http://127.0.0.1:8000/

## 📝 Comandos Úteis

### Criar uma nova app Django

```bash
python manage.py startapp nome_da_app
```

### Criar migrações após alterar modelos

```bash
python manage.py makemigrations
python manage.py migrate
```

### Acessar o shell do Django

```bash
python manage.py shell
```

### Coletar arquivos estáticos

```bash
python manage.py collectstatic
```

### Executar testes

```bash
python manage.py test
```

## 🔧 Configurações

### Banco de Dados

O projeto está configurado para usar SQLite, que é criado automaticamente na primeira execução das migrações. O arquivo do banco (`db.sqlite3`) será criado na raiz do projeto.

### Configurações do Django REST Framework

O projeto já vem com algumas configurações básicas do DRF:

- **Permissões:** `AllowAny` (todos podem acessar)
- **Paginação:** `PageNumberPagination` com 10 itens por página

Você pode modificar essas configurações no arquivo `api_padaria/settings.py`.

## 📦 Dependências

O projeto utiliza as seguintes dependências principais:

- `Django==6.0` - Framework web
- `djangorestframework==3.16.1` - Framework para APIs REST
- `asgiref==3.11.0` - Suporte ASGI
- `sqlparse==0.5.4` - Parser SQL

## 🔐 Segurança

**⚠️ IMPORTANTE:** Este projeto está configurado para desenvolvimento. Para produção, você deve:

1. Alterar o `SECRET_KEY` no arquivo `settings.py`
2. Definir `DEBUG = False`
3. Configurar `ALLOWED_HOSTS` adequadamente
4. Usar um banco de dados de produção (PostgreSQL, MySQL, etc.)
5. Configurar HTTPS
6. Implementar autenticação e autorização adequadas

## 📚 Recursos Adicionais

- [Documentação do Django](https://docs.djangoproject.com/)
- [Documentação do Django REST Framework](https://www.django-rest-framework.org/)
- [Tutorial Django REST Framework](https://www.django-rest-framework.org/tutorial/quickstart/)

## 👨‍💻 Desenvolvimento

Para contribuir com o projeto:

1. Crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
2. Faça commit das suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
3. Faça push para a branch (`git push origin feature/MinhaFeature`)
4. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença [especificar licença].

## 👤 Autor

Prof. Jose George

1.
2.
3.
4.
5.

---

Desenvolvido com ❤️ usando Django REST Framework

