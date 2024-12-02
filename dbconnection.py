import oracledb as db
#from . import database
import cx_Oracle
from api.API_Contenidos.swagger_server.models.pelicula import Pelicula
from api.API_Contenidos.swagger_server.models.actor import Actor
from api.API_Contenidos.swagger_server.models.director import Director
from api.API_Contenidos.swagger_server.models.capitulo import Capitulo
from api.API_Contenidos.swagger_server.models.serie import Serie
from api.API_Contenidos.swagger_server.models.temporada import Temporada
from api.API_Usuario.swagger_server.models.usuario import Usuario
from api.API_Visualizaciones.swagger_server.models.visualizaciones_peliculas import VisualizacionesPeliculas
from api.API_Visualizaciones.swagger_server.models.visualizaciones_series import VisualizacionesSeries
from api.API_Visualizaciones.swagger_server.models.recomendaciones_peliculas import RecomendacionesPeliculas
from api.API_Visualizaciones.swagger_server.models.recomendaciones_series import RecomendacionesSeries

def dbConectar():
    ip = "localhost"
    puerto = 1521
    s_id = "xe"

    usuario = "system"
    contrasena = "12345"

    print("---dbConectar---")
    print("---Conectando a Oracle---")

    try:
        conexion = db.connect(user=usuario, password=contrasena, host=ip, port=puerto, sid=s_id)
        print("Conexión realizada a la base de datos",conexion)
        return conexion
    except db.DatabaseError as error:
        print("Error en la conexión")
        print(error)
        return None

def dbSignUp(email=str, firstName=str, secondName=str, password1=str, password2=str):
    print("---dbSignUp---")
    
    try:
        cursor = conexion.cursor()
        print(email)
        print(firstName)
        print(secondName)
        print(password1)
        print(password2)
        consulta = "INSERT INTO asee_users (email, firstname, secondname, passwd) VALUES(:email, :firstName, :secondName, :password1)"
        if(password1 == password2):
            cursor.execute(consulta, [email, firstName, secondName, password1])
            print("Tupla insertada correctamente")
            print('------------------------------')
            cursor.close()
            conexion.commit()
            return True
        else:
            print("Error: Las contraseñas no coinciden")
            cursor.close()
            return False
    except db.DatabaseError as error:
        print("Error. No se ha podido crear el usuario")
        print(error)
        return False

def dbLogIn(email=str, password=str):
    print("---dbLogIn---")

    try:
        cursor = conexion.cursor()
        print(email)
        print(password)
        consulta = "SELECT user_id,email, passwd FROM asee_users WHERE email = :email AND passwd = :password"
        cursor.execute(consulta, [email, password])
        resul = cursor.fetchone()
        if(cursor.rowcount == 1):
            print("Usuario encontrado correctamente")
            if(resul[2] == password):
                print('Usuario y contraseña correctos')
            else:
                print('La contraseña no es correcta')
                return False
        else:
            print("Usuario no existente:",cursor.rowcount)
            return False
        print('------------------------------')
        
        cursor.close()
        conexion.commit()
        if resul[0] is None:
            return None
        else:
            return resul[0]
       
    except db.DatabaseError as error:
        print("Error. No se ha podido iniciar sesión")
        print(error)
        return False

def dbPrint():
    try:
        cursor = conexion.cursor()
        consulta = "SELECT * FROM asee_users"
        cursor.execute(consulta)
        for tupla in cursor:
            print(tupla)
        print("Total usuarios:", cursor.rowcount)
        cursor.close()
    except db.DatabaseError as error:
        print("Error: No hay nada")

def dbGetActors():
    print("---dbGetActors---")
    actores = []
    try:
        cursor = conexion.cursor()
        consulta = "SELECT * FROM asee_actors"
        cursor.execute(consulta)
        for tupla in cursor:
            print(tupla)
            actor = Actor(tupla[0], tupla[1], tupla[2])
            actores.append(actor.to_dict())
        print("Total actores:", cursor.rowcount)
        cursor.close()
        return actores
    except db.DatabaseError as error:
        print("Error: No se pueden obtener los actores")
        print(error)

