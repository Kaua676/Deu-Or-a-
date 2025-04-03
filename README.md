# 📝 Deu-Orça  

📌 **SOA em Django com PostgreSQL para Gestão de Orçamentos**  

Este repositório contém um sistema baseado em **Arquitetura Orientada a Serviços (SOA)**, desenvolvido com **Django** e **PostgreSQL**, para gerenciar usuários, orçamentos e cálculos financeiros.  

---

## 🚀 Tecnologias Utilizadas  

- 🐍 **Django** – Backend robusto e escalável  
- 🛢️ **PostgreSQL** – Banco de dados relacional poderoso  
- ⚡ **Django REST Framework** – Para criação da API  
- 📝 **WeasyPrint** – Para geração de PDFs  
- 🐳 **Docker** (Opcional) – Para facilitar o ambiente de desenvolvimento  

---

## 📌 Funcionalidades  

### 🔹 Serviço de Usuários  
- ✅ Cadastro e autenticação de usuários  
- ✅ Diferenciação entre administradores e clientes  
- ✅ Recuperação e atualização de dados  

### 🔹 Serviço de Orçamentos  
- ✅ Criação e edição de orçamentos  
- ✅ Associação de clientes a orçamentos  
- ✅ Exclusão e listagem de orçamentos  

### 🔹 Serviço de Cálculo  
- ✅ Cálculo automático de valores  
- ✅ Aplicação de descontos e impostos  

### 🔹 Serviço de Geração de PDF  
- ✅ Exportação de orçamentos para PDF  
- ✅ Personalização de layout  

---

## 📂 Estrutura do Projeto  

```bash
Deu-Orca/
├── usuarios/       # Serviço de usuários (cadastro, login, etc.)
├── orcamentos/     # Serviço de orçamentos e itens do orçamento
├── calculos/       # Serviço de cálculo de valores e impostos
├── pdfs/           # Serviço de geração de PDFs
├── settings.py     # Configurações do Django
├── urls.py         # Rotas principais do sistema
```

## ⚙️ Configuração do Ambiente

### 🔹 1. Clonar o Repositório
git clone https://github.com/seu-usuario/Deu-Orca.git
cd Deu-Orca

### 🔹 2. Configurar o Banco de Dados (PostgreSQL)
No settings.py, configure:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'deu_orca_db',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

### 🔹 3. Rodar as Migrações
python manage.py makemigrations
python manage.py migrate

### 🔹 4. Rodar o Servidor
python manage.py runserver

## 🔗 Endpoints Principais
Método	Endpoint	Descrição
POST	/api/usuarios/cadastrar	Cadastrar usuário
POST	/api/usuarios/login	Autenticar usuário
POST	/api/orcamentos/criar	Criar orçamento
GET	/api/orcamentos/{id}	Buscar orçamento por ID
POST	/api/calculo/orcamento	Calcular total do orçamento
POST	/api/pdf/gerar	Gerar orçamento em PDF

