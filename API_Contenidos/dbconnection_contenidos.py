import oracledb as db

def dbConectarContenidos():
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
        print("---Conexión a la base de datos de Contenidos---")
        return conexion
    except db.DatabaseError as error:
        print("Error en la conexión")
        print(error)
        return None

def dbGetActors():
    print("---dbGetActors---")
    actors = []
    try:
        cursor = conexion_contenidos.cursor()
        consulta = "SELECT * FROM asee_actors"
        cursor.execute(consulta)
        for tupla in cursor:
            print(tupla)
            actors.append(tupla)
        print("Total actores:", cursor.rowcount)
        cursor.close()
        return actors
    except db.DatabaseError as error:
        print("Error: No se pueden obtener los actores")
        print(error)

def dbGetActor(actor_id):
    print("---dbGetActor---")

    try:
        cursor = conexion_contenidos.cursor()
        consulta = "SELECT * FROM asee_actors WHERE actor_id = :actor_id"
        cursor.execute(consulta, [actor_id])
        tupla = cursor.fetchone()
        print(tupla)
        cursor.close()
        return tupla
    except db.DatabaseError as error:
        print("Error: No se puede obtener el actor")
        print(error)

def dbGetDirectors():
    print("---dbGetDirectors---")
    directores = []
    try:
        cursor = conexion_contenidos.cursor()
        consulta = "SELECT * FROM asee_directors"
        cursor.execute(consulta)
        for tupla in cursor:
            print(tupla)
            directores.append(tupla)
        print("Total directores:", cursor.rowcount)
        cursor.close()
        return directores
    except db.DatabaseError as error:
        print("Error: No se pueden obtener los directores")
        print(error)

def dbGetDirectorById(id):
    print("---dbGetDirectorById---")

    try:
        cursor = conexion_contenidos.cursor()
        consulta = "SELECT * FROM asee_directors WHERE director_id = :id"
        cursor.execute(consulta, [id])
        tupla = cursor.fetchone()
        print(tupla)
        cursor.close()
        return tupla
    except db.DatabaseError as error:
        print("Error: No se puede obtener el director")
        print(error)

def dbGetSeries():
    print("---dbGetSeries---")
    series = []
    
    try:
        cursor = conexion_contenidos.cursor()
        consulta = "SELECT * FROM asee_series"
        cursor.execute(consulta)
        for tupla in cursor:
            print(tupla)
            series.append(tupla)
            
        print("Total series:", cursor.rowcount)
        cursor.close()
        return series
    except db.DatabaseError as error:
        print("Error: No se pueden obtener las series")
        print(error)

def dbGetSeasonsOfSerie(id_serie):
    print("---dbGetSeasonsOfSerie---")
    temporadas = []
    
    try:
        cursor = conexion_contenidos.cursor()
        consulta = "SELECT * FROM asee_seasons WHERE serie = :id_serie"
        cursor.execute(consulta, [id_serie])
        for tupla in cursor:
            print(tupla)
            temporadas.append(tupla)
        
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
        cursor = conexion_contenidos.cursor()
        consulta = "SELECT * FROM asee_episodes WHERE season = :id_season AND serie = :id_serie"
        cursor.execute(consulta, [id_season, id_serie])
        for tupla in cursor:
            print(tupla)
            capitulos.append(tupla)
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
        cursor = conexion_contenidos.cursor()
        consulta = "SELECT * FROM asee_episodes WHERE serie = :id_serie"
        cursor.execute(consulta, [id_serie])
        for tupla in cursor:
            print(tupla)
            capitulos.append(tupla)
            
        print("Total capitulos de la serie ", id_serie, " es: ", cursor.rowcount)
        cursor.close()
        return capitulos
    except db.DatabaseError as error:
        print("Error: No se pueden obtener los capitulos de la serie ", id_serie)
        print(error)

def dbGetMovies():
    print("---dbGetMovies---")
    peliculas = []
    try:
        cursor = conexion_contenidos.cursor()
        consulta = "SELECT * FROM asee_movies"
        cursor.execute(consulta)
        for tupla in cursor:
            print(tupla)
            peliculas.append(tupla)
        print("Total películas:", cursor.rowcount)
        cursor.close()
        return peliculas
    except db.DatabaseError as error:
        print("Error: No se pueden obtener las películas")
        print(error)