def dbGetActor(actor_id):
    print("---dbGetActor---")

    try:
        cursor = conexion.cursor()
        consulta = "SELECT * FROM asee_actors WHERE actor_id = :actor_id"
        cursor.execute(consulta, [actor_id])
        tupla = cursor.fetchone()
        print(tupla)
        actor = Actor(tupla[0], tupla[1], tupla[2])
        cursor.close()
        return actor.to_dict()
    except db.DatabaseError as error:
        print("Error: No se puede obtener el actor")
        print(error)

def dbGetDirectors():
    print("---dbGetDirectors---")
    directores = []
    try:
        cursor = conexion.cursor()
        consulta = "SELECT * FROM asee_directors"
        cursor.execute(consulta)
        for tupla in cursor:
            print(tupla)
            director = Director(tupla[0], tupla[1], tupla[2])
            directores.append(director.to_dict())
        print("Total directores:", cursor.rowcount)
        cursor.close()
        return directores
    except db.DatabaseError as error:
        print("Error: No se pueden obtener los directores")
        print(error)

def dbGetDirectorById(id):
    print("---dbGetDirectorById---")

    try:
        cursor = conexion.cursor()
        consulta = "SELECT * FROM asee_directors WHERE director_id = :id"
        cursor.execute(consulta, [id])
        tupla = cursor.fetchone()
        print(tupla)
        director = Director(tupla[0], tupla[1], tupla[2])
        cursor.close()
        return director.to_dict()
    except db.DatabaseError as error:
        print("Error: No se puede obtener el director")
        print(error)

def dbGetSeries():
    print("---dbGetSeries---")
    actores = []
    temporadas = []
    capitulos = []
    series = []
    
    try:
        cursor = conexion.cursor()
        consulta = "SELECT * FROM asee_series"
        cursor.execute(consulta)
        for tupla in cursor:
            print(tupla)
            actores = dbGetActorsInSerie(tupla[0])
            temporadas = dbGetSeasonsOfSerie(tupla[0])
            capitulos = dbGetEpisodesOfSerie(tupla[0])
            serie = Serie(tupla[0], tupla[1], tupla[2], tupla[3], actores, temporadas, capitulos)
            series.append(serie.to_dict())
            
        print("Total series:", cursor.rowcount)
        cursor.close()
        return series
    except db.DatabaseError as error:
        print("Error: No se pueden obtener las series")
        print(error)

def dbGetSeasonsOfSerie(id_serie):
    print("---dbGetSeasonsOfSerie---")
    temporadas = []
    capitulos = []
    
    try:
        cursor = conexion.cursor()
        consulta = "SELECT * FROM asee_seasons WHERE serie = :id_serie"
        cursor.execute(consulta, [id_serie])
        for tupla in cursor:
            print(tupla)
            capitulos = dbGetEpisodesOfSeason(id_serie, tupla[0])
            temporada = Temporada(tupla[0], tupla[2], tupla[3], capitulos)
            temporadas.append(temporada.to_dict())
        
        print("Total temporadas de la serie ", id_serie, ": " , cursor.rowcount)
        cursor.close()
        return temporadas
    except db.DatabaseError as error:
        print("Error: No se pueden obtener las temporadas de la serie ", id_serie)
        print(error)
    
def dbGetEpisodesOfSeason(id_serie, id_season):
    print("---dbGetEpisodesOfSeason---")
    capitulos = []
    
    try:
        cursor = conexion.cursor()
        consulta = "SELECT * FROM asee_episodes WHERE season = :id_season AND serie = :id_serie"
        cursor.execute(consulta, [id_season, id_serie])
        for tupla in cursor:
            print(tupla)
            director = dbGetDirectorById(tupla[7])
            capitulo = Capitulo(tupla[0], tupla[1], tupla[5], tupla[4], tupla[6], director)
            capitulos.append(capitulo.to_dict())
        print("Total capitulos de la serie ", id_serie, " y la temporada " , id_season, " es: ", cursor.rowcount)
        cursor.close()
        return capitulos
    except db.DatabaseError as error:
        print("Error: No se pueden obtener los capitulos de la serie ", id_serie, " y la temporada " , id_season)
        print(error)

