#!/usr/bin/env python3
import connexion
from . import encoder

def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Contenidos - OpenAPI 3.0'}, pythonic_params=True)

    # Aseguramos que Flask (no uvicorn) sea el servidor utilizado
    app.run(port=8080, use_reloader=True)  # Usa Flask en lugar de uvicorn

if __name__ == '__main__':
    main()

