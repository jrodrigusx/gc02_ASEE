import oracledb as db
#from . import database

def dbConectar():
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
        consulta = "INSERT INTO asee_users VALUES(:email, :firstName, :secondName, :password1)"
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
        consulta = "SELECT email, passwd FROM asee_users WHERE email = :email AND passwd = :password"
        cursor.execute(consulta, [email, password])
        resul = cursor.fetchone()
        if(cursor.rowcount == 1):
            print("Usuario encontrado correctamente")
            if(resul[1] == password):
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
        return True
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

    try:
        cursor = conexion.cursor()
        consulta = "SELECT * FROM asee_actors"
        cursor.execute(consulta)
        for tupla in cursor:
            print(tupla)
        print("Total actores:", cursor.rowcount)
        cursor.close()
    except db.DatabaseError as error:
        print("Error: No se pueden obtener los actores")
        print(error)

def dbGetActor(actor_id):
    print("---dbGetActor---")

    try:
        cursor = conexion.cursor()
        consulta = "SELECT * FROM asee_actors WHERE actor_id = :actor_id"
        cursor.execute(consulta, [actor_id])
        for tupla in cursor:
            print(tupla)
        print("Total actores:", cursor.rowcount)
        cursor.close()
    except db.DatabaseError as error:
        print("Error: No se puede obtener el actor")
        print(error)

def dbGetDirectors():
    print("---dbGetDirectors---")

    try:
        cursor = conexion.cursor()
        consulta = "SELECT * FROM asee_directors"
        cursor.execute(consulta)
        for tupla in cursor:
            print(tupla)
        print("Total directores:", cursor.rowcount)
        cursor.close()
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
        cursor.close()
    except db.DatabaseError as error:
        print("Error: No se puede obtener el director")
        print(error)

def dbGetEpisodes():
    print("---dbGetEpisodes---")

def dbGetSeasons():
    print("---dbGetSeasons---")

def dbGetSeries():
    print("---dbGetSeries---")

def dbGetMovies():
    print("---dbGetMovies---")

    try:
        cursor = conexion.cursor()
        consulta = "SELECT * FROM asee_movies"
        cursor.execute(consulta)
        for tupla in cursor:
            print(tupla)
        print("Total películas:", cursor.rowcount)
        cursor.close()
    except db.DatabaseError as error:
        print("Error: No se pueden obtener las películas")
        print(error)

def dbGetMovieById(movie_id):
    print("---dbGetMovieById---")

    try:
        cursor = conexion.cursor()
        consulta = "SELECT * FROM asee_movies WHERE movie_id = :movie_id"
        cursor.execute(consulta, [movie_id])
        tupla = cursor.fetchone()
        print(tupla)
        cursor.close()
    except db.DatabaseError as error:
        print("Error: No se puede obtener la película")
        print(error)

def dbGetMovieByTitle(titulo):
    print("---dbGetMovieByTitle---")

    try:
        cursor = conexion.cursor()
        consulta = "SELECT * FROM asee_movies WHERE movie_title LIKE '%:titulo%'"
        cursor.execute(consulta, [titulo])
        tupla = cursor.fetchone()
        print(tupla)
        cursor.close()
    except db.DatabaseError as error:
        print("Error: No se puede obtener la película")
        print(error)

def dbGetMoviesByGenre(genero):
    print("---dbGetMoviesByGenre---")

    try:
        cursor = conexion.cursor()
        consulta = "SELECT * FROM asee_movies WHERE genre = :genero"
        cursor.execute(consulta, [genero])
        for tupla in cursor:
            print(tupla)
        print("Total películas del genero ", genero, ": " , cursor.rowcount)
        cursor.close()
    except db.DatabaseError as error:
        print("Error: No se pueden obtener las películas")
        print(error)