def dbGetEpisodesOfSerie(id_serie):
    print("---dbGetEpisodesOfSerie---")
    capitulos = []
    
    try:
        cursor = conexion.cursor()
        consulta = "SELECT * FROM asee_episodes WHERE serie = :id_serie"
        cursor.execute(consulta, [id_serie])
        for tupla in cursor:
            print(tupla)
            director = dbGetDirectorById(tupla[7])
            capitulo = Capitulo(tupla[0], tupla[1], tupla[5], tupla[4], tupla[6], director)
            capitulos.append(capitulo.to_dict())
            
        print("Total capitulos de la serie ", id_serie, " es: ", cursor.rowcount)
        cursor.close()
        return capitulos
    except db.DatabaseError as error:
        print("Error: No se pueden obtener los capitulos de la serie ", id_serie)
        print(error)

def dbGetMovies():
    print("---dbGetMovies---")
    actores = []
    peliculas = []
    try:
        cursor = conexion.cursor()
        consulta = "SELECT * FROM asee_movies"
        cursor.execute(consulta)
        for tupla in cursor:
            print(tupla)
            director = dbGetDirectorById(tupla[4])
            actores = dbGetActorsInMovie(tupla[0])
            pelicula = Pelicula(tupla[0], tupla[1], tupla[2], tupla[3], director, actores, tupla[5])
            peliculas.append(pelicula.to_dict())
        print("Total películas:", cursor.rowcount)
        cursor.close()
        return peliculas
    except db.DatabaseError as error:
        print("Error: No se pueden obtener las películas")
        print(error)

def dbGetMovieById(movie_id):
    print("---dbGetMovieById---")
    actores = []

    try:
        cursor = conexion.cursor()
        consulta = "SELECT * FROM asee_movies WHERE movie_id = :movie_id"
        cursor.execute(consulta, [movie_id])
        tupla = cursor.fetchone()
        print(tupla)
        director = dbGetDirectorById(tupla[4])
        actores = dbGetActorsInMovie(tupla[0])
        pelicula = Pelicula(tupla[0], tupla[1], tupla[2], tupla[3], director, actores, tupla[5])
        cursor.close()
        return pelicula.to_dict()
    except db.DatabaseError as error:
        print("Error: No se puede obtener la película")
        print(error)

def dbGetSerieById(id_serie):
    print("---dbGetSerieById---")
    actores = []
    temporadas = []
    capitulos = []
    
    try:
        cursor = conexion.cursor()
        consulta = "SELECT * FROM asee_series WHERE serie_id = :id_serie"
        cursor.execute(consulta, [id_serie])
        tupla = cursor.fetchone()
        print(tupla)
        actores = dbGetActorsInSerie(id_serie)
        temporadas = dbGetSeasonsOfSerie(id_serie)
        capitulos = dbGetEpisodesOfSerie(id_serie)
        serie = Serie(tupla[0], tupla[1], tupla[2], tupla[3], actores, temporadas, capitulos)
        cursor.close()
        return serie.to_dict()
    except db.DatabaseError as error:
        print("Error: No se puede obtener la serie ", id_serie)
        print(error)

def dbGetMoviesByTitle(titulo):
    print("---dbGetMoviesByTitle---")
    peliculas = []
    
    try:
        cursor = conexion.cursor()
        consulta = "SELECT * FROM asee_movies WHERE LOWER(movie_title) LIKE :titulo"
        titulo_aux = f"%{titulo.lower()}%"
        cursor.execute(consulta, [titulo_aux])
        for tupla in cursor:
            print(tupla)
            director = dbGetDirectorById(tupla[4]) 
            actores = dbGetActorsInMovie(tupla[0])
            pelicula = Pelicula(tupla[0], tupla[1], tupla[2], tupla[3], director, actores, tupla[5])
            peliculas.append(pelicula.to_dict())
        cursor.close()
        return peliculas
    except db.DatabaseError as error:
        print("Error: No se puede obtener la película")
        print(error)

