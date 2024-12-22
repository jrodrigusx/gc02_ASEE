FROM python:3.13-slim

# Establecer el directorio de trabajo
WORKDIR /app/API_Visualizaciones

# Copiar el archivo de dependencias al contenedor
COPY requirements.txt .

# Instalar las dependencias de Python necesarias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código de la aplicación
COPY . .

# Exponer el puerto utilizado por la aplicación
EXPOSE 5003

# Comando predeterminado para ejecutar la aplicación
CMD ["python", "swagger_server/_main_.py"]