FROM python:3.11-slim

WORKDIR /app

# Instalar dependencias
RUN pip install psutil

# Copiar el cliente
COPY client_socket_ram.py /app/client_socket_ram.py

CMD ["python", "client_socket_ram.py"]
