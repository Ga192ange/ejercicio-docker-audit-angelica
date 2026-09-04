FROM python:3.12-slim

WORKDIR /app

# Necesario para el healthcheck (curl -f http://localhost:5050/health)
RUN apt-get update && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Ejecutar como usuario no-root (buena práctica de seguridad)
RUN useradd -m appuser
USER appuser

EXPOSE 5050

CMD ["python", "app.py"]