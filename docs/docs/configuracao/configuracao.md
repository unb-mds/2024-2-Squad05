# Guia de Configuração e Execução do Projeto

Este guia fornece instruções detalhadas para configurar e executar o projeto Lumina, que utiliza Django, TailwindCSS, Docker e PostgreSQL. Você pode optar por configurar o projeto em um ambiente local ou utilizar Docker para simplificar o processo. Recomendamos o uso do Docker para uma configuração mais rápida e consistente. Siga as instruções abaixo conforme sua preferência.

---

## Pré-requisitos

Certifique-se de ter os seguintes pré-requisitos instalados:

### Ambiente Local

- **Python 3.13** ou superior
- **PostgreSQL** (se preferir usar localmente)
- **Node.js** (versão 20 ou superior) e **npm**
- **pip** e **venv** para gerenciamento de dependências
- **TailwindCSS CLI** (instalado via npm)
- **Git** (opcional, para gerenciar o repositório)

### Docker

- **Docker** (recomendado: versão mais recente)
- **Docker Compose**

---

## Configuração e Execução

Nossa aplicação é composta por dois serviços: `web` (Django) e `db` (PostgreSQL). A configuração e execução do projeto pode ser feita de duas formas: localmente ou usando Docker. Siga as instruções abaixo de acordo com a sua preferência.

## 1. Desenvolvimento Local

### Passo 1: Clonar o repositório

```bash
git clone https://github.com/unb-mds/2024-2-Squad05.git
```

### Passo 2: Configurar o ambiente virtual e instalar dependências

Entre no repositório clonado e execute os seguintes comandos no terminal:

```bash
python -m venv venv

source venv/bin/activate        # Para Linux/Mac
venv\Scripts\activate           # Para Windows

pip install --upgrade pip
pip install -r requirements.txt
```

### Passo 3: Configurar o banco de dados local

Configure o PostgreSQL com os seguintes dados:

- Banco de dados: `lumina_db`
- Usuário: `lumina_user`
- Senha: `lumina_password`

Atualize a variável `HOST` no arquivo `settings.py` para `127.0.0.1` ou `localhost`. Note que o PostgreSQL deve estar rodando localmente.

### Passo 4: Configurar o TailwindCSS

Instale o TailwindCSS CLI:

```bash
npm install -g tailwindcss
```

Compile os estilos com:

```bash
tailwindcss -i ./app/view/static/css/style.css -o ./app/view/static/dist style.css --watch
```

### Passo 5: Executar as migrações

```bash
python manage.py makemigrations
python manage.py migrate
```

### Passo 6: Executar o servidor local

```bash
python manage.py runserver
```

Acesse em: [http://127.0.0.1:8000](http://127.0.0.1:8000).

## 2. Docker

### Passo 1: Clonar o repositório

```bash
git clone https://github.com/unb-mds/2024-2-Squad05.git
```

### Passo 2: Construir e iniciar os contêineres

Altere para a pasta clonada. Certifique-se de que o Docker está ativo e execute:

```bash
docker-compose up --build
```

### Passo 3: Verificar logs e garantir que tudo está funcionando

Monitore os logs:

```bash
docker-compose logs -f
```

### Passo 4: Inicializar o banco de dados (primeira execução)

Acesse o contêiner do Django e aplique as migrações:

```bash
docker exec -it lumina-web bash
python manage.py makemigrations
python manage.py migrate
```

### Passo 5: Compilar o TailwindCSS

Ainda dentro do contêiner do Django, compile os estilos com:

```bash
npm install -g tailwindcss
tailwindcss -i ./app/view/static/css/style.css -o ./app/view/static/dist/style.css --watch
```

### Passo 6: Acessar a aplicação

Acesse em: [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

Tabela de Versionamento

| Versão | Data       | Descrição       | Autor(es)     |
| ------ | ---------- | --------------- | ------------- |
| 1.0    | 09/12/2024 | Criação inicial | Luiz Henrique |
