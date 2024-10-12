# Usando uma imagem base do Python
FROM python:3.9-slim

# Definindo o diretório de trabalho
WORKDIR /app

# Copiando o arquivo de requisitos primeiro para aproveitar o cache do Docker
COPY requirements.txt .

# Instalando as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiando o restante do código da aplicação
COPY . .

# Expondo a porta que a aplicação vai rodar
EXPOSE 8080

# Comando para rodar a aplicação
CMD ["python", "app.py"]