def dbGetSeriesByTitle(titulo):
    print("---dbGetSeriesByTitle---")
    actores = []
    temporadas = []
    capitulos = []
    series = []
    
    try:
        cursor = conexion.cursor()
        consulta = "SELECT * FROM asee_series WHERE LOWER(serie_title) LIKE :titulo"
        titulo_aux = f"%{titulo.lower()}%"
        cursor.execute(consulta, [titulo_aux])
        for tupla in cursor:
            print(tupla)
            actores = dbGetActorsInSerie(tupla[0])
            temporadas = dbGetSeasonsOfSerie(tupla[0])
            capitulos = dbGetEpisodesOfSerie(tupla[0])
            serie = Serie(tupla[0], tupla[1], tupla[2], tupla[3], actores, temporadas, capitulos)
            series.append(serie.to_dict())
        cursor.close()
        return series
    except db.DatabaseError as error:
        print("Error: No se pueden obtener las series del titulo ", titulo)
        print(error)

def dbGetMoviesByGenre(genero):
    print("---dbGetMoviesByGenre---")
    peliculas = []
    actores = []

    try:
        cursor = conexion.cursor()
        consulta = "SELECT * FROM asee_movies WHERE LOWER(genre) LIKE :genero"
        genero_aux = f"%{genero.lower()}%"
        cursor.execute(consulta, [genero_aux])
        for tupla in cursor:
            print(tupla)
            director = dbGetDirectorById(tupla[4])
            actores = dbGetActorsInMovie(tupla[0])
            pelicula = Pelicula(tupla[0], tupla[1], tupla[2], tupla[3], director, actores, tupla[5])
            peliculas.append(pelicula.to_dict())
        print("Total películas del genero ", genero, ": " , cursor.rowcount)
        cursor.close()
        return peliculas
    except db.DatabaseError as error:
        print("Error: No se pueden obtener las películas del genero ", genero)
        print(error)

def dbGetSeriesByGenre(genero):
    print("---dbGetSeriesByGenre---")
    actores = []
    temporadas = []
    capitulos = []
    series = []
    
    try:
        cursor = conexion.cursor()
        consulta = "SELECT * FROM asee_series WHERE LOWER(genre) LIKE :genero"
        genero_aux = f"%{genero.lower()}%"
        cursor.execute(consulta, [genero_aux])
        for tupla in cursor:
            print(tupla)
            actores = dbGetActorsInSerie(tupla[0])
            temporadas = dbGetSeasonsOfSerie(tupla[0])
            capitulos = dbGetEpisodesOfSerie(tupla[0])
            serie = Serie(tupla[0], tupla[1], tupla[2], tupla[3], actores, temporadas, capitulos)
            series.append(serie.to_dict())
            
        print("Total series del genero", genero, ": ", cursor.rowcount)
        cursor.close()
        return series
    except db.DatabaseError as error:
        print("Error: No se pueden obtener las series del genero ", genero)
        print(error)

def dbGetActorsInMovie(movie_id):
    print("---dbGetActorsInMovie---")
    actores = []
    
    try:
        cursor = conexion.cursor()
        consulta = "SELECT a.actor_id, a.actor_name, a.actor_birthdate FROM asee_actors a JOIN asee_actor_movie am ON a.actor_id = am.actor WHERE am.movie = :movie_id"
        cursor.execute(consulta, [movie_id])
        for tupla in cursor:
            print(tupla)
            actor = Actor(tupla[0], tupla[1], tupla[2])
            actores.append(actor.to_dict())

        print("Total actores:", cursor.rowcount)
        cursor.close()
        return actores
    except db.DatabaseError as error:
        print("Error: No se pueden obtener los actores de la película")
        print(error)

