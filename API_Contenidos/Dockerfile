FROM python:3.13-slim

WORKDIR /app/API_Contenidos

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5001

CMD ["python", "swagger_server/__main__.py"]