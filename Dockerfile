# Usar una imagen base de Python para tu aplicación
FROM python:3.13-slim

# Instalamos Apache y otras dependencias necesarias
RUN apt-get update && \
    apt-get install -y apache2 && \
    apt-get clean

# Copiar el archivo de requisitos de Python e instalar las dependencias
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copiar la aplicación Python (por ejemplo, API) al contenedor
COPY . /app/

COPY ./app.py /app/app.py

COPY ./static /var/www/html/static

COPY ./templates /var/www/html/

# Configurar Apache para servir archivos estáticos
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf

# Habilitar mod_rewrite de Apache para manejo de URLs si es necesario
RUN a2enmod rewrite

# Exponer puertos necesarios
EXPOSE 80 5000

# Iniciar Apache en primer plano y luego ejecutar la aplicación Python (por ejemplo, Flask)
CMD service apache2 start && python /app/app.py
