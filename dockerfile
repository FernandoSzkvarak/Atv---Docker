# Usar uma imagem base do Python
FROM python:3.9-slim

# Configurar o diretório de trabalho
WORKDIR /app

# Copiar o arquivo requirements.txt para o contêiner
COPY requirements.txt requirements.txt

# Instalar as dependências
RUN pip install -r requirements.txt

# Copiar o código da aplicação para o contêiner
COPY app.py app.py

# Expor a porta que o Flask usará
EXPOSE 5000

# Comando para iniciar a aplicação Flask
CMD ["python", "app.py"]
