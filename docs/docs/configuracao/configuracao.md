# Guia de Configuração e Execução do Projeto

Este guia fornece instruções detalhadas para configurar e executar o projeto Lumina. Você pode optar por configurar o projeto em um ambiente local ou utilizar Docker para simplificar o processo. Recomendamos o uso do Docker para uma configuração mais rápida e consistente, garantindo que todos os serviços necessários estejam disponíveis.

---

## Pré-requisitos

Certifique-se de ter os seguintes pré-requisitos instalados:

### Ambiente Local

- **Python 3.13** ou superior
- **PostgreSQL**
- **pip**
- **venv** (opcional, para criar um ambiente virtual)
- **Git** (opcional, para gerenciar o repositório)

### Docker

- **Docker**
- **Docker Compose**

---

## Configuração e Execução

Nossa aplicação é composta por dois serviços: `web` (Django) e `db` (PostgreSQL). A configuração e execução do projeto pode ser feita de duas formas: localmente ou usando Docker. Siga as instruções abaixo de acordo com a sua preferência.

## 1. Docker

É necessário a instalação do Docker e Docker Compose para executar o projeto com Docker. Você pode instalar o Docker Desktop para Windows e Mac ou o Docker Engine para Linux. Para instalar o Docker Compose, siga as instruções disponíveis na [documentação oficial](https://docs.docker.com/compose/install/).

### Passo 1: Clonar o repositório

```bash
git clone https://github.com/unb-mds/2024-2-Squad05.git
cd 2024-2-Squad05
```

### Passo 2: Construir e iniciar os contêineres

Primeiramente, certifique-se que a instalação do Docker e Docker Compose foram bem sucedidas e que estão sendo executados. Em seguida, execute o comando abaixo para construir e iniciar os contêineres:

```bash
docker compose up --build
```

### Passo 3: Verificar logs e garantir que tudo está funcionando

Para verificar os logs dos contêineres e garantir que tudo está funcionando corretamente, execute o comando abaixo:

```bash
docker compose logs -f
```

> Atenção: A aplicação utiliza a API da OpenAI para realizar a análise de sentimentos. Para utilizar a API, é necessário configurar a variável `OPENAI_API_KEY` com a sua chave de acesso.

### Passo 4: Acessar a aplicação

Acesse em: [http://127.0.0.1:8000](http://127.0.0.1:8000).

> **Dica:** Para facilitar o processo de desenvolvimento, considere utilizar extensões do VS Code como o [**Python**](https://marketplace.visualstudio.com/items?itemName=ms-python.python) e o [**Docker**](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker). Essas extensões fornecem suporte avançado para desenvolvimento em Python e gerenciamento de contêineres Docker diretamente do editor. Além disso, o **Docker Desktop** oferece uma interface gráfica amigável para gerenciar seus contêineres e imagens Docker.

## 2. Desenvolvimento Local

### Passo 1: Clonar o repositório

```bash
git clone https://github.com/unb-mds/2024-2-Squad05.git
cd 2024-2-Squad05
```

### Passo 2: Configurar o ambiente virtual e instalar dependências

Após clonar o repositório, crie um ambiente virtual e instale as dependências. Isso garante que as dependências do projeto não entrem em conflito com outras aplicações Python instaladas no seu sistema. Execute os comandos abaixo:

```bash
python -m venv venv

source venv/bin/activate        # Para Linux/Mac
venv\Scripts\activate           # Para Windows
```

Em seguida, instale as dependências do projeto:

```python
pip install --upgrade pip
pip install -r requirements.txt
```

### Passo 3: Configurar o banco de dados local

Esta etapa é necessária apenas se você optar por desenvolver localmente. Será necessário instalar o PostgreSQL e criar um banco de dados e um usuário para o projeto. Um tutorial de como fazer a instalação do PostgreSQL pode ser encontrado [aqui](https://www.postgresql.org/download/).

Atualize as seguintes variáveis no arquivo `settings.py` para refletir as configurações do seu banco de dados local:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'lumina_db',
        'USER': 'lumina_user',
        'PASSWORD': 'lumina_password',
        'HOST': '127.0.0.1',  # ou 'localhost'
        'PORT': '5432',
    }
}
```

### Passo 4: Executar as migrações

O projeto utiliza o Django ORM para gerenciar o banco de dados, então é necessário executar as migrações para criar as tabelas necessárias. Execute os comandos abaixo:

```bash
# Criar as migrações iniciais
python manage.py makemigrations

# Aplicar as migrações no banco de dados
python manage.py migrate
```

### Passo 5: Executar o servidor local

```bash
python manage.py runserver
```

Acesse em: [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

Tabela de Versionamento

| Versão | Data       | Descrição              | Autor(es)     |
| ------ | ---------- | ---------------------- | ------------- |
| 1.0    | 09/12/2024 | Criação inicial        | Luiz Henrique |
| 1.1    | 10/12/2024 | Atualização das etapas | Luiz Henrique |
| 1.2    | 12/12/2024 | Atualização das etapas | Luiz Henrique |