def dbGetActorsInSerie(serie_id):
    print("---dbGetActorsInSerie---")
    actores = []
    
    try:
        cursor = conexion.cursor()
        consulta = "SELECT a.actor_id, a.actor_name, a.actor_birthdate FROM asee_actors a JOIN asee_actor_serie as ON a.actor_id = as.actor WHERE as.movie = :movie_id"
        cursor.execute(consulta, [serie_id])
        for tupla in cursor:
            print(tupla)
            actor = Actor(tupla[0], tupla[1], tupla[2])
            actores.append(actor.to_dict())

        print("Total actores:", cursor.rowcount)
        cursor.close()
        return actores
    except db.DatabaseError as error:
        print("Error: No se pueden obtener los actores de la serie ", serie_id)
        print(error)

def dbGetMovieDirector(movie_id):
    print("---dbGetMovieDirector---")
    directores = []

    try:
        cursor = conexion.cursor()
        consulta = "SELECT ad.director_id, ad.director_name, ad.director_birthdate FROM asee_directors ad JOIN asee_movies am ON ad.director_id = am.director WHERE am.movie_id = :movie_id"
        cursor.execute(consulta, [movie_id])
        for tupla in cursor:
            print(tupla)
            director = Director(tupla[0], tupla[1], tupla[2])
            directores.append(director.to_dict())
        cursor.close()
        return directores
    except db.DatabaseError as error:
        print("Error: No se puede obtener el director de la película")
        print(error)

def dbGetUser(id):
    print("---dbGetUser---")

    try:
        cursor = conexion.cursor()
        consulta = "SELECT * FROM asee_users WHERE user_id = :id"
        cursor.execute(consulta, [id])
        tupla = cursor.fetchone()
        print(tupla)
        imagen = "imagen.jpg"
        mpago = "Paypal"
        idioma = "Español"
        
        if tupla is None:
            return None

        usuario = Usuario(tupla[0], tupla[2], tupla[3], tupla[1],tupla[4], imagen, mpago, idioma, tupla[5])
        cursor.close()
        return usuario.to_dict()
    except db.DatabaseError as error:
        print("Error: No se puede obtener el usuario")
        print(error)

def dbModifyUserName(id, nombre,apellidos):
    print("---dbModifyUserName---")
    try:
        cursor = conexion.cursor()
        print(nombre, apellidos)
        consulta = "UPDATE asee_users SET firstname = :nombre, secondname =:apellidos WHERE user_id = :id"
        cursor.execute(consulta, [nombre, apellidos, id])
        
        if cursor.rowcount == 1:
            print("Nombre del usuario ", id, " modificado. Nuevo nombre: ", nombre)
            respuesta = True
        else:
            print("No se ha podido modificar el nombre del usuario")
            respuesta = False
        
        cursor.close()
        conexion.commit()
        return respuesta
    except db.DatabaseError as error:
        print("Error: No se ha podido cambiar el nombre del usuario")
        print(error)
        return False

def dbModifyFavGenre(id, genero):
    print("---dbModifyFavGenre---")
    try:
        cursor = conexion.cursor()
        consulta = "UPDATE asee_users SET fav_genre = :genero WHERE user_id = :id"
        cursor.execute(consulta, [genero, id])
        
        if cursor.rowcount == 1:
            print("Genero favorito del usuario ", id, " modificado. Nuevo genero favorito: ", genero)
            respuesta = True
        else:
            print("No se ha podido modificar el genero favorito del usuario")
            respuesta = False
        
        cursor.close()
        conexion.commit()
        return respuesta
    except db.DatabaseError as error:
        print("Error: No se ha podido cambiar el genero favorito del usuario")
        print(error)
        return False

def dbModifylEmail(id, email):
    print("---dbModifylEmail---")
    try:
        cursor = conexion.cursor()
        consulta = "UPDATE asee_users SET email = :email WHERE user_id = :id"
        cursor.execute(consulta, [email, id])
        
        if cursor.rowcount == 1:
            print("Email del usuario ", id, " modificado. Nuevo email: ", email)
            respuesta = True
        else:
            print("No se ha podido modificar el email favorito del usuario")
            respuesta = False
        
        cursor.close()
        conexion.commit()
        return respuesta
    except db.DatabaseError as error:
        print("Error: No se ha podido cambiar el email del usuario")
        print(error)
        return False

