# Usa una imagen base de Python
FROM python:3.9-slim

# Instala dependencias necesarias
RUN pip install -r requirements.txt

# Copia el código y el archivo JSON al contenedor
WORKDIR /app
COPY  . .

# Expone el puerto 5000
EXPOSE 5000

# Ejecuta el servidor
# CMD ["python", "server.py"]
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "server:app"]
