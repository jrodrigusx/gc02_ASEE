from flask.json import JSONEncoder as FlaskJSONEncoder

class JSONEncoder(FlaskJSONEncoder):
    def default(self, obj):
        # Aquí puedes personalizar la serialización de objetos si es necesario
        return super().default(obj)