def dbModifyPassword(id, password):
    print("---dbModifyPassword---")
    try:
        cursor = conexion.cursor()
        consulta = "UPDATE asee_users SET passwd = :password WHERE user_id = :id"
        cursor.execute(consulta, [password, id])
        
        if cursor.rowcount == 1:
            print("Contraseña del usuario ", id, " modificada. Nueva contraseña: ", password)
            respuesta = True
        else:
            print("No se ha podido modificar la contarseña del usuario")
            respuesta = False
        
        cursor.close()
        conexion.commit()
        return respuesta
    except db.DatabaseError as error:
        print("Error: No se ha podido cambiar la contraseña del usuario")
        print(error)
        return False

def dbRemoveUser(id):
    print("---dbRemoveUser---")
    try:
        cursor = conexion.cursor()
        consulta = "DELETE FROM asee_users WHERE user_id = :id"
        cursor.execute(consulta, [id])
        if(cursor.rowcount == 1):
            print("Usuario eliminado correctamente")
            respuesta = True
        else:
            print("Usuario no existente en la base de datos:",cursor.rowcount)
            respuesta = False
        print('------------------------------')
        cursor.close()
        conexion.commit()
        return respuesta
    except db.DatabaseError as error:
        print("Error. No se ha podido eliminar el usuario")
        print(error)
        conexion.rollback()
        return False

def dbGetMovieViews(movie_id):
    print("---dbGetMovieViews---")
    
    try:
        cursor = conexion.cursor()
        consulta = "SELECT SUM(views) FROM asee_user_movie WHERE movie = :movie_id"
        cursor.execute(consulta, [movie_id])
        tupla = cursor.fetchone()
        total_views = tupla[0]
        view = VisualizacionesPeliculas(movie_id, movie_id, total_views)
        print("Visualizaciones de la pelicula ", movie_id, " = ", total_views)
        cursor.close()
        return view.to_dict()
    except db.DatabaseError as error:
        print("Error. No se han podido obtener las visualizaciones de la pelicula ", movie_id)
        print(error)

def dbGetSerieViews(serie_id):
    print("---dbGetSerieViews---")

    try:
        cursor = conexion.cursor()
        consulta = "SELECT SUM(views) FROM asee_user_serie WHERE serie = :serie_id"
        cursor.execute(consulta, [serie_id])
        tupla = cursor.fetchone()
        total_views = tupla[0]
        view = VisualizacionesSeries(serie_id, serie_id, total_views)
        print("Visualizaciones de la serie ", serie_id, " = ", total_views)
        cursor.close()
        return view.to_dict()
    except db.DatabaseError as error:
        print("Error. No se han podido obtener las visualizaciones de la serie ", serie_id)
        print(error)
        
def dbUpdateMovieViews(id, movie_id, nview):
    print("---dbUpdateMovieViews---")

    try:
        cursor = conexion.cursor()
        consul = "SELECT user_email FROM asee_user_movie WHERE user_email = (SELECT email FROM asee_users WHERE user_id = :id)"
        cursor.execute(consul, [id])
        tupla = cursor.fetchone()
        email = tupla[0]
        if tupla is not None:
            #actualizar
            consulta = "UPDATE asee_user_movie SET views = views + :nview WHERE movie = :movie_id AND user_email = :email"
            cursor.execute(consulta, [nview, movie_id, email])
            tupla2 = cursor.fetchone()
            if(cursor.rowcount == 1):
                print("Visualizaciones del usuario ", email, " y de la pelicula ", movie_id, " actualizadas")
                respuesta = True
            else:
                print("No se han podido actualizar las visualizaciones para ", email, " y pelicula ", movie_id)
                respuesta = False
        else:
            #insertar
            consulta3 = "INSERT INTO asee_user_movie VALUES (:email, :movie_id, :nview)"
            cursor.execute(consulta3, [email, movie_id, nview])
            if cursor.rowcount == 1:
                print("Se ha insertado visualizacion. Usuario: ", email, " Pelicula: ", movie_id)
                respuesta = True
            else:
                print("No se ha podido insertar la visulizacion. Usuario: ", email, "Pelicula: ", movie_id)
                respuesta = False

        cursor.close()
        return respuesta
    except db.DatabaseError as error:
        print("Error. No se han podido actualizar las visualizaciones de la pelicula ", movie_id, " usuario: ", id)
        print(error)
        return False

