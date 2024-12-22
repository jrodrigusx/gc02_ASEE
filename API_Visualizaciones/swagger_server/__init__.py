from flask import Blueprint

visualizaciones_blueprint = Blueprint('visualizaciones', __name__)

@visualizaciones_blueprint.route('/some_endpoint', methods=['GET'])
def example_endpoint():
    return {"message": "Este es un ejemplo de endpoint de visualizaciones"}