def dbGetMovieById(movie_id):
    print("---dbGetMovieById---")

    try:
        cursor = conexion_contenidos.cursor()
        consulta = "SELECT * FROM asee_movies WHERE movie_id = :movie_id"
        cursor.execute(consulta, [movie_id])
        tupla = cursor.fetchone()
        print(tupla)
        cursor.close()
        return tupla
    except db.DatabaseError as error:
        print("Error: No se puede obtener la película")
        print(error)

def dbGetSerieById(id_serie):
    print("---dbGetSerieById---")

    try:
        cursor = conexion_contenidos.cursor()
        consulta = "SELECT * FROM asee_series WHERE serie_id = :id_serie"
        cursor.execute(consulta, [id_serie])
        tupla = cursor.fetchone()
        print(tupla)
        cursor.close()
        return tupla
    except db.DatabaseError as error:
        print("Error: No se puede obtener la serie ", id_serie)
        print(error)

def dbGetMoviesByTitle(titulo):
    print("---dbGetMoviesByTitle---")
    peliculas = []
    
    try:
        cursor = conexion_contenidos.cursor()
        consulta = "SELECT * FROM asee_movies WHERE LOWER(movie_title) LIKE :titulo"
        titulo_aux = f"%{titulo.lower()}%"
        cursor.execute(consulta, [titulo_aux])
        for tupla in cursor:
            print(tupla)
            peliculas.append(tupla)
        cursor.close()
        return peliculas
    except db.DatabaseError as error:
        print("Error: No se puede obtener la película")
        print(error)

def dbGetSeriesByTitle(titulo):
    print("---dbGetSeriesByTitle---")
    series = []
    
    try:
        cursor = conexion_contenidos.cursor()
        consulta = "SELECT * FROM asee_series WHERE LOWER(serie_title) LIKE :titulo"
        titulo_aux = f"%{titulo.lower()}%"
        cursor.execute(consulta, [titulo_aux])
        for tupla in cursor:
            print(tupla)
            series.append(tupla)
        cursor.close()
        return series
    except db.DatabaseError as error:
        print("Error: No se pueden obtener las series del titulo ", titulo)
        print(error)

def dbGetMoviesByGenre(genero):
    print("---dbGetMoviesByGenre---")
    peliculas = []

    try:
        cursor = conexion_contenidos.cursor()
        consulta = "SELECT * FROM asee_movies WHERE LOWER(genre) LIKE :genero"
        genero_aux = f"%{genero.lower()}%"
        cursor.execute(consulta, [genero_aux])
        for tupla in cursor:
            print(tupla)
            peliculas.append(tupla)
        print("Total películas del genero ", genero, ": " , cursor.rowcount)
        cursor.close()
        return peliculas
    except db.DatabaseError as error:
        print("Error: No se pueden obtener las películas del genero ", genero)
        print(error)

def dbGetSeriesByGenre(genero):
    print("---dbGetSeriesByGenre---")
    series = []
    
    try:
        cursor = conexion_contenidos.cursor()
        consulta = "SELECT * FROM asee_series WHERE LOWER(genre) LIKE :genero"
        genero_aux = f"%{genero.lower()}%"
        cursor.execute(consulta, [genero_aux])
        for tupla in cursor:
            print(tupla)
            series.append(tupla)
            
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
        cursor = conexion_contenidos.cursor()
        consulta = "SELECT actor FROM asee_actor_movie WHERE movie = :movie_id"
        cursor.execute(consulta, [movie_id])
        for tupla in cursor:
            print(tupla)
            actores.append(tupla)

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
        cursor = conexion_contenidos.cursor()
        consulta = "SELECT actor FROM asee_actor_serie WHERE serie = :serie_id"
        cursor.execute(consulta, [serie_id])
        for tupla in cursor:
            print(tupla)
            actores.append(tupla)

        print("Total actores:", cursor.rowcount)
        cursor.close()
        return actores
    except db.DatabaseError as error:
        print("Error: No se pueden obtener los actores de la serie ", serie_id)
        print(error)

def dbGetMovieDirector(movie_id):
    print("---dbGetMovieDirector---")

    try:
        cursor = conexion_contenidos.cursor()
        consulta = "SELECT director FROM asee_movies WHERE movie_id = :movie_id"
        cursor.execute(consulta, [movie_id])
        tupla = cursor.fetchone()
        print(tupla)
        cursor.close()
        return tupla
    except db.DatabaseError as error:
        print("Error: No se puede obtener el director de la película")
        print(error)


conexion_contenidos = dbConectarContenidos()