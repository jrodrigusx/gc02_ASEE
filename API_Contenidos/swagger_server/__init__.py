from flask import Blueprint

contenidos_blueprint = Blueprint('contenidos', __name__)

@contenidos_blueprint.route('/some_endpoint', methods=['GET'])
def example_endpoint():
    return {"message": "Este es un ejemplo de endpoint de contenidos"}
