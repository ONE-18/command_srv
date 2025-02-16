# Usa una imagen base de Python
FROM python:3.9-slim

# Instala dependencias necesarias
RUN pip install flask

# Copia el código y el archivo JSON al contenedor
WORKDIR /app
COPY server.py /app
COPY commands.json /app

# Expone el puerto 5000
EXPOSE 5000

# Ejecuta el servidor
CMD ["python", "server.py"]
