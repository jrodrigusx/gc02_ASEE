import oracledb as db

def dbConectarVisualizaciones():
    ip = "host.docker.internal"
    puerto = 1521
    s_id = "xe"

    usuario = "system"
    contrasena = "12345"
    dsn = db.makedsn(ip, puerto, s_id)

    print("---dbConectar---")
    print("---Conectando a Oracle---")

    try:
        conexion = db.connect(user=usuario, password=contrasena, host=ip, port=puerto, sid=s_id)
        print("Conexión realizada a la base de datos",conexion)
        print("---Conexión a la base de datos de Visualizaciones---")
        return conexion
    except db.DatabaseError as error:
        print("Error en la conexión")
        print(error)
        return None

def dbGetMovieViews(movie_id):
    print("---dbGetMovieViews---")
    
    try:
        cursor = conexion_visualizaciones.cursor()
        consulta = "SELECT SUM(views) FROM asee_user_movie WHERE movie = :movie_id"
        cursor.execute(consulta, [movie_id])
        tupla = cursor.fetchone()
        print("Visualizaciones de la pelicula ", movie_id, " = ", tupla[0])
        cursor.close()
        return tupla[0]
    except db.DatabaseError as error:
        print("Error. No se han podido obtener las visualizaciones de la pelicula ", movie_id)
        print(error)

def dbGetSerieViews(serie_id):
    print("---dbGetSerieViews---")

    try:
        cursor = conexion_visualizaciones.cursor()
        consulta = "SELECT SUM(views) FROM asee_user_serie WHERE serie = :serie_id"
        cursor.execute(consulta, [serie_id])
        tupla = cursor.fetchone()
        print("Visualizaciones de la serie ", serie_id, " = ", tupla[0])
        cursor.close()
        return tupla[0]
    except db.DatabaseError as error:
        print("Error. No se han podido obtener las visualizaciones de la serie ", serie_id)
        print(error)
        
def dbUpdateMovieViews(user_id, movie_id):
    print("---dbUpdateMovieViews---")

    try:
        cursor = conexion_visualizaciones.cursor()
        consulta = "SELECT * FROM asee_user_movie WHERE user_id = :user_id AND movie = :movie_id"
        cursor.execute(consulta, [user_id, movie_id])
        tupla = cursor.fetchone()
        if tupla is not None:
            #actualizar
            consulta = "UPDATE asee_user_movie SET views = views + 1 WHERE user_id = :user_id AND movie = :movie_id"
            cursor.execute(consulta, [movie_id, user_id])
            cursor.fetchone()
            if(cursor.rowcount == 1):
                print("Visualizaciones del usuario ", user_id, " y de la pelicula ", movie_id, " actualizadas")
                respuesta = True
            else:
                print("No se han podido actualizar las visualizaciones para ", user_id, " y pelicula ", movie_id)
                respuesta = False
        else:
            #insertar
            consulta = "INSERT INTO asee_user_movie VALUES (:user_id, :movie_id, 1)"
            cursor.execute(consulta, [user_id, movie_id])
            if cursor.rowcount == 1:
                print("Se ha insertado visualizacion. Usuario: ", user_id, " Pelicula: ", movie_id)
                respuesta = True
            else:
                print("No se ha podido insertar la visulizacion. Usuario: ", user_id, "Pelicula: ", movie_id)
                respuesta = False

        cursor.close()
        return respuesta
    except db.DatabaseError as error:
        print("Error. No se han podido actualizar las visualizaciones de la pelicula ", movie_id, " usuario: ", user_id)
        print(error)
        return False

def dbUpdateSerieViews(user_id, serie_id):
    print("---dbUpdateSerieViews---")

    try:
        cursor = conexion_visualizaciones.cursor()
        consulta = "SELECT * FROM asee_user_serie WHERE user_id = :user_id AND serie = :serie_id"
        cursor.execute(consulta, [user_id, serie_id])
        tupla = cursor.fetchone()
        if tupla is not None:
            #actualizar
            consulta = "UPDATE asee_user_serie SET views = views + 1 WHERE user_id = :user_id AND serie = :serie_id"
            cursor.execute(consulta, [user_id, serie_id])
            cursor.fetchone()
            if(cursor.rowcount == 1):
                print("Visualizaciones del usuario ", user_id, " y de la serie ", serie_id, " actualizadas")
                respuesta = True
            else:
                print("No se han podido actualizar las visualizaciones para ", user_id, " y serie ", serie_id)
                respuesta = False
        else:
            #insertar
            consulta = "INSERT INTO asee_user_movie VALUES (:user_id, :serie_id, 1)"
            cursor.execute(consulta, [user_id, serie_id])
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
        print("Error. No se han podido actualizar las visualizaciones de la serie ", serie_id, " usuario: ", user_id)
        print(error)
        return False

def dbMovieRecomendations(user_id):
    print("---dbMovieRecomendations---")
    recoms = []

    try:
        cursor = conexion_visualizaciones.cursor()
        consulta = "SELECT * FROM asee_movies FETCH FIRST 5 ROWS ONLY"
        cursor.execute(consulta)
        for tupla in cursor:
            print(tupla)
            recoms.append(tupla)
        cursor.close()
        return recoms
    except db.DatabaseError as error:
        print("Error. No se han podido obtener las recomendaciones de peliculas")
        print(error)

def dbSerieRecomendations(user_id):
    print("---dbSerieRecomendations---")
    recoms = []

    try:
        cursor = conexion_visualizaciones.cursor()
        consulta = "SELECT * FROM asee_series FETCH FIRST 5 ROWS ONLY"
        cursor.execute(consulta)
        for tupla in cursor:
            print(tupla)
            recoms.append(tupla)
        cursor.close()
        return recoms
    except db.DatabaseError as error:
        print("Error. No se han podido obtener las recomendaciones de series")
        print(error)

def dbGetMovieHistory(user_id):
    try:
        cursor = conexion_visualizaciones.cursor()
        consulta = "SELECT movie FROM asee_user_movie WHERE user_id = :user_id"
        cursor.execute(consulta, [user_id,])
        peliculas = []
        for tupla in cursor:
            peliculas.append(tupla)
        return peliculas
    except db.DatabaseError as error:
        print("Error. No se han podido actualizar las visualizaciones de usuario")
        print(error)
        return False


conexion_visualizaciones = dbConectarVisualizaciones()