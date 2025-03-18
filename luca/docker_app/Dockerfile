# Basis-Image mit Python
FROM python:3.9

# Arbeitsverzeichnis setzen
WORKDIR /app

# Abhängigkeiten kopieren & installieren
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# App-Code kopieren
COPY . .

# Container starten
CMD ["python", "app.py"]