def dbGetActorsInMovie(movie_id):
    print("---dbGetActorsInMovie---")
    try:
        cursor = conexion.cursor()
        consulta = "SELECT actor, actor_role FROM asee_actor_movie WHERE movie_id = :movie_id"
        cursor.execute(consulta, [movie_id])
        for tupla in cursor:
            print(tupla)
        print("Total actores:", cursor.rowcount)
        cursor.close()
    except db.DatabaseError as error:
        print("Error: No se pueden obtener los actores de la película")
        print(error)

def dbGetDirectorsInMovie(movie_id):
    print("---dbGetDirectorsInMovie---")
    try:
        cursor = conexion.cursor()
        consulta = "SELECT nombre FROM asee_directors WHERE movie_id = :movie_id"
        cursor.execute(consulta, [movie_id])
        for tupla in cursor:
            print(tupla)
        print("Total directores:", cursor.rowcount)
        cursor.close()
    except db.DatabaseError as error:
        print("Error: No se pueden obtener los directores de la película")
        print(error)

def dbModifyUserName(id, nombre):
    print("---dbModifyUserName---")
    try:
        cursor = conexion.cursor()
        consulta = "UPDATE nombre = :nombre FROM asee_users WHERE user_id = :id"
        cursor.execute(consulta, [nombre, id])
        
        if cursor.rowcount == 1:
            print("Nombre del usuario ", id, " modificado. Nuevo nombre: ", nombre)
        else:
            print("No se ha podido modificar el nombre del usuario")
        
        cursor.close()
    except db.DatabaseError as error:
        print("Error: No se ha podido cambiar el nombre del usuario")
        print(error)

def dbModifyFavGenre(id, genero):
    print("---dbModifyFavGenre---")
    try:
        cursor = conexion.cursor()
        consulta = "UPDATE fav_genre = :genero FROM asee_users WHERE user_id = :id"
        cursor.execute(consulta, [genero, id])
        
        if cursor.rowcount == 1:
            print("Genero favorito del usuario ", id, " modificado. Nuevo genero favorito: ", genero)
        else:
            print("No se ha podido modificar el genero favorito del usuario")
        
        cursor.close()
    except db.DatabaseError as error:
        print("Error: No se ha podido cambiar el genero favorito del usuario")
        print(error)

def dbModifylEmail(id, email):
    print("---dbModifylEmail---")
    try:
        cursor = conexion.cursor()
        consulta = "UPDATE email = :email FROM asee_users WHERE user_id = :id"
        cursor.execute(consulta, [email, id])
        
        if cursor.rowcount == 1:
            print("Email del usuario ", id, " modificado. Nuevo email: ", email)
        else:
            print("No se ha podido modificar el email favorito del usuario")
        
        cursor.close()
    except db.DatabaseError as error:
        print("Error: No se ha podido cambiar el email del usuario")
        print(error)

def dbModifyPassword(id, password):
    print("---dbModifyPassword---")
    try:
        cursor = conexion.cursor()
        consulta = "UPDATE passwd = :password FROM asee_users WHERE user_id = :id"
        cursor.execute(consulta, [password, id])
        
        if cursor.rowcount == 1:
            print("Contraseña del usuario ", id, " modificada. Nueva contraseña: ", password)
        else:
            print("No se ha podido modificar la contarseña del usuario")
        
        cursor.close()
    except db.DatabaseError as error:
        print("Error: No se ha podido cambiar la contraseña del usuario")
        print(error)

def dbRemoveUser(email=str, password=str):
    print("---dbRemoveUser---")

    try:
        cursor = conexion.cursor()
        consulta = "DELETE FROM asee_users WHERE email = :email AND passwd = :password"
        cursor.execute(consulta, [email, password])
        resul = cursor.fetchone()
        if(cursor.rowcount == 1):
            print("Usuario eliminado correctamente")
        else:
            print("Usuario no existente en la base de datos:",cursor.rowcount)
            return False
        print('------------------------------')
        cursor.close()
        conexion.commit()
        return True
    except db.DatabaseError as error:
        print("Error. No se ha podido eliminar el usuario")
        print(error)
        return False

conexion = dbConectar()