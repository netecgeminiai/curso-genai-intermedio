FROM python:3.10-slim

WORKDIR /app

# Instalar dependencias optimizando caché
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar app
COPY router_api.py .

EXPOSE 8000

# Lanzar Uvicorn
CMD ["uvicorn", "router_api:app", "--host", "0.0.0.0", "--port", "8000"]
