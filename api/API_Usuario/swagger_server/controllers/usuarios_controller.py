import connexion
import six


from api.API_Usuario.swagger_server.models.id_contrasea_body import IdContraseaBody
from api.API_Usuario.swagger_server.models.id_correo_body import IdCorreoBody  # noqa: E501
from api.API_Usuario.swagger_server.models.id_generofavorito_body import IdGenerofavoritoBody  # noqa: E501
from api.API_Usuario.swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from api.API_Usuario.swagger_server.models.usuario import Usuario  # noqa: E501
from api.API_Usuario.swagger_server.models.usuarios_body import UsuariosBody  # noqa: E501
from api.API_Usuario.swagger_server.models.usuarios_id_body import UsuariosIdBody  # noqa: E501
from .. import util

from flask import request, jsonify
import dbconnection 

import oracledb
from flask import jsonify, request


def usuarios_id_contrasea_put(body, id):  # noqa: E501
    """Actualizar la contraseña del usuario

     # noqa: E501

    :param body: Nueva contraseña del usuario
    :type body: dict | bytes
    :param id: ID del usuario
    :type id: str

    :rtype: None
    """
   
    new_passwd = body.get('contrasea')

    if new_passwd:
        try:
            if dbconnection.dbModifyPassword(id, new_passwd):
                return {"mensaje": "Contraseña actualizada correctamente"}, 200
            else:
                return {"error": "No se pudo actualizar la contraseña"}, 400
        except Exception as e:
            return {"error": f"Error al actualizar contraseña: {str(e)}"}, 500
    else:
        return {"error": "Solicitud inválida"}, 400


def usuarios_id_correo_put(body, id):  # noqa: E501
    """Actualizar el correo del usuario

     # noqa: E501

    :param body: Nuevo correo electrónico del usuario
    :type body: dict | bytes
    :param id: ID del usuario
    :type id: str

    :rtype: None
    """
    
    new_email = body.get('correo')

    if new_email:
        try:
            if dbconnection.dbModifylEmail(id, new_email):
                return {"mensaje": "Correo actualizado correctamente"}, 200
            else:
                return {"error": "No se pudo actualizar el correo"}, 400
        except Exception as e:
            return {"error": f"Error al actualizar correo: {str(e)}"}, 500
    else:
        return {"error": "Solicitud inválida"}, 400


def usuarios_id_delete(id):  # noqa: E501
    """Eliminar un usuario

    Elimina un usuario existente identificado por su ID y su contraseña. # noqa: E501

    :param id: ID del usuario a eliminar
    :type id: str
    :param contrasea: Contraseña del usuario para confirmar la eliminación
    :type contrasea: str

    :rtype: InlineResponse200
    """
    usuario = dbconnection.dbGetUser(id)  # Llama a la función para obtener el usuario por ID
    if usuario:  
        result = dbconnection.dbRemoveUser(id)  # Llama a la función de eliminación en la base de datos
        if result:
            print("Usuario eliminado correctamente")
            return True
        else:
            return False
    else:
        return False


def usuarios_id_genero_favorito_put(body, id):  # noqa: E501
    """Actualizar el género favorito de un usuario

     # noqa: E501

    :param body: Nuevo género favorito
    :type body: dict | bytes
    :param id: ID del usuario a actualizar
    :type id: str

    :rtype: None
    """
    new_genero = body.get('genero_favorito')

    if new_genero:
        try:
            if dbconnection.dbModifyFavGenre(id,new_genero):
                return {"mensaje": "Contraseña actualizada correctamente"}, 200
            else:
                return {"error": "No se pudo actualizar la contraseña"}, 400
        except Exception as e:
            return {"error": f"Error al actualizar contraseña: {str(e)}"}, 500
    else:
        return {"error": "Solicitud inválida"}, 400


def usuarios_id_get(id):  # noqa: E501
    """Obtener un usuario por ID

     # noqa: E501

    :param id: ID del usuario a obtener
    :type id: str

    :rtype: Usuario
    """

    return dbconnection.dbGetUser(id) # Supongo que esta función existe en `dbconnection`.


def usuarios_id_put(body, id):  # noqa: E501
    """Actualizar el nombre de usuario

     # noqa: E501

    :param body: Nuevo nombre completo del usuario
    :type body: dict | bytes
    :param id: ID del usuario
    :type id: str

    :rtype: None
    """
   
    nombre = body.get('nombre')
    apellidos= body.get('apellidos')

    if nombre:
        try:
            if dbconnection.dbModifyUserName(id, nombre,apellidos):
                    return {"mensaje": "Usuario actualizado correctamente"}, 200
            else:
                return {"error": "No se pudo actualizar el usuario"}, 400
        except Exception as e:
            return {"error": f"Error al actualizar usuario: {str(e)}"}, 500
    else:
        return {"error": "Solicitud inválida"}, 400


def usuarios_post(body):  # noqa: E501
    """Crear un nuevo usuario

     # noqa: E501

    :param body: Datos necesarios para crear un nuevo usuario
    :type body: dict | bytes

    :rtype: Usuario
    """
    
    firstname = body.get("firstname")
    secondname = body.get("secondname")
    correo = body.get("correo")
    password1 = body.get("password1")
    password2 = body.get("password2")

    # Validar los datos
    if not all([firstname ,secondname , correo , password1 ,password2]):
        return jsonify({"error": "Faltan datos"}), 400

    # Crear el nuevo usuario
    nuevo_usuario = dbconnection.dbSignUp(email=correo,firstName=firstname,secondName=secondname, password1=password1,password2=password2)
    return {"mensaje": "Usuario creado correctamente", "usuario": correo}, 201
