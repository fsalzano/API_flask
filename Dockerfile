# Usa un'immagine base con Python
FROM python:3.11-slim

# Imposta la directory di lavoro
WORKDIR /hello_api

# Copia i file necessari
COPY requirements.txt .
COPY hello_api.py .

# Installa i pacchetti Python
RUN pip install --no-cache-dir -r requirements.txt

# Espone la porta 5000 (Flask default)
EXPOSE 5000

# Avvia l'app Flask
CMD ["python", "hello_api.py"]
