# Imagem oficial do Python
FROM python:3.13-slim

# Definir o diretório de trabalho como /app
WORKDIR /app

# Variáveis de ambiente para o Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Instalar as dependências
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código fonte para o diretório de trabalho
COPY . .

# Expor a porta padrão do Django
EXPOSE 8000

# Install Node.js
RUN apt-get update && apt-get install -y curl
RUN curl -sL https://deb.nodesource.com/setup_20.x | bash - 
RUN apt-get install -y nodejs

# Executar o comando de inicialização do Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