def dbUpdateSerieViews(user_id, serie_id):
    print("---dbUpdateSerieViews---")

    try:
        cursor = conexion.cursor()
        consul = "SELECT * FROM asee_user_serie WHERE user_id = :user_id AND serie = :serie_id"
        cursor.execute(consul, [user_id, serie_id])
        tupla = cursor.fetchone()
        if tupla is not None:
            #actualizar
            consul = "UPDATE asee_user_serie SET views = views + 1 WHERE user_id = :user_id AND serie = :serie_id"
            cursor.execute(consul, [user_id, serie_id])
            cursor.fetchone()
            if(cursor.rowcount == 1):
                print("Visualizaciones del usuario ", user_id, " y de la serie ", serie_id, " actualizadas")
                respuesta = True
            else:
                print("No se han podido actualizar las visualizaciones para ", user_id, " y serie ", serie_id)
                respuesta = False
        else:
            #insertar
            consul = "INSERT INTO asee_user_movie VALUES (:email, :serie_id, 1)"
            cursor.execute(consul, [user_id, serie_id])
            cursor.fetchone()
            if cursor.rowcount == 1:
                print("Se ha insertado visualizacion. Usuario: ", user_id, " Serie: ", serie_id)
                respuesta = True
            else:
                print("No se ha podido insertar la visulizacion. Usuario: ", user_id, "Serie: ", serie_id)
                respuesta = False

        cursor.close()
        return respuesta
    except db.DatabaseError as error:
        print("Error. No se han podido actualizar las visualizaciones de la serie ", serie_id, " usuario: ", id)
        print(error)
        return False

def dbMovieRecomendations(user_id):
    print("---dbMovieRecomendations---")
    recoms = []

    try:
        cursor = conexion.cursor()
        consulta = "SELECT * FROM asee_movies FETCH FIRST 5 ROWS ONLY"
        cursor.execute(consulta)
        for tupla in cursor:
            print(tupla)
            recoms.append(tupla[0])    
        movie_recom = RecomendacionesPeliculas(user_id, user_id, recoms)
        cursor.close()
        return movie_recom.to_dict()
    except db.DatabaseError as error:
        print("Error. No se han podido obtener las recomendaciones de peliculas")
        print(error)

def dbSerieRecomendations(user_id):
    print("---dbSerieRecomendations---")
    recoms = []

    try:
        cursor = conexion.cursor()
        consulta = "SELECT * FROM asee_series FETCH FIRST 5 ROWS ONLY"
        cursor.execute(consulta)
        for tupla in cursor:
            print(tupla)
            recoms.append(tupla[0])    
        serie_recom = RecomendacionesSeries(user_id, user_id, recoms)
        cursor.close()
        return serie_recom.to_dict()
    except db.DatabaseError as error:
        print("Error. No se han podido obtener las recomendaciones de series")
        print(error)

def dbGetMovieHistory(user_id):
    try:
        cursor = conexion.cursor()
        consul = "SELECT movie FROM asee_user_movie WHERE user_id = :user_id"
        cursor.execute(consul, [user_id,])
        peliculas = []
        for tupla in cursor:
            pelicula = dbGetMovieById(tupla[0])
            peliculas.append(pelicula)
        return peliculas
    except db.DatabaseError as error:
        print("Error. No se han podido actualizar las visualizaciones de usuario")
        print(error)
        return False
conexion = dbConectar()